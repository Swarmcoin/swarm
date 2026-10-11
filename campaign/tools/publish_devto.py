#!/usr/bin/env python3
"""Publish a Markdown article (with YAML front matter) to Dev.to through the Forem API.

    DEVTO_API_KEY=... python tools/publish_devto.py articles/top-privacy-coins-2026.md [--publish]

Without --publish the article is created as a draft, so it can be read once more on Dev.to
before it goes out. Front matter keys used: title, description, tags (max 4 on Dev.to),
canonical_url (omitted when it is the swarm.green placeholder), series (optional).
Prints the article URL. Re-running updates the same article if `devto_id` is in the front matter;
the script writes that id back into the file after the first publish.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.request
from pathlib import Path

import yaml

API = "https://dev.to/api/articles"


def split_front_matter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise SystemExit("no YAML front matter")
    return yaml.safe_load(m.group(1)) or {}, m.group(2)


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    publish = "--publish" in sys.argv
    if not args:
        print(__doc__)
        return 2
    key = os.environ.get("DEVTO_API_KEY")
    if not key:
        raise SystemExit("set DEVTO_API_KEY (Dev.to → Settings → Extensions → API keys)")
    path = Path(args[0])
    text = path.read_text(encoding="utf-8")
    meta, body = split_front_matter(text)
    # Dev.to renders the H1 from the title; drop a duplicate first heading in the body.
    body = re.sub(r"^\s*# .+\n", "", body, count=1)
    article = {
        "title": meta["title"],
        "body_markdown": body.strip() + "\n",
        "published": publish,
        "description": meta.get("description", "")[:150],
        "tags": [re.sub(r"[^a-z0-9]", "", t.lower()) for t in (meta.get("tags") or [])][:4],
    }
    canon = meta.get("canonical_url")
    if canon and canon.rstrip("/") not in ("https://swarm.green",):
        article["canonical_url"] = canon
    if meta.get("series"):
        article["series"] = meta["series"]

    payload = json.dumps({"article": article}).encode("utf-8")
    url, method = API, "POST"
    if meta.get("devto_id"):
        url, method = f"{API}/{meta['devto_id']}", "PUT"
    req = urllib.request.Request(url, data=payload, method=method, headers={
        "api-key": key, "Content-Type": "application/json", "Accept": "application/vnd.forem.api-v1+json",
        "User-Agent": "swarm-campaign/0.1 (+https://swarm.green)",
    })
    with urllib.request.urlopen(req, timeout=30) as r:  # noqa: S310
        data = json.loads(r.read().decode("utf-8"))
    print(("published: " if publish else "draft: ") + data.get("url", ""))
    if not meta.get("devto_id") and data.get("id"):
        meta["devto_id"] = data["id"]
        if publish and data.get("url"):
            meta["canonical_url"] = data["url"]
        path.write_text("---\n" + yaml.safe_dump(meta, sort_keys=False, allow_unicode=True) + "---\n" + text.split("\n---\n", 1)[1], encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
