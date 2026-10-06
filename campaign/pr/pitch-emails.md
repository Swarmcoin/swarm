# Pitch emails

Send from swarmofficial@atomicmail.io. Plain text, no attachments (paste the release below
the signature if the outlet wants it). One follow-up after five working days, then stop.
Never pitch price, never promise coverage-dependent "exclusives" we cannot keep, never send
the same email to two reporters at one outlet. Log every send in `outreach-tracker.csv`.

## A. Crypto reporters covering privacy (DL News, Blockworks, Decrypt, The Defiant, CoinDesk)

Subject: New PoW privacy coin on the Zcash stack opens public mining 1 Nov; permanent 20% allocation stated plainly

Hi [first name],

You have covered the privacy-coin story closely this year, so this one may be useful: SWARM
(SWM) has been running its own proof-of-work mainnet since 2 October and opens mining to
everyone on 1 November 2026 at 15:42 UTC.

Three things make it a story rather than another fork:

1. It runs the Zcash protocol stack (Zebra node, Orchard and Sapling pools) with consensus
   rules and cryptography unmodified, and it says so component by component. Dash adopted
   Orchard in July; Pirate Chain is testing it. Zcash's shielded pool is becoming the
   standard library of privacy coins.
2. Every block pays 80% to the miner and 20% to three published addresses, for the whole
   life of the chain. The project describes that as a permanent allocation and does not call
   it a fair launch. The 30-day closed start, in which only the project mined (about 0.99% of
   supply), is documented block by block in the explorer, with the stated reason.
3. The apps exist: a wallet on four platforms, an end-to-end encrypted messenger (Signal's
   code, SWARM's server, sign-in with the wallet's 24 words) that pays inside the chat, and a
   degoogled Chromium browser with the wallet in the toolbar.

What it is not: audited (no independent audit of the SWARM-specific changes yet), signed
(builds carry SHA-256 checksums instead), or listed anywhere. There is no sale and no price.

Facts on one page: https://swarm.green/what-is-swarm. Genesis hash and the three fund
addresses: https://swarm.green/verify. I can put you in touch with the founding team for a
call, and answer the hard questions in writing: why fork rather than contribute, why a
closed start, what the light-wallet server learns.

Thanks for reading,
[Name], SWARM
swarmofficial@atomicmail.io · x.com/swarm_coin

## B. FOSS and privacy-tech media (It's FOSS, The Register, CyberInsider, TechCrunch)

Subject: Degoogled Chromium with a shielded-payments wallet in the toolbar, and a Signal fork that pays inside the chat (open source, Windows/Linux/macOS)

Hi [first name],

Two open-source apps your readers may want to look at, both from the SWARM project:

SWARM Browser (Windows pre-release) is Chromium 153 from the ungoogled-chromium code base:
no Google API keys, no Safe Browsing lookups, no usage reports, no remote feature switches.
Referrers are not sent across sites, client hints are off, WebRTC does not reveal the local
address, HTTPS-only is on, DuckDuckGo is the default with suggestions off. The wallet sits
in the toolbar but the keys do not live in the browser; a small local wallet host holds
them. Missing today, and we say so on the download page: tracker blocking, phishing lists
(gone with Safe Browsing), signed builds, auto-updates, macOS and Linux.

SWARM Messenger (Windows, Linux, macOS) forks Signal Desktop, libsignal and Signal Server
and runs on SWARM's own server, never Signal's. You sign in with a wallet's 24 words instead
of a phone number; messages and calls are end-to-end encrypted; the wallet pane sits beside
the thread so a payment never leaves the conversation. First release, unsigned, no phone
app yet. AGPL-3.0.

Both are built for SWARM, a privacy coin on the Zcash protocol stack. The coin is not the
story for your readers and we will not pretend it is; the apps stand on their own.

Downloads with SHA-256 checksums: https://swarm.green/ecosystem. Code:
https://github.com/Swarmcoin. Happy to answer technical questions or arrange a call with
the people who built them.

