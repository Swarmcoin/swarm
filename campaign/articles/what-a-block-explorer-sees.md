---
title: "What a block explorer sees, and what it cannot"
description: "The Netflix Prize data showed in 2006 that removing names does not hide people. A transparent blockchain is that kind of dataset, published for good. What an explorer shows for a transparent payment, for a shielded one, and for a real SWARM mainnet block."
tags: [privacy, blockchain, cryptography, explainer]
canonical_url: https://swarm.green/
published: false
lint_judged: ["privacy-claims: 'Anonymity' in the title of the cited Narayanan-Shmatikov paper", "other-projects: Zcash and Zebra named as the stack attribution; Zcash in the ZIP 311 title and the cited ZecHub and ZIP links"]
---

# What a block explorer sees, and what it cannot

*Published by the SWARM project. SWARM is experimental software; nothing here is financial advice.*

## Eight ratings

In October 2006 Netflix opened a contest: a million dollars to whoever could predict film ratings 10% better than its own system. To make that possible it published about 100 million ratings that some 480,000 subscribers had given to 17,770 films, each with the date it was given. The subscribers' names were replaced by numbers.

Two researchers at the University of Texas at Austin, Arvind Narayanan and Vitaly Shmatikov, tested that. Their paper, first posted in October 2006 and published at the IEEE Symposium on Security and Privacy in 2008, showed how little it took. Someone who knows eight of a subscriber's ratings, two of which may be wrong, and the dates to within 14 days, can pick out that subscriber's row in 99% of cases. With two ratings and dates to within three days, 68%. They then matched rows against a small sample of public reviews on IMDb, and from the matched ratings read off apparent political and other sensitive preferences.

Netflix had announced a second contest with more data. On 12 March 2010 it cancelled it, after a class action under the Video Privacy Protection Act and questions from the Federal Trade Commission.

The lesson the paper drew applies far beyond films. The names were never what identified people. The pattern did: which items, which days, in what combination. Any sparse record of what someone did and when behaves the same way: purchases, locations, listening history, payments.

A transparent blockchain is that kind of dataset. It was published on purpose, it can never be withdrawn, and instead of film ratings to the day it holds exact amounts to the second.

## A transparent payment in any explorer

Open a payment on a transparent chain in a block explorer, Bitcoin or any chain built the same way, and you get a page like this:

- the transaction id and the block it is in, with the time;
- every input: which earlier outputs were spent, from which addresses, and how much each held;
- every output: which addresses received money, and exactly how much;
- the fee;
- and, one click away, every other transaction each of those addresses ever took part in.

All of it is indexed, searchable and free, for anyone, for as long as the chain exists.

Addresses are not names, and that is where people stop worrying. They should not. In 2013 Sarah Meiklejohn and colleagues published "A Fistful of Bitcoins", which set out the two methods chain analysis still uses. First, if several addresses are spent together as inputs to one transaction, one party controlled all of them, so they belong in one cluster. Second, an output that looks like change goes back into the sender's cluster. The researchers then made purchases themselves at exchanges and shops to attach names to clusters. Bitcoin's own white paper had warned of the first method in 2008, in section 10: transactions with several inputs "necessarily reveal that their inputs were owned by the same owner".

So the explorer does not show a name. It shows the pattern, and as the Netflix data showed, the pattern is the name. One payment to a shop that knows who you are labels the whole cluster, backwards and forwards in time. A fresh address for every payment does not undo this; the next time two of them are spent together, they are linked again.

## A shielded payment in the same kind of explorer

Now open a fully shielded transaction on the Zcash protocol stack. The explorer shows:

- the transaction id and the block, with the time;
- the fee;
- how many shielded parts the transaction has;
- and the fact that its zero-knowledge proof verified, which every node checked before accepting the block.

That is all. The sender, the receiver, the amount and the memo are on the chain only in encrypted form. The proof convinces every node that the payment is valid: the notes being spent exist, they were not spent before, and no money was created. It convinces them without showing which notes, whose they were or how much moved.

One boundary stays visible. When money moves from a transparent address into the shielded pool, or back out, the amount that crosses is public, because the network has to check that the totals add up. The transparent side of such a payment is as readable as any transparent payment. Fully shielded, start to finish, is the case where the explorer has nothing to show.

That leaves a practical question: if the explorer cannot see a shielded payment, how do you prove you were paid, or that you paid? Not with the explorer. On the Zcash protocol stack there are two tools. A viewing key lets whoever holds it see the payments to an address, without being able to spend anything; you can give one to an accountant or an auditor and to nobody else. A payment disclosure, described in ZIP 311, which is still a draft, lets the sender prove one specific payment to one specific person. Both reveal what you choose, to whom you choose. These are protocol features; whether a given wallet offers them in its interface is a question for that wallet.

## A real block on SWARM mainnet

SWARM is a proof-of-work chain built on the Zcash protocol stack as implemented by Zebra, with the consensus rules and the cryptography left unmodified. Its explorer is at mainnet.explore.swarm.green. Here is what it showed for one block on 9 October 2026.

Block 8,100 was mined at 16:54:42 UTC. Its page lists the reward in four parts, the same for every block for the life of the chain:

