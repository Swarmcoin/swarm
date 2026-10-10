<!-- venue: r/cryptodevs (a later version for the upstream coin's subreddit only after the moderators say yes by modmail, and only as a rewrite with its own lead), flair: Discussion or none (check the live flair list), account requirements: a developer's own account with GitHub history in the profile; comments in r/cryptodevs for at least a week before posting (10 to 21 October 2026 is comments-only), when: Tue 27 Oct 2026 15:00 UTC, notes for the human poster: the body starts with "I work on SWARM."; name files by path so readers can open them under github.com/Swarmcoin; answer every comment within 24 hours; if someone finds a bug, thank them and point to SECURITY.md for anything security-relevant; never discuss what SWM is worth; the story's source, for a reader who asks: the Bitcoin wiki page "Value overflow incident" (en.bitcoin.it) and CVE-2010-5139 -->

# On 15 August 2010 one Bitcoin block created 184 billion BTC. A coin's supply is an arithmetic claim, so here is our subsidy code to check

I work on SWARM. We built it, nothing in this post is for sale, and we will not discuss what SWM is worth; we want the code read.

## Block 74,638

On 15 August 2010, block 74,638 of the Bitcoin chain contained a transaction with two outputs of about 92.2 billion BTC each, 184,467,440,737.09551616 BTC in total. The transaction-checking code did not account for outputs so large that their sum overflowed: added together, two enormous values wrapped around, and the check that outputs do not exceed inputs passed.

A fixed client was published within about five hours of discovery, as a soft fork that rejected overflowing transactions and any output above 21 million BTC. Upgraded nodes built a new chain without the bad transaction, and on 16 August, at block 74,691, it overtook the old one. The incident is CVE-2010-5139, and the Bitcoin wiki page "Value overflow incident" records the details.

The cap was in the design all along; a missing bounds check elsewhere still let one block print almost nine thousand times the planned supply. The lesson: a coin's supply is an arithmetic claim that lives in code, and the only way to check it is to read the code that pays and validates the subsidy.

## Why I am telling you this

Our coin's supply rests on someone else's subsidy arithmetic plus a handful of parameters we set. Below is which part is which.

## What is unfinished, first

- No independent audit of the SWARM-specific changes has been published.
- Windows and macOS builds are unsigned. No reproducible builds for the Electron apps yet; the Rust binaries are built in CI from pinned toolchains (Rust 1.96).
- The browser is a Windows-only pre-release with no tracker blocking and no phishing lists. The messenger is a first release: one desktop per account, no phone app.
- The node and CPU-miner app is published only when public mining opens on 1 November 2026, 15:42 UTC. Please keep ASICs and rented hash power off the network.
- The light-wallet server learns which encrypted notes a wallet asked for. Shielding hides what is on the chain, not that you use SWARM from your ISP.

## Inherited, unmodified

SWARM is built on open-source foundations that have secured real value, left unmodified. Mainnet has been live since 2 October 2026, 15:42 UTC. No cryptographic primitive, proving system or parameter set is changed.

| Area | What we use | Where to look |
| --- | --- | --- |
| Consensus rules | The node's block and transaction validation, with the upstream network-upgrade rule set active when we forked | consensus and chain crates of the node repository |
| Proof of work | Equihash 200,9; upstream difficulty adjustment (DigiShield v3 variant, 75-second target, 17-block averaging window) | `…/src/work` in the chain crate |
| Shielded pools | Sapling and Orchard; transparent P2PKH and P2SH | upstream `sapling-crypto`, `orchard` |
| Transaction format | v5, the upstream format | `…/src/transaction` in the chain crate |
| Emission arithmetic | Upstream subsidy, halving and funding-stream code; we set amounts, heights and recipients only | the subsidy and funding-stream parameters file (`…/parameters/network/subsidy.rs` in the node repository; `doc/protocol.md` links it) |
| Address encoding | Bech32m unified, Base58Check transparent | upstream address crate |
| Light-wallet protocol | `CompactTxStreamer` gRPC | privacy-lightwallet-protocol-rust |

The Sapling and Orchard parameters are the public ones from the upstream ceremonies; we ran none of our own.

## Defined by SWARM

**Network.** `SwarmMainnet`, network magic `SWMN`.

**Genesis.** Hash `01b76d8a0f18c502b23ab6605e26296d189aa5770fc4a34155e5c7b250a0eff2`, header time 2026-10-02 15:41:37 UTC (Unix 1790955697), 0 spendable outputs. The genesis block in hex, the launch manifest and the key-ceremony record are published.

**Addresses.** Unified shielded `swm1…` (the wallet default), transparent `s1…` (P2PKH) and `s3…` (P2SH). The three funding-stream recipients and the mining payouts are `s3…`.

**Subsidy and funding streams.** 6.25 SWM (625,000,000 zatoshi) from height 1, halving every 1,680,000 blocks, coinbase maturity 100 blocks, 75-second spacing. The miner gets 80 % plus all fees; 8 % Core Development, 4 % Grants & Ecosystem, 8 % Community & Development Reserve go to three 2-of-3 multisig `s3…` addresses fixed in the genesis rules, for the whole life of the chain, about 4.2 million SWM in all. Not a premine: nothing exists before it is mined. We do not dress this up: 20 % of every block goes to the project for the life of the chain.

This is the part to review hardest. Each stream is `floor(reward × percent / 100)` zatoshi and the miner gets the remainder. Exact to the zatoshi through era 6; from era 7 the reward is no longer evenly divisible, the streams round down and the miner keeps the sub-zatoshi remainders, so the lifetime miner share is 80.000003 %. Total emission over 30 eras: 20,999,987.3152 SWM. The era table is in `doc/economics.md`. If you can make our replay of the arithmetic disagree with the code, open an issue.

**Closed start.** Until 31 October 2026, 15:42 UTC only the project's machines mine: about 33,408 blocks, about 208,800 SWM, about 0.99 % of the cap, split like every other block. The waiting list gets the next 24 hours, and from 1 November 2026, 15:42 UTC mining is open to everyone. No coins are promised.

**Light-wallet chain label.** `swarm-mainnet`, served by privacy-zaino at `lwd-main.swarm.green:443` over TLS. The SDK carrying the network definition is released as `swarm-sdk-mainnet-1` from privacy-zingolib and privacy-lightwallet-protocol-rust.

## What a transaction reveals

| Kind | On the chain | To the light-wallet server |
| --- | --- | --- |
| Shielded to shielded | that it exists, its fee, its size | which encrypted outputs the wallet fetched; not amounts or counterparties |
| Transparent to transparent | everything, as in Bitcoin | the addresses the wallet asked about |
| Mixed | the transparent side in full | both |

Run `zebrad` and `zainod` yourself and the second column disappears. Chain-rule changes ship as announced network upgrades; none is scheduled.

## What we are asking for

1. Diff the node repository (its name is in the README of github.com/Swarmcoin/swarm) against upstream at the fork commit and tell us if anything outside the network definition, the subsidy parameters and the address constants changed. It should not have.
2. Check the funding-stream recipients in the source against the three addresses in the README and in every coinbase output on mainnet.explore.swarm.green.
3. Build against `swarm-sdk-mainnet-1` and tell us what integration is missing.
4. Security findings go to SECURITY.md in the affected repository (private reporting), not this thread: 72 hours to acknowledge, 14 days to a first assessment, 90-day disclosure window. No bug bounty at present; credit in release notes if you want it.

## FAQ

**Isn't 20 % a dev tax?** In that sense, yes: 8 / 4 / 8 % of every block to three published multisig addresses, permanently. We do not dress it up; whether the trade is worth it is your call.

**Why fork instead of contributing? Isn't it a clone with a dev tax?** Consensus and cryptography stay upstream's. What differs is the network, the economics, the messenger that pays in the chat and the browser with the wallet in the toolbar. Bugs in shared code go upstream first.

**Why a closed start?** The published reason is that the infrastructure around the coin, liquidity pools included, needs coins before public mining begins.

**ASIC or GPU?** Equihash 200,9 is unchanged; ASICs exist, nothing in the rules keeps anyone out, and nobody promises home machines stay competitive.

**Is there an audit?** No independent audit of the SWARM-specific changes has been published.

**What does the light-wallet server learn?** The second column of the table.

**What is SWM worth?** Whatever people agree it is worth. Nobody promises you a price, and SWM can lose all its value.
