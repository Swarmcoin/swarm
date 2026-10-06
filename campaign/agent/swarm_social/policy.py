"""Guardrails: text checks and daily budgets. Loaded from policy.yaml."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml


@dataclass
class Violation:
    rule: str
    detail: str

    def __str__(self) -> str:
        return f"{self.rule}: {self.detail}"


class Policy:
    def __init__(self, data: dict[str, Any]):
        self.data = data
        self.banned_phrases: list[str] = [p.lower() for p in data.get("banned_phrases", [])]
        self.banned_regex = [re.compile(r, re.IGNORECASE) for r in data.get("banned_regex", [])]
        self.allowed_link_hosts: list[str] = data.get("allowed_link_hosts", [])
        # Hosts a *source* reply may never cite, even though source replies may link anywhere else.
        self.source_link_denied = [re.compile(r, re.IGNORECASE) for r in data.get("source_link_denied_regex", [])]
        self.disclaimer_triggers = [t.lower() for t in data.get("disclaimer_triggers", [])]
        self.disclaimers = [d.lower() for d in data.get("disclaimers", [])]
        self.max_post_chars: int = int(data.get("max_post_chars", 280))
        self.max_hashtags: int = int(data.get("max_hashtags", 1))
        self.budget: dict[str, Any] = data.get("budget", {})
        self.do_not_engage = [re.compile(r) for r in data.get("do_not_engage_regex", [])]
        self.never_reply_handles = {h.lower().lstrip("@") for h in data.get("never_reply_handles", [])}
        self.max_replies_per_account_per_day = int(data.get("max_replies_per_account_per_day", 2))
        self.reply_once_per_post = bool(data.get("reply_once_per_post", True))
        self.max_reply_age_hours = int(data.get("max_reply_age_hours", 36))
        targets = data.get("engagement_targets", {})
        self.targets: dict[str, list[str]] = {k: [h.lower() for h in v] for k, v in targets.items()}
        self.search_queries: list[str] = data.get("search_queries", [])

    @classmethod
    def load(cls, path: Path) -> "Policy":
        with open(path, encoding="utf-8") as f:
            return cls(yaml.safe_load(f) or {})

    # ----- text checks ---------------------------------------------------

    def check_text(self, text: str, *, is_reply: bool = False, max_chars: int | None = None,
                   source_links: bool = False) -> list[Violation]:
        """Return every rule the text breaks. Empty list means publishable.

        source_links=True is for the first reply under a story or explainer: it may cite any
        host (a court, an archive, a newspaper) except the ones in source_link_denied_regex.
        Every other text may link only to the official channels."""
        out: list[Violation] = []
        lowered = text.lower()
        limit = max_chars or self.max_post_chars
        # X counts every link as 23 characters (t.co), whatever its real length.
        effective = len(re.sub(r"https?://[^\s)\]]+", "x" * 23, text))
        if effective > limit:
            out.append(Violation("length", f"{effective} characters as X counts them, limit {limit}"))
        if not text.strip():
            out.append(Violation("empty", "no text"))

        for phrase in self.banned_phrases:
            if re.search(r"(?<!\w)" + re.escape(phrase) + r"(?!\w)", lowered):
                out.append(Violation("banned_phrase", f"contains '{phrase}'"))
        for rx in self.banned_regex:
            m = rx.search(text)
            if m:
                out.append(Violation("banned_pattern", f"matches '{rx.pattern}' at '{m.group(0)}'"))

        for url in re.findall(r"https?://[^\s)\]]+", text):
            url = url.rstrip(".,;:!?'\"")   # punctuation after a link is not part of it
            host = urlparse(url).netloc.lower()
            path = urlparse(url).path
            if source_links:
                if any(rx.search(url) for rx in self.source_link_denied):
                    out.append(Violation("link_host", f"source link to {host} is on the denied list"))
                continue
            ok = any(
                host == h or host.endswith("." + h) or (("/" in h) and (host + path).startswith(h))
                for h in self.allowed_link_hosts
            )
            if not ok:
                out.append(Violation("link_host", f"link to {host} is not an official channel"))

        hashtags = re.findall(r"(?<!\w)#\w+", text)
        if len(hashtags) > self.max_hashtags:
            out.append(Violation("hashtags", f"{len(hashtags)} hashtags, limit {self.max_hashtags}"))

        if not is_reply and any(re.search(r"(?<!\w)" + re.escape(t) + r"(?!\w)", lowered) for t in self.disclaimer_triggers):
            if not any(d in lowered for d in self.disclaimers):
                out.append(Violation("disclaimer", "mentions mining/rewards/waiting list without a disclaimer"))

        if text.count("!") > 1:
            out.append(Violation("tone", "more than one exclamation mark"))
        return out

    def may_engage_with(self, other_text: str, author_handle: str) -> tuple[bool, str]:
        if author_handle.lower().lstrip("@") in self.never_reply_handles:
            return False, "author is on the never-reply list"
        for rx in self.do_not_engage:
            m = rx.search(other_text)
            if m:
                return False, f"conversation matches do-not-engage pattern at '{m.group(0)}'"
        return True, "ok"

    # ----- budgets -------------------------------------------------------

    def cap(self, key: str, default: int = 0) -> int:
        return int(self.budget.get(key, default))

    def in_quiet_hours(self, now: datetime | None = None) -> bool:
        now = now or datetime.now(timezone.utc)
        return now.hour in set(self.budget.get("quiet_hours_utc", []))
