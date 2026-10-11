<!-- venue: Bitcointalk, Announcements (Altcoins), flair: n/a, account requirements: Jr. Member or higher (30 activity, 1 merit, about 30 days) so the thread can carry an image and is taken seriously; the account is registered on Sat 10 October 2026 at the earliest, so the thread opens about Mon 9 November 2026, after public mining has opened (see README.md, Dates); check the account once a week, when: as soon as the account qualifies, a weekday at 14:00 UTC, notes for the human poster: this is Markdown and MUST be converted to BBCode by hand before posting ([b], [table], [url], [code], [quote]); the subject field is short (about 80 characters, check on the day), so use the short subject below and put the full headline as the first bold line of the body; one thread only, bump at most once per 24 hours and only with real news; no bounty, no signature campaign, no free coins; answer "another clone" once with the FAQ and do not argue; never discuss what SWM is worth or the token on Base; before posting, re-read every date in this text and switch to the past tense where the date has passed -->

# [ANN] SWARM (SWM) | Shielded payments, proof of work (Equihash 200,9) | Mainnet live since 2 Oct 2026 | Closed start until 31 Oct, public mining from 1 Nov 2026 | Mined, not sold

Short subject for the subject field: `[ANN] SWARM (SWM) | Shielded payments, Equihash 200,9 | Mined, not sold`

I work on SWARM. We are the developers of SWARM (SWM). This thread says what we built and what is not finished. There is no sale, no bounty and no free coins, and we will not discuss what SWM is worth here. Mining is open to everyone from 1 November 2026, 15:42 UTC. No coins are promised. Please keep ASICs and rented hash power off the network.

## December 2010, on this forum

At the end of November 2010 WikiLeaks began publishing US diplomatic cables. Within days, and without any court order, the money stopped. PayPal suspended the organisation's donation account on 3 to 4 December. Visa and MasterCard stopped processing its donations on 7 December. Bank of America and Western Union followed. WikiLeaks later said the blockade destroyed 95 percent of its revenue.

On 5 December 2010, in a thread on this forum titled "Wikileaks contact info?", members argued that WikiLeaks should simply take Bitcoin. Satoshi Nakamoto answered with an appeal to WikiLeaks not to use it yet. "The project needs to grow gradually", he wrote; Bitcoin was still a small beta community, and the attention could destroy it. The post: https://bitcointalk.org/index.php?topic=1735.msg26999#msg26999. WikiLeaks began accepting Bitcoin in June 2011.

You do not have to admire WikiLeaks to see the point. The lesson in one line: a few payment companies can cut an organisation off in a week without a judge, and money that no company can switch off is the answer to that, whoever the target is.

Bitcoin made payments that nobody can switch off. It did not make them private: every amount and every address is public, for ever. SWARM is one attempt at that second half. The rest of this post says what it is, and first what it is not yet.

## What is unfinished

- Experimental software; use at your own risk.
- No independent audit of the SWARM-specific changes has been published. The upstream components have their own records and open issues; we inherit both.
- Windows and macOS builds are unsigned, so SmartScreen and Gatekeeper warn.
- The browser is a Windows-only pre-release with no tracker blocking and no phishing lists.
- The messenger is a first release: one desktop per account, no phone app yet.
- The light-wallet server we run learns which encrypted notes a wallet asked for. Run your own node and indexer to remove that.
- Shielding hides what is on the chain, not that you use SWARM from your ISP.
- No bug bounty. Vulnerabilities: private reporting as in SECURITY.md.

## What it is

SWARM is private money: a proof-of-work coin whose shielded payments keep the sender, the receiver and the amount encrypted on the chain, using zero-knowledge proofs. It is built on open-source foundations that have secured real value, left unmodified: the node is `zebrad` and the indexer is `zainod`, from the open-source node implementation we build on, and the wallets use zingolib. Consensus rules and cryptography are unmodified; SWARM adds its own network, its economics and its apps: a wallet, an end-to-end encrypted messenger that pays inside the chat, and a browser with the wallet built in. Transparent payments exist too; the wallet tells you which kind you are about to make.

## Specifications

| | |
| --- | --- |
| Name / ticker | SWARM / SWM |
| Consensus | Proof of work, Equihash 200,9, the upstream difficulty adjustment (a DigiShield v3 variant) |
| Target block time | 75 seconds |
| Block reward at launch | 6.25 SWM |
| Halving | every 1,680,000 blocks, about 4 years |
| Maximum supply | 20,999,987.3152 SWM |
| Coins in genesis | 0 |
| Coinbase maturity | 100 blocks |
| Shielded pools | Sapling and Orchard (the upstream public parameters; Orchard needs no trusted setup) |
| Transaction format | v5, the upstream format |
| Mainnet addresses | `swm1…` shielded (unified, wallet default), `s1…` transparent, `s3…` transparent script |
| Network name / magic | `SwarmMainnet` / `SWMN` |
| Light-wallet server | `lwd-main.swarm.green:443` (TLS), chain label `swarm-mainnet` |
| Mainnet live since | 2 October 2026, 15:42 UTC |
| Node software | `zebrad` from the node repository, named in the README of github.com/Swarmcoin/swarm; indexer `zainod` (`privacy-zaino`); wallet library `privacy-zingolib` |

## Block reward allocation

Every block, for the whole emission schedule, splits the same way:

