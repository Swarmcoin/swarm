# SWARM digital footprint: the first month (7 October to 6 November 2026)

One month, one arc: the chain is live, the apps exist, and on 1 November 2026 at 15:42 UTC
mining opens to everyone. Everything in this campaign leads to that date, and everything is
written so that it is still true the day after.

## What we are trying to achieve

| Outcome | How we will know (6 November) |
| --- | --- |
| People who care about financial privacy know SWARM exists and what it is | @swarm_coin followers and profile visits; search volume for "swarm coin"; direct traffic to swarm.green |
| The waiting list is full of people who will actually mine | Sign-ups on swarm.green/waitlist; node downloads on 31 October and 1 November; blocks found by non-project miners in the first week |
| The apps are tried by the people who will tell others | Downloads of Wallet, Messenger and Browser; issues opened on GitHub by outsiders; at least three independent reviews or write-ups |
| SWARM is on the lists that matter | MiningPoolStats, CoinPaprika, Blockspot, CoinGecko preview, CoinMarketCap untracked; at least one pool |
| Nobody can say we promised anything | Zero posts with price, returns or dates we did not keep |

## The pillars (what every piece of content is about)

1. **Facts.** The numbers, the split, the genesis hash, the closed start explained in full.
2. **Product.** Wallet, Messenger, Browser, Node: what each does, and what each does not do yet.
3. **Mining.** The countdown to 1 November, the waiting list, how to prepare, always with
   "No coins are promised."
4. **Landscape.** Why privacy by default matters in 2026: surveillance ledgers, the EU AMLR
   from 10 July 2027, the five questions to ask any privacy coin.
5. **Build.** Open source, upstream credit, verification, running your own node.
6. **Community.** Questions, thanks, bug reports, the scams to expect.

## The channels, in the order we invest

| Channel | Role | Cadence | Automation |
| --- | --- | --- | --- |
| **X (@swarm_coin)** | The base layer and the official voice | 2 posts a day at 09:00 and 16:00 UTC, a thread every Wednesday, exact-time posts at 15:42 UTC on 31 Oct and 1 Nov | Calendar scheduled in Metricool (or by the agent's scheduler); engagement by the agent every 30 min: mention replies autonomous, everything else proposed for one-click approval |
| **Long-form articles** | Depth and search; the material every other channel links to | 4 pieces in week 1 and 2, republished with canonical links | Dev.to and Paragraph by API; Medium by hand (its API is closed) |
| **Reddit** | Where the privacy-coin audience argues | 1 post a week in the right subreddit, daily comments | None (Reddit's API is closing and bots are spam there). A human, from an aged account |
| **Forums** | Bitcointalk ANN, Zcash Community Forum intro, Show HN for the apps, Nostr/Bluesky/Farcaster/Mastodon mirrors | ANN in week 2 once the account ranks; the rest in week 1 and 3 | Mirrors can be scheduled; the rest is human |
| **PR** | Earned coverage and listings | Press release on 7 October (mainnet live, mining opens 1 Nov) and 1 November (mining open); 25 targeted pitches | Drafted; sending is human. Wire service optional (Chainwire from $1,399) |
| **Listings** | Discoverability for miners and trackers | Week 1 forms, week 4 pools | Human, checklist in `forums/README.md` |

## The month, week by week

**Week 1 (7 to 13 October): what SWARM is.** X: definition, numbers, split, closed start,
wallet and messenger. Publish the four articles (`articles/`). Reddit: r/privacycoins and
r/cryptodevs write-ups, r/opensource for the apps. Forums: Zcash Community Forum intro;
first posts on Nostr, Bluesky, Farcaster, Mastodon; register the Bitcointalk account. PR:
release 1 out; pitch DL News, Blockworks, Decrypt, The Defiant, It's FOSS. Listings:
CoinPaprika, Blockspot, CoinGecko preview, CoinMarketCap untracked forms.

**Week 2 (14 to 20 October): the apps.** X: browser pre-release, the ungoogled thread,
addresses, honesty about what is missing. Reddit: r/altcoin and r/cryptocurrencies, comments
in r/zec and r/Monero threads. Forums: Show HN for the browser; Bitcointalk ANN when the
account can post it. PR: pitch the privacy YouTubers and podcasts with the apps, not the
coin; follow up week-1 pitches once.

**Week 3 (21 to 27 October): why it matters.** X: the five questions, the regulation, the
closed-start thread, the explorer, the countdown starts. Reddit: r/degoogle browser post;
r/CryptoMoonShots long-form if the account qualifies. Forums: Lemmy c/privacy; Publish0x and
InLeo republish of the comparison article. PR: pitch the mining angle to MiningPoolStats and
the Equihash pools; prepare release 2.

**Week 4 (28 October to 3 November): the opening.** X: daily countdown, the scams thread,
exact-time posts at 15:42 UTC on the 31st and the 1st, first-day support posts. Reddit:
r/selfhosted node guide; mining subreddits answer "ASIC or GPU?" honestly. PR: release 2 on
1 November; WhatToMine and pool listings as pools appear. The agent's reply budget goes up
for the weekend (humans on call too).

**Week 5 (4 to 6 November): after.** X: what a transaction reveals, the roadmap words, the
month in review. Everywhere: answer every open question, collect the bugs, publish what
shipped. Measure, then plan month two.

## Guardrails that apply to every channel

`VOICE.md` is the contract. In one line each: no price, no promises, no exaggerated
privacy, no audit claim, say what is missing first, official links only, never engage on
price or politics, never automate affection, never DM, security reports go private.

## Budget

| Item | Cost |
| --- | --- |
| X API, pay per use at the planned cadence | about $15 to $30 a month |
| Claude for the engagement agent (48 cycles a day, most of them short) | about $20 to $60 a month at medium effort |
| Metricool X add-on (Starter plan or higher) | about $5 a month plus the plan |
| GitHub Actions | free on a public repository |
| PR wire (optional) | Chainwire $1,399 to $6,499; U.Today $700; Crypto Briefing $300 to $750 |
| Everything else | time |

## What we measure, weekly

X: followers, profile visits, replies received, link clicks per post (Metricool analytics
or the X dashboard). Site: visits to /waitlist, /ecosystem and the articles (GA4 is already
on swarm.green). Chain: blocks found by addresses that are not the project's after 1
November (explorer). Community: GitHub issues from outsiders, Reddit comments answered within
24 h, forum threads alive. PR: pitches sent, replies, pieces published, listings live.

## Owners

Until the team grows, one person owns approvals (the review queue and the Reddit account),
one owns PR sending, and the agent owns the clock. Both humans read `agent/state/last-run.md`
in the Actions summary each morning.
