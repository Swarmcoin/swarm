<!-- venue: r/cryptodevs (reusable for r/zec in week 4 only after asking the moderators by modmail and rewriting the lead for a Zcash audience), flair: Discussion or none (check the live flair list), account requirements: a developer's own account with GitHub history in the profile; comment in the sub before posting, when: week 2, notes for the human poster: disclose in the first line; link the files by path so readers can open them in github.com/Swarmcoin; answer every comment within 24 hours; if someone finds a bug, thank them and point to SECURITY.md for anything security-relevant; never discuss price -->

# What we changed and what we did not when forking Zebra, Zaino and zingolib for a new network

Disclosure: we built this. We are posting because we want the diff read by people who know the Zcash stack, not because we want users. If you review one file, make it the subsidy code.

## The short version

SWARM (SWM) is a proof-of-work privacy coin that runs the Zcash protocol as Zebra implements it, with its own network definition. Mainnet has been live since 2 October 2026, 15:42 UTC. No cryptographic primitive, proving system or parameter set is modified. Everything we defined is listed in `doc/protocol.md` in github.com/Swarmcoin/swarm, and this post is a walk through that file.

Before the detail, what is not done: no independent audit of our changes, unsigned desktop builds, no reproducible builds for the Electron apps yet (the Rust binaries are built in CI from pinned toolchains, Rust 1.96), and the node and miner app is not published until public mining opens on 1 November 2026, 15:42 UTC.

## Inherited, unmodified

| Area | What we use | Where to look |
| --- | --- | --- |
| Consensus rules | Zebra's block and transaction validation, with the network-upgrade rule set active on Zcash mainnet at the time of the fork | `zebra-consensus`, `zebra-chain` in privacy-zebra |
| Proof of work | Equihash 200,9, Zcash's difficulty adjustment (DigiShield v3 variant, 75-second target, 17-block averaging window) | `zebra-chain/src/work` |
| Shielded pools | Sapling and Orchard; transparent P2PKH and P2SH | upstream `sapling-crypto`, `orchard`, `zcash_primitives` |
| Transaction format | Zcash v5 | `zebra-chain/src/transaction` |
| Emission arithmetic | Zebra's subsidy, halving and funding-stream code; we only set amounts, heights and recipients | `zebra-chain/src/parameters/network/subsidy.rs` |
| Address encoding | Bech32m unified addresses, Base58Check transparent | `zcash_address` |
| Light-wallet protocol | The `CompactTxStreamer` gRPC service | privacy-lightwallet-protocol-rust |

The Sapling and Orchard parameters are the public ones from the Zcash ceremonies. We did not run a ceremony and did not need to.

## Defined by SWARM

**Network definition.** `SwarmMainnet` and `SwarmTestnet`, network magic `SWMN`. Two networks run; the plain hostnames (`lwd.swarm.green`, `testnet.explore.swarm.green`) are testnet, the mainnet ones carry `-main` or `mainnet.`. Testnet coins have no value and the testnet keeps its own shielded prefix, `swarm1…`, so a wallet cannot confuse the two.

**Genesis.** Hash `01b76d8a0f18c502b23ab6605e26296d189aa5770fc4a34155e5c7b250a0eff2`, header time 2026-10-02 15:41:37 UTC (Unix 1790955697), 0 spendable outputs. The genesis block in hex, the launch manifest and the key-ceremony record are published with the chain; the website's network page is rendered from the same manifest and shows its SHA-256.

**Address prefixes (mainnet).** Unified shielded `swm1…` (the wallet default), transparent `s1…` (P2PKH) and `s3…` (P2SH). The three funding-stream recipients and the mining payouts are `s3…` addresses.

**Subsidy and funding streams.** 6.25 SWM (625,000,000 zatoshi) at height 1, halving every 1,680,000 blocks, coinbase maturity 100 blocks, 75-second spacing. Funding streams: 8% Core Development, 4% Grants & Ecosystem, 8% Community & Development Reserve, for the whole emission schedule, to three 2-of-3 multisig `s3…` addresses. The miner gets 80% plus all fees.

This is the part we want reviewed hardest. The arithmetic is upstream's: each stream is `floor(reward × percent / 100)` zatoshi, the miner gets the remainder. Exact to the zatoshi through era 6; from era 7 the reward is no longer evenly divisible, the streams round down and the miner gets the sub-zatoshi remainders, so the lifetime miner share is 80.000003%. Total emission over 30 eras: 20,999,987.3152 SWM. The era table is in `doc/economics.md`. If you can make our replay of the arithmetic disagree with the code, open an issue.

Stated plainly, because developers ask too: this allocation does not end. Zcash's Founders' Reward stopped after four years; ours runs until block rewards reach zero, about 4.2 million SWM to the three project destinations. We do not describe it as a fair launch.

**Light-wallet chain label.** `swarm-mainnet`, served by privacy-zaino at `lwd-main.swarm.green:443` over TLS. The SDK carrying the network definition is released as `swarm-sdk-mainnet-1` from privacy-zingolib and privacy-lightwallet-protocol-rust, so a third-party wallet can target the same chain without copying our constants by hand.

## What a transaction reveals, by kind

| Kind | On the chain | To the light-wallet server |
| --- | --- | --- |
| Shielded to shielded | that a transaction exists, its fee, its size | which encrypted outputs the wallet fetched and trial-decrypted; not amounts or counterparties |
| Transparent to transparent | everything, as in Bitcoin | the addresses the wallet asked about |
| Mixed | the transparent side in full, the shielded side as above | both |

Run `zebrad` from privacy-zebra and `zainod` from privacy-zaino yourself and the second column disappears.

## Upgrades

Chain-rule changes ship as announced network upgrades with an activation height, as upstream does. None is scheduled. Upstream security fixes are tracked and merged; we do not maintain a private patch set on consensus code.

## What we are asking for

1. Diff `privacy-zebra` against Zebra at the fork commit and tell us if anything outside the network definition, the subsidy parameters and the address constants changed. It should not have.
2. Check the funding-stream recipients in the source against the three addresses in `README.md` and in every coinbase on mainnet.explore.swarm.green.
3. Build the SDK against `swarm-sdk-mainnet-1` and tell us what the integration experience is missing.
4. Security findings go to SECURITY.md in the affected repository (private reporting), not to this thread. 72 hours to acknowledge, 14 days to a first assessment, 90-day disclosure window. No bug bounty at present; credit in release notes if you want it.

Mining opens to everyone on 1 November 2026, 15:42 UTC, Equihash 200,9, ASICs exist and nothing in the rules keeps anyone out. No coins are promised.

Repositories: github.com/Swarmcoin/privacy-zebra, privacy-zaino, privacy-zingolib, privacy-lightwallet-protocol-rust, and the documentation at github.com/Swarmcoin/swarm.
