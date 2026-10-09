<!-- venue: r/privacycoins (never post the same text anywhere else; a reuse in another subreddit is a rewrite), flair: Discussion (use "Announcement" only if the sidebar offers it), account requirements: a real account older than 3 months with comment history in r/privacycoins; comments in r/privacycoins for at least a week before posting (10 to 21 October 2026 is comments-only), when: Thu 22 Oct 2026 15:00 UTC, the first Reddit post; it moves to Thu 15 Oct 2026 15:00 UTC only if the owner names an aged account with real history by 12 Oct, notes for the human poster: the body starts with "I work on SWARM." and stays that way; answer every comment within 24 hours; never discuss what SWM is worth or any token on another chain; if a moderator removes it, do not repost; links only to swarm.green, mainnet.explore.swarm.green and github.com/Swarmcoin; the story's sources, for a reader who asks: Bitcoin Magazine "Genesis Files" on eCash and the regulation text EUR-Lex 32024R1624; the first posts on Nostr, Bluesky, Farcaster and Mastodon go out the same day -->

# Private digital cash worked in 1995 and was gone by 1998. Why eCash failed, and what that means for a new privacy coin

I work on SWARM. We built it, nothing in this post is for sale, and we will not discuss what SWM is worth in the comments.

## A bank in St. Louis, 1995

In 1982 David Chaum described blind signatures: a bank could sign a digital coin without seeing it, so the coin could not be forged and the bank could not link it to the person who later spent it. He patented the idea in 1983 and founded DigiCash in 1989 to turn it into eCash.

