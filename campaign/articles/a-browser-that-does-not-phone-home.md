---
title: "A browser that does not phone home: what we removed, what we switched on, and the wallet in the toolbar"
description: "Why a query log is a diary, what a stock browser sends before you type, what the SWARM Browser pre-release for Windows removes from Chromium, how the toolbar wallet keeps keys out of the browser, and what it cannot do yet."
tags: [privacy, browser, chromium, opensource]
canonical_url: https://swarm.green/
published: false
---

# A browser that does not phone home: what we removed, what we switched on, and the wallet in the toolbar

*Published by the SWARM project. SWARM is experimental software; nothing here is financial advice.*

## User 4417749

On 4 August 2006 AOL's research arm put about 20 million search queries online for researchers to study. They came from 657,000 users over three months, and each user's name had been replaced by a number. Five days later The New York Times named user No. 4417749. She was Thelma Arnold, 62, a widow in Lilburn, Georgia.

The reporters had not broken anything. They had read her queries: landscapers in Lilburn, homes sold in her subdivision, people with her surname, and the medical questions she had looked up for friends. Put together, the searches named their author. AOL withdrew the file within days; copies are still around.

The lesson is that a query log is a diary, and a number at the top of the page does not hide whose diary it is. A browser that sends what you type as you type it is a diary with a live feed.

## What a browser sends before you type

Your browser is the program that knows the most about you, and it runs for most of the day. A stock browser also reports on you by design, mostly to its vendor.

Before you have typed anything, a page can learn a good deal. The referrer header tells the next site which page you came from. Client hints report your browser version, platform and, on request, device model. WebRTC has exposed the local address of machines on home networks, though most builds now mask it. Fonts, screen size, canvas and audio add up to a fingerprint that the EFF's [Cover Your Tracks](https://coveryourtracks.eff.org/) test shows is often unique, no cookie needed.

Then there is the vendor channel. A stock Chrome build carries Google API keys and uses them. It sends what you type in the address bar to the search provider as you type, before you press Enter. It looks up pages against Safe Browsing, sends usage statistics, and takes remote feature switches from a server. Each piece has a reason. Together they keep a channel from your computer to one company open all day.

