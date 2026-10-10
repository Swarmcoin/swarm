<!-- venue: comments only, never posts, in r/CryptoCurrency, r/CryptoTechnology, r/privacycoins, the upstream coin's own subreddit (r/ plus its three-letter ticker; the lint forbids writing it; technical and design-comparison comments only) and r/cryptomining; never in r/privacy, r/PrivacyGuides, or the announcement threads of the largest ring-signature privacy coin's subreddit (r/ plus its name; the lint forbids writing it), flair: n/a, account requirements: an aged account above each subreddit's karma gate; every comment that names SWARM starts with "I work on SWARM.", when: from Sat 10 Oct 2026 onward (10 to 21 October 2026 is comments-only, no posts), notes for the human poster: answer the question first; rewrite every template before use so that no two comments are identical; several templates name no project on purpose, keep them that way; never discuss what SWM is worth beyond template 10; in the upstream coin's subreddit compare designs only, never projects or people; if a reply is hostile, answer once with facts or not at all; security reports get the SECURITY.md path and nothing else -->

# Ten comment templates

Rewrite before use. A template posted twice word for word is spam, and it reads like it. Each one starts with the answer; the ones that name SWARM start with the disclosure line and then the answer.

## 1. "How does a shielded payment actually hide anything?" (no project named)

It hides the contents, not the existence. The chain records that a valid transaction happened, its fee and its size, plus a zero-knowledge proof that inputs and outputs balance and that nothing was spent twice. Sender, receiver and amount sit in encrypted outputs that only the receiver's viewing key can open. Every node can check the proof; no node can read the payment. What the proof cannot hide is everything around it: your IP address, the server your wallet talks to, the timing.

## 2. "Isn't a privacy coin just a tool for criminals?" (no project named)

Shielding hides what is written to the chain and nothing else; your ISP, any exchange you use and your wallet's server still see what they see. Cash has the same property and buys far more groceries than anything else. The real design question is whether a permanent public record of every purchase should be the default for ordinary people, and few people would accept that for their bank statements.

## 3. "What does a light-wallet server learn about me?"

I work on SWARM. A light wallet asks the server for the encrypted notes that might be its own and decrypts them locally, so the server learns which notes you asked for and, for transparent addresses, which addresses. Not amounts, not counterparties of shielded payments, but not nothing. For SWARM it is written in SECURITY.md, and running your own `zebrad` and `zainod` removes it; the same holds for any wallet on the same upstream stack.

## 4. "SWARM is just another clone with a dev tax"

I work on SWARM, so weigh this accordingly. Partly right: 20 % of every block goes to three published 2-of-3 multisig addresses for the life of the chain (8 % Core Development, 4 % Grants & Ecosystem, 8 % Community & Development Reserve), and we do not dress that up. Consensus and cryptography are upstream's, unmodified. What differs is the network, the economics, a messenger that pays inside the chat and a browser with the wallet in the toolbar, all open at github.com/Swarmcoin. Whether that trade is worth it is your call.

## 5. "Was there a premine?"

I work on SWARM. No coins in the genesis block; every SWM that exists has been mined. There is a closed start: until 31 October 2026, 15:42 UTC only the project's machines mine, about 208,800 SWM or 0.99 % of the cap, split 80 % to the project's mining wallet and 20 % to the funds like every other block, all visible at mainnet.explore.swarm.green. The waiting list gets the next 24 hours; public mining opens 1 November 2026, 15:42 UTC. No coins are promised. Please keep ASICs and rented hash power off the network.

## 6. "Ring signatures or zero-knowledge pools: which privacy model is better?" (no project named)

Neither wins outright; they choose different crowds. Ring-signature designs make every transaction private by default, and the crowd you hide among is the ring of decoys picked for that payment. Shielded-pool designs prove validity with zero-knowledge proofs, and the crowd is everyone in the pool, but privacy is often optional and transparent transactions leak. Default-on keeps everyone in the crowd; optional makes integration easier and the pool smaller. Both camps argue for the same thing.

## 7. "Can I mine it on a GPU?"

I work on SWARM. The proof of work is Equihash 200,9, unchanged from upstream. ASICs for it exist and nothing in the rules keeps them out, so nobody can promise that a GPU or CPU stays competitive. Mining opens to everyone on 1 November 2026, 15:42 UTC through the SWARM Node app, published on swarm.green with its SHA-256 at that moment; check the checksum before you run it. No coins are promised. Please keep ASICs and rented hash power off the network.

## 8. "Has anyone checked the code?"

I work on SWARM. No independent audit of the SWARM-specific changes has been published. The components we build on, Signal and Chromium among them, have their own security records, and we inherit their open issues along with their fixes. Until someone independent reviews it, treat every claim on our site as a claim: read the source at github.com/Swarmcoin, compare checksums, look at the coinbase outputs in mainnet.explore.swarm.green. Security findings go to SECURITY.md, privately.

## 9. "Which wallet should I use for shielded payments?" (no project named)

Pick one that defaults to a shielded address and tells you, before you send, whether a payment is shielded or transparent. Then check three things: the source is open, the download has a published checksum you actually compare, and you know which server it talks to and what that server learns. If privacy matters more to you than convenience, run your own node and point the wallet at it; it costs a disk and an evening.

## 10. "What is SWM worth?" or any question about its value

I work on SWARM. Whatever people agree it is worth. Nobody promises you a price, and SWM can lose all its value. That is the whole answer I will give here, because a project's own people talking up its coin is exactly what you should distrust. If the technology is what you want to judge, the protocol and economics documents are at github.com/Swarmcoin/swarm, and the chain itself is at mainnet.explore.swarm.green.
