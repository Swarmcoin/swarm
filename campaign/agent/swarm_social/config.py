"""Configuration from environment variables. Nothing here is secret by itself."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

AGENT_DIR = Path(__file__).resolve().parent.parent          # campaign/agent
CAMPAIGN_DIR = AGENT_DIR.parent                              # campaign


def _truthy(value: str | None, default: bool) -> bool:
    if value is None or value.strip() == "":
        return default
    return value.strip().lower() in {"1", "true", "yes", "on", "live"}


@dataclass
class Settings:
    # Safety switch. LIVE must be set explicitly to actually publish anything.
    dry_run: bool = field(default_factory=lambda: not _truthy(os.getenv("SWARM_SOCIAL_LIVE"), False))
    # "auto" publishes directly; "review" writes every outgoing action to the review queue
    # and publishes nothing until `swarm-social approve` is run.
    approval: str = field(default_factory=lambda: os.getenv("SWARM_SOCIAL_APPROVAL", "review"))

    # X API v2, OAuth 1.0a user context (read + write) for the @swarm_coin account.
    x_api_key: str = field(default_factory=lambda: os.getenv("X_API_KEY", ""))
    x_api_secret: str = field(default_factory=lambda: os.getenv("X_API_SECRET", ""))
    x_access_token: str = field(default_factory=lambda: os.getenv("X_ACCESS_TOKEN", ""))
    x_access_secret: str = field(default_factory=lambda: os.getenv("X_ACCESS_SECRET", ""))
    x_bearer_token: str = field(default_factory=lambda: os.getenv("X_BEARER_TOKEN", ""))

    # Claude. The SDK also reads ANTHROPIC_API_KEY itself; we only need the model name here.
    model: str = field(default_factory=lambda: os.getenv("SWARM_SOCIAL_MODEL", "claude-opus-5-5"))
    effort: str = field(default_factory=lambda: os.getenv("SWARM_SOCIAL_EFFORT", "medium"))

    # Paths
    policy_path: Path = field(default_factory=lambda: Path(os.getenv("SWARM_SOCIAL_POLICY", AGENT_DIR / "policy.yaml")))
    calendar_path: Path = field(default_factory=lambda: Path(os.getenv("SWARM_SOCIAL_CALENDAR", CAMPAIGN_DIR / "x" / "calendar.json")))
    state_path: Path = field(default_factory=lambda: Path(os.getenv("SWARM_SOCIAL_STATE", AGENT_DIR / "state" / "state.json")))
    queue_path: Path = field(default_factory=lambda: Path(os.getenv("SWARM_SOCIAL_QUEUE", AGENT_DIR / "state" / "review-queue.json")))
    facts_fallback: Path = field(default_factory=lambda: CAMPAIGN_DIR / "facts" / "llms-full.txt")

    facts_url: str = "https://swarm.green/llms-full.txt"
    status_url: str = "https://swarm.green/data/status.json"

    # When Metricool publishes the calendar, the scheduler here must stay off,
    # otherwise every scheduled post goes out twice.
    scheduler_enabled: bool = field(default_factory=lambda: _truthy(os.getenv("SWARM_SOCIAL_SCHEDULER"), True))

    def x_credentials_present(self) -> bool:
        return all([self.x_api_key, self.x_api_secret, self.x_access_token, self.x_access_secret])


def load_settings() -> Settings:
    return Settings()
