"""A full dry-run cycle against the recorded fixture, driven the way the model drives the tools,
without a model and without credentials. This is the rehearsal the operator runs before the
first live cycle: `python tests/rehearse.py` prints the same thing as a report."""

import json
from datetime import datetime, timezone
from pathlib import Path

from swarm_social.agent import AgentRun, ReviewQueue
from swarm_social.cli import _write_report
from swarm_social.config import Settings
from swarm_social.policy import Policy
from swarm_social.state import State
from swarm_social.x_client import DryRunClient, Post

ROOT = Path(__file__).resolve().parents[1]
POLICY = Policy.load(ROOT / "policy.yaml")
FIXTURE = json.loads((Path(__file__).parent / "fixtures" / "mentions-2026-10-09.json").read_text(encoding="utf-8"))


def load_fixture_client() -> DryRunClient:
    now = datetime.now(timezone.utc).isoformat()
    mentions = [Post(created_at=now, **m) for m in FIXTURE["mentions"]]
    search = [Post(created_at=now, **p) for p in FIXTURE["search"]]
    return DryRunClient(seed_mentions=mentions, seed_search=search)


def rehearse(settings: Settings, policy: Policy = POLICY) -> tuple[State, ReviewQueue, DryRunClient, dict]:
    """Drive one cycle: mentions, answers, proposals, like suggestion, report. Returns what happened."""
    state, queue = State(settings.state_path), ReviewQueue(settings.queue_path)
    x = load_fixture_client()
    run = AgentRun(settings, policy, state, x, queue)
    t = {tool.name: tool for tool in run.tools()}
    seen = json.loads(t["get_new_mentions"].call({}))
    answers = {
        "privacyfan": "The sender, the receiver and the amount: all three stay encrypted on the chain. What the chain publishes is a proof that the payment is valid. https://swarm.green/what-is-swarm",
        "gpuminer_eu": "Public mining opens on 1 November 2026, 15:42 UTC, with SWARM Node (node and CPU miner) from swarm.green. Equihash 200,9; GPUs work. Please keep ASICs and rented hash power off the network. No coins are promised.",
        "sec_researcher": "Thank you. Please send it privately as described in SECURITY.md in the repository, and nothing in public until it is fixed. https://github.com/Swarmcoin/swarm",
        "zcash_builder": "We have not published the exact Zebra version yet; the fork is privacy-zebra on github.com/Swarmcoin, consensus rules and cryptography unmodified.",
    }
    results = {}
    for m in seen["mentions"]:
        text = answers.get(m["author"])
        if text:
            results[m["author"]] = t["reply_to_mention"].call({"post_id": m["id"], "text": text})
    results["like:zcash_builder"] = t["like_post"].call({"post_id": "1976000000000000006"})
    found = json.loads(t["search_recent"].call({"query_index": 2}))
    for p in found["posts"]:
        if p["author"] == "cryptocurious":
            results["proposal:cryptocurious"] = t["propose_reply"].call({
                "post_id": p["id"],
                "text": "Transparent: sender, receiver and amount are public on the chain. Shielded: the chain only sees a proof that the payment is valid. SWARM shields by default and lets you choose transparent.",
                "reason": "answers a real question with a fact; no promotion",
            })
        if p["author"] == "monero_maxi":
            results["proposal:monero_maxi"] = t["propose_reply"].call({
                "post_id": p["id"],
                "text": "Agreed that defaults matter. That is why SWARM wallets shield by default; transparent is the opt-in, not the other way round.",
                "reason": "fair point, we add the design answer without arguing",
            })
    state.log("agent_cycle", actions=run.actions, queued=len(queue.pending()))
    state.save()
    queue.save()
    _write_report(settings, state, queue, "rehearsal against tests/fixtures/mentions-2026-10-09.json")
    return state, queue, x, {"seen": seen, "found": found, "results": results}


def _settings(tmp_path, **kw) -> Settings:
    s = Settings(calendar_path=ROOT.parent / "x" / "calendar.json", state_path=tmp_path / "state.json",
                 queue_path=tmp_path / "review-queue.json", policy_path=ROOT / "policy.yaml")
    s.dry_run = True
    for k, v in kw.items():
        setattr(s, k, v)
    return s


def test_dry_run_cycle_review_mode(tmp_path):
    state, queue, x, out = rehearse(_settings(tmp_path, approval="review"))
    skipped = {s["author"]: s["reason"] for s in out["seen"]["skipped"]}
    # price talk is filtered before the model sees it; the opt-out is recorded
    assert "degen_trader" in skipped and "do-not-engage" in skipped["degen_trader"]
    assert "tired_user" in skipped and state.data["opt_out_handles"] == ["tired_user"]
    assert {m["author"] for m in out["seen"]["mentions"]} == {"privacyfan", "gpuminer_eu", "sec_researcher", "zcash_builder"}
    # the price-pump search result never reaches the proposals
    assert all(p["author"] != "newsbot" for p in out["found"]["posts"])
    # review mode: everything is queued, nothing is sent, not even in dry run
    assert all("queued" in r for r in out["results"].values()), out["results"]
    assert x.written == []
    kinds = sorted(i["kind"] for i in queue.pending())
    assert kinds == ["like", "reply", "reply", "reply", "reply", "reply", "reply"]
    report = (tmp_path / "last-run.md").read_text(encoding="utf-8")
    assert "auto mode locked" in report and "| `" in report


def test_dry_run_cycle_auto_mode_with_x_approval(tmp_path):
    state, queue, x, out = rehearse(_settings(tmp_path, approval="auto", x_ai_approval="rehearsal"))
    # mention replies go out (dry run), likes and proposals still wait for a human
    assert sum("published" in r for r in out["results"].values()) == 4
    assert "queued" in out["results"]["like:zcash_builder"]
    assert "queued" in out["results"]["proposal:cryptocurious"]
    assert len([w for w in x.written if w["kind"] == "post"]) == 4 and not [w for w in x.written if w["kind"] == "like"]
    assert state.count("replies") == 4 and state.count("likes") == 0
    assert len(queue.pending()) == 3


def test_every_rehearsal_answer_passes_policy():
    """The canned answers in the rehearsal are the kind of reply the agent should write; they must pass."""
    for text in [
        "The sender, the receiver and the amount: all three stay encrypted on the chain. What the chain publishes is a proof that the payment is valid. https://swarm.green/what-is-swarm",
        "Public mining opens on 1 November 2026, 15:42 UTC, with SWARM Node (node and CPU miner) from swarm.green. Equihash 200,9; GPUs work. Please keep ASICs and rented hash power off the network. No coins are promised.",
    ]:
        assert POLICY.check_text(text, is_reply=True) == [], text
