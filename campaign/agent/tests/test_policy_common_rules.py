"""One test per gap found on 2026-10-09 when policy.yaml was read line by line against the
marketing COMMON-RULES (section 4) and X's Automation Rules (updated April 2026)."""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

from swarm_social.agent import AgentRun, ReviewQueue
from swarm_social.calendar import CalendarPost
from swarm_social.config import Settings, load_settings
from swarm_social.policy import Policy
from swarm_social.scheduler import run_scheduler
from swarm_social.state import State
from swarm_social.x_client import DryRunClient, Post

ROOT = Path(__file__).resolve().parents[1]
POLICY = Policy.load(ROOT / "policy.yaml")

BASE_ADDRESS = "0xf904C14d21bEF5b8a5345a666C77C9cc2A24043B"
SOLANA_MINT = "9Fyen71zwaRs3QfUCsyUooTAkHfNqzUE17xbXwZL6qiH"
RETIRED_SOLANA_MINT = "5VXRk8ZDBrPvYrTnJCWSrK1SzaFkgqkXuY6P2VdYJjHJ"


def rules(text, **kw):
    return {v.rule for v in POLICY.check_text(text, **kw)}


# ----- price: never, in any form, from a project channel

def test_price_without_currency_sign_refused_in_replies():
    assert "banned_pattern" in rules("SWM trades at 4.15 on Base right now", is_reply=True)
    assert "banned_pattern" in rules("the SWM price is now 3.88", is_reply=True)
    assert "banned_pattern" in rules("the token is worth 2.70 on BNB Smart Chain", is_reply=True)
    assert "banned_pattern" in rules("worth about 3 on Solana", is_reply=True)
    # a history story is not a price statement
    assert "banned_pattern" not in rules("250 pesos a week, then worth 250 dollars. The president resigned.")
    # the published answer to price questions still passes
    assert rules("Whatever people agree it is worth. We don't promise a price, and SWM can lose all its value.", is_reply=True) == set()
    # figures that are not prices still pass
    assert rules("6.25 SWM per block, 75-second blocks, halving about every four years.", is_reply=True) == set()


def test_price_venues_never_named():
    assert "banned_phrase" in rules("Check DexScreener for the chart", is_reply=True)
    assert "banned_phrase" in rules("Listed on CoinGecko", is_reply=True)
    assert "banned_phrase" in rules("Swap on Uniswap", is_reply=True)


# ----- how we describe the relationship to Zcash

def test_copy_of_zcash_refused_friendly_fork_allowed():
    assert "banned_phrase" in rules("SWARM is a copy of Zcash with a new name", is_reply=True)
    assert "banned_phrase" in rules("Basically a Zcash clone", is_reply=True)
    assert rules("SWARM is built on the Zcash stack as implemented by Zebra; a friendly fork.", is_reply=True) == set()


# ----- privacy wording

def test_anonymous_refused():
    assert "banned_phrase" in rules("Payments are anonymous", is_reply=True)
    assert "banned_phrase" in rules("Full anonymity for everyone", is_reply=True)
    assert "banned_phrase" in rules("SWARM gives you anonymous payments", is_reply=True)
    # a history story or a regulation summary may use the word
    assert "banned_phrase" not in rules("The FBI sent him an anonymous letter urging him to kill himself.")
    assert "banned_phrase" not in rules("Crypto services may not offer anonymous accounts from 10 July 2027.")
    assert rules("Shielded payments keep the sender, the receiver and the amount encrypted on the chain.", is_reply=True) == set()


# ----- no testnet wording outward

def test_testnet_wording_and_explorer_refused():
    assert "banned_phrase" in rules("Try it on the testnet first", is_reply=True)
    assert "link_denied" in rules("https://testnet.explore.swarm.green/", is_reply=True)
    assert "link_host" not in rules("https://explore.swarm.green/ (SWARM mainnet)", is_reply=True)
    assert "link_host" not in rules("https://wallet.swarm.green/", is_reply=True)
    assert "link_host" not in rules("https://chat.swarm.green/", is_reply=True)


# ----- addresses carry their network

def test_address_needs_network_named_beside_it():
    assert "network_missing" in rules(f"The SWM token: {BASE_ADDRESS}", is_reply=True)
    assert "network_missing" not in rules(f"The SWM token on Base and on BNB Smart Chain: {BASE_ADDRESS}", is_reply=True)
    assert "network_missing" in rules(f"Mint {SOLANA_MINT}", is_reply=True)
    assert "network_missing" not in rules(f"Solana mint: {SOLANA_MINT}", is_reply=True)


def test_retired_solana_mint_refused():
    assert "banned_pattern" in rules(f"Solana mint: {RETIRED_SOLANA_MINT}", is_reply=True)
    assert "banned_pattern" not in rules(f"Solana mint: {SOLANA_MINT}", is_reply=True)


# ----- no multilevel in SWARM marketing

def test_multilevel_words_refused():
    for text in ("Build your downline", "MLM style rewards", "seven referral levels", "the leg leader share"):
        assert "banned_phrase" in rules(text, is_reply=True), text


# ----- downloads come from swarm.green, never a github release

def test_github_release_link_refused_code_link_allowed():
    assert "link_denied" in rules("https://github.com/Swarmcoin/swarm/releases/latest", is_reply=True)
    assert "link_denied" in rules("https://github.com/Swarmcoin/swarm-node/releases/download/v1/x.zip", is_reply=True)
    assert rules("Code: https://github.com/Swarmcoin/swarm", is_reply=True) == set()
    assert rules("Download: https://swarm.green/ecosystem", is_reply=True) == set()


