<!-- venue: (a) Hacker News Show HN, two separate submissions two weeks apart; (b) Nostr, Bluesky, Farcaster, Mastodon first posts, the apps post and the opening post; (c) Lemmy lemmy.ml/c/privacy, flair: n/a, account requirements: HN account with some comment history; social accounts registered Sat 10 October 2026 with domain verification (Bluesky handle = swarm.green by DNS, Mastodon profile link verified, Nostr NIP-05 if possible); Lemmy account on a general instance with some comment history, when: (a) browser Tue 20 October 2026, 14:00 UTC; messenger Tue 3 November 2026, 14:00 UTC; (b) first posts Thu 22 October 2026, 15:00 UTC (Thu 15 October if the owner names an aged Reddit account by 12 October, see README.md); apps post Thu 29 October 2026, 15:00 UTC; opening post Sun 1 November 2026, 15:42 UTC; (c) Fri 30 October 2026, 14:00 UTC, notes for the human poster: Show HN links to the GitHub repository, not to the download page; never ask for upvotes; HN is hostile to anything with a coin in it, so answer every technical question once and calmly; on Bluesky and Mastodon keep to the character limits given; one link per post, in the first reply unless marked otherwise; the source line under each story post goes in that first reply; never discuss what SWM is worth; every mention of mining or the waiting list carries "No coins are promised." -->

# Show HN texts, first social posts and a Lemmy post

## (a) Show HN

### Browser (Tue 20 October 2026, 14:00 UTC)

**Title:** Show HN: SWARM Browser – ungoogled Chromium with a shielded-payments wallet in the toolbar (Windows pre-release)

**Link:** https://github.com/Swarmcoin/swarm-browser

**First comment:**

I work on SWARM. Before you click anything, a browser has already told the site your language and your operating system, and by default Chromium adds client hints with its brand, major version and platform, with more detail when a site asks. When you do click a link, the Referer header tells the next site which page you came from, and a link with a ping attribute can tell a third server that you clicked.

This build is ungoogled-chromium at Chromium 153 with two additions. The first is a set of privacy defaults turned on: no referrer to other sites, no client hints, WebRTC does not leak the local address, link pings off, HTTPS-only on, DuckDuckGo with suggestions off, and a local new-tab page that calls no server until you ask it to. The second is a toolbar wallet for SWARM, a proof-of-work coin with shielded payments. The keys are not in the renderer: the toolbar talks to a small wallet host installed next to the browser, and we would like someone to review that boundary.

What it does not do yet: it is a Windows-only pre-release, unsigned, so SmartScreen warns. There is no ad or tracker blocking and no phishing list; Safe Browsing went out with the other Google services and nothing replaces it yet, which means it is not one to recommend to someone who clicks on things. No automatic updates, so Chromium security fixes depend on a manual download. Websites cannot reach the wallet. A full build takes many hours on one machine and is not reproducible yet. No independent audit of our changes has been published.

Downloads are on swarm.green/ecosystem/browser with SHA-256 checksums; compare with `Get-FileHash` before running anything. Licence BSD-3-Clause, as upstream. We will not discuss what SWM is worth here. Technical criticism welcome.

### Messenger (Tue 3 November 2026, 14:00 UTC, two weeks after the browser)

**Title:** Show HN: SWARM Messenger – a Signal-based messenger on our own server; sign in with a wallet seed, pay inside the chat

**Link:** https://github.com/Swarmcoin/swarm-messenger

**First comment:**

I work on SWARM. Signal's code is open, and Signal asks one thing of anyone who builds on it: do not connect your build to Signal's servers. We follow that rule by running only our own server; our builds carry our own trust roots and cannot talk to Signal's infrastructure at all.

What it is: we took Signal Desktop, Signal Server, libsignal, storage-service and calling-service, rebranded them and pointed them at that server. Two changes matter. Identity is the 24-word recovery phrase of a SWARM wallet instead of a phone number, with a username people find you by. And a payment in SWM (a proof-of-work coin, shielded by default) can be sent inside a conversation. The wallet logic is a shared TypeScript-over-Rust core, `swarm-wallet-core`, also used by our browser.

