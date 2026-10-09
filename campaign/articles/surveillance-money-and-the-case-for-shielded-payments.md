---
title: "Surveillance money: why every payment you make is a public record, and what a shielded payment changes"
description: "How payment records became diaries, why transparent ledgers made it worse, what a SWARM shielded payment hides and does not hide, and how SWM is issued."
tags: [privacy, cryptocurrency, cryptography, swarm]
canonical_url: https://swarm.green/
published: false
lint_judged: ["other-projects: Zcash, Zebra, Zaino and zingolib named as the stack attribution; Zcash's Founders' Reward as the historical reference for the permanent 20%"]
---

# Surveillance money: why every payment you make is a public record, and what a shielded payment changes

*Published by the SWARM project. SWARM is experimental software; nothing here is financial advice.*

## A feed nobody meant to publish

Venmo, the payment app, launched with a social feed. Every payment showed the two names, the time and the note the payer wrote, and the feed was public by default; only the amount was hidden. In 2018 the researcher Hang Do Thi Duc downloaded 207,984,218 public Venmo transactions from 2017 through the app's open interface and published what they showed in a project called "Public By Default". From the notes and the names alone she could follow one person's drug purchases, a couple's break-up and a family's daily routine.

None of those people had published anything. They had paid each other. In February 2018 the US Federal Trade Commission settled with PayPal, Venmo's owner, over Venmo misleading users about its privacy settings: limiting who saw future payments did not make them private unless a second setting was also changed.

The lesson is plain. A payment record is a diary, and most payment systems keep it.

## Who reads the diary

A bank statement lists counterparties, amounts, dates, merchants and places. Together they show where you live, work, shop, travel and worship. In the United States the Bank Secrecy Act of 1970 obliges banks to keep those records and to report on them. A Currency Transaction Report goes to FinCEN for cash above ten thousand dollars in a day. A Suspicious Activity Report is filed for transactions of five thousand dollars or more that bank staff judge suspicious, and the customer may not be told it exists.

Banks and depositors challenged the Act. On 1 April 1974 the Supreme Court upheld it in California Bankers Association v. Shultz, 416 U.S. 21. Two years later, in United States v. Miller, it held that customers have no Fourth Amendment interest in their bank records at all. Most countries have an equivalent regime. None of it needs a warrant naming you.

That is the bank. A transparent blockchain is worse. A bank shows your records to a few parties under rules. A transparent chain shows them to everyone, forever, under none. Each transaction lists the paying addresses, the receiving addresses and the exact amount, copied to every node and never deleted.

The defence usually offered is that addresses are pseudonyms. The Bitcoin white paper of 2008 already knew the limit: in section 10 it recommends a new key pair for each transaction and admits that some linking is still unavoidable when one payment spends several inputs. In 2013 the paper "A Fistful of Bitcoins" by Meiklejohn and colleagues turned that limit into a method. Two heuristics did most of the work. Common-input ownership: addresses spent together in one transaction belong to one owner. Change detection: the fresh output that looks like change goes back to the sender. The authors then bought and sold at exchanges and merchants to attach names to the clusters. Once one address in a cluster has a name, the whole cluster has it, backwards and forwards in time.

## Why the usual fixes fall short

**New addresses for every payment.** Wallets have long made a fresh address for each receipt. It stops the laziest observer and nobody else. The next spend that gathers those addresses links them again, by exactly the heuristic above.

**Mixing.** A mixer takes deposits from many people and pays out to new addresses, hoping to break the link. Deposits and withdrawals stay public, so amounts, timing and address reuse can re-link them; an operator may keep logs; and governments treat mixers as suspect by category. The US Treasury sanctioned Tornado Cash on 8 August 2022 and removed it from the sanctions list on 21 March 2025, after litigation.

Both fixes add privacy afterwards, on top of a ledger designed to show everything. A shielded pool is different in kind: sender, receiver and amount are never written to the chain at all, and there is no operator to subpoena.

## What Bitcoin fixed, and what it left open