| Part | Share | Amount | Paid to |
| --- | --- | --- | --- |
| Miner | 80% | 5.0 SWM | the miner's own payout address |
| Core Development | 8% | 0.5 SWM | `s3fLmEHc1xqs8KAe7QS7oupkhuGDjidV4eq` |
| Community & Development Reserve | 8% | 0.5 SWM | `s3g3pzQVhvVX17bzrrEN3vmcXZWSpj7KFVp` |
| Grants & Ecosystem | 4% | 0.25 SWM | `s3RiGvK5JzS8eh6ywN3K22f2LzDAhicgFuq` |

Open the block's only transaction, the coinbase that creates the new coins, and the explorer lists three transparent outputs: the three project addresses above, 1.25 SWM in total. Those addresses are transparent on purpose. Anyone can follow every coin they receive and every coin they spend, which is the point of publishing them.

The miner's 5.0 SWM is not among the outputs. The raw transaction, one click further, shows why: a shielded part with a proof attached and a balance of minus 5.0 SWM, which means 5.0 SWM entered the shielded pool. The amount crossing the boundary is visible, as described above. The address it went to is not.

The explorer's Shielded pools page adds up the same story. On 9 October 2026, at block 8,102, it showed 40,505 SWM in the shielded pool, called Ironwood, out of 50,637.5 SWM issued in total: almost exactly the miners' 80%. Until 31 October 2026, 15:42 UTC only the project's own machines mine; from 1 November 2026, 15:42 UTC mining is open to everyone, and the node software will be published on swarm.green. No coins are promised. SWM has no guaranteed value and can lose value, including all of it. Please keep ASICs and rented hash power off the network.

A shielded payment between two SWARM wallets appears on the same explorer the way the list above describes: an id, a block, a fee, its shielded parts, and nothing about who or how much. When we looked on 9 October 2026, the most recent hundred blocks held only their coinbase transactions, so there was no ordinary payment to point to. We would rather say that than stage one.

## What the explorer does not see, and who does

A block explorer only sees the chain. Other parties see other things, and shielding does not hide them.

**The light-wallet server.** SWARM Wallet is a light wallet: it does not download the whole chain, it asks the SWARM mainnet light-wallet server for compact blocks and checks them on your device. ZIP 307, the light-client design SWARM's wallet follows, sets a narrow goal: the server should not learn which transactions are addressed to you, because your device does the trial decryption. It still learns your IP address, when you sync, which block ranges you ask for and which transactions you send. If a wallet fetches a full transaction to read its memo, the server learns that this transaction interested this connection; ZIP 307 asks wallets to tell users that this reduces their privacy.

**Your internet provider.** It sees that you connect to the light-wallet server, when, and how much data moves. TLS hides the content, not the connection.

**Anyone you pay.** The person who receives your payment knows they received it, and how much, and from whom if you told them. Shielding keeps that off the public record, not out of their hands.

**Your own records.** Shielded notes stay on the chain for good, encrypted. Whoever later holds your 24 recovery words, or a viewing key derived from them, can read your history. Keep the words on paper, offline.

And the plain statement that applies to everything we ship: no independent audit of the SWARM-specific changes has been published; the upstream components have their own security records.

## Try it

Open mainnet.explore.swarm.green and pick any recent block. Look at the four parts of the reward, then open the coinbase transaction and count the outputs. Then open a payment on any transparent chain you like and click through its addresses for a few minutes.

The Netflix researchers needed eight ratings. A transparent explorer hands you the whole history at once. A shielded one hands you the fact that a valid payment happened, and leaves the rest to the people who made it.

## Sources

- The Netflix Prize data and its de-identification: Arvind Narayanan and Vitaly Shmatikov, "How To Break Anonymity of the Netflix Prize Dataset", arXiv cs/0610105 (October 2006, revised November 2007), published as "Robust De-anonymization of Large Sparse Datasets", IEEE Symposium on Security and Privacy 2008, DOI 10.1109/SP.2008.33, https://arxiv.org/abs/cs/0610105
- The dataset size, the cancelled sequel (12 March 2010), the lawsuit and the FTC: pointer, https://en.wikipedia.org/wiki/Netflix_Prize
- Clustering heuristics: Sarah Meiklejohn et al., "A Fistful of Bitcoins: Characterizing Payments Among Men with No Names", Internet Measurement Conference 2013, https://cseweb.ucsd.edu/~smeiklejohn/files/imc13.pdf
- The linked-inputs warning, section 10: Satoshi Nakamoto, "Bitcoin: A Peer-to-Peer Electronic Cash System", 2008, https://bitcoin.org/bitcoin.pdf
- What a shielded transaction shows: ZecHub, https://zechub.wiki/using-zcash/transactions
- Viewing keys: ZIP 310, "Security Properties of Sapling Viewing Keys", https://zips.z.cash/zip-0310 ; payment disclosures: ZIP 311, "Zcash Payment Disclosures" (Draft), https://zips.z.cash/zip-0311
- What a light-wallet server learns: ZIP 307, "Light Client Protocol for Payment Detection", https://zips.z.cash/zip-0307
- SWARM mainnet block 8,100, its coinbase transaction and the Shielded pools page, read on 9 October 2026 between 16:54 and 17:00 UTC: https://mainnet.explore.swarm.green
- The reward split and the three project addresses: https://swarm.green/network and https://swarm.green/verify ; source code: https://github.com/Swarmcoin
