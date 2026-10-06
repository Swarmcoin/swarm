<!-- venue: comments only in r/CryptoCurrency, r/Monero, r/zec, r/privacy and similar threads (never as posts), flair: n/a, account requirements: an aged account above each subreddit's karma gate; disclose that you work on SWARM whenever SWARM is mentioned, when: ongoing from week 1, notes for the human poster: answer the question first; adapt every template so that no two comments are identical; several templates mention no project on purpose, use them as written; never mention price; in r/Monero and r/zec never compare projects by anything but design; if a reply is hostile, answer once with facts or not at all; security reports get the SECURITY.md path and nothing else -->

# Ten comment templates

Rewrite before use. A template posted twice word for word is spam, and it reads like it.

## 1. "How does a shielded payment actually hide anything?" (no SWARM)

The chain records that a valid transaction happened, its fee and its size, and a zero-knowledge proof that the inputs and outputs balance. The sender, the receiver and the amount are encrypted outputs that only the receiver's viewing key can decrypt. Anyone can verify the proof; nobody can read the payment.

## 2. "Isn't a privacy coin just a tool for criminals?" (no SWARM)

Shielded payments hide what is written to the chain, and that is all they hide; your ISP, your exchange and your light-wallet server still see what they see. Cash has the same property and is used for groceries far more than for crime. The design question is whether a public ledger of every purchase is a reasonable default, and we think it is not.

## 3. "What does a light-wallet server learn about me?" (SWARM named once)

A light wallet asks the server for the encrypted notes that might be its own and decrypts locally, so the server learns which notes you asked for, and for transparent addresses, which addresses. Not amounts, not counterparties of shielded payments, but not nothing. On SWARM (disclosure: we work on it) that is in SECURITY.md in plain words, and running your own node and indexer removes it; the same is true of any Zcash-stack light wallet.

## 4. "SWARM is just another Zcash fork with a dev tax"

Partly right, and we are the developers, so take that into account. The consensus and cryptography are unmodified Zcash as Zebra implements them; the 20% of every block that goes to three published multisig addresses is permanent and we do not call it a fair launch. What is different is the product side: a messenger that pays inside the chat and a browser with the wallet in the toolbar, both open source at github.com/Swarmcoin.

## 5. "Was there a premine?"

No coins in the genesis block; every SWM that exists has been mined. There was a closed start: until 31 October 2026, 15:42 UTC only the project's machines mine, about 208,800 SWM or 0.99% of the cap, 80% to the project's mining wallet and 20% to the funds like every other block, visible at mainnet.explore.swarm.green. Public mining opens 1 November 2026, 15:42 UTC. We work on the project; no coins are promised.

## 6. "Monero vs Zcash: which privacy model is better?" (no SWARM)

Monero makes every transaction private by default with ring signatures, stealth addresses and confidential amounts; the anonymity set is the ring. Zcash-stack coins make privacy optional per transaction with zero-knowledge proofs; the anonymity set is the whole shielded pool, but transparent transactions leak. Default-on buys you a larger guaranteed set; optional buys you exchange compatibility and smaller proofs than you may expect. Both are honest trade-offs, and the two communities are arguing for the same thing.

## 7. "Can I mine it on a GPU?"

Equihash 200,9, the same proof of work as Zcash, unchanged. ASICs for it exist and nothing in the rules keeps them out, so there is no promise that a GPU or CPU stays competitive. Mining opens to everyone on 1 November 2026, 15:42 UTC through the SWARM Node app, and we work on the project. No coins are promised.

## 8. "Has it been audited?"

No independent audit of the SWARM-specific changes has been published. The upstream components (Zebra, Zaino, zingolib, Signal, Chromium) have their own security records, and we inherit their open issues as well as their fixes. We work on the project; treat every claim on the site as a claim until the source, the checksums and the explorer back it.

## 9. "Which wallet should I use for shielded ZEC?" (no SWARM)

Use a wallet that defaults to a unified address and tells you whether a given payment is shielded or transparent before you send it. Check that it is open source, that the download has a published checksum, and that you understand which light-wallet server it talks to. If privacy matters to you more than convenience, run your own node and point the wallet at it.

## 10. "What is SWM worth?" or any price question

Whatever people agree it is worth. We don't promise a price, and SWM has no guaranteed value and can lose value, including all of it. We work on the project and will not discuss price here; the technical documentation is at github.com/Swarmcoin if that is useful to you.
