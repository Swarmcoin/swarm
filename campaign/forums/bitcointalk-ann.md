<!-- venue: Bitcointalk, Announcements (Altcoins), flair: n/a, account requirements: Jr. Member or higher (30 activity, 1 merit, about 30 days) so the thread can carry an image and is taken seriously; register now and earn activity by answering questions elsewhere on the forum, when: as soon as the account qualifies, ideally before 1 November 2026, notes for the human poster: this is Markdown and MUST be converted to BBCode by hand before posting ([b], [table], [url], [code]); one thread only, bump at most once per 24 hours and only with real news; no bounty, no signature campaign, no airdrop; answer "another Zcash clone" once with the FAQ and do not argue; never discuss price or the token on Base -->

# [ANN] SWARM (SWM) | Shielded payments, PoW Equihash | Mainnet live 2 Oct 2026 | Public mining 1 Nov 2026 | No premine, no sale

We are the developers. This thread describes what we built and what is not finished. There is no sale, no bounty and no airdrop, and we will not discuss price here.

## What it is

SWARM is private money: a proof-of-work coin whose shielded payments keep the sender, the receiver and the amount encrypted on the chain, using zero-knowledge proofs. It is built on the Zcash protocol stack as implemented by Zebra, the Zcash Foundation's full node. Consensus rules and cryptography are unmodified; SWARM adds its own network, its economics and its apps: a wallet, an end-to-end encrypted messenger that pays inside the chat, and a browser with the wallet built in. Transparent payments exist too; the wallet tells you which kind you are about to make.

## Specifications

| | |
| --- | --- |
| Name / ticker | SWARM / SWM |
| Consensus | Proof of work, Equihash 200,9, Zcash difficulty adjustment (DigiShield v3 variant) |
| Target block time | 75 seconds |
| Block reward at launch | 6.25 SWM |
| Halving | every 1,680,000 blocks, about 4 years |
| Maximum supply | 20,999,987.3152 SWM |
| Coins in genesis | 0 |
| Coinbase maturity | 100 blocks |
| Shielded pools | Sapling and Orchard (public Zcash ceremony parameters) |
| Transaction format | Zcash v5 |
| Mainnet addresses | `swm1…` shielded (unified, wallet default), `s1…` transparent, `s3…` transparent script |
| Network name / magic | `SwarmMainnet` / `SWMN` |
| Light-wallet server | `lwd-main.swarm.green:443` (TLS), chain label `swarm-mainnet` |
| Mainnet live since | 2 October 2026, 15:42 UTC |
| Node software | Zebra fork (`privacy-zebra`), indexer Zaino fork (`privacy-zaino`) |

## Block reward allocation

Every block, for the whole emission schedule, splits the same way:

| Share | Recipient | Destination |
| --- | --- | --- |
| 80% | the miner, plus all fees | the miner's own address |
| 8% | Core Development | `s3fLmEHc1xqs8KAe7QS7oupkhuGDjidV4eq` (2-of-3 multisig) |
| 4% | Grants & Ecosystem | `s3RiGvK5JzS8eh6ywN3K22f2LzDAhicgFuq` (2-of-3 multisig) |
| 8% | Community & Development Reserve | `s3g3pzQVhvVX17bzrrEN3vmcXZWSpj7KFVp` (2-of-3 multisig) |

Plainly: 20% of every block reward goes to three project addresses, and unlike Zcash's Founders' Reward this does not end: about 4.2 million SWM over the life of the chain. The percentages are fixed in the genesis rules and cannot be changed; the destinations only through a formal protocol upgrade. Every halving reduces all four amounts proportionally. It is not a premine: nothing exists before it is mined, and every payment is visible in every coinbase in the explorer. We do not call SWARM a fair launch. Keys for the three addresses were generated offline at the launch key ceremony; two of three are needed to spend.

## Closed start and the mining schedule

- 2 October 2026, 15:42 UTC: mainnet starts. Genesis holds no coins.
- Until 31 October 2026, 15:42 UTC: only the project's own machines mine. About 33,408 blocks, about 208,800 SWM, about 0.99% of the cap, split like every other block: 80% to the project's mining wallet, 20% to the three funds, visible at mainnet.explore.swarm.green.
- 31 October 2026, 15:42 UTC to 1 November 2026, 15:42 UTC: the people on the waiting list (swarm.green/waitlist) can mine too.
- From 1 November 2026, 15:42 UTC: mining is open to everyone, and the SWARM Node app (node plus CPU miner) is published on swarm.green.

