# SWARM campaign kit

The first month of SWARM's digital footprint: a 30-day X calendar, an agent that runs the
@swarm_coin account within strict guardrails, long-form articles, Reddit, forum and PR kits,
and the research they rest on. Everything is written so that it is true and stays true.

Start with [STRATEGY.md](STRATEGY.md) (the plan) and [VOICE.md](VOICE.md) (the rules).

| Directory | What is in it |
| --- | --- |
| `x/` | `calendar.yaml` (56 posts and 5 threads, 7 October to 6 November 2026), the built `calendar.json`, `calendar.md` for reading, `metricool-import.csv`, and `engagement-targets.md` |
| `agent/` | `swarm-social`, the Python agent: scheduler, guarded engagement loop, review queue, tests. See [agent/README.md](agent/README.md) |
| `articles/` | Four long-form pieces: the 2026 privacy-coin comparison and three problem-and-solution articles (coin, browser, messenger) |
| `medium/` | How the articles are published: Medium by hand, Dev.to and Paragraph by API |
| `reddit/` | The four-week Reddit plan, six posts and comment templates, for a human to post |
| `forums/` | Bitcointalk ANN, Zcash Community Forum intro, Show HN texts, first posts for Nostr/Bluesky/Farcaster/Mastodon, the listings checklist |
| `pr/` | Two press releases, the media list, pitch emails per segment, the outreach tracker |
| `research/` | What we found out about the X API, Metricool, Reddit, Medium, forums, PR targets and the privacy-coin landscape, with sources |
| `facts/` | A committed copy of swarm.green/llms-full.txt, the only facts the agent may state |
| `tools/` | `build_calendar.py` (validate and build the calendar), `publish_devto.py`, `push_to_metricool.md` |

## The smooth path, for the person running this

1. **Metricool.** Add the @swarm_coin X account to the Metricool brand (X is a paid add-on,
   about $5 a month on Starter or higher). Then either import `x/metricool-import.csv` in
   the planner, or ask the assistant in this workspace to push the calendar through the
   Metricool connector (it schedules threads too). Set the repository variable
   `SWARM_SOCIAL_SCHEDULER=0` so the agent does not also publish the calendar.
2. **X API.** Create a developer app for @swarm_coin at developer.x.com, buy a small credit
   balance (pay per use; about $15 to $30 a month at this cadence), generate OAuth 1.0a
   user tokens with read and write, and put the four values plus a Claude API key in the
   repository secrets named in `.github/workflows/social-x.yml`.
3. **Dry run first.** The workflow runs every 30 minutes in dry-run mode until the variable
   `SWARM_SOCIAL_LIVE` is `1`. Read `campaign/agent/state/last-run.md` in the Actions
   summary for a few days. Nothing is sent.
4. **Go live in review mode.** Set `SWARM_SOCIAL_LIVE=1`. Mention replies are still queued
   until you set `SWARM_SOCIAL_APPROVAL=auto`; proposals to other accounts are always
   queued. Approve from the Actions "Run workflow" button (`approve: all` or ids), or
   locally with `swarm-social approve`.
5. **Then auto.** `SWARM_SOCIAL_APPROVAL=auto` lets the agent answer mentions on its own,
   within the daily caps in `agent/policy.yaml`. Everything else still waits for you.
6. **Articles, Reddit, forums, PR** are human tasks with everything pre-written; each
   directory's README says what to do on which day.

## Keeping it honest

Every outgoing text, scheduled or generated, is checked by `agent/policy.yaml`: no price or
returns, no promises, no exaggerated privacy claims, no audit claim, a disclaimer whenever
mining or rewards come up, official links only, at most one hashtag, 280 characters as X
counts them. `python tools/build_calendar.py` refuses to build a calendar that breaks a rule;
the test suite in `agent/tests` proves the rules hold before each run.
