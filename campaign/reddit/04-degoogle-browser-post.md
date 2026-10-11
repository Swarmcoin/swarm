<!-- venue: r/degoogle, flair: none or Discussion (verify on the day; never a crypto flair), account requirements: an account with comment history in r/degoogle; comments in r/degoogle for at least a week before posting (10 to 21 October 2026 is comments-only), when: Wed 28 Oct 2026 15:00 UTC, notes for the human poster: the body starts with "I work on SWARM."; technical framing only; the coin is in exactly one sentence (the disclosure) and never in the comments unless asked directly; if the mods consider the wallet a disqualifier, accept it; link only to swarm.green and github.com/Swarmcoin; do not argue with ungoogled-chromium purists, they are right about what a fork should and should not add; the Referer spelling source, for a reader who asks: RFC 1945 and the Wikipedia article "HTTP referer" -->

# What your browser tells a website before you have clicked anything, and the defaults we changed in a degoogled Chromium 153 build

I work on SWARM. We maintain the browser fork described below, nothing in it is for sale, and its toolbar extension is a wallet for SWARM's coin, SWM, whose worth we will not discuss; that is the only sentence about the coin in this post.

## The quiet part of a page load

Before you click anything on a page, a stock Chromium has usually told several parties a good deal:

- **Where you came from.** The `Referer` header names the page that sent you. The word is misspelled, and has been since it entered the HTTP specification: by the time RFC 1945 described HTTP/1.0 in May 1996 the spelling was fixed in place, and it stays because every server reads it that way. The newer `Referrer-Policy` header spells it correctly. Current Chromium trims cross-site referrers to the site's address, but it still says where you were.
- **What you run.** User-agent client hints (`Sec-CH-UA`, `Sec-CH-UA-Platform`, `Sec-CH-UA-Mobile`) go out with requests, and a site can ask for more: platform version, device model, full browser version.
- **What you are typing.** With search suggestions on, the address bar sends each keystroke to the search engine to fetch suggestions, before you press Enter.
- **Your network addresses.** WebRTC, the real-time connection API, lets a page set up peer connections, and depending on the browser's policy that can expose your addresses, including the one on your local network.
- **What you click.** `<a ping>` asks the browser to send a separate request to a tracking address when you follow a link. Chromium honours it by default.

None of this is hidden; it is all in the specifications and the settings pages. The lesson is simpler: the defaults are the privacy policy. Most people never open the settings, so what the browser does out of the box is what it does.

## Why I am telling you this

We changed those defaults in our own ungoogled-chromium build, and this sub is the right place to be told where we got it wrong. What is missing comes first.

## What is missing

- **No ad or tracker blocking.** No built-in list, no bundled blocker. Install your own extension; we have not tested which ones work with our build.
- **No phishing or malware lists.** Safe Browsing is gone and nothing replaces it. Nothing warns you about a dangerous site.
- **Windows only**, 64-bit Intel or AMD. No macOS, no Linux.
- **Unsigned.** SmartScreen warns on first start.
- **No automatic updates.** Chromium ships security fixes often; here every update is a manual download. If you cannot commit to checking back, use upstream ungoogled-chromium, which has packagers keeping it current.
- **Built on our own machine**, one build at a time, many hours each. Not reproducible yet.
- No independent audit of the SWARM-specific changes has been published.

## Base and removed

ungoogled-chromium at Chromium 153. Everything it removes, we remove, because we build from its tree with our patches on top: Google API keys (no sign-in, no sync), Safe Browsing lookups, usage and crash reports, and remote feature switches (field trials and variations). Patches are in `swarm-browser` under github.com/Swarmcoin.

## Switched on by default (our changes)

- Other sites are not told which page you came from
- Client hints are not sent, and less about the system is reported
- WebRTC does not reveal the local network address
- `<a ping>` is off
- Sites are not added as search engines automatically
- HTTPS-only mode is on
- Default search is DuckDuckGo with suggestions off, so nothing leaves while you type; change it in Settings
- The new-tab page is local; its tiles ask no server anything until you switch the network tile on

## Verifying a download

Download only from swarm.green/ecosystem/browser. The installer and the portable zip both carry their SHA-256. In PowerShell:

```
Get-FileHash .\<file>
```

Compare with the value on the page before you run anything.

## Questions for this sub

1. Which defaults should a fork turn on that ungoogled-chromium leaves at upstream values, and which of ours break ordinary sites?
2. Is a Chromium fork without Safe Browsing acceptable for non-expert users, or should we not call it a privacy browser until a replacement list ships?
3. For Linux packagers: what would you need from us to make a build feasible?

We expect the view that a browser fork should only remove and never add. That is a reasonable position; the upstream project exists for exactly that, and we point people to it rather than compete with it.