Published reason: "the infrastructure around the coin, liquidity pools included, needs coins before public mining begins; the aim is an orderly, predictable start." No coins are promised. Mined, not sold.

## Software and checksums

All downloads: swarm.green/ecosystem. Every file is listed with its SHA-256; release notes and checksum files: github.com/Swarmcoin/swarm-releases.

- SWARM Wallet: Windows, macOS, Linux, Android APK. Fork of Zingo PC / zingo-mobile. MIT.
- SWARM Messenger: Windows, macOS (Apple silicon), Linux. Fork of Signal Desktop and Signal Server on SWARM's own server, never Signal's; sign in with the 24 words, pay inside the chat. AGPL-3.0.
- SWARM Browser: Windows pre-release. ungoogled-chromium (Chromium 153) with the wallet in the toolbar. BSD-3-Clause.
- SWARM Node: published when mining opens.

Verify before you install:

```
sha256sum <file>        # Linux
shasum -a 256 <file>    # macOS
Get-FileHash <file>     # Windows PowerShell
```

Compare with the value on the download page. Builds are unsigned, so SmartScreen and Gatekeeper warn; a wrong checksum is another matter.

## Verify the chain

Genesis hash: `01b76d8a0f18c502b23ab6605e26296d189aa5770fc4a34155e5c7b250a0eff2`
Genesis header time: 2026-10-02 15:41:37 UTC (Unix 1790955697)

Compare your node's block 0 with that and with the explorer. Plain hostnames (`lwd.swarm.green`, `testnet.explore.swarm.green`) are testnet; mainnet names carry `-main` or `mainnet.`. Testnet coins have no value.

## Links (official only)

- Website: swarm.green
- Explorer: mainnet.explore.swarm.green
- Source code, all repositories: github.com/Swarmcoin
- Technical documentation: github.com/Swarmcoin/swarm (`doc/protocol.md`, `doc/economics.md`)
- Email: swarmofficial@atomicmail.io

Anything else claiming to be SWARM is not us. We never ask for recovery words, private keys or a payment. No official Telegram or Discord exists.

## Honest status

- Experimental software; use at your own risk.
- No independent audit of the SWARM-specific changes has been published. Upstream components (Zebra, Zaino, zingolib, Signal, Chromium) have their own records and open issues; we inherit both.
- Windows and macOS builds are unsigned.
- The browser is a Windows-only pre-release with no tracker blocking and no phishing lists.
- The messenger is a first release: one desktop per account, no phone app yet.
- The light-wallet server we run learns which encrypted notes a wallet asked for. Run your own node and indexer to remove that.
- Shielding hides what is on the chain, not that you use SWARM from your ISP.
- No bug bounty. Vulnerabilities: private reporting as in SECURITY.md.

## FAQ

**Why fork Zcash instead of contributing?** We wanted a different network with a permanent allocation rule, which is not something to propose to Zcash. Consensus and cryptography stay unmodified, we track upstream fixes, and bugs in shared code go upstream first.

**Isn't the 20% a dev tax?** Yes: 20% of every block, for the whole life of the chain, to three published 2-of-3 multisig addresses, 8/4/8, fixed in the genesis rules. We do not call it a fair launch.

**Why a closed start?** "The infrastructure around the coin, liquidity pools included, needs coins before public mining begins; the aim is an orderly, predictable start." Those coins are mined like any other block, 80% to the project's mining wallet and 20% to the funds, visible in the explorer.

**ASIC or GPU?** Equihash 200,9. ASICs exist; nothing in the rules keeps anyone out, at either end.

**Has it been audited?** No independent audit of the SWARM-specific changes yet. Upstream components have their own records.

**What does the light-wallet server learn?** Which encrypted notes a wallet asked for; for transparent addresses, which addresses. Not shielded amounts or counterparties. Your own node and indexer remove it.

**Exchange? Price?** Not discussed in this thread. SWM has no guaranteed value and can lose value, including all of it.
