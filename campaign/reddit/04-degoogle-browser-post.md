<!-- venue: r/degoogle, flair: none or Discussion (verify on the day; never a crypto flair), account requirements: an account with comment history in r/degoogle or r/privacy; comment in the sub for a week first, when: week 3, notes for the human poster: technical framing only; the coin is mentioned in exactly one sentence and never in the comments unless asked directly; if the mods consider the wallet a disqualifier, accept it; link only to swarm.green and github.com/Swarmcoin; do not argue with ungoogled-chromium purists, they are right about what a fork should and should not add -->

# A degoogled Chromium 153 build with privacy defaults switched on: what we removed, what we turned on, and what is still missing

Disclosure: we maintain this fork. It is a Windows-only pre-release of ungoogled-chromium with our own defaults and a toolbar extension; the extension is a cryptocurrency wallet for the SWARM network, and that is the only sentence about it in this post.

## Base

ungoogled-chromium at Chromium 153. Everything ungoogled-chromium removes, we remove, because we build from their tree with our patches on top. Patches are in `swarm-browser` under github.com/Swarmcoin.

## Removed (inherited from ungoogled-chromium)

- Google API keys: no sign-in, no sync, no Google-backed services
- Safe Browsing lookups
- Usage and crash reports
- Remote feature switches (field trials and variations)

## Switched on by default (our changes)

- Referrer: other sites are not told which page you came from
- Client hints are not sent, and less about the system is reported to sites
- WebRTC does not reveal the local network address
- Link-tracking pings (`<a ping>`) are off
- Sites are not added as search engines automatically
- "Always use secure connections" is on
- Default search engine is DuckDuckGo with search suggestions off, so nothing is sent while you type; change it in Settings
- New-tab page is a local start page whose tiles ask no server anything until you switch the network tile on

## What is missing, honestly

- **No ad or tracker blocking.** There is no built-in list and no bundled blocker. Install your own extension if you need one; we have not tested which ones work with our build.
- **No phishing or malware lists.** Safe Browsing is gone and nothing replaces it. Nothing warns you about a dangerous site. We are looking at non-Google alternatives but nothing has shipped.
- **Windows only**, 64-bit Intel or AMD. No macOS, no Linux.
- **Unsigned.** SmartScreen warns on first start. We have no vendor certificate yet.
- **No automatic updates.** Chromium publishes security fixes often; with this build, every update is a manual download. If you cannot commit to checking the download page, use upstream ungoogled-chromium, which has a community of packagers keeping it current.
- **Built on our own machine.** One Chromium build at a time, many hours each. Not reproducible yet.

## Verifying a download

Download only from swarm.green/ecosystem/browser. The installer and the portable zip are both listed with their SHA-256. In PowerShell:

```
Get-FileHash .\<file>
```

Compare with the value on the page before you run anything.

## Questions we would like answered

1. Which privacy defaults do you think a fork should turn on that ungoogled-chromium leaves at upstream values, and which of ours go too far for ordinary sites?
2. Is a Chromium fork without Safe Browsing acceptable for non-expert users, or should we refuse to call it a privacy browser until a replacement list ships?
3. For Linux packagers: what would you need from us to make a build feasible?

We expect the view that a browser fork should add nothing and only remove. That is a fair position; the upstream project exists for exactly that, and we link to it rather than compete with it.
