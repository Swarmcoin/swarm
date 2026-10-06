from pathlib import Path

from swarm_social.policy import Policy

POLICY = Policy.load(Path(__file__).resolve().parents[1] / "policy.yaml")


def rules(text, **kw):
    return {v.rule for v in POLICY.check_text(text, **kw)}


def test_plain_fact_passes():
    assert rules("SWARM is private money. Shielded payments keep sender, receiver and amount encrypted on the chain. https://swarm.green/what-is-swarm") == set()


def test_price_talk_refused():
    assert "banned_pattern" in rules("SWM is trading at $0.60 today")
    assert "banned_phrase" in rules("SWM is going to the moon")
    assert "banned_pattern" in rules("up 40% gain this week")


def test_hype_refused():
    assert "banned_phrase" in rules("A revolutionary privacy coin 🚀")


def test_privacy_overclaims_refused():
    assert "banned_phrase" in rules("SWARM payments are untraceable")
    assert "banned_phrase" in rules("SWARM is fully anonymous")
    assert "banned_phrase" in rules("The code is audited")


def test_unofficial_link_refused():
    assert "link_host" in rules("Trade here https://some-exchange.example/swm")
    assert "link_host" not in rules("Chain: https://mainnet.explore.swarm.green/")
    assert "link_host" not in rules("Code: https://github.com/Swarmcoin/swarm")
    assert "link_host" in rules("Code: https://github.com/someone-else/swarm")


def test_mining_needs_disclaimer():
    assert "disclaimer" in rules("Public mining opens on 1 November 2026, 15:42 UTC.")
    assert "disclaimer" not in rules("Public mining opens on 1 November 2026, 15:42 UTC. No coins are promised.")
    # replies are exempt from the disclaimer rule (they answer a question, briefly)
    assert "disclaimer" not in rules("Mining opens on 1 November.", is_reply=True)


def test_length_and_hashtags():
    assert "length" in rules("x" * 281)
    assert "hashtags" in rules("Privacy by default #privacy #zcash")
    assert "hashtags" not in rules("Privacy by default #privacy")


def test_tone():
    assert "tone" in rules("Live!! Now!!")


def test_do_not_engage():
    assert POLICY.may_engage_with("when will SWM list on Binance?", "someone")[0] is False
    assert POLICY.may_engage_with("free airdrop send 1 SWM get 2", "someone")[0] is False
    assert POLICY.may_engage_with("How does a shielded address differ from a transparent one?", "someone")[0] is True
