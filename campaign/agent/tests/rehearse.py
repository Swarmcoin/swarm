#!/usr/bin/env python3
"""Local dry-run cycle against the recorded fixture, no credentials, no model, no network.

    cd campaign/agent && python tests/rehearse.py            # review mode (default)
    cd campaign/agent && python tests/rehearse.py --auto     # auto mode, as if X had approved the bot

Writes state, queue and last-run.md into a temporary folder and prints the report.
"""

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))   # works without `pip install -e`
from test_dry_run_fixture import _settings, rehearse  # noqa: E402

if __name__ == "__main__":
    auto = "--auto" in sys.argv
    tmp = Path(tempfile.mkdtemp(prefix="swarm-social-rehearsal-"))
    settings = _settings(tmp, approval="auto" if auto else "review", x_ai_approval="rehearsal" if auto else "")
    state, queue, x, out = rehearse(settings)
    print(f"# rehearsal in {tmp}\n")
    print("skipped:", *[f"  @{s['author']}: {s['reason']}" for s in out["seen"]["skipped"]], sep="\n")
    print("\nresults:", *[f"  {k}: {v}" for k, v in out["results"].items()], sep="\n")
    print(f"\nwould have sent (dry run): {len(x.written)}; waiting for a human: {len(queue.pending())}\n")
    print((tmp / "last-run.md").read_text(encoding="utf-8"))