Encryption on the wire does not close that channel, and it does not hide where you go. With TLS 1.3 your provider cannot read the page, but the name of the site still travels in plaintext in the first handshake message, the Server Name Indication, unless [Encrypted Client Hello](https://blog.cloudflare.com/encrypted-client-hello/) is in use, and it is not yet everywhere.

## Why the usual answers fall short

**Extensions on top of Chrome.** A blocking extension helps against trackers on pages. It does nothing about what the browser itself sends, because it runs inside that browser and under its rules.

**Switching settings off.** Many of Chrome's data flows can be switched off, one by one, in menus that move between versions. Some cannot, because the request is compiled in. A setting is a promise to behave; a removed function is a fact.

**Tor Browser** is the strongest answer to a different question: hiding where your traffic comes from, by routing it through three relays. The [Tor Project](https://support.torproject.org/about/) is clear about the cost and the limits, including that logging into an account still identifies you. We recommend it for that job.

**Wallet extensions.** A wallet extension keeps the signing key in the browser. A page exploit, a malicious extension or a careless update can reach it there. The browser is the least trustworthy place on your computer to keep money.

## The base: ungoogled-chromium

[ungoogled-chromium](https://github.com/ungoogled-software/ungoogled-chromium) takes the vendor channel out of Chromium at the source. It removes functionality tied to Google domains, disables Safe Browsing, rewrites Google hostnames in the code to a domain that does not exist and blocks them at runtime, and strips pre-built binaries. It does not by itself stop fingerprinting or referrers; those need settings. SWARM Browser starts from it and switches those settings on.

## What SWARM Browser does

SWARM Browser 153.0.8010.52-6 is a pre-release for Windows. It is built on Chromium 153 from the ungoogled-chromium code base. We credit the ungoogled-chromium project for most of what follows; the SWARM parts are the wallet, the start page, the side panel and the colours.

### Google's services taken out

No Google API keys. No Safe Browsing lookups. No usage reports. No remote feature switches. These are not disabled; the code paths that make the calls are removed in the source.

### Privacy defaults switched on

The referrer is not sent across sites. Client hints are not sent, so less about your system is reported. WebRTC does not reveal your local network address. Link-tracking pings are off. Sites are not added as search engines automatically. The setting that always uses HTTPS is on, so a plain-HTTP page is not loaded without a warning.

### Search

The default search engine is DuckDuckGo, with search suggestions off, so nothing is sent while you type; a query leaves your machine when you press Enter and not before. You can choose another engine in Settings.

### SWARM Start and the Navigator

A SWARM welcome page opens on the first start. Every new tab opens SWARM Start, with a search box, the SWARM shortcuts and a set of tiles. The tiles ask no server anything until you switch the network tile on; a new tab is a local page, not a request. The SWARM Navigator is a side panel opened from the SWARM mark beside the address bar.

### The wallet in the toolbar, the keys outside the browser

The SWARM Wallet button sits beside the address bar. From it you see your balance on SWARM mainnet, receive and send SWM, and open your history in the side panel. The keys never live in the browser. The wallet in the toolbar talks to a small wallet host that is installed with the browser and runs as a separate program. A compromised page or extension does not have the keys to find, because they are not there.

The wallet host is a light wallet, like SWARM Wallet: it talks to the SWARM mainnet light-wallet server, which learns which encrypted notes it fetched and not the amounts or the counterparties. Your network provider sees that connection. Shielding protects what is on the chain, not the fact that you use SWARM.

The source is at github.com/Swarmcoin, under the same BSD-3-Clause licence as upstream.

### How to tell a real site from a copy

Because this build has no phishing lists, the check is yours, and it is a short one. A copy can imitate a page perfectly; it cannot imitate the domain. Read the address bar from the end of the host backwards: `swarm.green.example.com` belongs to example.com, not to swarm.green. The padlock only says the connection to that domain is encrypted; a phishing site has one too. Reach money sites from a bookmark you made yourself, not from a link in an email, a reply or an advert. The EFF's [guide to avoiding phishing](https://ssd.eff.org/module/how-avoid-phishing-attacks) says the same: go to the site yourself.

## What it does not do yet

This is the list from the download page, and we would rather you read it here than find out later.

- Pre-release. This is the first public build. Expect rough edges, and tell us what breaks.
- Unsigned. Windows SmartScreen warns before the first start: choose More info, then Run anyway. Check the SHA-256 first.
- Windows only. 64-bit Windows on Intel or AMD. There is no macOS or Linux build yet.
- No automatic updates yet. A new version is a new download from the page. Chromium publishes security fixes often, so check back.
- No ad or tracker blocking yet, and no phishing lists. Google Safe Browsing is removed with the other Google services, so nothing warns you about a dangerous site. Be careful with links, most of all near your wallet.
- Rewards. A rewards page is included, but it pays nothing.
- Paying websites. Websites cannot reach the wallet in this pre-release, so paying a site from the browser is not part of it.

Two more that apply to everything SWARM ships: no independent audit of the SWARM-specific changes has been published; the upstream components have their own security records. And the browser cannot hide from your network provider that you are using it.

## How to try it

1. Go to swarm.green/ecosystem/browser. There are two ways to get the same build: an installer, 204 MB, and a portable zip, 288 MB, which you unpack and run. Only download from swarm.green.
2. Before you install, check the SHA-256. In Windows PowerShell:

   ```
   Get-FileHash <file>
   ```

   Compare the result with the value under Verify download on the page. Every character must match. If it does not, delete the file.
3. Installer: run it. When SmartScreen warns, choose More info, then Run anyway. Portable zip: unpack it to a folder of your own and start `chrome.exe` inside it; the file keeps the name it has in Chromium. The wallet host comes inside the folder.
4. The SWARM Wallet button is pinned beside the address bar. If it is not, pin it from the puzzle-piece icon. Create a new wallet, or restore one from its 24-word recovery phrase.
5. Write the words on paper and keep them offline. Anyone who has them has the coins. Never type a recovery phrase into a website, and remember that nothing in this build warns you about a phishing page.

If you would rather keep money out of the browser entirely, SWARM Wallet for Windows, macOS and Linux is at swarm.green/ecosystem/wallet with its own checksums.

## What comes next

Only what the roadmap already says, and the roadmap gives no dates for unfinished work. The goal is a browser where paying a site is one click with the same confirmation screen as the wallet, where a site can ask for a payment but never take one, where trackers are blocked and fingerprinting is reduced, and where each site gets only the permissions you give it, with the wallet never one of them by default.

The pieces not in the pre-release are listed under Planned, which on our roadmap means not started: paying a site from the address bar, blocking ads and trackers, warning about phishing sites, and builds for macOS and Linux. The rewards page pays nothing, and nothing about rewards is promised. Signed builds are on the roadmap.

Until then: a browser that does not phone home, a wallet whose keys stay out of it, and a list of what is missing that we wrote before anyone else had to.

## Sources

- The AOL search-log release, 4 August 2006, and the identification of user No. 4417749: The New York Times, 9 August 2006, "A Face Is Exposed for AOL Searcher No. 4417749" (cited by identifier; the site refuses automated requests); pointer: https://en.wikipedia.org/wiki/AOL_search_log_release
- Browser fingerprinting test, EFF: https://coveryourtracks.eff.org/
- Server Name Indication and Encrypted Client Hello, Cloudflare: https://blog.cloudflare.com/encrypted-client-hello/
- What Tor does and does not hide, Tor Project: https://support.torproject.org/about/
- What ungoogled-chromium removes: https://github.com/ungoogled-software/ungoogled-chromium
- How to avoid phishing attacks, EFF Surveillance Self-Defense: https://ssd.eff.org/module/how-avoid-phishing-attacks
- SWARM Browser build, sizes and limits: https://swarm.green/ecosystem/browser; roadmap: https://swarm.green/roadmap; source code: https://github.com/Swarmcoin