Bitcoin's first block, mined on 3 January 2009, carries that day's Times headline about a second bank bailout. What Bitcoin solved was scarcity without a bank: a hard cap, proof of work, a published issuance schedule that halves on its own. That frame is right, and SWARM keeps it. SWARM's cap is 20,999,987.3152 SWM; each block pays 6.25 SWM; the reward halves every 1,680,000 blocks; the work is proof of work. What SWARM adds is a ledger that records nothing it does not have to.

The tool that makes that possible is a zero-knowledge proof. The classic picture is a ring-shaped cave with a locked door at the back: Peggy goes in by one branch, Victor shouts which branch she must come out of, and only someone who knows the word that opens the door can obey every time. After twenty rounds a bluffer survives about once in a million tries, yet Victor never hears the word. A shielded payment works the same way: it proves that a spend is valid without saying who paid, who was paid or how much.

## What SWARM does

### A shielded payment, exactly

SWARM is private money. A shielded payment keeps the sender, the receiver and the amount encrypted on the chain. The network still checks that the coins exist, have not been spent before, were the sender's to spend, and that no value was created; it checks all of that with a zero-knowledge proof. For a shielded-to-shielded payment the chain records that a transaction exists, its fee and its size. An optional memo travels encrypted, readable only by the recipient.

SWARM Wallet gives you a shielded address, `swm1…` on SWARM mainnet, by default and tells you which kind of payment you are about to make. Transparent addresses, `s1…` and `s3…`, exist where visibility is wanted, such as an exchange deposit. Anything sent transparently is public forever.

### What it does not hide

