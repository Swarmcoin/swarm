<!-- venue: internal plan for the Reddit posts in this folder, flair: n/a, account requirements: see the table, when: weeks 1 to 4 starting the week of 12 October 2026, notes for the human poster: this file is the plan, not a post; read ../VOICE.md and ../research/community-and-forums-2026-10.md before touching Reddit -->

# Reddit plan: four weeks, one human, no bots

Reddit's public Data API closes in stages from 31 October 2026 (research file, section "Reddit"). That changes nothing for us: automated promotional posting was already spam under Reddit's rules. Every post in this folder is posted by a person, from a real account with a real history, and that person answers the comments.

The posts are numbered in the order they go out. Each file starts with an HTML comment that names the venue, the flair, the account requirement, the week and the notes for the poster. The text below the comment is the post.

## The four weeks

| Week | Subreddit | Post file | Flair | Account requirement | What success looks like |
| --- | --- | --- | --- | --- | --- |
| 1 | r/privacycoins | `01-privacycoins-launch-writeup.md` | Discussion (use "Announcement" only if the sidebar offers it) | Account older than 3 months with comment history in r/privacycoins and r/zec; one week of real comments in the sub first | The post stays up; the hard questions in the FAQ are asked and answered in the thread; at least one reader checks the explorer or the genesis hash and says so |
| 2 | r/cryptodevs | `02-cryptodevs-technical-post.md` | Discussion or none (check the live list) | A developer's own account with GitHub history linked in the profile; comments in the sub before posting | Code review: a comment or a GitHub issue that points at a specific line in privacy-zebra, privacy-zaino or privacy-zingolib |
| 2 | r/opensource | `03-opensource-browser-and-messenger.md` | **Promotional** (required for anything you built) | Any real account older than 30 days; read the sidebar rules on the day of posting | The post stays up under the Promotional flair; licence and build questions get answered; nobody has to ask "is this a coin ad" because the text answered it |
| 3 | r/degoogle | `04-degoogle-browser-post.md` | None or "Discussion" (verify); never a crypto flair | Account with history in r/degoogle or r/privacy; comments first | Not removed as crypto promotion; feedback on the privacy defaults, the removed services and what should be added |
| 3 | r/selfhosted | `05-selfhosted-run-a-node.md` | "Guide" or "Self Help" (verify the live list) | Account with self-hosting history; comments first | One reader other than us builds `zebrad` and reports the result, good or bad |
| 4 | r/zec | reuse `02` with a Zcash-specific lead, rewritten | As the mods say | **Ask the moderators by modmail first** and post only with their yes | The mods allow the post; the thread stays technical; we thank and credit upstream in every reply |
| 4 | r/altcoin, r/altcoins, r/cryptocurrencies | reuse `01`, rewritten (not the same text) | As each sidebar says | Account with history; read each rule page the day of posting | Stays up; the FAQ answers hold without new facts being invented |
| ongoing | r/CryptoCurrency, r/Monero, r/privacy, r/zec | `06-comment-templates.md` (comments only, never posts) | n/a | Aged account with karma above the sub's gate | Comments answer the question first and are not removed; no thread becomes an argument |
| never | r/PrivacyGuides, r/signal, r/Bitcoin, r/ethdev, r/0xPolygon, r/privacytoolsIO | none | n/a | n/a | n/a: not posted, not commented as promotion |
| last priority | r/CryptoMoonShots | none written; only if the team decides it is worth a 1,000-character post | required | 3 months, 100 karma, 1 post per 24 h | Low-value audience; probably skip |

r/CryptoMarkets only later and only with data (research file). r/CryptoCurrency gets a link only when a third party has written about SWARM; we never post our own site there.

## Rules for the human poster

1. **Engage first.** Comment in the subreddit for at least one week before posting there. Answer other people's questions. If your comment history is only about SWARM, you are a spammer in the eyes of every moderator, and they are right.
2. **Never post the same text twice.** Each subreddit gets its own text. Reusing a file means rewriting it for that audience, not copy and paste. Reddit's spam filter and the moderators both look for duplicate text across subreddits.
3. **Answer every comment within 24 hours.** Including the hostile ones. One factual answer with the link, then stop. If someone found a bug, thank them and say what we will do, not when.
4. **Never argue.** If a thread turns into an argument, our last comment is a fact and a link. We do not get the last word.
5. **Never mention price.** Not the SWM token on Base, not exchanges, not "when listing", not comparisons with other coins' value. If asked: "Whatever people agree it is worth. We don't promise a price, and SWM can lose all its value."
6. **If a moderator removes it, do not repost.** Not in the same sub, not with a changed title, not from another account. Write to the mods once, politely, asking what rule it broke, and move on.
7. **Say what is missing first.** Every post leads with the unfinished parts: no audit, unsigned builds, pre-release browser, closed start. Readers who find this out from us trust the rest.
8. **Links.** Only swarm.green, mainnet.explore.swarm.green and github.com/Swarmcoin. Every download link comes with the SHA-256 step. No shorteners.
9. **Disclosure.** Say you work on the project in the first line or the flair. Reddit's self-promotion guideline and most subreddits' rules require it; our voice does too.
10. **Disclaimers.** Any post or comment that mentions mining, rewards or the waiting list carries one of: "No coins are promised." / "SWM has no guaranteed value and can lose value, including all of it." / "Mined, not sold."
11. **Security reports in comments** get one reply: the path to SECURITY.md in github.com/Swarmcoin/swarm, and a request to continue in private.
12. **Keep a log.** Date, subreddit, link to the post, flair used, outcome. The next poster needs it so that rule 2 and rule 6 hold.