[Name], SWARM
swarmofficial@atomicmail.io

## C. Privacy podcasts and YouTubers (Opt Out, Monero Talk, NBTV, Techlore, The Hated One)

Subject: A Zcash-stack privacy coin that will answer the hard questions on your show

Hi [first name],

We built SWARM, a proof-of-work privacy coin on the Zcash protocol stack, and we would like
to be interviewed by someone who will not be kind about it.

The questions we expect, and will answer plainly: why fork Zcash instead of contributing;
whether a permanent 20% block allocation to three project funds is a dev tax (it is an
allocation, and we do not call the launch fair); why the first 30 days were mined by the
project alone; what optional privacy leaks; what the light-wallet server learns; why
Equihash when ASICs exist; what is not audited (everything SWARM-specific, so far).

What we think is worth your audience's time: a messenger where the payment happens inside
the encrypted chat and the identity is the wallet, not a phone number; a browser with
Google removed and the wallet in the toolbar; and a project that lists what is missing on
every download page.

Public mining opens 1 November 2026, 15:42 UTC. Any time before or after works.
https://swarm.green · https://github.com/Swarmcoin

[Name], SWARM
swarmofficial@atomicmail.io

## D. Zcash ecosystem (ZecHub, Zcash Community Forum, Zingo Labs, Zcash Foundation)

Subject: A friendly fork introduces itself: SWARM on the Zcash stack, nothing in consensus or cryptography changed

Hello,

We are the team behind SWARM (SWM), a new network running the Zcash protocol as implemented
by Zebra, with Zaino as indexer and zingolib as the wallet SDK. We changed the network
definition, the genesis, the address prefixes (swm1, s1, s3), the emission schedule and the
funding streams, and nothing else. Consensus rules and cryptography are upstream's,
unmodified; we will track upstream fixes and ship chain changes only as announced network
upgrades, as you do.

We owe the existence of the project to Electric Coin Company, the Zcash Foundation and
Zingo Labs, and we say so on every page. We will not recruit your contributors, we will not
compare ZEC and SWM, and we would like to be told where we are wrong. We have posted an
introduction on the community forum [link] and would welcome your criticism there. If a
contribution of ours is useful upstream, it is yours.

Technical detail of what is inherited and what is defined:
https://github.com/Swarmcoin/swarm/blob/main/doc/protocol.md

With thanks,
[Name], SWARM
swarmofficial@atomicmail.io

## E. Mining pools and indexes (from 25 October)

Subject: New Equihash 200,9 coin, Zebra fork, public mining opens 1 Nov 2026 15:42 UTC

Hello,

SWARM (SWM) opens public mining on 1 November 2026, 15:42 UTC. Technical summary for pool
operators:

- Proof of work: Equihash 200,9, Zcash's difficulty adjustment, 75-second target.
- Node: Zebra fork (github.com/Swarmcoin/privacy-zebra), standard RPC surface, network
  magic SWMN, network name SwarmMainnet.
- Block reward 6.25 SWM; funding-stream outputs (8% / 4% / 8%) are part of every coinbase;
  the miner's 80% goes to the payout address. Coinbase maturity 100 blocks.
- Addresses: transparent s1 (P2PKH) and s3 (P2SH); shielded swm1 for wallets.
- Explorer: https://mainnet.explore.swarm.green. Genesis hash and endpoints:
  https://swarm.green/verify.
- There is no exchange listing and no price; we are not asking you to promote anything,
  only to list the coin if your miners want it.

Questions to the privacy-zebra repository or this address. No coins are promised.

[Name], SWARM
swarmofficial@atomicmail.io

## Follow-up (one, after five working days)

Subject: Re: [original subject]

Hi [first name], one follow-up in case this was buried. The short version: SWARM opens
public mining on 1 November 2026 at 15:42 UTC; facts on one page at
https://swarm.green/what-is-swarm. If it is not for you, no reply needed and I will not
write again. Thanks, [Name]
