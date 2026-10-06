# swarm-social: the @swarm_coin agent

Two layers, one policy.

**The scheduler** publishes the posts in `../x/calendar.json` whose time has come. No model
is involved; a calendar post that breaks the policy is refused and logged, never published.
Turn it off (`SWARM_SOCIAL_SCHEDULER=0`) when Metricool publishes the calendar.

**The agent** runs one cycle at a time with Claude (`claude-opus-5-5` by default) through the
SDK's tool runner. It can only act through tools, and every tool enforces the policy and the
budget. What it may do on its own, and what it may only propose, follows X's Automation Rules:

| Action | Mode `review` (default) | Mode `auto` |
| --- | --- | --- |
| Reply to a post that @mentioned us | queued for approval | published, within caps |
| Like a friendly mention | queued | done, within caps |
| Reply to a post found by search or on a target account | **always queued**, with the agent's reason | **always queued** |
| Original post outside the calendar | queued | published, max 4 a day, not in quiet hours, 45 min apart |
| Follow anyone | never | never |
| DM anyone | never | never |

Every cycle ends with a plain report; the GitHub Action puts it in the step summary and
commits `state/state.json` (what was done) and `state/review-queue.json` (what waits for you).

## Install and run

```bash
cd campaign/agent
pip install -e ".[dev]"
python -m pytest -q                      # 16 tests: policy, scheduler, agent tools
swarm-social status                      # what is due, today's counters, queue size
swarm-social check "SWM is going to $5"  # ✗ banned_pattern
swarm-social post-due                    # publish due calendar posts (dry run unless LIVE)
swarm-social engage                      # one agentic cycle
swarm-social queue                       # the review queue as a table
swarm-social approve a1b2c3d4 e5f6a7b8   # or --all
swarm-social reject --all
```

Without `SWARM_SOCIAL_LIVE=1` nothing touches X: a dry-run client logs what would have been
sent. Without `ANTHROPIC_API_KEY`, `engage` cannot run; `post-due` does not need it.

## Configuration

| Variable | Meaning |
| --- | --- |
| `SWARM_SOCIAL_LIVE` | `1` to publish. Default: dry run |
| `SWARM_SOCIAL_APPROVAL` | `review` (default) or `auto` |
| `SWARM_SOCIAL_SCHEDULER` | `0` when Metricool owns the calendar |
| `SWARM_SOCIAL_MODEL`, `SWARM_SOCIAL_EFFORT` | default `claude-opus-5-5`, `medium` |
| `X_API_KEY`, `X_API_SECRET`, `X_ACCESS_TOKEN`, `X_ACCESS_SECRET` | OAuth 1.0a user context for @swarm_coin |
| `X_BEARER_TOKEN` | optional |
| `ANTHROPIC_API_KEY` | Claude |
| `SWARM_SOCIAL_POLICY`, `SWARM_SOCIAL_CALENDAR`, `SWARM_SOCIAL_STATE`, `SWARM_SOCIAL_QUEUE` | paths, for tests and alternative setups |

`policy.yaml` holds the rules: banned phrases and patterns, allowed link hosts, disclaimer
triggers, daily caps, quiet hours, do-not-engage patterns, engagement tiers and search
queries. Change the policy, not the prompt, when you want different behaviour.

## Where the agent gets its facts

The system prompt contains `VOICE.md`, the live copy of swarm.green/llms-full.txt (with the
committed copy in `../facts/` as fallback) and the live network status from
swarm.green/data/status.json. The agent is told to say "we have not published that yet"
rather than guess, and the policy refuses dollar figures and promises regardless.

## Costs

X API is pay per use (post about $0.015, a post with a link about $0.20, a read about
$0.005). The 30-minute cycle reads mentions and a handful of timelines; at the planned
cadence the account costs roughly $15 to $30 a month. Claude at medium effort costs a few
cents per cycle; most cycles find nothing and end early.

## Compliance notes

- Automated replies only to people who mentioned us: X Automation Rules.
- No automated following, no bulk liking, no duplicate posts, no trend posting.
- The agent never DMs. Help goes to swarm.green/support or swarmofficial@atomicmail.io, in public.
- A reply that looks like a vulnerability report gets the SECURITY.md pointer and nothing else.
