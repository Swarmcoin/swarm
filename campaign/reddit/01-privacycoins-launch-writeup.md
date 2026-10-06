<!-- venue: r/privacycoins (reusable in r/cryptodevs only after swapping in the technical lead from 02 and rewriting; never post the same text twice), flair: Discussion (use "Announcement" only if the sidebar offers it), account requirements: a real account older than 3 months with comment history in r/privacycoins and r/zec; comment in the sub for one week before posting, when: week 1, notes for the human poster: post on a weekday between 14:00 and 17:00 UTC; state in the first line that you work on the project; answer every comment within 24 hours; never discuss price or the token on Base; if a moderator removes it, do not repost; links only to swarm.green, mainnet.explore.swarm.green and github.com/Swarmcoin -->

# SWARM (SWM) mainnet is live: a Zcash-stack privacy coin with a wallet, a messenger and a browser. Here is exactly how it works and what is unfinished.

Disclosure: we are the people who built this. This is a description, not a pitch. Nothing here is advice to buy anything, and we will not discuss price in the comments.

## What is unfinished, first

- No independent audit of the SWARM-specific changes has been published. The upstream components (Zebra, Zaino, zingolib, Signal, Chromium) have their own security records and their own open issues; we inherit both.
- The Windows and macOS builds are unsigned. SmartScreen and Gatekeeper warn, and they are right to.
- The browser is a Windows-only pre-release with no tracker blocking and no phishing lists. Safe Browsing went out with the rest of Google's services and nothing has replaced it yet.
- The messenger is a first release: one desktop per account, no phone app.
- The node and CPU-miner app is not published until public mining opens on 1 November 2026, 15:42 UTC. Until then only the project's own machines mine (more on that below).
- The light-wallet server we run learns which encrypted notes your wallet asked for. Not amounts, not counterparties, but it is not nothing. Running your own node and indexer removes it.
- Shielding hides what is written to the chain. It does not hide from your ISP that you use SWARM.

## What it is

SWARM is a proof-of-work coin on the Zcash protocol stack as implemented by Zebra, the Zcash Foundation's full node. The consensus rules and the cryptography are the upstream ones, unmodified: Equihash 200,9, Sapling and Orchard shielded pools, v5 transactions, the public Sapling and Orchard parameters from the Zcash ceremonies. What we defined is the network itself: a genesis block, the network magic, address prefixes, an emission schedule with a fixed allocation, and the apps around it.

The numbers:

- Block time 75 seconds, 6.25 SWM per block, halving every 1,680,000 blocks (about four years)
- Maximum supply 20,999,987.3152 SWM
- Genesis block holds 0 spendable coins; every SWM that exists has been mined
- Coinbase maturity 100 blocks
- Mainnet addresses: `swm1…` shielded (unified, the wallet default), `s1…` transparent, `s3…` transparent script
- Genesis hash `01b76d8a0f18c502b23ab6605e26296d189aa5770fc4a34155e5c7b250a0eff2`
- Live since 2 October 2026, 15:42 UTC

The table of what is inherited and what we defined is in `doc/protocol.md` at github.com/Swarmcoin/swarm.

## Where every block goes

Every block, for the whole emission schedule: 80% to the miner (plus all fees), 8% to Core Development, 4% to Grants & Ecosystem, 8% to a Community & Development Reserve. The three project destinations are `s3…` 2-of-3 multisig addresses fixed in the genesis rules; the percentages cannot be changed, the destinations only by a formal protocol upgrade. Over the life of the chain about 4.2 million SWM go to those three addresses.

It is a permanent allocation. It is not a premine, because nothing exists before it is mined and it is paid block by block where anyone can see it in the explorer. But it does not end the way Zcash's Founders' Reward ended after four years, and we do not call SWARM a "fair launch". Those words would be false.

## The closed start

Until 31 October 2026, 15:42 UTC only the project's own machines can mine. In those 29 days about 33,408 blocks are produced, about 208,800 SWM, about 0.99% of the cap. Those are ordinary blocks: 80% to the project's mining wallet, 20% to the three funds, all visible at mainnet.explore.swarm.green. For the following 24 hours the people on the waiting list can mine too, and from 1 November 2026, 15:42 UTC mining is open to everyone, with the node software published on swarm.green at that moment.

The published reason, quoted from the site: "the infrastructure around the coin, liquidity pools included, needs coins before public mining begins; the aim is an orderly, predictable start." You can disagree with that reasoning. We would rather you disagreed with the real one than with a hidden one. No coins are promised.

## The apps

- **SWARM Wallet** (Windows, macOS, Linux, Android APK): a fork of Zingo PC and zingo-mobile. Shielded by default; it labels every address with its kind.
- **SWARM Messenger** (Windows, macOS on Apple silicon, Linux): a fork of Signal Desktop and Signal Server, running on our own server and never on Signal's. You sign in with the wallet's 24 words, no phone number, and you can pay inside the chat. AGPL-3.0.
- **SWARM Browser** (Windows pre-release): ungoogled-chromium, Chromium 153, with the wallet in the toolbar. The keys live in a small wallet host installed next to the browser, not in the renderer. BSD-3-Clause.

## Before you install anything

Download only from swarm.green/ecosystem. Every file is listed with its SHA-256. Check it:

```
sha256sum <file>                        # Linux
shasum -a 256 <file>                    # macOS
Get-FileHash <file>                     # Windows PowerShell
```

Compare the output with the value on the download page; if it differs, do not install. We never ask for recovery words, keys or a payment.

## What we would like from you

Read `doc/protocol.md` and `doc/economics.md`, check the funding-stream code in `zebra-chain/src/parameters/network/subsidy.rs` in privacy-zebra against the numbers above, and tell us where our wording overstates what the software does. Pull requests and issues are open in every repository under github.com/Swarmcoin.

## FAQ

**Why fork Zcash instead of contributing?** Because what we wanted to build is a different network with a different economic rule set, and a fixed, permanent allocation is not something to propose to Zcash. The consensus and cryptography stay as upstream wrote them, we track upstream fixes, and bugs we find in shared code go upstream first.

**Isn't the 20% allocation a dev tax?** Yes, in the sense that 20% of every block reward goes to three project addresses for the whole life of the chain. 8% Core Development, 4% Grants & Ecosystem, 8% Community & Development Reserve, paid block by block to published 2-of-3 multisig addresses, percentages fixed in the genesis rules. We do not call it a fair launch. Whether the trade is worth it is your call.

**Why a closed start?** Published reason: "the infrastructure around the coin, liquidity pools included, needs coins before public mining begins; the aim is an orderly, predictable start." The coins are mined like any other block, 80% to the project's mining wallet and 20% to the funds, visible in the explorer. About 0.99% of the cap.

**ASIC or GPU?** Equihash 200,9, unchanged from upstream. ASICs for it exist, and nothing in the rules keeps anyone out, at either end. We do not promise that home machines stay competitive.

**Has it been audited?** No independent audit of the SWARM-specific changes has been published. The upstream components have their own records.

**What does the light-wallet server learn?** Which encrypted notes a wallet asked for, and for transparent addresses, which addresses it asked about. Not amounts or counterparties of shielded payments. Run your own node (privacy-zebra) and indexer (privacy-zaino) and it learns nothing.

Links: swarm.green, mainnet.explore.swarm.green, github.com/Swarmcoin. SWM has no guaranteed value and can lose value, including all of it.
