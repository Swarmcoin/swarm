<!-- venue: (a) Hacker News Show HN, two separate submissions at least two weeks apart; (b) Nostr, Bluesky, Farcaster, Mastodon first posts; (c) Lemmy lemmy.ml/c/privacy, flair: n/a, account requirements: HN account with some comment karma; social accounts with domain verification (Bluesky handle = swarm.green, Mastodon profile link verified, Nostr NIP-05 if possible), when: (a) browser week 2 or 3, messenger week 5 or 6; (b) week 1; (c) week 3, notes for the human poster: Show HN links to the GitHub repository, not to the download page; never ask for upvotes; HN is anti-crypto, answer every technical point once and calmly; on Bluesky and Mastodon keep to the character limits given; one link per post; never discuss price; every mention of mining carries "No coins are promised." -->

# Show HN texts, first social posts and a Lemmy post

## (a) Show HN

### Browser

**Title:** Show HN: SWARM Browser – ungoogled Chromium with a shielded-payments wallet in the toolbar (Windows pre-release)

**Link:** https://github.com/Swarmcoin/swarm-browser

**First comment:**

We built this and we would like it taken apart. It is ungoogled-chromium at Chromium 153 with two additions: a set of privacy defaults turned on (no referrer to other sites, no client hints, WebRTC does not leak the local address, link pings off, HTTPS-only on, DuckDuckGo with suggestions off, a local new-tab page that calls no server until you ask it to) and a toolbar wallet for SWARM, a proof-of-work privacy coin on the Zcash protocol stack. The keys are not in the renderer: the toolbar talks to a small wallet host installed next to the browser, and we would like someone to review that boundary.

What is missing: it is a Windows-only pre-release, unsigned, so SmartScreen warns. There is no ad or tracker blocking and no phishing list; Safe Browsing went out with the other Google services and nothing replaces it yet, which means it is not safe to recommend to someone who clicks on things. No automatic updates, so Chromium security fixes depend on a manual download. Websites cannot reach the wallet. A full build takes many hours on one machine and is not reproducible yet. No independent audit of our changes.

Downloads are on swarm.green/ecosystem/browser with SHA-256 checksums; compare with `Get-FileHash` before running anything. Licence BSD-3-Clause, as upstream. We will not discuss the coin's price here. Technical criticism welcome.

### Messenger

**Title:** Show HN: SWARM Messenger – a Signal fork on our own server, sign in with a wallet seed, pay inside the chat

**Link:** https://github.com/Swarmcoin/swarm-messenger

**First comment:**

We forked Signal Desktop, Signal Server, libsignal, storage-service and calling-service, rebranded them and pointed them at our own server; the builds carry our trust roots and cannot talk to Signal's infrastructure, which is the one rule Signal asks forks to follow. Two changes matter: identity is the 24-word recovery phrase of a SWARM wallet instead of a phone number, with a username people find you by, and a payment in SWM (a proof-of-work privacy coin on the Zcash stack, shielded by default) can be sent inside a conversation. The wallet logic is a shared TypeScript-over-Rust core, `swarm-wallet-core`, also used by our browser.

What is missing: this is a 0.1.x first release. One desktop per account, no phone app. Windows, Linux and Apple-silicon macOS only, all unsigned; macOS needs `xattr -dr com.apple.quarantine`. If our server is down the chat is down, though the chain is not. No reproducible builds. No independent audit of our changes; Signal's security record is Signal's, and whatever we broke is ours. The light-wallet server the payment side uses learns which encrypted notes a wallet asked for; running your own node and indexer removes that.

Everything is AGPL-3.0, server included, at github.com/Swarmcoin. Downloads on swarm.green/ecosystem/messenger with SHA-256 checksums: `sha256sum` or `shasum -a 256` before installing. We will not discuss price. We would like review of the seed-as-identity decision most of all.

## (b) First posts

### Nostr