What it does not do yet: this is a 0.1.x first release. One desktop per account, no phone app. Windows, Linux and Apple-silicon macOS only, all unsigned; macOS needs `xattr -dr com.apple.quarantine`. If our server is down the chat is down, though the chain is not. No reproducible builds. No independent audit of our changes has been published; Signal's security record is Signal's, and whatever we broke is ours. The light-wallet server the payment side uses learns which encrypted notes a wallet asked for; running your own node and indexer removes that.

Everything is AGPL-3.0, server included, at github.com/Swarmcoin. Downloads on swarm.green/ecosystem/messenger with SHA-256 checksums: `sha256sum` or `shasum -a 256` before installing. We will not discuss what SWM is worth here. We would like review of the seed-as-identity decision most of all.

## (b) Social posts

These are our own accounts, so they speak as "we". Story first: each first post is a piece of history a reader can enjoy without ever installing anything, and SWARM gets one or two sentences at the end.

### Nostr, first post (Thu 22 October 2026, 15:00 UTC)

On 11 January 2009 Hal Finney posted two words: "Running bitcoin". The next day he received the first Bitcoin transaction, 10 coins from Satoshi Nakamoto. He was no newcomer: he had worked on PGP, and in 2004 he built the first reusable proof-of-work system. Diagnosed with ALS in 2009, he kept writing software as the illness took his movement. He died on 28 August 2014. Privacy tools are built by people, often at a cost to themselves.

We build SWARM, a proof-of-work coin whose shielded payments keep sender, receiver and amount encrypted on the chain; mining opens to everyone on 1 November 2026, 15:42 UTC. No coins are promised. Please keep ASICs and rented hash power off the network.

Source for the first reply: https://www.coingecko.com/learn/who-is-hal-finney-first-bitcoin-transaction

### Bluesky, first post (Thu 22 October 2026, 15:00 UTC; under 300 characters)

On 9 March 1993 Eric Hughes wrote: "Privacy is necessary for an open society in the electronic age." We build SWARM, a coin whose shielded payments keep sender, receiver and amount encrypted on the chain. Live since 2 October 2026; a first release, no audit yet.

Source for the first reply: Eric Hughes, A Cypherpunk's Manifesto, 9 March 1993, https://www.elon.edu/u/imagining/expert_predictions/a-cypherpunks-manifesto/

### Farcaster, first post (Thu 22 October 2026, 15:00 UTC)

In 1982 David Chaum described blind signatures: a bank could sign a digital coin without seeing it, so a payment could be private and still impossible to forge. He founded DigiCash in 1989, and in late 1995 Mark Twain Bank in St. Louis became the first bank to issue its eCash. By 1998 it had about 300 merchants and 5,000 users, and DigiCash filed for bankruptcy that year. Private digital money existed 27 years before Bitcoin.

SWARM takes the other road: no company in the middle, proof of work, and shielded payments that keep sender, receiver and amount encrypted on the chain. Mainnet since 2 October 2026; a first release, and no independent audit of our changes has been published.

Source for the first reply: https://bitcoinmagazine.com/culture/genesis-files-how-david-chaums-ecash-spawned-cypherpunk-dream

### Mastodon, first post (Thu 22 October 2026, 15:00 UTC; under 500 characters)

In 1993 US Customs opened a criminal investigation into Phil Zimmermann because PGP, his free encryption program, had spread abroad, and strong encryption counted as a munition. In 1995 MIT Press printed PGP's source code as a book, which could be exported legally. The case was dropped on 11 January 1996, without charges.

We build SWARM: shielded payments on a proof-of-work chain. Unfinished: no audit, unsigned builds, a Windows-only browser pre-release.

Source for the first reply: https://www.mit.edu/~prz/EN/news/PRZ_case_dropped.html

### Fifth post: the apps (Thu 29 October 2026, 15:00 UTC; Nostr, Farcaster, Bluesky; Mastodon see the cadence note)

Signal's code is open, and Signal asks one thing of anyone who builds on it: stay off Signal's servers. SWARM Messenger does; it runs on our own server, you sign in with 24 words and you can pay inside the chat. With SWARM Wallet and SWARM Browser (ungoogled-chromium with the wallet in the toolbar, Windows pre-release) that makes three open-source apps, all first releases, all unsigned. Every download has a SHA-256 on the page; check it before you install.

