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
| Like a friendly mention | queued | **queued** (X forbids automated likes) |
| Reply to a post found by search or on a target account | **always queued**, with the agent's reason | **always queued** |
| Original post outside the calendar | queued | published, max 4 a day, not in quiet hours, 45 min apart |
| Follow anyone | never | never |
| DM anyone | never | never |
| Answer a person who asked us to stop | never | never (opt-outs are recorded in the state) |

`auto` needs two variables: `SWARM_SOCIAL_APPROVAL=auto` **and** `SWARM_SOCIAL_X_AI_APPROVAL=<reference of
X's written approval>`. X's Automation Rules (April 2026, II.B.3) require "prior written and explicit
approval from X" for any AI reply bot; without the reference the run stays in review mode and the
summary says so. Owner steps, verified against the vendors' pages: [OWNER-SETUP.md](OWNER-SETUP.md).

Every cycle ends with a plain report; the GitHub Action puts it in the step summary and
commits `state/state.json` (what was done) and `state/review-queue.json` (what waits for you).

## Install and run

```bash
cd campaign/agent
pip install -e ".[dev]"
python -m pytest -q                      # 36 tests: policy, common rules, scheduler, agent tools, fixture cycle
python tests/rehearse.py                 # one dry-run cycle against tests/fixtures, no key, no network
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
| `SWARM_SOCIAL_X_AI_APPROVAL` | reference of X's written approval for an AI reply bot; empty = `auto` is ignored |
| `SWARM_SOCIAL_SCHEDULER` | `0` when Metricool owns the calendar |
| `SWARM_SOCIAL_MODEL`, `SWARM_SOCIAL_EFFORT` | default `claude-opus-5-5`, `medium` |
| `X_API_KEY`, `X_API_SECRET`, `X_ACCESS_TOKEN`, `X_ACCESS_SECRET` | OAuth 1.0a user context for @swarm_coin |
| `X_BEARER_TOKEN` | optional |
| `ANTHROPIC_API_KEY` | Claude |
| `SWARM_SOCIAL_POLICY`, `SWARM_SOCIAL_CALENDAR`, `SWARM_SOCIAL_STATE`, `SWARM_SOCIAL_QUEUE` | paths, for tests and alternative setups |

`policy.yaml` holds the rules: banned phrases and patterns, allowed and denied link hosts,
disclaimer triggers, the ASIC sentence on mining calls, the network-beside-address rule,
opt-out phrases, daily caps, quiet hours, do-not-engage patterns, engagement tiers and search
queries. Change the policy, not the prompt, when you want different behaviour. The marketing
common rules (vault, `marketing/agents/COMMON-RULES.md`, section 4) are each covered by a test
in `tests/test_policy_common_rules.py`.

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

## Compliance notes (X Automation Rules, help.x.com, updated April 2026)

- Automated replies only to people who opted in by mentioning us, one reply per interaction.
- "You may not like posts ... in an automated manner": likes are only ever queued for a human.
- "The deployment or operation of any AI reply bot requires prior written and explicit approval
  from X": auto mode is locked behind `SWARM_SOCIAL_X_AI_APPROVAL`.
- Opt-outs are honoured: a mention that asks us to stop puts the handle into
  `state.json` (`opt_out_handles`) and it is never answered again until a human removes it.
- No automated following, no duplicate posts, no trend posting.
- The agent never DMs. Help goes to swarm.green/support or swarmofficial@atomicmail.io, in public.
- A reply that looks like a vulnerability report gets the SECURITY.md pointer and nothing else.
