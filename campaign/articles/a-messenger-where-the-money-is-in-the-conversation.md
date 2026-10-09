---
title: "A messenger where the money is in the conversation: Signal's protocol, SWARM's server, no phone number"
description: "Why metadata says more than content, what end-to-end encryption does and does not protect, and how SWARM Messenger runs Signal's open-source protocol on SWARM's own server, signs you in with 24 words instead of a phone number, and puts shielded payments inside the chat."
tags: [privacy, messaging, encryption, signal]
canonical_url: https://swarm.green/
published: false
---

# A messenger where the money is in the conversation: Signal's protocol, SWARM's server, no phone number

*Published by the SWARM project. SWARM is experimental software; nothing here is financial advice.*

## Just metadata

In 2016 three Stanford researchers, Jonathan Mayer, Patrick Mutchler and John Mitchell, tested a claim that governments had made for years: that the records of who called whom, and when, are far less sensitive than what was said. They collected call and text metadata from volunteers through an Android app. No call was recorded and no message was read.

It was enough. One participant called a cardiology group, a medical laboratory, a pharmacy and a hotline for a heart device; the records pointed to a heart condition. Another participant's calls pointed to a firearm purchase. Another called a hardware store, a hydroponics supplier and a head shop; the records suggested a cannabis grow. The paper also found that phone numbers were easy to tie back to names using public directories and social media.

The people who collect metadata for a living have said the same thing more bluntly. In April 2014, in a debate at Johns Hopkins University with the law professor David Cole, Michael Hayden, a former director of the NSA and the CIA, said: "We kill people based on metadata." He added that the United States does not do this with the domestic telephone records programme; the remark was about overseas targeting. The point stands for what metadata can support.

The lesson is about the key that unlocks all of it. A phone number ties those records to a name, and almost every messenger makes your phone number your identity.

## What encryption hides, and what it does not

End-to-end encryption is a real protection. Only the two endpoints hold the keys, so the server in the middle relays ciphertext it cannot read. A breach of the server, a demand to the operator or a tap on the wire yields no message content.

What it hides is what you said, not that you said it. The EFF's guide to [why metadata matters](https://ssd.eff.org/module/why-metadata-matters) lists what stays visible: which account talked to which, when, how often, how much, and from which IP address. Good messengers shrink that; none can encrypt the fact that two devices exchanged packets.

The protocol most serious messengers use is Signal's, and its core is the [double ratchet](https://signal.org/docs/specifications/doubleratchet/) designed by Trevor Perrin and Moxie Marlinspike. Two gears turn at once. One turns with every message: each message gets a fresh key derived from a chain, the chain moves on, and the old key is thrown away, so a key stolen later cannot read earlier messages. The other turns with every reply: each side sends a new public key and mixes the new shared secret into its chain, so someone who copied the state at one moment is locked out again after the next exchange. There is no single long-lived key to steal.

That protection was nearly made optional in Europe. In May 2022 the European Commission proposed a regulation to fight child sexual abuse online that would have let authorities order messaging services to scan private messages, end-to-end encrypted ones included. The aim, protecting children, is one we share. The method would have meant scanning everyone's private messages, and an end-to-end encrypted app cannot do that without breaking the promise that only the two ends can read. In July 2025 the Council presidency revived mandatory detection orders; a blocking minority formed and the plan was pulled from a vote in October 2025. On 26 November 2025 the Council agreed a position centred on voluntary detection and risk mitigation, without mandatory scanning, as [eucrim](https://eucrim.eu/news/csa-regulation-council-position-reached/) reports; negotiations with Parliament follow, and [EDRi](https://edri.org/our-work/csa-regulation-document-pool/) keeps the documents.

## Why the usual answers fall short

**Payment apps with a chat attached** solve convenience and create surveillance. The company in the middle sees every conversation and every payment, holds your money, and can freeze either.

**Messengers with a coin bolted on** often have a custodial wallet, messaging that is not end-to-end encrypted by default, or a transparent coin, so the payment made in private is public on a ledger. A private chat about a public payment is not private.

**Signal** is the best answer to private messaging that exists, and the protocol SWARM Messenger runs is Signal's. But Signal asks for a phone number to register, and we wanted money in the chat on keys we hold ourselves.

What we wanted was Signal's cryptography, a server we run, an identity that is not a phone number, and a shielded payment that happens in the chat without the chat ever touching the chain.

## What SWARM Messenger does

<!-- OWNER ITEM 316: calls and groups written as planned per Marketing Desk default 2026-10-09; version from the download rows; confirm with the owner, then delete this marker -->
SWARM Messenger 0.1.5 is a desktop app for Windows, macOS and Linux.

It is built on Signal Desktop, libsignal, Signal Server and Signal's other server components, all open source from Signal Messenger LLC, and it is published under the AGPL-3.0 licence as upstream is. We did not write the encryption, and we did not change it. We credit Signal for it here and in every repository.

### SWARM's server, never Signal's

The app talks only to SWARM's own server, chat.swarm.green. It never registers with, connects to or sends anything through Signal's servers. Signal's protocol gives the server as little as it can: relays carry ciphertext and the minimum needed to deliver it. The server is run by the project and can go down; your messages are encrypted before they reach it.

### Sign in with 24 words, not a phone number

There is no phone number and no account to create. You sign in with your wallet's 24 words. Those words are your chat identity and your wallet; they never leave your computer. People find you by the username you set in Settings. Nobody in a chat with you learns anything they can use to call you, bill you or find you elsewhere.

### End-to-end encrypted messages