We are SWARM (SWM): a proof-of-work privacy coin on the Zcash protocol stack as implemented by Zebra. Shielded payments keep sender, receiver and amount encrypted on the chain. 75-second blocks, 6.25 SWM per block, 20,999,987 SWM at most, no coins in genesis. Mainnet live since 2 October 2026; public mining from 1 November 2026, 15:42 UTC. Every block pays 80% to the miner and 20% to three published project addresses, permanently; we do not call that a fair launch. No independent audit yet, unsigned builds. No coins are promised. https://swarm.green

### Bluesky (under 300 characters)

SWARM (SWM) is a proof-of-work privacy coin on the Zcash stack via Zebra. Shielded payments: sender, receiver and amount encrypted on chain. Mainnet live since 2 October 2026; public mining from 1 November 2026. 20% of each block funds the project, permanently. No audit yet. swarm.green

### Farcaster

SWARM (SWM): proof of work, Equihash 200,9, Zcash consensus and cryptography unmodified via Zebra. 6.25 SWM per block, 75 s, 20,999,987 SWM cap, 0 coins in genesis. Mainnet live since 2 October 2026, public mining from 1 November 2026, 15:42 UTC. 80% of each block to the miner, 20% to three published project addresses, for the life of the chain. No audit of our changes yet; builds unsigned. No coins are promised; no price talk from this account. https://swarm.green

### Mastodon (under 500 characters)

We are the developers of SWARM (SWM), a proof-of-work privacy coin on the Zcash protocol stack as implemented by Zebra. Shielded payments keep sender, receiver and amount encrypted on the chain. Mainnet live since 2 October 2026; mining opens to everyone on 1 November 2026, 15:42 UTC. Unfinished: no independent audit of our changes, unsigned builds, a Windows-only browser pre-release. 20% of every block funds the project, permanently. No coins are promised. https://swarm.green

### Fifth post (any of the four, the following week): the apps

Three open-source apps around the chain: SWARM Wallet (Windows, macOS, Linux, Android), SWARM Messenger (a Signal fork on our own server, sign in with 24 words, pay in the chat, AGPL-3.0) and SWARM Browser (ungoogled Chromium with the wallet in the toolbar, Windows pre-release, BSD-3-Clause). All unsigned, all early. Every download has a SHA-256 on the page; check it before you install. https://github.com/Swarmcoin

## (c) Lemmy, lemmy.ml/c/privacy (about 300 words)

**Title:** A degoogled Chromium 153 build with privacy defaults on: what it removes, what it still lacks

We maintain a fork of ungoogled-chromium and would like the view of people who care about this more than about the project behind it. Disclosure: the fork carries a toolbar wallet for a cryptocurrency we build, SWARM; that is the only sentence about the coin here, and we will not discuss it in the comments unless asked directly.

The base is ungoogled-chromium at Chromium 153, so everything upstream removes is removed: Google API keys, Safe Browsing lookups, usage and crash reports, remote feature switches. On top we turn on: no referrer to other sites, no client hints and less system information to sites, WebRTC not revealing the local network address, link-tracking pings off, sites not added as search engines automatically, HTTPS-only on, DuckDuckGo as default search with suggestions off so nothing is sent while you type, and a local new-tab page whose tiles call no server until you switch the network tile on.

What is missing, and we would rather you heard it from us: no ad or tracker blocking and no phishing list, so with Safe Browsing gone nothing warns you about a dangerous site. Windows 64-bit only. Unsigned, so SmartScreen warns. No automatic updates, which with Chromium's security cadence is a real cost; if you cannot check the download page regularly, upstream ungoogled-chromium with a packager is the better choice. Built on one machine, not reproducible yet, no independent audit.

Downloads are on swarm.green/ecosystem/browser with SHA-256 checksums next to each file; run `Get-FileHash` and compare before you start it. Source and patches: github.com/Swarmcoin/swarm-browser, BSD-3-Clause.

Questions: which defaults would you add or revert, and is a Chromium fork without any dangerous-site list acceptable to call a privacy browser at all? We expect the answer "a fork should only remove", and we think it is a fair one.
