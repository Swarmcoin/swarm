<!-- venue: internal plan for the Reddit posts in this folder, flair: n/a, account requirements: see the table, when: comments from Sat 10 Oct 2026, first post Thu 22 Oct 2026 15:00 UTC, last dated post Thu 29 Oct 2026 15:00 UTC, notes for the human poster: this file is the plan, not a post; read ../VOICE.md and ../research/community-and-forums-2026-10.md before touching Reddit -->

# Reddit plan: comments first, five posts, one human, no bots

Reddit's public Data API closes in stages from 31 October 2026 (research file, section "Reddit"). That changes nothing for us: automated promotional posting was already spam under Reddit's rules. Every post in this folder is posted by a person, from a real account with a real history, and that person answers the comments.

Every post leads with a story, an explainer or a question that is worth reading for someone who will never install our software; SWARM comes in where it is the honest example (owner rule: promotion at most one piece in five). Each file starts with an HTML comment that names the venue, the flair, the account requirement, the date and the notes for the poster. The text below the comment is the post.

The first posts on Nostr, Bluesky, Farcaster and Mastodon go out the same day as the first Reddit post (Thu 22 Oct 2026, or Thu 15 Oct 2026 if that post moves).

## The plan

| When (UTC) | Subreddit | Post file | Flair | Account requirement | What success looks like |
| --- | --- | --- | --- | --- | --- |
| 10 to 21 Oct 2026 | the comment subreddits below and every subreddit we will post in | comments only, no posts; `06-comment-templates.md` where a template fits | n/a | The posting account, aged, with real history | At least a week of useful comments in each subreddit before its post; none about SWARM unless asked |
| Thu 22 Oct 2026 15:00 (Thu 15 Oct only if the owner names an aged account with real history by 12 Oct) | r/privacycoins | `01-privacycoins-launch-writeup.md` | Discussion (use "Announcement" only if the sidebar offers it) | Account older than 3 months with comment history in r/privacycoins; a week of real comments in the sub first | The post stays up; the hard questions in the FAQ are asked and answered in the thread; at least one reader checks the explorer or the genesis hash and says so |
| Mon 26 Oct 2026 15:00 | r/opensource | `03-opensource-browser-and-messenger.md` | **Promotional** (required for anything you built) | Any real account older than 30 days; a week of comments first; read the sidebar rules on the day | The post stays up under the Promotional flair; licence and build questions get answered; nobody has to ask "is this a coin ad" because the text answered it |
| Tue 27 Oct 2026 15:00 | r/cryptodevs | `02-cryptodevs-technical-post.md` | Discussion or none (check the live list) | A developer's own account with GitHub history in the profile; a week of comments first | Code review: a comment or a GitHub issue that names a specific line in the node repository, privacy-zaino or privacy-zingolib |
| Wed 28 Oct 2026 15:00 | r/degoogle | `04-degoogle-browser-post.md` | None or "Discussion" (verify); never a crypto flair | Account with history in r/degoogle; a week of comments first | Not removed as crypto promotion; feedback on the defaults, the removed services and what should be added |
| Thu 29 Oct 2026 15:00 (not Friday: r/selfhosted moves vibe-coded project posts into a Friday thread) | r/selfhosted | `05-selfhosted-run-a-node.md` | "Guide" or "Self Help" (verify the live list) | Account with self-hosting history; a week of comments first | One reader other than us builds `zebrad` and reports the result, good or bad |
| not dated; the planner sets it | the upstream coin's own subreddit (r/ plus its three-letter ticker; the lint forbids writing it) | reuse `02` with its own lead, rewritten | As the mods say | **Ask the moderators by modmail first** and post only with their yes | The mods allow the post; the thread stays technical; we thank and credit upstream in every reply |
| not dated; the planner sets it | r/altcoin, r/altcoins, r/cryptocurrencies | reuse `01`, rewritten (not the same text) | As each sidebar says | Account with history; read each rule page on the day | Stays up; the FAQ answers hold without new facts being invented |
| from Sat 10 Oct 2026, ongoing | r/CryptoCurrency, r/CryptoTechnology, r/privacycoins, the upstream coin's subreddit (technical and design comparisons only), r/cryptomining | `06-comment-templates.md` (comments only, never posts) | n/a | Aged account with karma above the sub's gate | Comments answer the question first and are not removed; no thread becomes an argument |
| never | r/privacy, r/PrivacyGuides, the announcement threads of the largest ring-signature privacy coin's subreddit, r/signal, r/Bitcoin, r/ethdev, r/0xPolygon, r/privacytoolsIO | none | n/a | n/a | n/a: never posted and never commented by us |
| last priority | r/CryptoMoonShots | none written; only if the team decides it is worth a 1,000-character post | required | 3 months, 100 karma, 1 post per 24 h | Low-value audience; probably skip |

r/CryptoMarkets only later and only with data (research file). r/CryptoCurrency gets a link only when a third party has written about SWARM; we never post our own site there.

## Rules for the human poster

1. **Engage first.** Comment in the subreddit for at least one week before posting there; 10 to 21 October 2026 is comments-only. Answer other people's questions. If your comment history is only about SWARM, you are a spammer in the eyes of every moderator, and they are right.
2. **Never post the same text twice.** Each subreddit gets its own text. Reusing a file means rewriting it for that audience, not copy and paste. Reddit's spam filter and the moderators both look for duplicate text across subreddits.
3. **Answer every comment within 24 hours.** Including the hostile ones. One factual answer with the link, then stop. If someone found a bug, thank them and say what we will do, not when.
4. **Never argue.** If a thread turns into an argument, our last comment is a fact and a link. We do not get the last word.
5. **Never discuss what SWM is worth.** Not any token on another chain, not where it trades or might trade, not comparisons with other coins' value. If asked: "Whatever people agree it is worth. Nobody promises you a price, and SWM can lose all its value."
6. **If a moderator removes it, do not repost.** Not in the same sub, not with a changed title, not from another account. Write to the mods once, politely, asking what rule it broke, and move on.
7. **Say what is missing first.** Every post states the unfinished parts before the SWARM facts: no independent audit, unsigned builds, pre-release browser, closed start. Readers who find this out from us trust the rest.
8. **Links.** Only swarm.green, mainnet.explore.swarm.green and github.com/Swarmcoin. Every download mention comes with the SHA-256 step. No shorteners. Story sources are named in the text; their links sit in each file's notes for a reader who asks.
9. **Disclosure.** Every post and every comment that names SWARM starts with "I work on SWARM." followed by one sentence: we built it, nothing is for sale, we will not discuss what SWM is worth. Reddit's self-promotion guideline and most subreddits' rules require disclosure; our voice does too.
10. **Disclaimers.** Any post or comment that mentions mining, rewards or the waiting list carries "No coins are promised." and "Please keep ASICs and rented hash power off the network." "Mined, not sold." may be added.
11. **Security reports in comments** get one reply: the path to SECURITY.md in github.com/Swarmcoin/swarm, and a request to continue in private.
12. **Keep a log.** Date, subreddit, link to the post, flair used, outcome. The next poster needs it so that rule 2 and rule 6 hold.