Bluesky cut (under 300 characters): Signal asks one thing of anyone who builds on its code: stay off Signal's servers. SWARM Messenger runs on our own server; sign in with 24 words, pay inside the chat. Open source, a first release, unsigned. Check the SHA-256 on the page before you install.

First reply: https://swarm.green/ecosystem

### Story post (Sat 31 October 2026, 15:00 UTC; Nostr, Bluesky, Farcaster; Mastodon skips it)

In 1983 West Germany planned a full census: nationality, work, even how people got to work, with the answers to be shared with local registries. Citizens' initiatives called for a boycott, and several people took the Census Act to the Federal Constitutional Court. On 15 December 1983 the court struck down parts of the law and named a new right: informational self-determination. A society in which people cannot know who knows what about them, it held, is incompatible with that right. The reasoning still stands: people who fear being recorded stop exercising their freedoms.

Bluesky cut (under 300 characters): On 15 December 1983 West Germany's Federal Constitutional Court, ruling on a census many citizens had set out to boycott, created a right to informational self-determination. Its reasoning: people who fear being recorded stop exercising their freedoms.

Source for the first reply: Federal Constitutional Court, judgment of 15 December 1983 (English summary), https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/EN/1983/12/rs19831215_1bvr020983en.html

### Opening post (Sun 1 November 2026, 15:42 UTC; the same text on Nostr, Bluesky, Farcaster and Mastodon; link in the post)

Mining on SWARM is open to everyone from now, 1 November 2026, 15:42 UTC. The SWARM Node app is on swarm.green/ecosystem with its SHA-256; check it before you run it. No coins are promised. Please keep ASICs and rented hash power off the network.

### Cadence

- One post a week per network after the first posts, story first; the product is the example, at most one post in five, never two in a row.
- Mastodon: one post a week at most. The apps post of 29 October is held on Mastodon until Sun 8 November 2026 so that the opening post on 1 November keeps the account at one a week.
- On Nostr, Bluesky and Farcaster the apps post (29 October) and the opening post (1 November) are both about the product; the story post on Sat 31 October 2026, 15:00 UTC (the 1983 census ruling, above) sits between them so two product posts never follow each other. Mastodon skips the story post.
- Replies as a developer, in one or two sentences, with the fact and the link. Never argue.

## (c) Lemmy, lemmy.ml/c/privacy (Fri 30 October 2026, 14:00 UTC; about 300 words)

**Title:** What your browser tells a site before you click, and a degoogled Chromium 153 build that tells it less

I work on SWARM. Open any page and your browser has already sent the site your language and your operating system; Chromium also sends client hints with its brand, major version and platform, and more if the site asks. Click a link and the Referer header tells the next site where you came from; a link with a ping attribute can tell a third server that you clicked. None of this needs a cookie.

We maintain a build of ungoogled-chromium that turns as much of that off as we could without breaking sites. Disclosure: the build carries a toolbar wallet for a cryptocurrency we make, SWARM; that is the only sentence about the coin here, and we will not discuss it in the comments unless asked directly.

The base is ungoogled-chromium at Chromium 153, so everything upstream removes is removed: Google API keys, Safe Browsing lookups, usage and crash reports, remote feature switches. On top we turn on: no referrer to other sites, no client hints, WebRTC not revealing the local network address, link pings off, sites not added as search engines automatically, HTTPS-only on, DuckDuckGo with suggestions off, and a local new-tab page that calls no server until you switch the network tile on.

What is missing, and we would rather you heard it from us: no ad or tracker blocking and no phishing list, so with Safe Browsing gone nothing warns you about a dangerous site. Windows 64-bit only. Unsigned, so SmartScreen warns. No automatic updates, which with Chromium's security cadence is a real cost; if you cannot check the download page regularly, upstream ungoogled-chromium with a packager is the better choice. Built on one machine, not reproducible yet, no independent audit.

Downloads: swarm.green/ecosystem/browser, with a SHA-256 next to each file; run `Get-FileHash` and compare before you start it. Source and patches: github.com/Swarmcoin/swarm-browser, BSD-3-Clause.

Questions: which defaults would you add or revert, and is a Chromium build without any dangerous-site list acceptable to call a privacy browser at all? We expect the answer "a fork should only remove", and we take it seriously.