| Share | Recipient | Destination |
| --- | --- | --- |
| 80 % | the miner, plus all fees | the miner's own address |
| 8 % | Core Development | `s3fLmEHc1xqs8KAe7QS7oupkhuGDjidV4eq` (2-of-3 multisig) |
| 4 % | Grants & Ecosystem | `s3RiGvK5JzS8eh6ywN3K22f2LzDAhicgFuq` (2-of-3 multisig) |
| 8 % | Community & Development Reserve | `s3g3pzQVhvVX17bzrrEN3vmcXZWSpj7KFVp` (2-of-3 multisig) |

We do not dress this up: 20 % of every block goes to the project for the life of the chain. It does not end after a few years; over the whole schedule it comes to about 4.2 million SWM. The percentages are fixed in the genesis rules and cannot be changed; the destinations only through a formal protocol upgrade. Every halving reduces all four amounts proportionally. It is not a premine: nothing exists before it is mined, and every payment is visible in every coinbase in the explorer. Keys for the three addresses were generated offline at the launch key ceremony; two of three are needed to spend.

## Closed start and the mining schedule

- 2 October 2026, 15:42 UTC: mainnet starts. Genesis holds no coins.
- Until 31 October 2026, 15:42 UTC: only the project's own machines mine. About 33,408 blocks, about 208,800 SWM, about 0.99 % of the cap, split like every other block: 80 % to the project's mining wallet, 20 % to the three funds, visible at mainnet.explore.swarm.green.
- 31 October 2026, 15:42 UTC to 1 November 2026, 15:42 UTC: the people on the waiting list (swarm.green/waitlist) can mine too.
- From 1 November 2026, 15:42 UTC: mining is open to everyone, and the SWARM Node app (node plus CPU miner) is published on swarm.green.

Published reason for the closed start: "the infrastructure around the coin, liquidity pools included, needs coins before public mining begins; the aim is an orderly, predictable start." No coins are promised. Mined, not sold.

## Software and checksums

All downloads: swarm.green/ecosystem. Every file is listed with its SHA-256; release notes and checksum files: github.com/Swarmcoin/swarm-releases.

- SWARM Wallet: Windows, macOS, Linux, Android APK. Built on zingolib. MIT.
- SWARM Messenger: Windows, macOS (Apple silicon), Linux. Built on Signal Desktop and Signal Server, running on SWARM's own server, never Signal's; sign in with the 24 words, pay inside the chat. AGPL-3.0.
- SWARM Browser: Windows pre-release. ungoogled-chromium (Chromium 153) with the wallet in the toolbar. BSD-3-Clause.
- SWARM Node (node plus CPU miner): published on swarm.green when mining opens on 1 November 2026, 15:42 UTC.

Verify before you install:

```
sha256sum <file>        # Linux
shasum -a 256 <file>    # macOS
Get-FileHash <file>     # Windows PowerShell
```

Compare with the value on the download page. Builds are unsigned, so SmartScreen and Gatekeeper warn; a wrong checksum is another matter: do not run that file.

## Verify the chain

Genesis hash: `01b76d8a0f18c502b23ab6605e26296d189aa5770fc4a34155e5c7b250a0eff2`
Genesis header time: 2026-10-02 15:41:37 UTC (Unix 1790955697)

Compare your node's block 0 with that and with the mainnet explorer at mainnet.explore.swarm.green. The mainnet light-wallet server is `lwd-main.swarm.green:443`.

## Links (official only)

- Website: swarm.green
- Explorer (mainnet): mainnet.explore.swarm.green
- Source code, all repositories: github.com/Swarmcoin
- Technical documentation: github.com/Swarmcoin/swarm (`doc/protocol.md`, `doc/economics.md`)
- Email: swarmofficial@atomicmail.io

Anything else claiming to be SWARM is not us. We never ask for recovery words, private keys or a payment. No official Telegram or Discord exists.

## FAQ

**Isn't the 20 % a dev tax?** Call it that if you like; we will not argue about the word. 20 % of every block, for the whole life of the chain, goes to three published 2-of-3 multisig addresses, 8 / 4 / 8, fixed in the genesis rules. Every payment is in a coinbase you can read in the explorer.

**Isn't this just another clone? Why build on existing code instead of contributing to it?** It is built on the upstream protocol stack, and we say so in the first lines rather than wait to be found out. Consensus rules and cryptography are unmodified, because rewriting proven cryptography is how coins lose their users' money. What is ours is the network definition, the economics and the apps. We did not propose our allocation rule upstream because a permanent 20 % is not something to ask another chain to adopt; it is a design for our network. We track upstream fixes, and bugs we find in shared code go upstream first.

**Why a closed start?** Published reason: "the infrastructure around the coin, liquidity pools included, needs coins before public mining begins; the aim is an orderly, predictable start." Those coins were mined like any other block, 80 % to the project's mining wallet and 20 % to the funds, visible in the explorer: about 208,800 SWM, about 0.99 % of the cap.

**ASIC or GPU?** Equihash 200,9. ASICs for it exist, and nothing in the rules keeps anyone out, at either end. We ask anyway: please keep ASICs and rented hash power off the network. The SWARM Node app mines on the CPU.

**Is there an audit?** No independent audit of the SWARM-specific changes has been published. The upstream components have their own records.

**What does the light-wallet server learn?** Which encrypted notes a wallet asked for; for transparent addresses, which addresses. Not shielded amounts or counterparties. Your own node and indexer remove it.

**What is SWM worth?** Whatever people agree it is worth. Nobody promises you a price, and SWM can lose all its value. We will not discuss trading in this thread.
