#!/usr/bin/env python3
"""Run the policy's banned phrases, banned patterns and link-host rules over long-form files
(articles, Reddit and forum posts, press releases). Length, hashtag and disclaimer rules are
X-specific and are skipped here. Non-zero exit if anything is found.

    python tools/check_prose.py articles/*.md reddit/*.md forums/*.md pr/*.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

CAMPAIGN = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(CAMPAIGN / "agent"))
from swarm_social.policy import Policy  # noqa: E402

# Links to other projects' sites and to cited sources are fine in articles; only SWARM-looking
# links must be official. Anything on these hosts is checked against the policy's allow-list.
SWARM_LINK_HOSTS = ("swarm", "swm")

# Phrases that are fine in prose when they describe what we do NOT claim.
PROSE_EXEMPT = {"fair launch", "audited", "untraceable", "anonymous coin", "fully anonymous", "100% private", "massive", "huge"}


def main(paths: list[str]) -> int:
    policy = Policy.load(CAMPAIGN / "agent" / "policy.yaml")
    bad = 0
    for p in paths:
        text = Path(p).read_text(encoding="utf-8")
        lowered = text.lower()
        for phrase in policy.banned_phrases:
            if phrase in PROSE_EXEMPT:
                continue
            for m in re.finditer(r"(?<!\w)" + re.escape(phrase) + r"(?!\w)", lowered):
                line = text.count("\n", 0, m.start()) + 1
                print(f"{p}:{line}: banned phrase '{phrase}'")
                bad += 1
        for rx in policy.banned_regex:
            for m in rx.finditer(text):
                line = text.count("\n", 0, m.start()) + 1
                print(f"{p}:{line}: banned pattern '{m.group(0)}'")
                bad += 1
        for m in re.finditer(r"https?://([^\s)\]\"'>]+)", text):
            host = m.group(1).split("/")[0].lower()
            if any(k in host for k in SWARM_LINK_HOSTS):
                full = m.group(0)
                if policy.check_text(full):
                    line = text.count("\n", 0, m.start()) + 1
                    print(f"{p}:{line}: SWARM-looking link to unofficial host {host}")
                    bad += 1
    print(f"{len(paths)} files, {bad} problems")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
