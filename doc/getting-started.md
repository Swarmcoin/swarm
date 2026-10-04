# Getting started

## 1. SWARM Wallet (desktop)

1. Open https://swarm.green/ecosystem/wallet and pick your platform: Windows (installer or portable zip), Linux (AppImage or .deb), macOS (Apple silicon and Intel).
2. Note the SHA-256 shown beside the file. After the download, compute the digest and compare:

   ```bash
   sha256sum SWARM-Wallet-0.1.0-mainnet.10-x86_64.AppImage        # Linux
   shasum -a 256 SWARM-Wallet-0.1.0-mainnet.10-mac-arm64.dmg      # macOS
   certutil -hashfile SWARM-Wallet-0.1.0-mainnet.10-win-x64-setup.exe SHA256   # Windows
   ```

3. Install. Windows SmartScreen and macOS Gatekeeper warn because the builds are not yet signed with a vendor certificate; the checksum is your verification.
4. Create a wallet. **Write the 24 words on paper.** They are the only way back into your coins; nobody can reset them.
5. Set a lock code. It locks the app on this device; it does not replace the 24 words.
6. The wallet syncs with `lwd-main.swarm.green` and shows your `swm1…` address under Receive.

## 2. SWARM Wallet for Android

The Android wallet is a direct APK from https://swarm.green/ecosystem/wallet (checksum beside it). Allow installs from your browser or file manager once, install, then the same steps as on desktop. The Google Play listing and the App Store version are in preparation.

## 3. Receiving and sending

- Give out your `swm1…` address. It is a unified address: senders with a shielded wallet pay you privately.
- Sending: paste the recipient's address, enter the amount, optionally a memo (encrypted, only the recipient reads it). The wallet refuses an address of the other network.
- A transparent address (`s1…`) is for the rare case where the other side needs a visible payment, for example an exchange deposit. Anything sent transparently is public forever.

## 4. Following the chain

https://mainnet.explore.swarm.green shows every block, every transaction and, for each block, the four parts of the reward. Search by height, block hash, transaction id or transparent address. Shielded amounts and counterparties are not visible there, by design.

## 5. Mining

Public mining opens on **1 November 2026, 15:42 UTC** (early access for 24 hours before, from 31 October 2026, 15:42 UTC). Until then only the project's own machines mine; see the [closed start](economics.md#the-closed-start).

When it opens: install SWARM Node from https://swarm.green/ecosystem (same checksum routine), enter your payout address (your wallet's `swm1…` address works; the app can show it), start. The app runs a full node and mines Equihash 200,9 on your CPU; it reports its measured rate and the blocks it found. Rewards mature after 100 blocks. A mining guide is published on the site when the closed start ends.

## 6. SWARM Messenger

Download from https://swarm.green/ecosystem/messenger (Windows, Linux, macOS). Sign in with your wallet's 24 words: there is no phone number and no account to create. Messages and calls are end-to-end encrypted and travel through SWARM's own server; payments happen inside the conversation from the wallet pane. Group chats and settings sync are supported.

## 7. SWARM Browser (pre-release)

A Windows build of Chromium 153 from the ungoogled-chromium code base with Google's services removed and the SWARM wallet inside. Pre-release: expect rough edges. https://swarm.green/ecosystem/browser.

## 8. Running your own node

`zebrad` from [privacy-zebra](https://github.com/Swarmcoin/privacy-zebra) joins the mainnet with the default configuration; see [building.md](building.md). The chain is young, so disk use is small today; it grows with the chain.

## Help

- Questions: issues in this repository, or `swarmofficial@atomicmail.io`.
- Security problems: [SECURITY.md](../SECURITY.md), privately.
- News: https://x.com/swarm_coin.
