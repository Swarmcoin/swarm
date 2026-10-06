"""The 30-day calendar: campaign/x/calendar.json, built from calendar.yaml by tools/build_calendar.py."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path


@dataclass
class CalendarPost:
    id: str
    when: datetime                 # timezone-aware, UTC
    text: str
    pillar: str = ""
    thread: list[str] = field(default_factory=list)   # follow-up posts, in order
    media: list[str] = field(default_factory=list)    # public image URLs (Metricool only)
    reply: str = ""                                   # first reply under the post, after the thread: the link or the source
    notes: str = ""

    @classmethod
    def from_dict(cls, d: dict) -> "CalendarPost":
        when = datetime.fromisoformat(d["when"].replace("Z", "+00:00"))
        if when.tzinfo is None:
            when = when.replace(tzinfo=timezone.utc)
        return cls(id=d["id"], when=when.astimezone(timezone.utc), text=d["text"], pillar=d.get("pillar", ""),
                   thread=list(d.get("thread", [])), media=list(d.get("media", [])), reply=d.get("reply", "") or "", notes=d.get("notes", ""))


def load_calendar(path: Path) -> list[CalendarPost]:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    posts = [CalendarPost.from_dict(d) for d in data["posts"]]
    posts.sort(key=lambda p: p.when)
    return posts


def due_posts(posts: list[CalendarPost], posted_ids: set[str], now: datetime | None = None, window_hours: float = 6.0) -> list[CalendarPost]:
    """Posts whose time has come and that have not been posted. Anything older than the window
    is skipped rather than published late: a stale 'opens in 3 days' post does harm."""
    now = now or datetime.now(timezone.utc)
    earliest = now - timedelta(hours=window_hours)
    return [p for p in posts if p.id not in posted_ids and earliest <= p.when <= now]


def upcoming(posts: list[CalendarPost], posted_ids: set[str], now: datetime | None = None, hours: float = 48) -> list[CalendarPost]:
    now = now or datetime.now(timezone.utc)
    return [p for p in posts if p.id not in posted_ids and now < p.when <= now + timedelta(hours=hours)]
