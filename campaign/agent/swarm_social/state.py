"""Persistent state: what we posted, whom we answered, today's counters.

Stored as one JSON file that the GitHub Action commits back to the repository, so every
run (and every human) can see exactly what the agent did.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def utc_today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


class State:
    def __init__(self, path: Path):
        self.path = path
        self.data: dict[str, Any] = {
            "posted_calendar_ids": [],
            "replied_post_ids": [],
            "liked_post_ids": [],
            "reposted_post_ids": [],
            "last_mention_id": None,
            "opt_out_handles": [],   # people who asked us to stop; never answered again (X Automation Rules)
            "last_post_at": None,
            "daily": {},          # "YYYY-MM-DD": {"posts": n, "replies": n, "likes": n, "reposts": n, "replies_by_account": {}}
            "log": [],            # last 500 actions, newest last
        }
        if path.exists():
            with open(path, encoding="utf-8") as f:
                self.data.update(json.load(f))

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.data["log"] = self.data["log"][-500:]
        tmp = self.path.with_suffix(".tmp")
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
            f.write("\n")
        tmp.replace(self.path)

    # ----- counters -----
    def today(self) -> dict[str, Any]:
        d = self.data["daily"].setdefault(utc_today(), {"posts": 0, "replies": 0, "likes": 0, "reposts": 0, "replies_by_account": {}})
        d.setdefault("replies_by_account", {})
        return d

    def count(self, kind: str) -> int:
        return int(self.today().get(kind, 0))

    def bump(self, kind: str, account: str | None = None) -> None:
        d = self.today()
        d[kind] = int(d.get(kind, 0)) + 1
        if kind == "replies" and account:
            acc = account.lower().lstrip("@")
            d["replies_by_account"][acc] = d["replies_by_account"].get(acc, 0) + 1

    def replies_to(self, account: str) -> int:
        return int(self.today()["replies_by_account"].get(account.lower().lstrip("@"), 0))

    def minutes_since_last_post(self) -> float:
        ts = self.data.get("last_post_at")
        if not ts:
            return 1e9
        last = datetime.fromisoformat(ts)
        return (datetime.now(timezone.utc) - last).total_seconds() / 60

    def mark_post(self) -> None:
        self.data["last_post_at"] = datetime.now(timezone.utc).isoformat()
        self.bump("posts")

    def log(self, action: str, **fields: Any) -> None:
        entry = {"at": datetime.now(timezone.utc).isoformat(), "action": action, **fields}
        self.data["log"].append(entry)
