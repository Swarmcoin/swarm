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

## Schedule

| Date | Article | Dev.to | Medium | Paragraph | Others |
| --- | --- | --- | --- | --- | --- |
| 8 Oct | `surveillance-money-and-the-case-for-shielded-payments.md` | publish | import, submit to The Capital | post | Publish0x |
| 10 Oct | `top-privacy-coins-2026.md` | publish | import, submit to Coinmonks | post | HackerNoon submission, InLeo |
| 15 Oct | `a-browser-that-does-not-phone-home.md` | publish | import, submit to Level Up Coding | post | share in r/degoogle on 21 Oct |
| 22 Oct | `a-messenger-where-the-money-is-in-the-conversation.md` | publish | import | post | Publish0x |

Each publication day gets one X post from the agent or the calendar linking to the Dev.to
URL (the calendar has a slot free at 16:00 UTC on 11, 18 and 25 October for exactly this).

## Before publishing anything

- Fill in `canonical_url` in the front matter with the Dev.to URL after the first publish.
- Reconcile the two open questions noted in `../articles/README.md` (messenger calls and
  groups; the version numbers on the messenger page) with the product team.
- Run `python tools/check_prose.py articles/*.md` to confirm the policy's banned phrases
  are absent.