In late 1995 Mark Twain Bank in St. Louis became the first bank to issue it. By 1998 it had enrolled about 300 merchants and about 5,000 users. DigiCash filed for bankruptcy that year, and its assets passed to eCash Technologies and, in 2002, to InfoSpace. (Dates and numbers: Bitcoin Magazine's "Genesis Files" piece on eCash. The reasons are still argued about, so I leave them alone.)

Private digital money was invented 27 years before Bitcoin, and it failed on adoption, not on cryptography. Privacy, unlike most software, needs a crowd. A shielded pool hides you among the people who use it. If almost nobody shields, the few who do stand out.

The crowd question now has a date. EU Regulation 2024/1624, the anti-money-laundering regulation, applies from 10 July 2027. From then, regulated crypto service providers in the EU may not keep accounts without identity checks and may not handle coins whose payments hide sender, receiver and amount. That bans those coins from EU exchanges; it does not ban holding them or paying someone directly. In Europe, private payments will live in self-custody.

## Why I am telling you this

We launched a privacy coin this month, and the eCash story is the honest test for it: a new shielded pool is small. Here is what SWARM is and what is unfinished.

## What is unfinished, first

- No independent audit of the SWARM-specific changes has been published. The components we build on have their own records and open issues; we inherit both.
- The Windows and macOS builds are unsigned; SmartScreen and Gatekeeper warn.
- The browser is a Windows-only pre-release with no tracker blocking and no phishing lists.
- The messenger is a first release: one desktop per account, no phone app.
- The node and CPU-miner app is published only when public mining opens on 1 November 2026, 15:42 UTC. Please keep ASICs and rented hash power off the network.
- The light-wallet server we run learns which encrypted notes your wallet asked for. Not amounts, not counterparties, but not nothing. Your own node and indexer remove it.
- Shielding hides what is on the chain, not that you use SWARM from your ISP.

## What it is

SWARM is a proof-of-work coin built on open-source foundations that have secured real value, left unmodified: the consensus rules and the cryptography are upstream's. Equihash 200,9, the Sapling and Orchard shielded pools, v5 transactions, the public Sapling and Orchard parameters from the upstream protocol's ceremonies. We defined the network: genesis block, network magic, address prefixes, the emission schedule with its allocation, and the apps.

- Block time 75 seconds, 6.25 SWM per block, halving every 1,680,000 blocks (about four years)
- Maximum supply 20,999,987.3152 SWM; the genesis block holds no spendable coins, so every SWM that exists has been mined
- Addresses: `swm1…` shielded (the wallet default), `s1…` transparent, `s3…` transparent script
- Genesis hash `01b76d8a0f18c502b23ab6605e26296d189aa5770fc4a34155e5c7b250a0eff2`
- Mainnet live since 2 October 2026, 15:42 UTC

## Where every block goes

We do not dress this up: 20 % of every block goes to the project for the life of the chain. 80 % to the miner plus all fees, 8 % Core Development, 4 % Grants & Ecosystem, 8 % Community & Development Reserve. The three project destinations are `s3…` 2-of-3 multisig addresses fixed in the genesis rules; the percentages cannot be changed, the destinations only by a formal protocol upgrade. Over the life of the chain that is about 4.2 million SWM. It is not a premine: nothing exists before it is mined, and it is paid block by block in public. It also does not stop after four years.

## The closed start

Until 31 October 2026, 15:42 UTC only the project's own machines mine. In those 29 days about 33,408 blocks are produced, about 208,800 SWM, about 0.99 % of the cap: ordinary blocks, 80 % to the project's mining wallet and 20 % to the three funds, all visible at mainnet.explore.swarm.green. For the next 24 hours the people on the waiting list can mine too, and from 1 November 2026, 15:42 UTC mining is open to everyone, with the node software published on swarm.green at that moment.

The published reason: "the infrastructure around the coin, liquidity pools included, needs coins before public mining begins; the aim is an orderly, predictable start." No coins are promised. Please keep ASICs and rented hash power off the network.

## The apps

- **SWARM Wallet** (Windows, macOS, Linux; the download page also names Android, where a new version is being published): built on zingolib, through our fork privacy-zingolib. Shielded by default.
- **SWARM Messenger** (Windows, macOS on Apple silicon, Linux): Signal Desktop and Signal Server, forked and run on our own server, never on Signal's. You sign in with the wallet's 24 words, no phone number, and you can pay inside the chat. AGPL-3.0.
- **SWARM Browser** (Windows pre-release): ungoogled-chromium on Chromium 153 with the wallet in the toolbar. Keys stay in a small wallet host, not in the renderer. BSD-3-Clause.

Download only from swarm.green/ecosystem, where every file carries its SHA-256. Check it before you install:

```
sha256sum <file>          # Linux
shasum -a 256 <file>      # macOS
Get-FileHash <file>       # Windows PowerShell
```

If the value differs from the page, do not install. We never ask for recovery words, keys or a payment.

## FAQ

**Isn't the 20 % allocation a dev tax?** Yes, in that sense: a fifth of every block reward, split 8 % Core Development, 4 % Grants & Ecosystem, 8 % Community & Development Reserve, to published multisig addresses for the whole life of the chain. It is permanent and we do not dress it up. Whether the trade is worth it is your call.

**Isn't this just another clone with a dev tax? Why fork instead of contributing?** Consensus and cryptography are upstream's, unmodified. What differs is the network, the economics, a messenger that pays inside the chat and a browser with the wallet in the toolbar; a permanent allocation is not something to propose upstream. Bugs in shared code go upstream first.

**Why a closed start?** For the published reason quoted above; about 0.99 % of the cap, in ordinary blocks visible in the explorer.

**ASIC or GPU?** Equihash 200,9, unchanged. ASICs for it exist and nothing in the rules keeps anyone out. We make no promise that home machines stay competitive.

**Is there an audit?** No independent audit of the SWARM-specific changes has been published. The upstream components have their own records.

**What does the light-wallet server learn?** Which encrypted notes a wallet asked for and which transparent addresses it asked about; not amounts or counterparties. Run `zebrad` and `zainod` yourself and it learns nothing.

**What is SWM worth?** Whatever people agree it is worth. Nobody promises you a price, and SWM can lose all its value.

What I would like from this thread: check `doc/protocol.md` and `doc/economics.md` at github.com/Swarmcoin/swarm against the subsidy and funding-stream parameters file (`…/parameters/network/subsidy.rs` in the node repository; `doc/protocol.md` links it), and say where our wording overstates the software.
