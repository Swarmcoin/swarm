---
title: "Surveillance money: why every payment you make is a public record, and what a shielded payment changes"
description: "How transparent ledgers turn every transfer into a permanent public record, what a SWARM shielded payment hides and does not hide, and how SWM is issued."
tags: [privacy, cryptocurrency, zero-knowledge, swarm]
canonical_url: https://swarm.green/
published: false
---

# Surveillance money: why every payment you make is a public record, and what a shielded payment changes

*Published by the SWARM project. SWARM is experimental software; nothing here is financial advice.*

## The problem: a ledger everyone can read

Most digital money is surveillance money. When you pay by card, your bank, the merchant's bank and the card network each keep a record of who paid whom, how much and when. When you pay with most cryptocurrencies, the record is worse, not better: it is copied to every node in the network, it names the paying and receiving addresses and the exact amount, and it never goes away.

A transparent ledger is exactly what the name says. Each transaction lists where the coins came from, where they went and how many there were, in the clear. Anyone can download the whole history.

The defence usually offered is that addresses are pseudonyms. That defence has not held. Chain analysis is a mature industry. It clusters addresses that spend together, follows change outputs, watches timing and amounts, and ties clusters to names the moment one address touches an exchange with identity checks or a public donation page. Once one address in a cluster has a name, the whole cluster has a name, backwards and forwards in time.

The consequences are ordinary and unpleasant. A salary paid on a transparent chain shows your salary to every shop you pay. A shop's income is visible to its competitors and its landlord.

## Why the existing answers fall short

### New addresses for every payment

Wallets have long generated a fresh address for each receipt. It helps against the laziest observer and nobody else. The spend that gathers those addresses together links them again, and the heuristics that do the linking are public knowledge.

### Mixing

CoinJoin-style mixing joins several people's payments into one transaction so that inputs and outputs are harder to pair. It needs coordination, and in custodial forms it needs trust. The amounts stay visible, the fact of having mixed is itself visible on the ledger, and some services treat mixed coins as suspicious by default.

What these two share is that privacy is added afterwards, on top of a ledger designed to show everything. SWARM starts from a ledger designed to show nothing it does not have to.

## What SWARM does

### A shielded payment, exactly

SWARM is private money. A shielded payment keeps the sender, the receiver and the amount encrypted on the chain. What the network checks is that the payment is valid: that the coins exist, that they have not been spent before, that the sender was allowed to spend them, and that no value was created out of nothing. It checks all of that with a zero-knowledge proof, which lets a node verify the statement without learning the facts behind it.

What the chain records for a shielded-to-shielded payment is that a transaction exists, its fee and its size. Not who paid, not who was paid, not how much. An optional memo travels with the payment, encrypted so that only the recipient can read it.

SWARM Wallet gives you a shielded address, `swm1…`, by default and tells you which kind of payment you are about to make. Transparent addresses, `s1…` and `s3…`, exist for the cases where visibility is wanted, for example an exchange deposit. Anything sent transparently is public forever, and a mixed transaction exposes its transparent side in full. Privacy is a choice you make per payment; the wallet makes the shielded choice the default one.

### What it does not hide

Shielding protects what is written to the chain. It does not protect everything about how you use the network, and we say so first.

Your network provider can see that you connect to a SWARM light-wallet server, `lwd-main.swarm.green:443`, and when. The light-wallet server learns which encrypted notes your wallet fetched and trial-decrypted; it does not learn the amounts or the counterparties, but it knows that your connection asked. If that matters to you, run your own node and indexer, or use a network-level privacy tool. SWARM does not make you invisible on the network, and we do not say that it does.

### Built on the Zcash protocol stack, unmodified

We did not write the cryptography, and we did not change it. SWARM runs the Zcash protocol as implemented by Zebra, the full node built by the Zcash Foundation. The shielded pools are Sapling and Orchard; the transaction format is Zcash v5; the proving parameters are the public ones from the Zcash ceremonies. The protocol itself is the work of Electric Coin Company and the Zcash Foundation over many years of review. The indexer behind our light-wallet servers and the wallet libraries are forks of Zaino and zingolib from Zingo Labs.

No cryptographic primitive, proving system or parameter set is modified. What SWARM defines is its own network: the name `SwarmMainnet`, the genesis block, the address prefixes, the emission schedule and the allocation. The protocol page at github.com/Swarmcoin lists each item as inherited or defined, so every claim can be checked against the source.

### Proof of work and the 80 / 8 / 4 / 8 split

