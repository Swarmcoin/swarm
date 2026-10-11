# Reddit, Medium, forums and listings (research, 6 October 2026)

Direct fetches of reddit.com, bitcointalk, forums and listing sites were blocked from the
research sandbox; the facts below come from search excerpts and secondary sources. Items
marked (verify) need a look at the live page.

## Reddit

**The Reddit public Data API is closing.** Announced 30 September 2026: new Data API access
requests stop 31 October 2026, unregistered apps lose access on 12 January 2027, and the
public Data API closes for everyone in March 2027. Bots move to Devvit (mod-installed apps
inside a subreddit, not a promotion channel) or a commercial agreement ($0.24 per 1,000
calls; $12,000 a month bundles). Self-service OAuth app creation already needs a manual
ticket. **Conclusion: no Reddit bot. A human posts from a real, aged account. Automated
promotional posting is spam under Reddit's rules regardless of the API.**

| Subreddit | Size | Rules that matter | Post? |
| --- | --- | --- | --- |
| r/CryptoCurrency | 10.1M | Project self-promotion without a known external source is removed; karma and age gates; strict anti-shilling | Comments and technical discussion only; link a third-party article once one exists |
| r/CryptoMoonShots | 2.3M | Account 3 months and 100 karma; post 1,000+ characters; one post per 24 h; flair required | Possible, low-quality audience; last priority |
| r/privacy | 1.6M | No self-promotion; crypto promotion treated as spam (verify exact text) | No announcement; answer questions in comments only |
| r/PrivacyGuides | 83k | No posts about cryptocurrencies not listed on privacyguides.org | **No** |
| r/privacytoolsIO | — | Dormant | Skip |
| r/Monero | 354k | No price talk; community hostile to other-coin promotion (verify) | No announcement; honest technical comparison in comments only |
| r/zec | 34k | No price or memes; fork policy unknown (verify) | Ask the mods first; a Zcash-stack technical post may be welcome |
| r/privacycoins | small | Topical | **Yes, first home** |
| r/cryptodevs | small | Developer-focused | **Yes**, technical post |
| r/altcoin, r/altcoins, r/cryptocurrencies | small to 13k | Lighter moderation | Yes |
| r/CryptoMarkets | 2.0M | Trading focus, anti-shilling | Later, only with data |
| r/degoogle | 497k | Technical only, no politics | Browser post, framed as a degoogled Chromium build; no coin promotion |
| r/signal | — | Sensitive about third-party clients | Avoid; if asked, say the messenger runs on SWARM's own server, never Signal's |
| r/opensource | 250k | Self-promotion allowed with the "Promotional" flair | **Yes**, browser and messenger repositories |
| r/selfhosted | 639k | Must be about self-hosting | Node and explorer self-hosting guide only |
| r/Bitcoin, r/ethdev, r/0xPolygon | — | Off-topic | No |

Four-week sequence: see `../reddit/README.md`.

## Medium and alternatives

- Medium's API is closed to new integrations since 1 January 2025; no new integration
  tokens. Publishing is manual (editor or RSS import). Medium's cryptocurrency policy: the
  project's email domain must match the verified account email, the project domain goes in
  the bio, no bounty or ambassador content, or the account is treated as spam.
- Publications that take crypto and privacy pieces: Coinmonks (about 1M followers; add as
  writer via their form, verify), Level Up Coding (submit@gitconnected.com with a draft
  link), The Capital, Geek Culture, DataDrivenInvestor (each has a "write for us" page,
  verify).
- With APIs: **Dev.to** (free REST API, `POST /api/articles`, `api-key` header),
  **Paragraph** (Mirror merged into it in November 2025; REST API, CLI, MCP), Ghost (Admin
  API). Hashnode paywalled its API in June 2026. Substack has no write API.
- HackerNoon: contribute.hackernoon.com, human review of 3 to 5 business days, vested
  interest must be disclosed; low-quality blockchain pieces are rejected.

## Forums

- **Bitcointalk**: the announcement goes in Announcements (Altcoins). New accounts cannot
  post images; a branded announcement realistically needs Jr. Member (30 activity, 1
  merit, about 30 days). Bumps once per 24 h, no duplicate threads. **Register the account
  now** and earn activity by answering questions elsewhere on the forum.
- **Zcash Community Forum** (forum.zcashcommunity.com): Discourse, code of conduct.
  Precedent: Ycash announced itself there in 2019 as a friendly fork and was tolerated;
  Zclassic and Bitcoin Private were seen as cash grabs. Credit ECC, Zcash Foundation and
  Zingo Labs; do not recruit their developers; do not attack ZEC.
- **Privacy Guides forum**: no self-promotion unless listed; the path is a tool suggestion
  for the browser or messenger, written by a user, not by us.
- **Lemmy**: lemmy.ml/c/privacy allows on-topic FOSS; lemmy.world crypto communities
  (verify rules).
- **Hacker News**: Show HN only for something people can run (the browser and messenger
  binaries qualify; a coin announcement does not). Strongly anti-crypto; expect hostility
  about the coin.
- **Lobste.rs**: invite-only, crypto off-topic. Skip.
- **Nostr**: no central moderation; announcements are fine. **Bluesky**: new guidelines
  since 15 October 2025, active crypto-scam enforcement; plain facts are fine.
  **Farcaster**: crypto-native, good fit. **Mastodon**: fosstodon.org (invite-only, FOSS,
  crypto-sceptical), mastodon.social, infosec.exchange (verify rules).
- **Publish0x**, **Hive/InLeo**: crypto-native blogging, still active.

## Listings and mining indexes

- CoinGecko: tracked listing needs a tracked exchange; otherwise a "preview/untracked"
  listing via the request form (regular about 5 days, Fast Pass 24 h).
- CoinMarketCap: tracked listing needs an exchange with material volume; untracked listing
  otherwise (explorer, site, contact required).
- CoinPaprika (free form, about a month), Blockspot (free form), CoinCodex (needs a
  supported exchange), CryptoRank listing page.
- **MiningPoolStats** adds new PoW coins through their "new coins" contact; this is the
  index miners actually read. **WhatToMine** adds pools through a request form that needs a
  pool API.
