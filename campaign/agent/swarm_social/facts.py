"""The source of truth the agent writes from: swarm.green/llms-full.txt and the live status feed.

The agent is never allowed to invent a number. Everything it says about SWARM must come from
these two documents, which the project itself publishes.
"""

from __future__ import annotations

import json
import urllib.request
from pathlib import Path


def _get(url: str, timeout: float = 10.0) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "swarm-social/0.1 (+https://swarm.green)"})
    with urllib.request.urlopen(req, timeout=timeout) as r:  # noqa: S310 - fixed https URLs
        return r.read()


def load_facts(url: str, fallback: Path) -> str:
    try:
        text = _get(url).decode("utf-8")
        if "SWARM" in text and len(text) > 2000:
            return text
    except Exception:  # network is optional; the committed copy is the fallback
        pass
    return fallback.read_text(encoding="utf-8")


def load_status(url: str) -> dict:
    """Live network figures: block height, difficulty, mean block time. Empty dict if unreachable."""
    try:
        data = json.loads(_get(url).decode("utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def status_summary(status: dict) -> str:
    if not status:
        return "Live network status is unavailable right now; do not quote a block height."
    parts = []
    for key in ("height", "blockHeight", "block_height"):
        if key in status:
            parts.append(f"block height {status[key]}")
            break
    for key in ("difficulty",):
        if key in status:
            parts.append(f"difficulty {status[key]}")
    for key in ("meanBlockTime", "mean_block_time", "meanBlockTimeSeconds"):
        if key in status:
            parts.append(f"mean block time over the last 100 blocks {status[key]} s")
            break
    for key in ("updated", "updatedAt", "generatedAt", "timestamp"):
        if key in status:
            parts.append(f"as of {status[key]}")
            break
    return "Live mainnet status from swarm.green/data/status.json: " + ", ".join(parts) + "." if parts else json.dumps(status)[:500]