<!-- OWNER ITEM 316: calls and groups written as planned per Marketing Desk default 2026-10-09; version from the download rows; confirm with the owner, then delete this marker -->
Messages are end-to-end encrypted with the Signal protocol. Only you and the person you write to can read a message. You verify a contact once, and you are told if their key ever changes.

<!-- OWNER ITEM 316: calls and groups written as planned per Marketing Desk default 2026-10-09; version from the download rows; confirm with the owner, then delete this marker -->
The first release is one-to-one chat with photos, files and payments. Group chats and voice and video calls are on the roadmap under Planned, which means not started and no date.

### The wallet in the pane, the payment in the chat

The app has a wallet pane. From it you send SWM on SWARM mainnet to the person you are talking to without leaving the conversation, and you can ask for or share a payment address inside a chat. A message can ask for a payment; it can never spend for you. The payment itself is an ordinary shielded SWARM payment: sender, receiver and amount encrypted on the chain, carried through the SWARM mainnet light-wallet server like any payment from SWARM Wallet.

### Keys kept apart, nothing on the chain

Your chat identity is separate from your spending key. Both come from the same 24 words, but the key that signs your messages is not the key that spends your coins, and your wallet address does not publish who you talk to. No message is ever written to the chain. The chain only records that a valid payment happened; who asked for it, and in which conversation, stays in the encrypted chat.

### What the server and the network still see

Your network provider can see that you connect to chat.swarm.green and to the light-wallet server. The messenger server sees the minimum it needs to deliver ciphertext to the right account. The light-wallet server learns which encrypted notes your wallet fetched, not the amounts or the counterparties. End-to-end encryption protects the content of what you say; it does not hide that you use SWARM.

## What it does not do yet

- A first release. The first public desktop version, 0.1.0, shipped on 28 September 2026. Expect rough edges, and tell us what breaks.
- Unsigned. The Windows build is not signed, so SmartScreen warns. The macOS build is not signed by Apple, so you remove the quarantine flag by hand once, as described below.
- No phone app. There is no Android or iPhone version. One desktop per account.
- macOS is Apple silicon only, macOS 13 or later. There is no Intel build yet. Windows 10 or 11 on Intel or AMD, 64-bit. Linux: a .deb for Debian 12 and later or Ubuntu 22.04 and later, or an AppImage.
- No independent audit of the SWARM-specific changes has been published. Signal's components have their own security record, which SWARM inherits along with their open issues.
- The 24 words are everything. Anyone who has them has your chat identity and your coins. Nobody at SWARM can reset them, and we will never ask for them.

## How to try it

<!-- OWNER ITEM 316: calls and groups written as planned per Marketing Desk default 2026-10-09; version from the download rows; confirm with the owner, then delete this marker -->
1. Go to swarm.green/ecosystem/messenger and choose your platform. The current version is 0.1.5; the Windows installer is 191 MB. Only download from swarm.green.
2. Note the SHA-256 beside the file. After the download, compute the digest and compare it:

   ```
   Get-FileHash <file>                   # Windows PowerShell
   shasum -a 256 <file>                  # macOS
   sha256sum <file>                      # Linux
   ```

   Every character must match the value under Verify download. If it does not, delete the file.
3. Windows: run the installer; when SmartScreen warns, choose More info, then Run anyway. macOS: open the disk image, drag SWARM Messenger to Applications, then run once in Terminal: `xattr -dr com.apple.quarantine "/Applications/SWARM Messenger.app"`. Linux: install the .deb, or make the AppImage executable and run it.
4. Sign in with your wallet's 24 words. If you do not have a wallet yet, SWARM Wallet at swarm.green/ecosystem/wallet creates one and shows you the words; write them on paper and keep them offline.
5. Set a username in Settings. That is how people find you.
6. Open the wallet pane, and pay from inside the conversation.

A note on the words: they are your chat identity and your wallet. Type them into the app and nowhere else. Never into a website, never into a message, never for anyone who asks.

## What comes next

<!-- OWNER ITEM 316: calls and groups written as planned per Marketing Desk default 2026-10-09; version from the download rows; confirm with the owner, then delete this marker -->
Only what the roadmap already says. The roadmap's Planned list, which means not started and carries no dates, names the Android and iPhone apps, group chats, and voice and video calls. Signed builds are in development. Nothing is promised and nothing has a date; each piece is announced when it is finished and reviewed.

What exists today is a messenger that runs Signal's protocol on SWARM's server, signs you in without a phone number, and lets the money stay in the conversation. The source is at github.com/Swarmcoin. Read it, build it, check it.

## Sources

- Mayer, Mutchler and Mitchell, "Evaluating the privacy properties of telephone metadata", PNAS vol. 113 no. 20 (2016), doi 10.1073/pnas.1508081113 (cited by identifier; the site refuses automated requests)
- Michael Hayden at Johns Hopkins University, April 2014, reported by David Cole, The New York Review of Books, 10 May 2014: https://www.nybooks.com/online/2014/05/10/we-kill-people-based-metadata/ ; with Hayden's qualification: https://www.justsecurity.org/10311/michael-hayden-kill-people-based-metadata/
- Why metadata matters, EFF Surveillance Self-Defense: https://ssd.eff.org/module/why-metadata-matters
- The Double Ratchet Algorithm, Trevor Perrin and Moxie Marlinspike, Signal: https://signal.org/docs/specifications/doubleratchet/
- EU child sexual abuse regulation, Council position of 26 November 2025, eucrim: https://eucrim.eu/news/csa-regulation-council-position-reached/ ; EDRi document pool: https://edri.org/our-work/csa-regulation-document-pool/
- SWARM Messenger download page, versions and requirements: https://swarm.green/ecosystem/messenger; roadmap: https://swarm.green/roadmap; source code: https://github.com/Swarmcoin