# ----- every mining call carries the ASIC sentence

def test_mining_call_needs_asic_sentence():
    call = "Public mining is open. Anyone can run SWARM Node from this moment. No coins are promised."
    assert "mining_call" in rules(call)
    assert "mining_call" not in rules(call + " Please keep ASICs and rented hash power off the network.")
    # replies answer a question briefly and are exempt, like the disclaimer rule
    assert "mining_call" not in rules("Mining opens on 1 November.", is_reply=True)
    # a post that merely mentions mining is not a call
    assert "mining_call" not in rules("Every SWM that exists has been mined. No coins are promised.")


def test_scheduler_accepts_asic_sentence_anywhere_in_the_package(tmp_path):
    now = datetime.now(timezone.utc)
    cal = {"posts": [
        {"id": "call-ok", "when": now.isoformat(), "text": "Public mining is open. Anyone can run SWARM Node from this moment. No coins are promised.",
         "thread": ["Please keep ASICs and rented hash power off the network."]},
        {"id": "call-bad", "when": now.isoformat(), "text": "Public mining is open. Anyone can run SWARM Node from this moment. No coins are promised.",
         "thread": ["Download from swarm.green."]},
    ]}
    cal_path = tmp_path / "calendar.json"
    cal_path.write_text(json.dumps(cal))
    s = Settings(calendar_path=cal_path, state_path=tmp_path / "state.json", queue_path=tmp_path / "q.json", policy_path=ROOT / "policy.yaml")
    s.dry_run = True
    state = State(s.state_path)
    assert run_scheduler(s, POLICY, state, DryRunClient()) == ["call-ok"]
    refused = [e for e in state.data["log"] if e["action"] == "refused_calendar_post"]
    assert refused and refused[0]["id"] == "call-bad" and any("mining_call" in p for p in refused[0]["problems"])


# ----- X Automation Rules: opt-outs are honoured, likes are never automated, AI replies need X's approval

def _mention(id_, author, text):
    return Post(id=id_, text=text, author_handle=author, author_id="7", created_at=datetime.now(timezone.utc).isoformat())


def _settings(tmp_path, **kw):
    cal = tmp_path / "calendar.json"
    cal.write_text(json.dumps({"posts": []}))
    s = Settings(calendar_path=cal, state_path=tmp_path / "state.json", queue_path=tmp_path / "queue.json", policy_path=ROOT / "policy.yaml")
    s.dry_run = True
    for k, v in kw.items():
        setattr(s, k, v)
    return s


def test_opt_out_is_recorded_and_honoured(tmp_path):
    assert POLICY.is_opt_out("@swarm_coin stop replying to me")
    assert POLICY.is_opt_out("@swarm_coin please don't reply")
    assert not POLICY.is_opt_out("@swarm_coin what does shielded mean?")
    s = _settings(tmp_path, approval="auto", x_ai_approval="test-approval")
    state = State(s.state_path)
    x = DryRunClient(seed_mentions=[_mention("1", "carol", "@swarm_coin stop replying to me")])
    run = AgentRun(s, POLICY, state, x, ReviewQueue(s.queue_path))
    tools = {t.name: t for t in run.tools()}
    out = json.loads(tools["get_new_mentions"].call({}))
    assert out["mentions"] == [] and "opt-out" in out["skipped"][0]["reason"]
    assert state.data["opt_out_handles"] == ["carol"]
    # a later, friendly mention from the same person is still never answered
    x.seed_mentions = [_mention("2", "carol", "@swarm_coin how does mining work?")]
    run2 = AgentRun(s, POLICY, state, x, ReviewQueue(s.queue_path))
    out2 = json.loads({t.name: t for t in run2.tools()}["get_new_mentions"].call({}))
    assert out2["mentions"] == [] and "opted out" in out2["skipped"][0]["reason"]


def test_likes_are_never_automated_even_in_auto_mode(tmp_path):
    s = _settings(tmp_path, approval="auto", x_ai_approval="test-approval")
    x = DryRunClient(seed_mentions=[_mention("1", "dave", "@swarm_coin nice work on the wallet")])
    run = AgentRun(s, POLICY, State(s.state_path), x, ReviewQueue(s.queue_path))
    tools = {t.name: t for t in run.tools()}
    tools["get_new_mentions"].call({})
    out = tools["like_post"].call({"post_id": "1"})
    assert "queued" in out and x.written == []
    assert "refused" in tools["like_post"].call({"post_id": "1"})


def test_auto_mode_locked_without_x_written_approval(monkeypatch):
    assert Settings(approval="auto", x_ai_approval="").effective_approval()[0] == "review"
    assert Settings(approval="auto", x_ai_approval="X ticket 2026-11-01").effective_approval()[0] == "auto"
    assert Settings(approval="review", x_ai_approval="").effective_approval()[0] == "review"
    monkeypatch.setenv("SWARM_SOCIAL_APPROVAL", "auto")
    monkeypatch.delenv("SWARM_SOCIAL_X_AI_APPROVAL", raising=False)
    assert load_settings().approval == "review"
    monkeypatch.setenv("SWARM_SOCIAL_X_AI_APPROVAL", "X ticket 2026-11-01")
    assert load_settings().approval == "auto"
