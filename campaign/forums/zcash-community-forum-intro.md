<!-- venue: forum.zcashcommunity.com (Discourse), category: Community or General (check what the Ycash thread used), flair: n/a, account requirements: an account that has read, liked and replied to other threads for a few days (Discourse trust level); read the code of conduct, when: week 2, notes for the human poster: NO download links in the first post; ask whether they are welcome; thank ECC, Zcash Foundation and Zingo Labs by name; never criticise ZEC or its funding decisions; never recruit anyone; if the thread turns hostile, answer each technical point once and stop; never discuss price -->

# Introducing SWARM, a friendly fork built on Zebra, Zaino and zingolib

Hello. We are the developers of SWARM (SWM), a proof-of-work coin that runs the Zcash protocol as Zebra implements it, with its own network definition. Mainnet has been live since 2 October 2026. We are posting to say thank you, to say exactly what we changed, and to invite criticism. We are not here to recruit anyone.

## Thank you

Everything that makes SWARM work was written here. The full node is a fork of Zebra, by the Zcash Foundation. The indexer behind our light-wallet servers and explorer is a fork of Zaino, by Zingo Labs. The wallets are forks of zingolib, Zingo PC and zingo-mobile, also by Zingo Labs. The protocol itself, the Sapling and Orchard pools, the proving systems and the public parameters from the ceremonies come from Electric Coin Company and the researchers who worked with them. We did not run a ceremony and did not need to; that is a debt.

Each fork keeps its upstream history and licence, and our changes are published under the same licence as the upstream (MIT / Apache-2.0 for the node, Apache-2.0 for the indexer, MIT for the wallets).

## What we did not change

Consensus rules and cryptography. Block and transaction validation are Zebra's, with the network-upgrade rule set active on Zcash mainnet at the time of the fork. Equihash 200,9 and the difficulty adjustment are unchanged. Sapling and Orchard, v5 transactions, Bech32m unified addresses and Base58Check transparent addresses, the `CompactTxStreamer` light-wallet service: all upstream. No cryptographic primitive, proving system or parameter set is modified. `doc/protocol.md` in github.com/Swarmcoin/swarm has a table of where to check each claim, and we would welcome anyone here checking it.

## What we changed

A network definition: `SwarmMainnet`, network magic `SWMN`, a genesis block with no spendable coins (hash `01b76d8a0f18c502b23ab6605e26296d189aa5770fc4a34155e5c7b250a0eff2`), address prefixes `swm1…` for unified shielded, `s1…` and `s3…` for transparent, and the testnet prefix `swarm1…`. The subsidy: 6.25 SWM, 75-second blocks, halving every 1,680,000 blocks, 20,999,987.3152 SWM in total using Zebra's own arithmetic. Funding streams: 8% Core Development, 4% Grants & Ecosystem, 8% Community & Development Reserve, to three 2-of-3 multisig addresses, for the whole emission schedule. The light-wallet chain label is `swarm-mainnet` and the SDK release is `swarm-sdk-mainnet-1`.

We want to be direct about the funding streams because this forum has spent years debating development funding and knows the arguments better than we do. SWARM's 20% does not end the way the Founders' Reward ended. It is permanent, paid block by block to published addresses. We do not call it a fair launch, and we are not proposing it as a model for anyone else. It is our design for our network, open to your criticism.

We also started closed: until 31 October 2026, 15:42 UTC only our own machines mine (about 0.99% of the cap, split like every other block), then 24 hours for a waiting list, then public mining from 1 November 2026. The published reason is that the infrastructure around the coin needs coins before public mining begins. No coins are promised.

On top of the chain we built a messenger (a fork of Signal Desktop and Signal Server, on our own server, signing in with the wallet's 24 words and paying inside the chat) and a browser (ungoogled-chromium with the wallet in the toolbar). Both are open source and early.

## Commitments

- Upstream fixes to Zebra, Zaino and zingolib will be tracked and merged. We do not maintain a private patch set on consensus code.
- Bugs we find in shared code go upstream first, through the upstream projects' security processes.
- We will not recruit contributors from ECC, the Zcash Foundation, Zingo Labs or this forum. If someone chooses to help us, that is their decision, and we will not ask.
- We will not criticise Zcash or its funding decisions, here or anywhere.
- We will say what is missing before anyone else does: no independent audit of our changes, unsigned desktop builds, a pre-release browser, a first-release messenger, and a light-wallet server that learns which notes a wallet asked for.

## What we would like

Criticism. If our description of what is inherited and what is defined is wrong anywhere, we would like to know. If the funding-stream arithmetic in our replay of `subsidy.rs` disagrees with the code, we would like to know. If the way we credit upstream falls short, tell us how to fix it.

We have deliberately not linked downloads in this post. If the moderators and the community would rather we did not, we will not; if a link to the ecosystem page is welcome, we will add it in a reply. Documentation and source: github.com/Swarmcoin. Thank you for the years of work we are standing on.
