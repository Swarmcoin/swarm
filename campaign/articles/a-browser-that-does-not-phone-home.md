---
title: "A browser that does not phone home: what we removed, what we switched on, and the wallet in the toolbar"
description: "What the SWARM Browser pre-release for Windows removes from Chromium, which privacy defaults it turns on, how the toolbar wallet keeps keys out of the browser, and what it cannot do yet."
tags: [privacy, browser, chromium, opensource, swarm]
canonical_url: https://swarm.green/
published: false
---

# A browser that does not phone home: what we removed, what we switched on, and the wallet in the toolbar

*Published by the SWARM project. SWARM is experimental software; nothing here is financial advice.*

## The problem: the biggest data pipe on your computer

Your browser is the program that knows the most about you. It sees every page you read, every search you type, every form you fill in, and it runs for most of the day. For most people that browser is Chrome, and Chrome is made by a company whose revenue comes from advertising.

That shows in the defaults. A stock Chrome build carries Google API keys and uses them. It sends what you type in the address bar to the search provider as you type, before you press Enter. It looks up pages against Safe Browsing. It sends usage statistics and crash reports. It takes remote feature switches, so that the behaviour of the browser on your machine can be changed from a server without a new version being installed. None of this is hidden, and each piece has a reason. Together they make a channel from your computer to Google that is open all day.

Then there is what the web does to you through any browser. The referrer header tells the next site which page you came from. Client hints report your operating system, CPU architecture, device model and full browser version so that a site can fingerprint you without a cookie. WebRTC can reveal the local address of your machine on your home network. Hyperlink auditing sends a ping to a tracking server when you click a link. Sites quietly register themselves as search engines in your settings.

And if you keep cryptocurrency in a browser extension, the keys that spend your money live inside the same process as every web page you open and every other extension you installed.

## Why the existing answers fall short

### Extensions on top of Chrome

A blocking extension helps against trackers on web pages. It does nothing about what the browser itself sends, because it runs inside that browser and under its rules. The extension platform decides what an extension may see and block, and that platform is not set by you.

### Switching the settings off

Many of Chrome's data flows can be switched off, one by one, in menus that move between versions. Some cannot be switched off at all, because the code that makes the request is compiled in. A setting is a promise to behave; a removed function is a fact.

### Privacy browsers with their own business model

Several browsers ship with tracking blocked and a different company's services wired in instead, sometimes with a token or a rewards programme attached. We respect the work, and we think a browser whose privacy comes from a company's goodwill is a different design from one whose privacy comes from code you can read. Tor Browser is the strongest answer to a different question, hiding where your traffic comes from, and carries the cost that comes with that.

### Wallet extensions

A wallet extension keeps the signing key in the browser. A page exploit, a malicious extension or a careless update can reach it there. The browser is the least trustworthy place on your computer to keep money.

## What SWARM Browser does

SWARM Browser 153.0.8010.52-6 is a pre-release for Windows. It is built on Chromium 153 from the ungoogled-chromium code base, which removes Google's services from Chromium rather than switching them off. We credit the ungoogled-chromium project for most of what follows; the SWARM parts are the wallet, the start page, the side panel and the colours.

### Google's services taken out

No Google API keys. No Safe Browsing lookups. No usage reports. No remote feature switches. These are not disabled; the code paths that make the calls are removed in the source.

### Privacy defaults switched on

Other sites are not told which page you came from: the referrer is not sent across sites. Client hints are not sent, and less about your system is reported to sites. WebRTC does not reveal your local network address. Link-tracking pings are off. Sites are not added as search engines automatically. Always use secure connections is on, so a page that offers only plain HTTP is not loaded without a warning.

### Search

The default search engine is DuckDuckGo, with search suggestions off, so nothing is sent while you type; a query leaves your machine when you press Enter and not before. The search box on SWARM Start and the address bar use it. You can choose another engine in Settings.

### SWARM Start and the Navigator

A SWARM welcome page opens on the first start. Every new tab opens SWARM Start, with a search box, the SWARM shortcuts and a set of tiles. The tiles ask no server anything until you switch the network tile on; a new tab is a local page, not a request. The SWARM Navigator is a side panel opened from the SWARM mark beside the address bar.

### The wallet in the toolbar, the keys outside the browser

The SWARM Wallet button sits beside the address bar. From it you see your balance, receive and send SWM, and open your history in the side panel. The keys never live in the browser. The wallet in the toolbar talks to a small wallet host that is installed with the browser on your computer and runs as a separate program. A compromised page or extension in the browser does not have the keys to find, because they are not there.

The wallet host is a light wallet, like SWARM Wallet: it talks to the project's light-wallet server, which learns which encrypted notes it fetched and not the amounts or the counterparties. Your network provider sees that connection. Shielding protects what is on the chain, not the fact that you use SWARM.

The browser was built on the project's own build machine, and the source is at github.com/Swarmcoin, under the same BSD-3-Clause licence as upstream.

## What it does not do yet

This is the list from the download page, and we would rather you read it here than find out later.

- Pre-release. This is the first public build. Expect rough edges, and tell us what breaks.
- Unsigned. Windows SmartScreen warns before the first start: choose More info, then Run anyway. Check the SHA-256 first.
- Windows only. 64-bit Windows on Intel or AMD. There is no macOS or Linux build yet.
- No automatic updates yet. A new version is a new download from the page. Chromium publishes security fixes often, so check back.
- No ad or tracker blocking yet, and no phishing lists. Google Safe Browsing is removed with the other Google services, so nothing warns you about a dangerous site. Be careful with links, most of all near your wallet.
- Rewards. A rewards page is included, but it pays nothing yet.
- Paying websites. Websites cannot reach the wallet in this pre-release, so paying a site from the browser is not part of it.

Two more that apply to everything SWARM ships: no independent audit of the SWARM-specific changes has been published, and the upstream components carry their own security records and open issues. And the browser cannot hide from your network provider that you are using it.

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

A separate wallet app is also published: if you would rather keep money out of the browser entirely, SWARM Wallet for Windows, macOS and Linux is at swarm.green/ecosystem/wallet with its own checksums.

## What comes next

Only what the roadmap already says, and the roadmap gives no dates for unfinished work. The goal for the browser is one where paying a site is one click with the same confirmation screen as the wallet, where a site can ask for a payment but never take one, where trackers are blocked and fingerprinting is reduced, and where each site gets only the permissions you give it, with the wallet never one of them by default.

The pieces not in the pre-release are listed under Planned, which on our roadmap means not started: paying a site from the address bar, blocking ads and trackers, warning about phishing sites, and builds for macOS and Linux. The rewards page pays nothing, and nothing about rewards is promised. Signed builds are on the roadmap.

Until then, a browser that does not phone home, a wallet whose keys stay out of it, and a list of what is missing that we wrote before anyone else had to.
