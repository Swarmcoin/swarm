#!/usr/bin/env python3
"""Build x/calendar.json and x/metricool-import.csv from x/calendar.yaml, after checking every
post against agent/policy.yaml. Exits non-zero if any post breaks a rule, so a bad post never
reaches the scheduler.

    python tools/build_calendar.py            # build + check
    python tools/build_calendar.py --check    # check only
"""

from __future__ import annotations

import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

CAMPAIGN = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(CAMPAIGN / "agent"))
from swarm_social.policy import Policy  # noqa: E402

SRC = CAMPAIGN / "x" / "calendar.yaml"
OUT_JSON = CAMPAIGN / "x" / "calendar.json"
OUT_CSV = CAMPAIGN / "x" / "metricool-import.csv"
OUT_MD = CAMPAIGN / "x" / "calendar.md"
METRICOOL_TZ = "America/Santo_Domingo"   # the brand's timezone in Metricool; the CSV is written in it


def main(check_only: bool = False) -> int:
    policy = Policy.load(CAMPAIGN / "agent" / "policy.yaml")
    data = yaml.safe_load(SRC.read_text(encoding="utf-8"))
    posts = data["posts"]
    problems: list[str] = []
    seen: set[str] = set()
    for p in posts:
        if p["id"] in seen:
            problems.append(f"{p['id']}: duplicate id")
        seen.add(p["id"])
        when = p["when"]
        if isinstance(when, str):
            when = datetime.fromisoformat(when.replace("Z", "+00:00"))
        if when.tzinfo is None:
            when = when.replace(tzinfo=timezone.utc)
        p["when"] = when.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
        for v in policy.check_text(p["text"]):
            problems.append(f"{p['id']}: {v}")
        for i, t in enumerate(p.get("thread", []) or []):
            for v in policy.check_text(t, is_reply=True):
                problems.append(f"{p['id']}[thread {i+1}]: {v}")
    posts.sort(key=lambda p: p["when"])
    if problems:
        print("calendar refused:\n  " + "\n  ".join(problems))
        return 1
    print(f"{len(posts)} posts, {sum(len(p.get('thread') or []) for p in posts)} thread replies, "
          f"{sum(1 for p in posts if 'http' in p['text'])} posts with a link; all pass the policy")
    if check_only:
        return 0

    OUT_JSON.write_text(json.dumps({"built": datetime.now(timezone.utc).isoformat(timespec="seconds"), "source": "x/calendar.yaml", "posts": posts}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Metricool bulk-import CSV. Metricool's importer wants one row per post with local date and
    # time; threads are not importable by CSV, so a thread's follow-ups are listed in the Notes
    # column for the MCP/API push (tools/push_to_metricool.md explains both paths).
    from zoneinfo import ZoneInfo
    tz = ZoneInfo(METRICOOL_TZ)
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Text", "Date", "Time", "Draft", "Twitter", "Picture Url 1", "Thread (not importable by CSV)", "Id", "Pillar"])
        for p in posts:
            local = datetime.fromisoformat(p["when"].replace("Z", "+00:00")).astimezone(tz)
            w.writerow([p["text"], local.strftime("%Y-%m-%d"), local.strftime("%H:%M"), "FALSE", "TRUE",
                        (p.get("media") or [""])[0], " ||| ".join(p.get("thread") or []), p["id"], p.get("pillar", "")])

    lines = ["# X calendar, 7 October to 6 November 2026 (UTC)", "", "Built from `calendar.yaml`; edit that file, then run `python tools/build_calendar.py`.", ""]
    day = None
    for p in posts:
        d = p["when"][:10]
        if d != day:
            day = d
            lines += ["", f"## {datetime.fromisoformat(d).strftime('%A %d %B %Y')}", ""]
        lines.append(f"**{p['when'][11:16]} UTC** · `{p['id']}` · {p.get('pillar','')}" + (" · thread" if p.get("thread") else "") + (" · image" if p.get("media") else ""))
        lines.append("")
        lines.append("> " + p["text"].replace("\n", "  \n> "))
        for t in p.get("thread") or []:
            lines.append(">> " + t)
        lines.append("")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON.name}, {OUT_CSV.name}, {OUT_MD.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main(check_only="--check" in sys.argv))
