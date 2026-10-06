<!-- venue: internal plan for the forum, social and listing posts in this folder, flair: n/a, account requirements: see the table, when: weeks 1 to 6 starting the week of 12 October 2026, notes for the human poster: this file is the plan, not a post; read ../VOICE.md and ../research/community-and-forums-2026-10.md first; every venue below is posted by a person from a real account -->

# Forum, social and listing plan

The research file (`../research/community-and-forums-2026-10.md`) says which venues tolerate a new coin and under what conditions. This file turns that into a plan. The posts themselves are in this folder: `bitcointalk-ann.md`, `zcash-community-forum-intro.md` and `show-hn-and-short-posts.md`.

Rules that apply everywhere: say what is missing first; disclose that we built it; link only to swarm.green, mainnet.explore.swarm.green and github.com/Swarmcoin; never mention price or the token on Base; never argue; every mention of mining or the waiting list carries "No coins are promised." or an equivalent; security reports get the SECURITY.md path and nothing else.

## Forums and social venues

| Venue | What to post | Account prerequisites | Timing | Risk notes (from the research file) |
| --- | --- | --- | --- | --- |
| Bitcointalk, Announcements (Altcoins) | `bitcointalk-ann.md`, converted to BBCode by hand; one thread, bumped at most once per 24 h with real news | **Register now.** New accounts cannot post images; a branded ANN realistically needs Jr. Member (30 activity, 1 merit, about 30 days). Earn activity by answering questions elsewhere on the forum first | Thread opens when the account reaches Jr. Member, ideally before 1 November 2026 so the mining date is still ahead | Duplicate threads get merged or deleted; bounty and signature campaigns read as spam and we run none; expect "another Zcash clone" in the first page of replies and answer it once with the FAQ |
| Zcash Community Forum (forum.zcashcommunity.com, Discourse) | `zcash-community-forum-intro.md`; no download links in the first post | Discourse trust level: read for a few days, like and reply to other threads before creating one; read the code of conduct | Week 2, after the Reddit r/privacycoins post has had its first round of questions | Ycash was tolerated as a friendly fork; Zclassic and Bitcoin Private were not. Credit ECC, Zcash Foundation and Zingo Labs; never recruit their contributors; never criticise ZEC; ask whether download links are welcome before posting one |
| Privacy Guides forum (discuss.privacyguides.net) | Nothing from us. The only path is a **tool suggestion** for the browser or the messenger written by a user who is not us, in their own words | A real user with their own account | Only when such a user exists; never prompted by us | No self-promotion unless the tool is listed; a suggestion seeded by the project would be found out and would close the door for good |
| Lemmy (lemmy.ml/c/privacy; lemmy.world crypto communities) | The 300-word browser post from `show-hn-and-short-posts.md` section (c) in c/privacy; verify the rules of any lemmy.world crypto community before posting there | An account on a general instance with some comment history | Week 3, same week as the r/degoogle post | On-topic FOSS is welcome; a coin announcement in c/privacy is not; keep the coin to one sentence |
| Hacker News | Show HN for the browser and, separately and at least two weeks later, for the messenger; text in `show-hn-and-short-posts.md` section (a). **Never** a Show HN for the coin | Account with some comment karma; a brand-new account's Show HN tends to sink | Browser in week 2 or 3 (a weekday, 13:00 to 15:00 UTC); messenger in week 5 or 6 | Strongly anti-crypto; expect hostility about the wallet and answer every technical point once, calmly; do not ask anyone to upvote (HN penalises it) |
| Lobste.rs | Nothing | n/a | n/a | Invite-only, crypto off-topic |
| Nostr | Section (b) first post; then the weekly explainer thread in the same voice | A keypair, a profile that names swarm.green, a NIP-05 on swarm.green if we can set it up | Week 1 | No central moderation; no risk beyond our own wording |
| Bluesky | Section (b) first post, under 300 characters | Account; set the handle to the domain (swarm.green) through DNS verification so it cannot be impersonated | Week 1 | Guidelines since 15 October 2025 with active crypto-scam enforcement; plain facts are fine, anything that reads as a sale is not |
| Farcaster | Section (b) first post | Account | Week 1 | Crypto-native; the "no price" rule still applies, and it will be tested in replies |
| Mastodon | Section (b) first post, under 500 characters, on mastodon.social or infosec.exchange (verify rules); **not** fosstodon.org unless invited, and even then expect crypto-scepticism | Account with a verified link to swarm.green in the profile | Week 1 | Many instances defederate crypto promotion; one post per week at most, replies as a developer |
| Publish0x, Hive/InLeo | A long-form version of the r/privacycoins write-up, rewritten for the platform, with the same FAQ | Account; Publish0x needs author approval | Week 4 | Crypto-native and tolerant; the audience will ask about price, and we do not answer |
| Medium | Not in this folder; see `../medium/` once written | Verified account whose email domain matches the project domain; project domain in the bio | — | Publishing is manual; no bounty or ambassador content |

## Listing sites and mining indexes: checklist

Each row is a form or an email, filled once by a person. None of these involves a payment; if a site asks for one, we do not pay and we say so if asked.

| Site | Listing type | What it needs | Status |
| --- | --- | --- | --- |
| CoinGecko | Preview/untracked (a tracked listing needs a tracked exchange, which we do not have and do not discuss) | Request form; name, ticker, description, swarm.green, explorer URL, GitHub organisation, genesis date, supply figures (max 20,999,987.3152 SWM; circulating from the explorer); regular queue about 5 days | [ ] |
| CoinMarketCap | Untracked (tracked needs an exchange with material volume) | Request form; explorer, site, contact email swarmofficial@atomicmail.io, project description, supply, launch date 2 October 2026 | [ ] |
| CoinPaprika | Free form, about a month | Same facts; logo from swarm.green brand page | [ ] |
| Blockspot | Free form | Same facts; the explorer link | [ ] |
| CoinCodex | Needs a supported exchange | Skip until that exists; do not ask | [ ] |
| CryptoRank | Listing page | Same facts | [ ] |
| MiningPoolStats | New coin via their "new coins" contact; this is the index miners actually read | Algorithm Equihash 200,9, block time 75 s, reward 6.25 SWM, explorer, a pool once one exists; submit after 1 November 2026 when mining is public, with the SWARM Node download linked | [ ] |
| WhatToMine | Pool request form; needs a pool API | Only once a public pool exists; we do not run one and do not promise one | [ ] |

Facts for every form come from `../facts/llms-full.txt`. Never invent a number; if a form demands a figure we do not publish (a price, a market cap), leave it blank or write "not applicable".

## Order of work

1. Week 1: register Bitcointalk; set up Nostr, Bluesky, Farcaster, Mastodon with domain verification; first short posts.
2. Week 2: Zcash Community Forum introduction; Show HN for the browser.
3. Week 3: Lemmy c/privacy browser post.
4. Week 4: Publish0x and InLeo long form; listing forms for CoinGecko, CoinMarketCap, CoinPaprika, Blockspot, CryptoRank.
5. When the Bitcointalk account qualifies: the ANN thread.
6. After 1 November 2026: MiningPoolStats; WhatToMine only once a pool exists; Show HN for the messenger in week 5 or 6.

Keep a log (date, venue, link, outcome) next to this file.
