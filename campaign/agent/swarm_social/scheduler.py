"""Deterministic layer: publish calendar posts whose time has come. No model involved."""

from __future__ import annotations

import logging
from datetime import datetime, timezone

from .calendar import CalendarPost, due_posts, load_calendar
from .config import Settings
from .policy import Policy
from .state import State
from .x_client import XClient

log = logging.getLogger("swarm_social.scheduler")


def run_scheduler(settings: Settings, policy: Policy, state: State, x: XClient, now: datetime | None = None) -> list[str]:
    """Publish every due calendar post (and its thread). Returns the ids published."""
    if not settings.scheduler_enabled:
        log.info("scheduler disabled (SWARM_SOCIAL_SCHEDULER=0); Metricool owns the calendar")
        return []
    now = now or datetime.now(timezone.utc)
    posts = load_calendar(settings.calendar_path)
    posted = set(state.data["posted_calendar_ids"])
    published: list[str] = []
    for post in due_posts(posts, posted, now):
        if state.count("posts") >= policy.cap("posts_per_day", 4):
            log.warning("daily post cap reached; %s waits", post.id)
            break
        problems = policy.check_text(post.text)
        for i, t in enumerate(post.thread):
            problems += [p for p in policy.check_text(t, is_reply=True)]
        if post.reply:
            problems += policy.check_text(post.reply, is_reply=True, source_links=True)
        # The ASIC sentence may sit anywhere in the package (post, thread, first reply).
        problems = [p for p in problems if p.rule != "mining_call"]
        problems += policy.check_mining_call(" ".join([post.text, *post.thread, post.reply]))
        if problems:
            # A calendar post that breaks policy is a bug in the calendar; never publish it silently.
            log.error("calendar post %s refused: %s", post.id, "; ".join(map(str, problems)))
            state.log("refused_calendar_post", id=post.id, problems=[str(p) for p in problems])
            continue
        _publish(post, state, x)
        published.append(post.id)
    state.save()
    return published


def _publish(post: CalendarPost, state: State, x: XClient) -> None:
    root = x.create_post(post.text)
    last = root
    for t in post.thread:
        last = x.create_post(t, reply_to=last)
    if post.reply:
        # Links and sources go in the first reply: a link in the post itself costs reach.
        x.create_post(post.reply, reply_to=last)
    state.data["posted_calendar_ids"].append(post.id)
    state.mark_post()
    state.log("calendar_post", id=post.id, x_id=root, pillar=post.pillar, thread_len=len(post.thread), has_reply=bool(post.reply))
    log.info("published %s as %s", post.id, root)
