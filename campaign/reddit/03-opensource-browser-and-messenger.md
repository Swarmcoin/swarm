<!-- venue: r/opensource, flair: Promotional (required; the sub allows self-promotion only under this flair), account requirements: any real account older than 30 days; comments in r/opensource for at least a week before posting (10 to 21 October 2026 is comments-only); read the sidebar rules on the day of posting, when: Mon 26 Oct 2026 15:00 UTC, notes for the human poster: the body starts with "I work on SWARM."; this post is about two open-source projects and their licences, the coin stays in the short paragraph that explains why the apps have a wallet; name repositories under github.com/Swarmcoin; answer licence questions precisely; never discuss what SWM is worth; the story's source, for a reader who asks: Phil Zimmermann's own announcement that the case was dropped, mit.edu/~prz/EN/news/PRZ_case_dropped.html -->

# In 1995 MIT Press printed PGP's source code as a book. Why publishing in the open is still the best defence a privacy tool has

I work on SWARM. We built the two projects below, nothing in this post is for sale, and we will not discuss what SWM, the coin they carry a wallet for, is worth.

## A program printed on paper

In 1991 Phil Zimmermann released Pretty Good Privacy, PGP, as free software. It spread outside the United States, and in 1993 US Customs opened a criminal investigation under the Arms Export Control Act, because strong encryption was then classed as a munition.

In 1995 MIT Press published the complete C source of PGP as a printed book, "PGP Source Code and Internals". A book could be exported legally. Anyone abroad could scan the pages and compile the program again.

On 11 January 1996 the Justice Department dropped the investigation, after three years, without charges. Zimmermann's own announcement of that decision is still online on his MIT page. PGP became the most widely used e-mail encryption tool of the decade.

The lesson I take from it: when a privacy tool is treated as something to control, publishing it in the open is the defence. Code that anyone can read, print and rebuild cannot be quietly withdrawn, and nobody has to take the authors' word for what it does.

## Why I am telling you this

We maintain two forks of privacy software, a browser and a messenger, and the only reason anyone should trust them is that every line is public under the upstream licence. Here is what is missing, then what they are.

## What is unfinished, first

- No independent audit of the SWARM-specific changes has been published. Signal's and Chromium's security records are theirs; the bugs we add are ours.
- Unsigned on Windows and macOS: SmartScreen warns, and macOS needs `xattr -dr com.apple.quarantine` after install.
- The browser is a Windows 64-bit pre-release with no tracker blocking and no phishing lists. Safe Browsing went out with the other Google services and nothing replaces it yet. No automatic updates, so Chromium security fixes depend on you checking back. Websites cannot reach the wallet. One build at a time on our own machine, many hours each.
- The messenger is a first release (0.1.x): one desktop per account, no phone app, Apple silicon only on macOS. It runs on our server; if the server goes down, the chat goes down, the chain does not. No reproducible builds yet for the Electron apps.
- The node and CPU-miner app is published only when public mining opens on 1 November 2026, 15:42 UTC. No coins are promised. Please keep ASICs and rented hash power off the network.
- The light-wallet server the wallet talks to learns which encrypted notes it asked for. Shielding hides what is on the chain, not that you use SWARM from your ISP.

## What they are

We run two forks: one of ungoogled-chromium, one of Signal Desktop.

**SWARM Browser** builds on ungoogled-chromium, currently Chromium 153, and adds a wallet to the toolbar: balance, receive, send, and history in a side panel. The keys never live in the browser process; the toolbar talks to a small wallet host installed next to the browser. Licence: BSD-3-Clause, as upstream. Repository: `swarm-browser`.

**SWARM Messenger** builds on Signal Desktop, Signal Server, libsignal and storage-service, rebranded and pointed at our own server, never at Signal's. You sign in with the 24-word recovery phrase of a SWARM wallet instead of a phone number, people find you by a username you set, and you can send a payment inside the conversation. Licence: AGPL-3.0, as upstream; the server side is published because AGPL requires it and because we think it should be anyway. Repositories: `swarm-messenger`, `swarm-messenger-server`, `swarm-libsignal`, `swarm-storage-service`.

Both use `swarm-wallet-core` (MIT), a typed TypeScript layer over a Rust addon built on zingolib, so the wallet logic is one codebase shared by both apps.

The coin, in one paragraph: SWARM (SWM) is a proof-of-work privacy coin, built on open-source foundations that have secured real value, left unmodified, with shielded payments that keep sender, receiver and amount encrypted on the chain. Mainnet has been live since 2 October 2026, 15:42 UTC, in a closed start until 31 October 2026, 15:42 UTC, then 24 hours for the waiting list, then public mining from 1 November 2026, 15:42 UTC. Every block pays 80 % to the miner plus fees and 20 % to three project addresses (8 % Core Development, 4 % Grants & Ecosystem, 8 % Community & Development Reserve) for the life of the chain, about 4.2 million SWM to 2-of-3 multisig addresses fixed in the genesis rules. We do not dress this up; it is not a premine either, since nothing exists before it is mined. That is why the apps have a wallet; the coin's own documentation is at github.com/Swarmcoin/swarm.

## Why forks and not upstream contributions

ungoogled-chromium would not take a wallet, and should not. Signal does not accept third-party clients on its servers, and should not; that is why the messenger runs only against our own server and carries our own trust roots. Each fork keeps its upstream history and licence, our changes are published under the same licence, and upstream fixes are tracked and merged.

## Building

The browser: `swarm-browser` builds ungoogled-chromium for Windows with the SWARM patches and the wallet host; expect many hours and a large machine. The messenger: pnpm and Node 22, the SWARM-specific steps are in the README of `swarm-messenger`; the server stack is Java 21 and Maven, with a staging stack in `swarm-messenger-server`. The wallet core: `npm ci && npm run typecheck && npm test` runs with the addon mocked; `npm run neon` builds the native addon and needs Rust and protoc. The map of every component is `doc/building.md` in `swarm`.

## If you install a binary

Download only from swarm.green/ecosystem. Every file carries its SHA-256; compare before you run it:

```
sha256sum <file>        # Linux
shasum -a 256 <file>    # macOS
Get-FileHash <file>     # Windows PowerShell
```

If it differs, do not run it. Keep the 24 words offline; we will never ask for them.

## What we want from this thread

Licence questions, especially on the AGPL boundary between client, server and the MIT wallet core. Packaging advice for Linux and macOS browser builds. Anyone willing to review how the wallet host keeps keys away from the renderer. Issues and pull requests are open in every repository under github.com/Swarmcoin.
