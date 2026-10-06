---
title: "A messenger where the money is in the conversation: Signal's protocol, SWARM's server, no phone number"
description: "How SWARM Messenger runs Signal's open-source protocol and server on SWARM's own infrastructure, signs you in with your wallet's 24 words instead of a phone number, and puts shielded payments inside the chat."
tags: [privacy, messaging, encryption, signal, swarm]
canonical_url: https://swarm.green/
published: false
---

# A messenger where the money is in the conversation: Signal's protocol, SWARM's server, no phone number

*Published by the SWARM project. SWARM is experimental software; nothing here is financial advice.*

## The problem: paying the person you are talking to

Most payments between people start as a conversation. Splitting a bill, paying back a loan, buying something from someone you know. And at the moment the money moves, the conversation stops. You leave the chat, open a payment app, ask for an address or an account, paste it back, check that what you pasted is what they sent, and hope that the chat app did not show that address to anyone else on the way.

If the payment app is one of the popular ones, it knows both of you. It knows the amount, the time and the note you wrote. Some have made that feed public by default. All of them keep it.

There is a second problem underneath: identity. Almost every messenger identifies you by your phone number. The number is tied to your name through your carrier, it can be taken over through your carrier, it is uploaded from every contact list you are in, and it is the same number you gave the bank, the dentist and the delivery service. To message someone you must hand them a global identifier for your whole life.

## Why the existing answers fall short

### Payment apps with a chat attached

They solve the convenience problem and create a surveillance one. The company in the middle sees every conversation and every payment, holds your money, and can freeze either. The chat is rarely end-to-end encrypted, and the payment never is.

### Messengers with a coin bolted on

Some messengers have added a wallet. Often the wallet is custodial, the messaging is not end-to-end encrypted by default, or the coin is transparent, so the payment you made in private is public on a ledger. A private chat about a public payment is not private.

### Signal

Signal is the best answer to private messaging that exists, and the protocol SWARM Messenger runs is Signal's. But Signal requires a phone number to register, and we wanted money in the chat on keys we hold ourselves.

What we wanted was Signal's cryptography, a server we run, an identity that is not a phone number, and a shielded payment that happens in the chat without the chat ever touching the chain.

## What SWARM Messenger does

SWARM Messenger 0.1.5 is a desktop app for Windows, macOS and Linux. It is a fork of Signal Desktop, of libsignal, of Signal Server and of Signal's storage and calling services, all by Signal Messenger LLC, published under the AGPL-3.0 licence as upstream is. We did not write the encryption, and we did not change it. We credit Signal for it here and in every repository.

### SWARM's server, never Signal's

The app talks only to SWARM's own server, chat.swarm.green. It never registers with, connects to or sends anything through Signal's servers; rebranded builds of the messenger talk only to SWARM's. Signal's protocol gives the server as little as it can: relays carry ciphertext and the minimum needed to deliver it. The server is run by the project and can go down; your messages are encrypted before they reach it.

### Sign in with 24 words, not a phone number

There is no phone number and no account to create. You sign in with your wallet's 24 words. Those words are your chat identity and your wallet; they never leave your computer. People find you by the username you set in Settings. Nobody in a chat with you learns anything they can use to call you, bill you or find you elsewhere.

### End-to-end encrypted messages and calls

Messages and calls are end-to-end encrypted with the Signal protocol. Only you and the person you write to can read a message. You can send photos and files. Group chats are supported, and so is settings sync. You verify a contact once, and you are told if their key ever changes.

### The wallet in the pane, the payment in the chat

The app has a wallet pane. From it you send SWM to the person you are talking to without leaving the conversation, and you can ask for or share a payment address inside a chat. A message can ask for a payment; it can never spend for you. The payment itself is an ordinary shielded SWARM payment: sender, receiver and amount encrypted on the chain, carried through the light-wallet server like any payment from SWARM Wallet.

### Keys kept apart, nothing on the chain

Your chat identity is separate from your spending key. Both come from the same 24 words, but the key that signs your messages is not the key that spends your coins, and your wallet address does not publish who you talk to. No message is ever written to the chain. The chain only ever records that a valid payment happened; who asked for it, and in which conversation, stays in the encrypted chat.

### What the server and the network still see

The same limits as the rest of SWARM apply, and we state them before anyone else does. Your network provider can see that you connect to chat.swarm.green and to the light-wallet server. The messenger server sees the minimum it needs to deliver ciphertext to the right account. The light-wallet server learns which encrypted notes your wallet fetched, not the amounts or the counterparties. End-to-end encryption protects the content of what you say; it does not hide that you use SWARM.

## What it does not do yet

- A first release. The first public desktop version, 0.1.0, shipped on 28 September 2026; 0.1.5 is current. Expect rough edges, and tell us what breaks.
- Unsigned. The Windows build is not signed, so SmartScreen warns. The macOS build is not signed by Apple, so you remove the quarantine flag by hand once, as described below.
- No phone app. There is no Android or iPhone version. One desktop per account.
- macOS is Apple silicon only, macOS 13 or later. There is no Intel build yet. Windows 10 or 11 on Intel or AMD, 64-bit. Linux: a .deb for Debian 12 and later or Ubuntu 22.04 and later, or an AppImage.
- No independent audit of the SWARM-specific changes has been published. Signal's components have their own security record, which SWARM inherits along with their open issues.
- The 24 words are everything. Anyone who has them has your chat identity and your coins. Nobody at SWARM can reset them, and we will never ask for them.

## How to try it

1. Go to swarm.green/ecosystem/messenger and choose your platform. The current version is 0.1.5. Only download from swarm.green.
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

Only what the roadmap already says. The roadmap's Planned list, which means not started and carries no dates, names the Android and iPhone apps, and further work on groups and on voice and video calls. Signed builds are in development. Nothing is promised and nothing has a date; each piece is announced when it is finished and reviewed.

What exists today is a messenger that runs Signal's protocol on SWARM's server, signs you in without a phone number, and lets the money stay in the conversation. The source is at github.com/Swarmcoin. Read it, build it, check it.
