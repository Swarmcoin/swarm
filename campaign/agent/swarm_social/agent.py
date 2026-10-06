"""The agentic layer: Claude runs the @swarm_coin account for one cycle, within the policy.

What the model may do on its own, and what it may only propose, follows X's Automation Rules:

* Answering people who @mentioned us is opt-in engagement and may be published directly
  (when SWARM_SOCIAL_APPROVAL=auto). Keyword-triggered automated replies are prohibited by X,
  so anything found through search or on a target account's timeline is only ever *proposed*
  into the review queue, where a human approves it with one command.
* Likes are capped low and only allowed on posts that mention us. Following is never
  automated.
* Every text passes the policy before it leaves; the model cannot bypass it.

Everything the model says about SWARM comes from swarm.green/llms-full.txt and the live status
feed, both passed in the system prompt. It is told not to invent numbers, and the policy
refuses dollar figures and promises anyway.
"""

from __future__ import annotations

import json
import logging
import uuid
from datetime import datetime, timezone
from pathlib import Path

import anthropic
from anthropic import beta_tool

from .calendar import load_calendar, upcoming
from .config import Settings
from .facts import load_facts, load_status, status_summary
from .policy import Policy
from .state import State
from .x_client import Post, XClient

log = logging.getLogger("swarm_social.agent")

VOICE_PATH = Path(__file__).resolve().parent.parent.parent / "VOICE.md"


# --------------------------------------------------------------------------- review queue

