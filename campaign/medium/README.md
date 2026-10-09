# Publishing the articles

The four pieces in `../articles/` are written once and published in this order, each with a
canonical link back to the first home so search engines do not see duplicates.

| Order | Where | How | Why |
| --- | --- | --- | --- |
| 1 | **Dev.to** (dev.to/swarmcoin) | `python tools/publish_devto.py articles/<file>.md` with `DEVTO_API_KEY` set; publishes as a draft first | Free API, developer audience, instant; becomes the canonical URL |
| 2 | **Medium** (medium.com/@swarm_coin) | By hand: Medium's API has been closed to new integrations since 1 January 2025. Paste the Markdown into the editor (or use "Import a story" with the Dev.to URL, which keeps the canonical link). Set the publication: submit the comparison piece to Coinmonks and Level Up Coding (submit@gitconnected.com with the draft link), the browser piece to Level Up Coding, the coin and messenger pieces to The Capital or DataDrivenInvestor | Reach; the publications bring the readers |
| 3 | **Paragraph** (paragraph.com/@swarm) | Paste or use their CLI; set the canonical URL | Crypto-native readers, on-chain publishing |
| 4 | **Publish0x** and **InLeo** | Paste | Crypto blogging audiences that still convert to Reddit and X traffic |
| 5 | **HackerNoon** (comparison piece only) | contribute.hackernoon.com; disclose the vested interest; human review takes 3 to 5 working days | Search reach; they reject low-quality blockchain content, which this is not |

Medium's cryptocurrency policy: the account's verified email must be on the project's domain
(use swarmofficial@atomicmail.io and put swarm.green in the bio), no bounty or ambassador
content, or the account is treated as spam. Each article already carries a one-line disclosure
that it is published by the project.

## Publishing plan

One article a week, on Tuesdays, published on Dev.to at 09:00 UTC.

| Week | Date | Article | Day plan |
| --- | --- | --- | --- |
| 1 | Tuesday 13 October 2026 | `top-privacy-coins-2026.md` | Dev.to draft by script in the morning, read back by the session, owner "go" in chat, then `--publish`; the same day the person named in owner item 318 pastes it into Medium ("Import a story" from the Dev.to URL keeps the canonical link) and submits it to Coinmonks; Paragraph optional |
| 2 | Tuesday 20 October 2026 | `surveillance-money-and-the-case-for-shielded-payments.md` | Same; Medium submission to The Capital |
| 3 | Tuesday 27 October 2026 | `a-browser-that-does-not-phone-home.md` | Same; Medium submission to Level Up Coding; r/degoogle share by the Reddit session where the subreddit's rules allow |
| 4 | Tuesday 3 November 2026 | `a-messenger-where-the-money-is-in-the-conversation.md` | Same; only after owner item 316 is settled and the markers in the article are deleted |

Week 1 is the first Tuesday after the owner's Dev.to key is in `D:/privacy/scripts/campaign/.env`
as `DEVTO_API_KEY` (gitignored; never committed, never printed). If it arrives later, all four
dates slide by whole weeks in the same order.

Canonical URL: the Dev.to post, or swarm.green if the website session publishes a copy there
first.

The script is run from `campaign/` as `DEVTO_API_KEY=... python tools/publish_devto.py
articles/<file>.md`. It creates a draft first; never run it with `--publish` without the
owner's "go" for that article in chat.

After publishing, the link goes to the X session (first reply under a post, never a link post),
the Reddit session (where self-posts are allowed) and the listings session (directory entries).
Each article link goes into the first reply under the thematically closest X post on its
Tuesday; the X session picks the post. No new X posts are added for links.
