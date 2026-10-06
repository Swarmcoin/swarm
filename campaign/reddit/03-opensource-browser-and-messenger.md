<!-- venue: r/opensource, flair: Promotional (required; the sub allows self-promotion only under this flair), account requirements: any real account older than 30 days; read the sidebar rules on the day of posting, when: week 2, notes for the human poster: this is about two open-source projects and their licences, not about the coin; keep the coin to the one paragraph that explains why the wallet exists; link repositories by name under github.com/Swarmcoin; answer licence questions precisely; never discuss price -->

# Two forks we maintain in the open: a degoogled Chromium with a built-in wallet (BSD-3-Clause) and a Signal-based messenger on our own server (AGPL-3.0)

Disclosure and the flair say it: we built these, and this is a promotional post. We would rather have your criticism of the code than your download.

## What they are

**SWARM Browser** is a fork of ungoogled-chromium, currently on Chromium 153, with a cryptocurrency wallet in the toolbar. The wallet shows a balance, receives and sends, and keeps history in a side panel. The keys never live in the browser process: the toolbar talks to a small wallet host that is installed next to the browser. Licence: BSD-3-Clause, as upstream. Repository: `swarm-browser`.

**SWARM Messenger** is a fork of Signal Desktop, Signal Server, libsignal, storage-service and calling-service, rebranded and pointed at our own server, never at Signal's. You sign in with the 24-word recovery phrase of a SWARM wallet instead of a phone number, people find you by a username you set, and you can send a payment inside the conversation. Licence: AGPL-3.0, as upstream, and the server side is published because AGPL requires it and because we think it should be anyway. Repositories: `swarm-messenger`, `swarm-messenger-server`, `swarm-libsignal`, `swarm-storage-service`, `swarm-calling-service`.

Both use `swarm-wallet-core` (MIT), a typed TypeScript layer over a Rust addon built on zingolib, so the wallet logic is one codebase shared by the messenger and the browser.

The coin, in one paragraph: SWARM (SWM) is a proof-of-work privacy coin on the Zcash protocol stack as implemented by Zebra, with shielded payments that keep sender, receiver and amount encrypted on the chain. That is why the apps have a wallet. This post is not about the coin; its own documentation is at github.com/Swarmcoin/swarm.

## What they do not do yet

Browser:

- Pre-release, Windows 64-bit only. No macOS or Linux build.
- Unsigned: SmartScreen warns on first start.
- No ad or tracker blocking and no phishing lists. Safe Browsing was removed with the other Google services and nothing replaces it yet.
- No automatic updates. A new version is a new download, so Chromium security fixes depend on you checking back.
- Websites cannot reach the wallet. Paying a site from the browser is not part of this release.
- Built on the project's own build machine; a full Chromium build takes many hours, and it is one build at a time in CI.

Messenger:

- First release (0.1.x). One desktop per account, no phone app, no Intel Mac build (Apple silicon only on macOS).
- Unsigned on Windows and macOS; macOS needs `xattr -dr com.apple.quarantine` after install.
- Runs on our server. If the server goes down, the chat goes down; the chain does not.
- No reproducible builds yet for the Electron apps.

Both: no independent audit of our changes. Signal's and Chromium's security records are theirs; the bugs we add are ours.

## Why forks and not upstream contributions

ungoogled-chromium would not take a wallet, and should not. Signal does not accept third-party clients on its servers, and should not; that is why the messenger runs only against our own server and carries our trust roots. Each fork keeps its upstream history and licence, and our changes are published under the same licence as the upstream. Upstream fixes are tracked and merged.

## Building

The browser: `swarm-browser` builds ungoogled-chromium for Windows with the SWARM patches and the wallet host; expect many hours and a large machine. The messenger: pnpm, Node 22, the SWARM-specific steps are in the README of `swarm-messenger`; the server stack is Java 21 and Maven, with a staging stack in `swarm-messenger-server`. The wallet core: `npm ci && npm run typecheck && npm test` runs with the addon mocked; `npm run neon` builds the native addon and needs Rust and protoc. The map of every component is `doc/building.md` in `swarm`.

## If you install a binary

Download only from swarm.green/ecosystem. Every file is listed with its SHA-256; compare before you run it:

```
sha256sum <file>        # Linux
shasum -a 256 <file>    # macOS
Get-FileHash <file>     # Windows PowerShell
```

Keep the 24 words offline. We will never ask for them.

## What we want from this thread

Licence questions, especially on the AGPL boundary between client, server and the wallet core. Packaging advice for Linux and macOS browser builds. Anyone who wants to review how the wallet host isolates keys from the renderer. Issues and pull requests are open in every repository under github.com/Swarmcoin.