class ReviewQueue:
    def __init__(self, path: Path):
        self.path = path
        self.items: list[dict] = []
        if path.exists():
            self.items = json.loads(path.read_text(encoding="utf-8")).get("items", [])

    def add(self, kind: str, text: str, *, target_post_id: str = "", author: str = "", reason: str = "", source: str = "") -> str:
        item_id = uuid.uuid4().hex[:8]
        self.items.append({
            "id": item_id, "kind": kind, "text": text, "target_post_id": target_post_id, "author": author,
            "reason": reason, "source": source, "status": "pending", "created_at": datetime.now(timezone.utc).isoformat(),
        })
        return item_id

    def pending(self) -> list[dict]:
        return [i for i in self.items if i["status"] == "pending"]

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps({"items": self.items}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    def to_markdown(self) -> str:
        pend = self.pending()
        if not pend:
            return "_Review queue is empty._\n"
        lines = ["| id | kind | to | text | why |", "|---|---|---|---|---|"]
        for i in pend:
            to = f"@{i['author']} ({i['target_post_id']})" if i["author"] else (i["target_post_id"] or "—")
            cell = i['text'].replace('|', '\|').replace(chr(10), ' ')   # Python 3.11: no backslash inside an f-string expression
            lines.append(f"| `{i['id']}` | {i['kind']} | {to} | {cell} | {i['reason']} |")
        lines.append("")
        lines.append("Approve with `swarm-social approve <id> [<id>...]` or `swarm-social approve --all`; reject with `swarm-social reject <id>`.")
        return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------- the run

class AgentRun:
    """One cycle. Holds the tools' shared state so the model can only act through them."""

    def __init__(self, settings: Settings, policy: Policy, state: State, x: XClient, queue: ReviewQueue):
        self.s, self.p, self.st, self.x, self.q = settings, policy, state, x, queue
        self.actions = 0
        self.notes: list[str] = []
        self.seen_posts: dict[str, Post] = {}
        self.mentioned_us: set[str] = set()

    # ----- helpers
    def _remember(self, posts: list[Post], mentioned: bool = False) -> list[dict]:
        out = []
        for p in posts:
            self.seen_posts[p.id] = p
            if mentioned:
                self.mentioned_us.add(p.id)
            out.append({"id": p.id, "author": p.author_handle, "created_at": p.created_at,
                        "age_hours": round(p.age_hours(), 1), "text": p.text, "metrics": p.public_metrics})
        return out

    def _budget_left(self) -> dict[str, int]:
        return {
            "posts": self.p.cap("posts_per_day", 4) - self.st.count("posts"),
            "replies": self.p.cap("replies_per_day", 12) - self.st.count("replies"),
            "likes": self.p.cap("likes_per_day", 20) - self.st.count("likes"),
            "actions_this_run": self.p.cap("max_actions_per_run", 8) - self.actions,
        }

    def _spend(self) -> str | None:
        if self.actions >= self.p.cap("max_actions_per_run", 8):
            return "refused: this run's action cap is reached; finish with a summary."
        self.actions += 1
        return None

    def _deliver(self, kind: str, text: str, *, reply_to: str | None = None, author: str = "", reason: str = "", source: str = "") -> str:
        """Publish now, or queue for review, depending on settings."""
        if self.s.approval != "auto":
            item = self.q.add(kind, text, target_post_id=reply_to or "", author=author, reason=reason, source=source)
            self.st.log("queued", kind=kind, item=item, to=reply_to, author=author)
            return f"queued for human review as item {item} (SWARM_SOCIAL_APPROVAL={self.s.approval})."
        x_id = self.x.create_post(text, reply_to=reply_to)
        if kind == "post":
            self.st.mark_post()
        else:
            self.st.bump("replies", author)
            self.st.data["replied_post_ids"].append(reply_to)
        self.st.log(kind, x_id=x_id, to=reply_to, author=author, text=text, dry_run=self.s.dry_run)
        return f"published as {x_id}" + (" (dry run, nothing was sent)" if self.s.dry_run else "")

    # ----- tools
    def tools(self) -> list:
        run = self

        @beta_tool
        def get_new_mentions() -> str:
            """Fetch posts that @mentioned @swarm_coin since the last run. These people opted in to a reply.
            Posts that match the do-not-engage rules, are too old, or were already answered are filtered out
            and listed under `skipped` with the reason."""
            since = run.st.data.get("last_mention_id")
            posts = run.x.mentions(since)
            if posts:
                newest = max(posts, key=lambda p: int(p.id) if p.id.isdigit() else 0)
                if newest.id.isdigit():
                    run.st.data["last_mention_id"] = newest.id
            keep, skipped = [], []
            for p in posts:
                ok, why = run.p.may_engage_with(p.text, p.author_handle)
                if p.id in run.st.data["replied_post_ids"]:
                    ok, why = False, "already answered"
                elif p.age_hours() > run.p.max_reply_age_hours:
                    ok, why = False, f"older than {run.p.max_reply_age_hours} h"
                elif run.st.replies_to(p.author_handle) >= run.p.max_replies_per_account_per_day:
                    ok, why = False, "daily per-account reply cap reached"
                (keep if ok else skipped).append((p, why))
            return json.dumps({"mentions": run._remember([p for p, _ in keep], mentioned=True),
                               "skipped": [{"id": p.id, "author": p.author_handle, "reason": w} for p, w in skipped]}, ensure_ascii=False)

        @beta_tool
        def get_target_posts(tier: str = "tier1", max_accounts: int = 4) -> str:
            """Read the latest original posts of the accounts in an engagement tier (tier1 = the ecosystem we build on,
            tier2 = privacy advocates and journalists, tier3 = peer privacy projects). Accounts rotate by day so
            every account is read a few times a week. Replies to these posts can only be *proposed* (propose_reply),
            never published directly: X forbids automated replies that the other person did not ask for."""
            handles = run.p.targets.get(tier, [])
            if not handles:
                return json.dumps({"error": f"unknown tier {tier}", "tiers": list(run.p.targets)})
            day = datetime.now(timezone.utc).toordinal()
            start = (day * max_accounts) % len(handles)
            chosen = [handles[(start + i) % len(handles)] for i in range(min(max_accounts, len(handles)))]
            out = {}
            for h in chosen:
                try:
                    out[h] = run._remember(run.x.user_recent_posts(h, max_results=5))
                except Exception as e:  # one failing account must not end the run
                    out[h] = {"error": str(e)[:200]}
            return json.dumps(out, ensure_ascii=False)

        @beta_tool
        def search_recent(query_index: int = 0) -> str:
            """Run one of the policy's search queries (0-based index into policy.search_queries) and return recent
            public posts. Use it to find people talking about SWARM or about shielded payments. Anything found here
            is reply-by-proposal only."""
            if not 0 <= query_index < len(run.p.search_queries):
                return json.dumps({"error": "no such query", "queries": run.p.search_queries})
            posts = run.x.search_recent(run.p.search_queries[query_index])
            keep = [p for p in posts if run.p.may_engage_with(p.text, p.author_handle)[0] and p.author_handle.lower() != run.x.me()["handle"].lower()]
            return json.dumps({"query": run.p.search_queries[query_index], "posts": run._remember(keep)}, ensure_ascii=False)

        @beta_tool
        def check_text(text: str, is_reply: bool = False) -> str:
            """Check a draft against the publishing policy before using it. Returns the list of violations; an empty
            list means it may be published. Fix every violation; never try to work around one."""
            return json.dumps([str(v) for v in run.p.check_text(text, is_reply=is_reply)])

        @beta_tool
        def reply_to_mention(post_id: str, text: str) -> str:
            """Answer a post that @mentioned us (it must come from get_new_mentions). One reply per post, at most two
            per account per day. The text is policy-checked; a violation is refused and returned to you to fix."""
            if post_id not in run.mentioned_us:
                return "refused: only posts returned by get_new_mentions may be answered directly; use propose_reply."
            if post_id in run.st.data["replied_post_ids"]:
                return "refused: already answered."
            p = run.seen_posts[post_id]
            if run.st.replies_to(p.author_handle) >= run.p.max_replies_per_account_per_day:
                return "refused: per-account daily reply cap."
            if run._budget_left()["replies"] <= 0:
                return "refused: daily reply cap reached."
            problems = run.p.check_text(text, is_reply=True)
            if problems:
                return "refused by policy: " + "; ".join(map(str, problems))
            if (why := run._spend()):
                return why
            return run._deliver("reply", text, reply_to=post_id, author=p.author_handle, reason="answered a mention", source="mention")

        @beta_tool
        def propose_reply(post_id: str, text: str, reason: str) -> str:
            """Put a suggested reply to a post we were NOT mentioned in into the human review queue. Give the reason a
            human would want to post it (what we add to the conversation). It is never published automatically."""
            p = run.seen_posts.get(post_id)
            if p is None:
                return "refused: unknown post id; read it first with get_target_posts or search_recent."
            if p.id in run.st.data["replied_post_ids"] or any(i["target_post_id"] == post_id for i in run.q.items):
                return "refused: already answered or already queued."
            problems = run.p.check_text(text, is_reply=True)
            if problems:
                return "refused by policy: " + "; ".join(map(str, problems))
            if (why := run._spend()):
                return why
            item = run.q.add("reply", text, target_post_id=post_id, author=p.author_handle, reason=reason, source="proposal")
            run.st.log("proposed_reply", item=item, to=post_id, author=p.author_handle)
            return f"queued for human review as item {item}."

        @beta_tool
        def like_post(post_id: str) -> str:
            """Like a post that mentioned us, when it is friendly or useful. Only posts from get_new_mentions qualify;
            likes are capped per day. Never like in bulk."""
            if post_id not in run.mentioned_us:
                return "refused: only posts that mention us may be liked by the agent."
            if post_id in run.st.data["liked_post_ids"]:
                return "refused: already liked."
            if run._budget_left()["likes"] <= 0:
                return "refused: daily like cap reached."
            if (why := run._spend()):
                return why
            if run.s.approval == "auto":
                run.x.like(post_id)
                run.st.bump("likes")
                run.st.data["liked_post_ids"].append(post_id)
                run.st.log("like", post_id=post_id, dry_run=run.s.dry_run)
                return "liked" + (" (dry run)" if run.s.dry_run else "")
            item = run.q.add("like", "", target_post_id=post_id, author=run.seen_posts[post_id].author_handle, reason="friendly mention", source="mention")
            return f"queued for human review as item {item}."

        @beta_tool
        def publish_post(text: str, reason: str) -> str:
            """Publish an original post that is not on the calendar: a correction, an answer to a recurring question,
            a note about something that just happened on the network. Check the upcoming calendar first so you do not
            duplicate it. Refused in quiet hours, when the daily post cap is reached, or within 45 minutes of the last
            post. In review mode it is queued instead."""
            if run.p.in_quiet_hours():
                return "refused: quiet hours (UTC)."
            if run._budget_left()["posts"] <= 0:
                return "refused: daily post cap reached."
            if run.st.minutes_since_last_post() < run.p.cap("min_minutes_between_posts", 45):
                return "refused: too soon after the last post."
            problems = run.p.check_text(text)
            if problems:
                return "refused by policy: " + "; ".join(map(str, problems))
            if (why := run._spend()):
                return why
            return run._deliver("post", text, reason=reason, source="agent")

        @beta_tool
        def upcoming_calendar(hours: int = 48) -> str:
            """The scheduled posts of the next N hours, so you do not say what the calendar is about to say."""
            try:
                posts = load_calendar(run.s.calendar_path)
            except FileNotFoundError:
                return "[]"
            posted = set(run.st.data["posted_calendar_ids"])
            return json.dumps([{"id": p.id, "when": p.when.isoformat(), "text": p.text} for p in upcoming(posts, posted, hours=hours)], ensure_ascii=False)

        @beta_tool
        def note_for_humans(text: str) -> str:
            """Leave a note for the team in the run report: a question you could not answer from the facts, a bug report
            you saw, a conversation a human should join, a recurring confusion worth a calendar post."""
            run.notes.append(text)
            return "noted."

        return [get_new_mentions, get_target_posts, search_recent, check_text, reply_to_mention,
                propose_reply, like_post, publish_post, upcoming_calendar, note_for_humans]


SYSTEM_TEMPLATE = """You are running the X account @swarm_coin for the SWARM (SWM) project for one cycle. You act only through the tools; every text you send passes a policy you cannot bypass. Work carefully and stop when the useful work is done. Doing nothing is a fine outcome when nothing needs an answer.

## Voice and rules (from VOICE.md)
{voice}

## The facts you may state (the project's own published document)
{facts}

## Live network status
{status}

## Today's remaining budget
{budget}

## What to do this cycle
1. Call get_new_mentions. For each mention that asks something or says something worth answering, write a reply in the project's voice (one or two sentences, the fact and at most one official link, no hashtags), check it with check_text, then reply_to_mention. Friendly mentions may be liked. Bug reports: thank them and point to the repository or swarmofficial@atomicmail.io; security problems: point to SECURITY.md only.
2. Call get_target_posts for one tier (rotate: tier1 on even days, tier2 on odd days; tier3 at most once a week) and search_recent for at most two queries. Where @swarm_coin has something true and useful to add, and only then, use propose_reply with a reason. Never propose a reply that just promotes SWARM; the reader must learn something. Two or three good proposals beat ten weak ones.
3. If you saw a question that keeps coming up, a correction worth making, or a notable network event, and the upcoming calendar does not cover it, you may publish_post once. Otherwise do not post: the calendar carries the schedule.
4. End with a short plain-text report for the team: what you answered, what you proposed, what you skipped and why, and anything in note_for_humans. No marketing language in the report.

Never invent a number, a date or a feature. If the facts above do not contain the answer, say so in the reply ("we have not published that yet") rather than guess. Never discuss price or the SWM token on Base. Never argue. Never reply twice to the same person in one cycle.
"""


def build_system(settings: Settings, state: State, policy: Policy, budget: dict[str, int]) -> str:
    voice = VOICE_PATH.read_text(encoding="utf-8") if VOICE_PATH.exists() else "(VOICE.md missing)"
    facts = load_facts(settings.facts_url, settings.facts_fallback)
    status = status_summary(load_status(settings.status_url))
    return SYSTEM_TEMPLATE.format(voice=voice, facts=facts, status=status, budget=json.dumps(budget))


def run_agent(settings: Settings, policy: Policy, state: State, x: XClient, queue: ReviewQueue, client: anthropic.Anthropic | None = None) -> str:
    """One cycle. Returns the model's final report. Saves state and queue."""
    run = AgentRun(settings, policy, state, x, queue)
    client = client or anthropic.Anthropic()
    system = build_system(settings, state, policy, run._budget_left())
    runner = client.beta.messages.tool_runner(
        model=settings.model,
        max_tokens=16000,
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        output_config={"effort": settings.effort},
        tools=run.tools(),
        max_iterations=20,
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        messages=[{"role": "user", "content": f"Begin the cycle. It is {datetime.now(timezone.utc).isoformat(timespec='minutes')} UTC."}],
    )
    report = ""
    for message in runner:
        if message.stop_reason == "refusal":
            report = "The model declined to continue this cycle (safety refusal). Nothing further was done."
            break
        texts = [b.text for b in message.content if b.type == "text"]
        if texts:
            report = "\n".join(texts)
    if run.notes:
        report += "\n\nNotes for humans:\n" + "\n".join(f"- {n}" for n in run.notes)
    state.log("agent_cycle", actions=run.actions, queued=len(queue.pending()))
    state.save()
    queue.save()
    return report
