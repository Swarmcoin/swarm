import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from swarm_social.agent import AgentRun, ReviewQueue
from swarm_social.calendar import CalendarPost, due_posts
from swarm_social.config import Settings
from swarm_social.policy import Policy
from swarm_social.scheduler import run_scheduler
from swarm_social.state import State
from swarm_social.x_client import DryRunClient, Post

ROOT = Path(__file__).resolve().parents[1]
POLICY = Policy.load(ROOT / "policy.yaml")


def _settings(tmp_path, calendar, **kw) -> Settings:
    cal = tmp_path / "calendar.json"
    cal.write_text(json.dumps({"posts": calendar}))
    s = Settings(calendar_path=cal, state_path=tmp_path / "state.json", queue_path=tmp_path / "queue.json", policy_path=ROOT / "policy.yaml")
    for k, v in kw.items():
        setattr(s, k, v)
    return s


def test_due_posts_window():
    now = datetime(2026, 10, 10, 12, 0, tzinfo=timezone.utc)
    posts = [
        CalendarPost("a", now - timedelta(hours=1), "due"),
        CalendarPost("b", now - timedelta(hours=10), "stale, skipped"),
        CalendarPost("c", now + timedelta(hours=1), "future"),
    ]
    assert [p.id for p in due_posts(posts, set(), now)] == ["a"]
    assert due_posts(posts, {"a"}, now) == []


def test_scheduler_publishes_thread_and_refuses_policy_breaks(tmp_path):
    now = datetime.now(timezone.utc)
    when = (now - timedelta(minutes=5)).isoformat()
    cal = [
        {"id": "ok", "when": when, "text": "SWARM is private money.", "thread": ["Shielded by default.", "Transparent when you choose."], "reply": "Details: https://swarm.green"},
        {"id": "bad", "when": when, "text": "SWM to the moon 🚀"},
    ]
    s = _settings(tmp_path, cal, dry_run=True)
    state = State(s.state_path)
    x = DryRunClient()
    published = run_scheduler(s, POLICY, state, x)
    assert published == ["ok"]
    posts = [w for w in x.written if w["kind"] == "post"]
    assert len(posts) == 4 and posts[1]["reply_to"] == posts[0]["id"] and posts[2]["reply_to"] == posts[1]["id"]
    # the link travels in the first reply under the thread, never in the post itself
    assert posts[3]["reply_to"] == posts[2]["id"] and "https://swarm.green" in posts[3]["text"]
    assert state.data["posted_calendar_ids"] == ["ok"]
    assert any(e["action"] == "refused_calendar_post" for e in state.data["log"])
    # second run: nothing new
    assert run_scheduler(s, POLICY, State(s.state_path), DryRunClient()) == []


def _tools(run):
    return {t.name: t for t in run.tools()}


def _mention(id_="1001", author="alice", text="@swarm_coin what does a shielded payment hide?"):
    return Post(id=id_, text=text, author_handle=author, author_id="7", created_at=datetime.now(timezone.utc).isoformat())


def test_agent_tools_review_mode_queues_everything(tmp_path):
    s = _settings(tmp_path, [], dry_run=True, approval="review")
    state, queue = State(s.state_path), ReviewQueue(s.queue_path)
    x = DryRunClient(seed_mentions=[_mention()])
    run = AgentRun(s, POLICY, state, x, queue)
    t = _tools(run)
    mentions = json.loads(t["get_new_mentions"].call({}))
    assert [m["id"] for m in mentions["mentions"]] == ["1001"]
    out = t["reply_to_mention"].call({"post_id": "1001", "text": "The sender, the receiver and the amount. https://swarm.green/what-is-swarm"})
    assert "queued" in out
    assert len(queue.pending()) == 1 and x.written == []


def test_agent_tools_auto_mode_publishes_mention_reply_only(tmp_path):
    s = _settings(tmp_path, [], dry_run=True, approval="auto")
    state, queue = State(s.state_path), ReviewQueue(s.queue_path)
    found = Post(id="2002", text="Thinking about shielded payments lately", author_handle="bob", created_at=datetime.now(timezone.utc).isoformat())
    x = DryRunClient(seed_mentions=[_mention()], seed_search=[found])
    run = AgentRun(s, POLICY, state, x, queue)
    t = _tools(run)
    t["get_new_mentions"].call({})
    t["search_recent"].call({"query_index": 2})
    # keyword-found post: direct reply refused, proposal allowed
    assert "refused" in t["reply_to_mention"].call({"post_id": "2002", "text": "Hello"})
    assert "queued" in t["propose_reply"].call({"post_id": "2002", "text": "Shielded means the chain verifies the payment without learning sender, receiver or amount.", "reason": "answers the question"})
    # mention: published directly
    out = t["reply_to_mention"].call({"post_id": "1001", "text": "The sender, the receiver and the amount."})
    assert "published" in out
    assert state.count("replies") == 1 and "1001" in state.data["replied_post_ids"]
    # second reply to the same post refused
    assert "refused" in t["reply_to_mention"].call({"post_id": "1001", "text": "Again"})
    # like only on mentions
    assert "refused" in t["like_post"].call({"post_id": "2002"})
    assert "liked" in t["like_post"].call({"post_id": "1001"})


def test_policy_blocks_agent_text(tmp_path):
    s = _settings(tmp_path, [], dry_run=True, approval="auto")
    run = AgentRun(s, POLICY, State(s.state_path), DryRunClient(seed_mentions=[_mention()]), ReviewQueue(s.queue_path))
    t = _tools(run)
    t["get_new_mentions"].call({})
    assert "refused by policy" in t["reply_to_mention"].call({"post_id": "1001", "text": "SWM is $5 soon, buy now"})


def test_do_not_engage_filters_mentions(tmp_path):
    s = _settings(tmp_path, [], dry_run=True)
    x = DryRunClient(seed_mentions=[_mention(text="@swarm_coin wen Binance listing? price?")])
    run = AgentRun(s, POLICY, State(s.state_path), x, ReviewQueue(s.queue_path))
    out = json.loads(_tools(run)["get_new_mentions"].call({}))
    assert out["mentions"] == [] and out["skipped"][0]["id"] == "1001"


def test_action_cap_per_run(tmp_path):
    s = _settings(tmp_path, [], dry_run=True, approval="auto")
    state = State(s.state_path)
    mentions = [_mention(id_=str(3000 + i), author=f"user{i}") for i in range(12)]
    run = AgentRun(s, POLICY, state, DryRunClient(seed_mentions=mentions), ReviewQueue(s.queue_path))
    t = _tools(run)
    t["get_new_mentions"].call({})
    results = [t["reply_to_mention"].call({"post_id": str(3000 + i), "text": "Shielded hides sender, receiver and amount."}) for i in range(12)]
    assert sum("published" in r for r in results) == POLICY.cap("max_actions_per_run")
    assert any("action cap" in r for r in results)
