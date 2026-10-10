"""Thin wrapper over tweepy for the few X API v2 calls we need, plus a dry-run twin.

Pay-per-use pricing (2026) bills every call, and a post that contains a URL costs about
13 times a plain post, so this layer counts calls and the policy keeps links rare.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Protocol

log = logging.getLogger("swarm_social.x")


@dataclass
class Post:
    id: str
    text: str
    author_id: str = ""
    author_handle: str = ""
    created_at: str = ""
    conversation_id: str = ""
    in_reply_to_user_id: str = ""
    public_metrics: dict[str, int] = field(default_factory=dict)

    def age_hours(self) -> float:
        if not self.created_at:
            return 0.0
        created = datetime.fromisoformat(self.created_at.replace("Z", "+00:00"))
        return (datetime.now(timezone.utc) - created).total_seconds() / 3600


class XClient(Protocol):
    def me(self) -> dict[str, str]: ...
    def create_post(self, text: str, *, reply_to: str | None = None, quote: str | None = None) -> str: ...
    def like(self, post_id: str) -> None: ...
    def repost(self, post_id: str) -> None: ...
    def mentions(self, since_id: str | None, max_results: int = 25) -> list[Post]: ...
    def search_recent(self, query: str, max_results: int = 10) -> list[Post]: ...
    def user_recent_posts(self, handle: str, max_results: int = 5) -> list[Post]: ...
    def own_recent_posts(self, max_results: int = 10) -> list[Post]: ...


_POST_FIELDS = ["created_at", "author_id", "conversation_id", "in_reply_to_user_id", "public_metrics"]


def _to_posts(response: Any) -> list[Post]:
    if response is None or not getattr(response, "data", None):
        return []
    users = {}
    includes = getattr(response, "includes", None) or {}
    for u in includes.get("users", []) or []:
        users[str(u.id)] = u.username
    out = []
    for t in response.data:
        created = t.created_at.isoformat() if getattr(t, "created_at", None) else ""
        out.append(Post(
            id=str(t.id), text=t.text, author_id=str(getattr(t, "author_id", "") or ""),
            author_handle=users.get(str(getattr(t, "author_id", "")), ""), created_at=created,
            conversation_id=str(getattr(t, "conversation_id", "") or ""),
            in_reply_to_user_id=str(getattr(t, "in_reply_to_user_id", "") or ""),
            public_metrics=dict(getattr(t, "public_metrics", {}) or {}),
        ))
    return out


class TweepyClient:
    """Live client. OAuth 1.0a user context for the single owned account."""

    def __init__(self, api_key: str, api_secret: str, access_token: str, access_secret: str, bearer_token: str = ""):
        import tweepy  # imported here so dry runs and tests need no network stack

        self._client = tweepy.Client(
            bearer_token=bearer_token or None,
            consumer_key=api_key, consumer_secret=api_secret,
            access_token=access_token, access_token_secret=access_secret,
            wait_on_rate_limit=False,
        )
        self.calls: dict[str, int] = {}
        self._me: dict[str, str] | None = None

    def _count(self, name: str) -> None:
        self.calls[name] = self.calls.get(name, 0) + 1

    def me(self) -> dict[str, str]:
        if self._me is None:
            self._count("users.me")
            r = self._client.get_me(user_auth=True)
            self._me = {"id": str(r.data.id), "handle": r.data.username}
        return self._me

    def create_post(self, text: str, *, reply_to: str | None = None, quote: str | None = None) -> str:
        self._count("posts.create")
        r = self._client.create_tweet(text=text, in_reply_to_tweet_id=reply_to, quote_tweet_id=quote, user_auth=True)
        return str(r.data["id"])

    def like(self, post_id: str) -> None:
        self._count("likes.create")
        self._client.like(post_id, user_auth=True)

    def repost(self, post_id: str) -> None:
        self._count("reposts.create")
        self._client.retweet(post_id, user_auth=True)

    def mentions(self, since_id: str | None, max_results: int = 25) -> list[Post]:
        self._count("users.mentions")
        r = self._client.get_users_mentions(
            self.me()["id"], since_id=since_id, max_results=max(5, min(max_results, 100)),
            tweet_fields=_POST_FIELDS, expansions=["author_id"], user_fields=["username"], user_auth=True,
        )
        return _to_posts(r)

    def search_recent(self, query: str, max_results: int = 10) -> list[Post]:
        self._count("posts.search")
        r = self._client.search_recent_tweets(
            query=query, max_results=max(10, min(max_results, 100)),
            tweet_fields=_POST_FIELDS, expansions=["author_id"], user_fields=["username"], user_auth=True,
        )
        return _to_posts(r)

    def user_recent_posts(self, handle: str, max_results: int = 5) -> list[Post]:
        self._count("users.by_username")
        u = self._client.get_user(username=handle.lstrip("@"), user_auth=True)
        if not u.data:
            return []
        self._count("users.posts")
        r = self._client.get_users_tweets(
            u.data.id, max_results=max(5, min(max_results, 100)), exclude=["retweets", "replies"],
            tweet_fields=_POST_FIELDS, user_auth=True,
        )
        posts = _to_posts(r)
        for p in posts:
            p.author_handle = u.data.username
        return posts

    def own_recent_posts(self, max_results: int = 10) -> list[Post]:
        self._count("users.posts")
        r = self._client.get_users_tweets(self.me()["id"], max_results=max(5, min(max_results, 100)), tweet_fields=_POST_FIELDS, user_auth=True)
        return _to_posts(r)


class DryRunClient:
    """Logs every write, performs no network call. Reads return canned or empty data.

    `seed_mentions` / `seed_search` let tests and rehearsals feed the agent realistic input.
    """

    def __init__(self, seed_mentions: list[Post] | None = None, seed_search: list[Post] | None = None, handle: str = "swarm_coin"):
        self.handle = handle
        self.seed_mentions = seed_mentions or []
        self.seed_search = seed_search or []
        self.written: list[dict[str, Any]] = []
        self.calls: dict[str, int] = {}
        self._n = 0

    def _next_id(self) -> str:
        self._n += 1
        return f"dry-{self._n}"

    def me(self) -> dict[str, str]:
        return {"id": "0", "handle": self.handle}

    def create_post(self, text: str, *, reply_to: str | None = None, quote: str | None = None) -> str:
        pid = self._next_id()
        self.written.append({"kind": "post", "id": pid, "text": text, "reply_to": reply_to, "quote": quote})
        log.info("DRY RUN post%s: %s", f" (reply to {reply_to})" if reply_to else "", text)
        return pid

    def like(self, post_id: str) -> None:
        self.written.append({"kind": "like", "post_id": post_id})
        log.info("DRY RUN like %s", post_id)

    def repost(self, post_id: str) -> None:
        self.written.append({"kind": "repost", "post_id": post_id})
        log.info("DRY RUN repost %s", post_id)

    def mentions(self, since_id: str | None, max_results: int = 25) -> list[Post]:
        return list(self.seed_mentions)

    def search_recent(self, query: str, max_results: int = 10) -> list[Post]:
        return list(self.seed_search)

    def user_recent_posts(self, handle: str, max_results: int = 5) -> list[Post]:
        return [p for p in self.seed_search if p.author_handle.lower() == handle.lower().lstrip("@")]

    def own_recent_posts(self, max_results: int = 10) -> list[Post]:
        return [Post(id=w["id"], text=w["text"], author_handle=self.handle) for w in self.written if w["kind"] == "post"][-max_results:]