SWARM is secured by proof of work, Equihash 200,9, with a 75-second target block time. Each block pays 6.25 SWM, halving every 1,680,000 blocks, about every 4 years, so the supply approaches 20,999,987.3152 SWM and never exceeds it. The genesis block holds no coins. Every SWM that exists has been mined. Mined, not sold.

Every block reward is split the same way: 80% to the miner who found the block, 8% to Core Development, 4% to Grants & Ecosystem and 8% to the Community & Development Reserve. The three project shares go to published 2-of-3 multisig addresses, fixed in the genesis rules. The percentages cannot be changed; the destinations can change only through a formal protocol upgrade.

Two things need saying plainly. First, the 20% allocation is permanent. Unlike Zcash's Founders' Reward, which ended after 4 years, SWARM's allocation runs for the whole life of the chain, shrinking with each halving; over that life about 4.2 million SWM go to the three project destinations. Second, because of that allocation, we do not call this a fair launch. It is not a premine, since nothing exists before it is mined and every share is paid block by block in public where anyone can count it. But it is an allocation, and a launch with an allocation is not what people mean by that phrase.

Specialised hardware for Equihash exists, and nothing in the rules keeps larger miners out. We do not promise that home computers stay competitive.

### A closed start, then public mining

Mainnet has been live since 2 October 2026, 15:42 UTC. The start is closed: until 31 October 2026, 15:42 UTC only the project's own machines mine. In those 29 days about 33,408 blocks are produced and about 208,800 SWM, about 0.99% of the cap, split like every other block. For the following 24 hours the people on the waiting list can mine too. From 1 November 2026, 15:42 UTC mining is open to everyone, and the node software is published on swarm.green.

The reason is an orderly start: the infrastructure around the coin, liquidity pools included, needs coins before public mining begins. That is an aim, not a promise about anything. No coins are promised. SWM has no guaranteed value and can lose value, including all of it.

### 24 words

When you create a wallet, it gives you 24 words. They are the only way back into your coins. Nobody at SWARM can reset or recover them, and we will never ask for them. The wallet's lock code protects the app on one device; it does not replace the words. Write them on paper and keep the paper offline.

## What it does not do yet

- No independent audit of the SWARM-specific changes has been published. The upstream components have their own security records, and SWARM inherits them, including their open issues. An independent review of the code as launched is in development; its findings will be published, including the uncomfortable ones.
- Builds for Windows and macOS are not yet signed with a vendor certificate. The operating systems warn; the SHA-256 checksum is your verification.
- The light-wallet server learns which encrypted notes a wallet asks for.
- You cannot mine yet, and there is no mining pool. Every miner will be solo when mining opens.
- The published Android wallet, 0.2.0-mainnet.4, no longer connects to the network; the version that does is being prepared. Today the wallet is for Windows, macOS and Linux.

## How to try it

1. Open swarm.green/ecosystem/wallet and pick your platform. The current version is SWARM Wallet 0.1.0-mainnet.11. Only download from swarm.green.
2. Note the SHA-256 shown beside the file. After the download, compute the digest and compare it:

   ```
   sha256sum <file>                      # Linux
   shasum -a 256 <file>                  # macOS
   certutil -hashfile <file> SHA256      # Windows
   ```

   If the two values differ, delete the file.
3. Install. Windows SmartScreen and macOS Gatekeeper warn because the build is unsigned; the matching checksum is what tells you the file is ours.
4. Create a wallet. Write the 24 words on paper. Set a lock code.
5. The wallet syncs with the mainnet light-wallet server and shows your `swm1…` address under Receive. A sender with a shielded wallet pays you privately.
6. Follow the chain at mainnet.explore.swarm.green. Every block shows the four parts of its reward; shielded amounts and counterparties are not visible there, by design. The genesis hash to check against is `01b76d8a0f18c502b23ab6605e26296d189aa5770fc4a34155e5c7b250a0eff2`.

## What comes next

Only what the roadmap already says. In development, with no dates, because a date on unfinished work is a guess: signed macOS builds, the Android and iOS mainnet wallets, a second seed node in a different failure domain, custody tooling for the three published funds, and the independent security review. Next after that is SWARM Market, where merchants are paid in SWM, shielded by default, without custody. Planned and not started: a pool protocol for miners, and integrations in other software.

Public mining opens on 1 November 2026, 15:42 UTC. Until then, the wallet, the explorer and the source at github.com/Swarmcoin are there to be read, built and checked. If the site and the code ever disagree, the code is right and the site gets fixed.