Shielding protects what is written to the chain, and we say so first. Your network provider can see that you connect to the SWARM mainnet light-wallet server, `lwd-main.swarm.green:443`, and when. The light-wallet server sees your IP address and which blocks your wallet fetched. Trial decryption happens on your device, so the server should not learn which notes are yours, as [ZIP 307](https://zips.z.cash/zip-0307) sets out, but it knows that your connection asked. Run your own node and indexer, or use a network-level privacy tool, if that matters to you.

### Built on the Zcash protocol stack, unmodified

We did not write the cryptography, and we did not change it. SWARM runs the Zcash protocol as implemented by Zebra, the full node built by the Zcash Foundation: the Sapling and Orchard pools, the v5 transaction format, the public proving parameters from the Zcash ceremonies. The indexer and wallet libraries are forks of Zaino and zingolib from Zingo Labs. What SWARM defines is its own network: the name `SwarmMainnet`, the genesis block, the address prefixes, the emission schedule and the allocation. The protocol page at github.com/Swarmcoin lists each item as inherited or defined.

### Proof of work and the 80 / 8 / 4 / 8 split

SWARM mainnet runs Equihash 200,9 with a 75-second target block time. The genesis block holds no coins; every SWM that exists has been mined. Every block pays 80% to the miner, 8% to Core Development, 4% to Grants & Ecosystem and 8% to the Community & Development Reserve, the last three to published 2-of-3 multisig addresses fixed in the genesis rules. The percentages cannot be changed; the destinations only through a formal protocol upgrade.

Two things need saying plainly. The 20% allocation is permanent: unlike Zcash's Founders' Reward, which ended after 4 years, it runs for the whole life of the chain, about 4.2 million SWM in all. It is not a premine, since every share is paid block by block in public, but it is an allocation: 20% of every block, for the life of the chain. Specialised Equihash hardware (ASICs) exists, and nothing in the rules keeps larger miners out. Please keep ASICs and rented hash power off the network.

### A closed start, then public mining

SWARM mainnet has been live since 2 October 2026, 15:42 UTC. Until 31 October 2026, 15:42 UTC only the project's own machines mine: about 33,408 blocks and about 208,800 SWM, about 0.99% of the cap, split like every other block. The waiting list can mine for the following 24 hours, and from 1 November 2026, 15:42 UTC mining is open to everyone. The reason is an orderly start: the infrastructure around the coin needs coins before public mining begins. That is an aim, not a promise. No coins are promised. SWM has no guaranteed value and can lose value, including all of it.

### Two wallets, and 24 words

SWARM Wallet 0.1.0-mainnet.11 runs on Windows, macOS 12 or later (Apple silicon and Intel builds) and Linux. A hosted wallet also exists at wallet.swarm.green: you sign in with an email address, and the SWARM server holds that wallet and can see its balances, addresses and payments. The hosted wallet is the convenient option. The desktop wallet is the private one, because its keys never leave your computer.

The desktop wallet gives you 24 words. They are the only way back into your coins; nobody at SWARM can reset them, and we will never ask for them. The hosted wallet shows its 24 words too, so you can move it to the desktop wallet whenever you choose. Write the words on paper and keep the paper offline.

## What it does not do yet

- No independent audit of the SWARM-specific changes has been published. The upstream components have their own security records, and SWARM inherits them, including their open issues. An independent review of the code as launched is in development; its findings will be published, including the uncomfortable ones.
- Builds for Windows and macOS are not yet signed with a vendor certificate. The operating systems warn; the SHA-256 checksum is your verification.
- The light-wallet server learns which encrypted notes a wallet asks for.
- You cannot mine yet, and there is no mining pool. Every miner will be solo when mining opens.
- The old Android wallet, 0.2.0-mainnet.4, no longer connects to SWARM mainnet; the new Android build is being published. Today the desktop wallet is for Windows, macOS and Linux.

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
5. The wallet syncs with the SWARM mainnet light-wallet server and shows your `swm1…` address under Receive. A sender with a shielded wallet pays you privately.
6. Follow the chain at mainnet.explore.swarm.green, the SWARM mainnet explorer. Every block shows the four parts of its reward; shielded amounts and counterparties are not visible there, by design. The SWARM mainnet genesis hash to check against is `01b76d8a0f18c502b23ab6605e26296d189aa5770fc4a34155e5c7b250a0eff2`.

## What comes next

Only what the roadmap already says. In development, with no dates, because a date on unfinished work is a guess: signed macOS builds, the Android and iOS mainnet wallets, a second seed node in a different failure domain, custody tooling for the three published funds, and the independent security review. Next after that is SWARM Market, where merchants are paid in SWM, shielded by default, without custody. Planned and not started: a pool protocol for miners, and integrations in other software.

Public mining on SWARM mainnet opens on 1 November 2026, 15:42 UTC. Until then, the wallet, the explorer and the source at github.com/Swarmcoin are there to be read, built and checked. If the site and the code ever disagree, the code is right and the site gets fixed.

## Sources

- Hang Do Thi Duc, "Public By Default" (207,984,218 public Venmo transactions from 2017), as reported by CNN Money, 17 July 2018 (cited by identifier; the site refuses automated requests)
- US Federal Trade Commission, press release of February 2018 on the PayPal settlement over Venmo's privacy settings (cited by identifier)
- Bank Secrecy Act, FinCEN: https://www.fincen.gov/resources/statutes-and-regulations/bank-secrecy-act
- California Bankers Association v. Shultz, 416 U.S. 21 (1974), Library of Congress scan: https://tile.loc.gov/storage-services/service/ll/usrep/usrep416/usrep416021/usrep416021.pdf ; FindLaw: https://caselaw.findlaw.com/court/us-supreme-court/416/21.html
- United States v. Miller (1976), pointer: https://en.wikipedia.org/wiki/United_States_v._Miller
- Bitcoin white paper (2008), section 10: https://bitcoin.org/bitcoin.pdf
- Meiklejohn et al., "A Fistful of Bitcoins", Internet Measurement Conference 2013: https://cseweb.ucsd.edu/~smeiklejohn/files/imc13.pdf
- Tornado Cash sanctions, US Treasury, 8 August 2022: https://home.treasury.gov/news/press-releases/jy0916 ; delisting, 21 March 2025: https://home.treasury.gov/news/press-releases/sb0057
- Bitcoin's genesis headline, facsimile of The Times, 3 January 2009: https://www.thetimes03jan2009.com/
- The zero-knowledge cave, Quisquater, Guillou et al., CRYPTO 1989: https://link.springer.com/chapter/10.1007/0-387-34805-0_60
- What a light-wallet server learns, ZIP 307: https://zips.z.cash/zip-0307
- SWARM mainnet facts: https://swarm.green/network, https://swarm.green/verify, https://swarm.green/ecosystem/wallet; source code: https://github.com/Swarmcoin/swarm-releases
