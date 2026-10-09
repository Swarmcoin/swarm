<!-- venue: forum.zcashcommunity.com (Discourse), category: Community or General, flair: n/a, account requirements: an account registered on Sat 10 October 2026 that has read, liked and replied to other threads since then (Discourse trust level); read the code of conduct first, when: Thu 15 October 2026, 14:00 UTC; fallback Tue 20 October 2026, 14:00 UTC if the account's trust level does not yet allow a new topic, notes for the human poster: NO download links in the first post; ask whether a link is welcome; thank Electric Coin Company, the Zcash Foundation and Zingo Labs by name; never criticise Zcash, ZEC or its funding decisions; never ask anyone to join us; if the thread turns hostile, answer each technical question once and stop; never discuss what SWM is worth. lint: other-projects hits are the upstream names, allowed by D-2026-10-09-MKT-DESK-3 (attribution on their own forum, not a comparison); the owner sees this text before it is posted; every other rule applies and passes -->

# Introducing SWARM, a friendly fork built on Zebra, Zaino and zingolib

I work on SWARM. We are its developers, and we are posting here first to say thank you, then to say exactly what we changed, and to ask for criticism. SWARM (SWM) is a proof-of-work coin that runs the Zcash protocol as Zebra implements it, with its own network definition. Its mainnet has been live since 2 October 2026.

## The weekend of 22 and 23 October 2016

Most of you know this story better than we do. We tell it because it is the reason this post exists.

Ten years ago this month, six people in different places ran one computation together. Zcash was about to launch, and its shielded pool needed public parameters. Making them produced secret material that, if anyone kept it, would let them forge coins that nobody could detect. The ceremony Zooko Wilcox organised was built so that the secret could only be rebuilt if all six colluded: as long as one of them destroyed their share, nobody could forge anything.

The participants bought new computers in person. Peter Todd ran his part on a laptop in a car while he drove for hours through the interior of British Columbia, and on the Monday he took the laptop apart and burned its components with a propane torch. Morgen Peck, a journalist, followed the ceremony, and her reporting became the Radiolab episode "The Ceremony".

Later upgrades removed the need for a trusted setup altogether; Orchard has none. What we are describing is the 2016 ceremony.

The lesson we took from it: trust can be engineered away, so that even the makers of a system cannot cheat it. The people on this forum did that work, in public and at real personal cost.

## Thank you

We did not run a ceremony and did not need to. The public parameters, the node, the indexer and the wallet library are all yours, and SWARM stands on them. That is the debt, and this post is first a thank-you.

Thank you to Electric Coin Company, for the protocol, the Sapling and Orchard pools, the proving systems and the research behind them. Thank you to the Zcash Foundation, for Zebra, the full node SWARM runs. Thank you to Zingo Labs, the authors of Zaino and zingolib: Zaino is the indexer behind our light-wallet servers and our explorer, and zingolib is inside every SWARM wallet.

Our repositories are `privacy-zebra`, `privacy-zaino` and `privacy-zingolib` under github.com/Swarmcoin. Each keeps its upstream history and licence, and our changes are published under the same licence as the upstream (MIT / Apache-2.0 for the node, Apache-2.0 for the indexer, MIT for the wallets).

## What we did not change

Consensus rules and cryptography. Block and transaction validation are Zebra's, with the network-upgrade rule set that was active on Zcash mainnet when we branched. Equihash 200,9 and the difficulty adjustment are unchanged. Sapling and Orchard, v5 transactions, Bech32m unified addresses and Base58Check transparent addresses, the `CompactTxStreamer` light-wallet service: all upstream. No cryptographic primitive, proving system or parameter set is modified. `doc/protocol.md` in github.com/Swarmcoin/swarm has a table of where to check each claim, and we would welcome anyone here checking it.

## What we changed

- A network definition: `SwarmMainnet`, network magic `SWMN`, and a genesis block with no spendable coins (hash `01b76d8a0f18c502b23ab6605e26296d189aa5770fc4a34155e5c7b250a0eff2`).
- Address prefixes: `swm1…` for unified shielded addresses, `s1…` and `s3…` for transparent ones.
- The subsidy: 6.25 SWM per block, 75-second blocks, halving every 1,680,000 blocks, 20,999,987.3152 SWM in total, computed with Zebra's own arithmetic.
- Funding streams: 8 % Core Development, 4 % Grants & Ecosystem, 8 % Community & Development Reserve, to three 2-of-3 multisig addresses, for the whole emission schedule.
- The light-wallet chain label `swarm-mainnet` and the SDK release `swarm-sdk-mainnet-1`.

## The funding streams, stated plainly

This forum has spent years on development funding and knows the arguments better than we do, so here is ours without decoration. SWARM's 20 % does not end the way the Founders' Reward ended. It is permanent, paid block by block to published addresses for the life of the chain. We do not dress this up: 20 % of every block goes to the project for the life of the chain. We are not proposing it as a model for anyone else; it is our design for our network, and it is open to your criticism.

## The closed start

We also started closed. Until 31 October 2026, 15:42 UTC only our own machines mine: about 33,408 blocks, about 208,800 SWM, about 0.99 % of the cap, split like every other block. Then the waiting list has 24 hours, and from 1 November 2026, 15:42 UTC mining is open to everyone. The published reason is that the infrastructure around the coin needs coins before public mining begins. No coins are promised. Please keep ASICs and rented hash power off the network.

## The apps, in two sentences

On top of the chain we built a messenger on Signal Desktop and Signal Server, running only on our own server, where you sign in with the wallet's 24 words and can pay inside the chat, and a browser on ungoogled-chromium with the wallet in the toolbar. Both are open source and first releases.

## Commitments

- Upstream fixes to Zebra, Zaino and zingolib will be tracked and merged. We do not keep a private patch set on consensus code.
- Bugs we find in shared code go upstream first, through the upstream projects' security processes.
- We will not ask anyone from ECC, the Foundation, the upstream teams or this forum to join us.
- We will not criticise Zcash or its funding decisions, here or anywhere.
- We say what is missing before anyone else does: no independent audit of the SWARM-specific changes has been published; desktop builds are unsigned; the browser is a pre-release; the messenger is a first release; and the light-wallet server we run learns which notes a wallet asked for.

A friendly fork that credits its upstream was tolerated here before, as Ycash was; two that did not were not. We would like to be judged by the same measure.

## What we would like

Criticism. If our description of what is inherited and what is defined is wrong anywhere, we would like to know. If the funding-stream arithmetic in our replay of `subsidy.rs` disagrees with the code, we would like to know. If the way we credit upstream falls short, tell us how to fix it.

We have deliberately not linked any downloads in this post. Is a link to our download page welcome here? If the moderators and the community would rather we did not post one, we will not; if it is welcome, we will add it in a reply. Documentation and source: github.com/Swarmcoin. Thank you for the years of work we are standing on.
