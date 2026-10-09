"""Command line: `swarm-social <command>`.

  status            what the calendar and the state say
  post-due          publish calendar posts whose time has come (deterministic)
  engage            one agentic cycle: mentions, targets, proposals
  cycle             post-due, then engage (what the cron job runs)
  queue             show the review queue
  approve ID...     publish approved queue items (or --all)
  reject ID...      drop queue items
  check "text"      policy-check a text
  enqueue POST "t"  put a human-drafted reply (the daily reply sheet) into the same review queue
  report            write state/last-run.md for the GitHub step summary

Nothing is sent unless SWARM_SOCIAL_LIVE=1 and X credentials are present.
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path

from .agent import ReviewQueue, run_agent
from .calendar import load_calendar, upcoming
from .config import Settings, load_settings
from .policy import Policy
from .scheduler import run_scheduler
from .state import State
from .x_client import DryRunClient, TweepyClient, XClient


def make_x(settings: Settings) -> XClient:
    if settings.dry_run or not settings.x_credentials_present():
        if not settings.dry_run:
            logging.warning("SWARM_SOCIAL_LIVE is set but X credentials are missing; falling back to dry run")
            settings.dry_run = True
        return DryRunClient()
    return TweepyClient(settings.x_api_key, settings.x_api_secret, settings.x_access_token, settings.x_access_secret, settings.x_bearer_token)


def cmd_status(settings: Settings, policy: Policy, state: State, args) -> int:
    posts = load_calendar(settings.calendar_path)
    posted = set(state.data["posted_calendar_ids"])
    print(f"mode: {'DRY RUN' if settings.dry_run else 'LIVE'}; approval: {settings.approval}; scheduler: {'on' if settings.scheduler_enabled else 'off (Metricool)'}")
    if settings.approval != "auto" and not settings.x_ai_approval:
        print("auto mode is locked until SWARM_SOCIAL_X_AI_APPROVAL holds X's written approval reference")
    opted = state.data.get("opt_out_handles", [])
    if opted:
        print(f"opted out (never answered again): {', '.join('@' + h for h in opted)}")
    print(f"calendar: {len(posts)} posts, {len(posted)} published, {len([p for p in posts if p.id not in posted])} remaining")
    t = state.today()
    print(f"today (UTC): posts {t['posts']}/{policy.cap('posts_per_day')}, replies {t['replies']}/{policy.cap('replies_per_day')}, likes {t['likes']}/{policy.cap('likes_per_day')}")
    for p in upcoming(posts, posted, hours=48):
        print(f"  {p.when:%Y-%m-%d %H:%M} UTC  [{p.id}] {p.text[:90]}")
    q = ReviewQueue(settings.queue_path)
    print(f"review queue: {len(q.pending())} pending")
    return 0


def cmd_post_due(settings: Settings, policy: Policy, state: State, args) -> int:
    x = make_x(settings)
    ids = run_scheduler(settings, policy, state, x)
    print(f"published {len(ids)} calendar post(s): {', '.join(ids) if ids else 'none due'}")
    return 0


def cmd_engage(settings: Settings, policy: Policy, state: State, args) -> int:
    x = make_x(settings)
    queue = ReviewQueue(settings.queue_path)
    report = run_agent(settings, policy, state, x, queue)
    print(report)
    _write_report(settings, state, queue, report)
    return 0


def cmd_cycle(settings: Settings, policy: Policy, state: State, args) -> int:
    cmd_post_due(settings, policy, state, args)
    return cmd_engage(settings, policy, state, args)


def cmd_queue(settings: Settings, policy: Policy, state: State, args) -> int:
    print(ReviewQueue(settings.queue_path).to_markdown())
    return 0


def cmd_approve(settings: Settings, policy: Policy, state: State, args) -> int:
    queue = ReviewQueue(settings.queue_path)
    x = make_x(settings)
    chosen = queue.pending() if args.all else [i for i in queue.pending() if i["id"] in set(args.ids)]
    if not chosen:
        print("nothing to approve")
        return 0
    for item in chosen:
        if item["kind"] in ("reply", "post"):
            problems = policy.check_text(item["text"], is_reply=item["kind"] == "reply")
            if problems:
                print(f"{item['id']}: still refused by policy: {'; '.join(map(str, problems))}")
                continue
            x_id = x.create_post(item["text"], reply_to=item["target_post_id"] or None)
            if item["kind"] == "post":
                state.mark_post()
            else:
                state.bump("replies", item["author"])
                state.data["replied_post_ids"].append(item["target_post_id"])
        elif item["kind"] == "like":
            x.like(item["target_post_id"])
            x_id = item["target_post_id"]
            state.bump("likes")
            state.data["liked_post_ids"].append(item["target_post_id"])
        else:
            print(f"{item['id']}: unknown kind {item['kind']}")
            continue
        item["status"] = "published"
        item["published_at"] = datetime.now(timezone.utc).isoformat()
        item["x_id"] = x_id
        state.log("approved_" + item["kind"], item=item["id"], x_id=x_id, dry_run=settings.dry_run)
        print(f"{item['id']}: {item['kind']} published as {x_id}{' (dry run)' if settings.dry_run else ''}")
    queue.save()
    state.save()
    return 0


def cmd_enqueue(settings: Settings, policy: Policy, state: State, args) -> int:
    """Put a human-drafted reply into the same review queue the agent uses, so the daily reply sheet and
    the agent's proposals are one list and no post is answered twice. Refused when the post is already
    answered or queued, or when the text breaks the policy."""
    post_id = args.post.rstrip("/").split("/")[-1].split("?")[0]   # accepts a post id or its x.com URL
    if not post_id.isdigit():
        print(f"refused: '{args.post}' is not a post id or x.com status URL")
        return 1
    queue = ReviewQueue(settings.queue_path)
    if post_id in state.data["replied_post_ids"] or any(i["target_post_id"] == post_id for i in queue.items):
        print(f"refused: post {post_id} is already answered or already in the queue")
        return 1
    problems = policy.check_text(args.text, is_reply=True)
    if problems:
        print("refused by policy: " + "; ".join(map(str, problems)))
        return 1
    item = queue.add("reply", args.text, target_post_id=post_id, author=args.author.lstrip("@"), reason=args.reason, source=args.source)
    queue.save()
    state.log("enqueued", item=item, to=post_id, author=args.author, source=args.source)
    state.save()
    print(f"queued as item {item}; approve with `swarm-social approve {item}`")
    return 0


def cmd_reject(settings: Settings, policy: Policy, state: State, args) -> int:
    queue = ReviewQueue(settings.queue_path)
    ids = set(args.ids)
    n = 0
    for item in queue.items:
        if item["status"] == "pending" and (args.all or item["id"] in ids):
            item["status"] = "rejected"
            n += 1
    queue.save()
    print(f"rejected {n}")
    return 0


def cmd_check(settings: Settings, policy: Policy, state: State, args) -> int:
    problems = policy.check_text(args.text, is_reply=args.reply)
    if problems:
        for p in problems:
            print(f"✗ {p}")
        return 1
    print(f"✓ ok ({len(args.text)} chars)")
    return 0


def cmd_report(settings: Settings, policy: Policy, state: State, args) -> int:
    _write_report(settings, state, ReviewQueue(settings.queue_path), "")
    print(settings.state_path.parent / "last-run.md")
    return 0


def _write_report(settings: Settings, state: State, queue: ReviewQueue, report: str) -> None:
    out = settings.state_path.parent / "last-run.md"
    t = state.today()
    lines = [
        f"# @swarm_coin agent — {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC",
        "",
        f"Mode: **{'dry run' if settings.dry_run else 'LIVE'}**, approval: **{settings.approval}**"
        + ("" if settings.approval == "auto" else " (auto mode locked until X's written approval is recorded in SWARM_SOCIAL_X_AI_APPROVAL)") + ".",
        f"Today: {t['posts']} posts, {t['replies']} replies, {t['likes']} likes.",
        "",
        "## Agent report", "", report or "_(no agent cycle in this run)_", "",
        "## Review queue", "", queue.to_markdown(), "",
        "## Last actions", "",
    ]
    for e in state.data["log"][-15:]:
        lines.append(f"- {e['at'][:16]} {e['action']} " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False)[:80]}" for k, v in e.items() if k not in ("at", "action")))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    for stream in (sys.stdout, sys.stderr):   # Windows consoles default to cp1252; the reports carry UTF-8
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="swarm-social", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status").set_defaults(fn=cmd_status)
    sub.add_parser("post-due").set_defaults(fn=cmd_post_due)
    sub.add_parser("engage").set_defaults(fn=cmd_engage)
    sub.add_parser("cycle").set_defaults(fn=cmd_cycle)
    sub.add_parser("queue").set_defaults(fn=cmd_queue)
    sub.add_parser("report").set_defaults(fn=cmd_report)
    a = sub.add_parser("approve"); a.add_argument("ids", nargs="*"); a.add_argument("--all", action="store_true"); a.set_defaults(fn=cmd_approve)
    r = sub.add_parser("reject"); r.add_argument("ids", nargs="*"); r.add_argument("--all", action="store_true"); r.set_defaults(fn=cmd_reject)
    c = sub.add_parser("check"); c.add_argument("text"); c.add_argument("--reply", action="store_true"); c.set_defaults(fn=cmd_check)
    e = sub.add_parser("enqueue", help="put a human-drafted reply into the review queue (the daily reply sheet)")
    e.add_argument("post", help="post id or x.com status URL"); e.add_argument("text")
    e.add_argument("--author", default="", help="handle of the post's author"); e.add_argument("--reason", default="reply sheet")
    e.add_argument("--source", default="sheet"); e.set_defaults(fn=cmd_enqueue)
    args = ap.parse_args(argv)

    settings = load_settings()
    policy = Policy.load(settings.policy_path)
    state = State(settings.state_path)
    return args.fn(settings, policy, state, args)


if __name__ == "__main__":
    sys.exit(main())
