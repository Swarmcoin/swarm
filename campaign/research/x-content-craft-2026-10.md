# What makes an X account worth following in 2026 — research for @swarm_coin

Status: RESEARCH (not a plan, nothing posted). Date: 2026-10-06. Author: campaign research subagent.
Scope: how X ranks posts today, which formats earn reads and follows, who does education/story content well, mistakes to avoid, and a drafting checklist plus weekly mix for two posts a day with promotion at most every fifth or sixth post.

Evidence labels used below: **[code]** = read directly from X's open-source repository on 2026-10-06; **[measured]** = a dataset or experiment with a stated sample; **[official]** = a statement by X staff or an X help page; **[anecdotal]** = a creator or vendor claim without a published method.

---

## 1. How X ranks posts in 2026

**The system.** X open-sourced its For You stack at [github.com/xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) on 20 Jan 2026, published the ranking weights and visibility filters on 13 Aug 2026 and now commits near-daily ([TechCrunch, 13 Aug 2026](https://techcrunch.com/2026/08/13/x-open-sources-its-ranking-algorithm-letting-users-see-if-theyve-been-shadowbanned/); [dated release log](https://keywordseverywhere.com/news/social-algorithm-updates/x-algorithm-open-source/)). The README describes the pipeline: candidate sources (in-network "Thunder", out-of-network "Phoenix" retrieval, SimClusters), hydration, filters, a Grok-architecture transformer ("Phoenix") that predicts the probability of each action per viewer, a weighted sum of those probabilities, then author-diversity decay, an out-of-network discount and a small new-author boost ([README](https://github.com/xai-org/x-algorithm)) **[code]**. Since 27–30 Nov 2025 the Following feed is also Grok-ranked by default; chronological remains an option ([Musk, 27 Nov 2025](https://x.com/elonmusk/status/1993921748597920232)) **[official]**.

**Current default weights** (`home-mixer/params/param.rs`, main branch, 2026-10-06) **[code]**:

| Predicted action | Weight | Note |
|---|---|---|
| Like (favorite) | 0.5 | baseline |
| Repost | 1.0 | |
| Click (open post) | 0.3 | |
| Open link | 0.2 | positive, not a penalty |
| Photo expand / video open | 0.05 / 0.07 | |
| Dwell | 0.05 (+0.004 per unit of continuous dwell; click-dwell 0.4) | "not dwelled" is -0.02 |
| Share (generic) | 2.0 | |
| Follow author | 4.0 | |
| Reply | 5.0 | **+15 if the viewer and author follow each other** (total 20) |
| Quote post | 5.0 | same as a reply |
| Share via DM | 5.0 | |
| **Share via copy link** | **20.0** | the single highest positive weight |
| Not interested | -47.52 | |
| Block author | -31.2 | |
| Mute author | -58.8 | |
| Report | -234.0 | |

Two cautions written into the code itself: weights multiply *predicted probabilities*, not counts ("one report cancels 468 likes" is explicitly called wrong), and engagement only counts when the post was served in the Home timeline, so "coordinating via groupchat has no ranking impact" ([param.rs comments](https://github.com/xai-org/x-algorithm/blob/main/home-mixer/params/param.rs)) **[code]**. Engagement pods are therefore pointless by design.

**What changed from the 2023 numbers people still quote.** The 2023 heavy ranker weighted a reply 13.5, a reply the author then engaged with 75, a like 0.5 and a report -369 ([twitter/the-algorithm-ml recap README, 5 Apr 2023](https://github.com/twitter/the-algorithm-ml/blob/main/projects/home/recap/README.md)) **[code, historical]**. The "replies are 27x likes" line in most 2026 marketing posts comes from there; today's config is 10x for strangers and 40x for mutuals. The mutual-follow reply boost was A/B tested from 10 Jul 2026, launched at 20 on 13 Jul and lowered to 15 on 24 Jul ([docs/BIDIRECTIONAL_BOOST_CHANGE.md](https://github.com/xai-org/x-algorithm/blob/main/docs/BIDIRECTIONAL_BOOST_CHANGE.md)) **[code, official]**. Practical reading: posts that make *people who follow you back* want to reply are the most valuable thing a small account can produce, so following back real community members matters.

**Dwell time** is in the weights (dwell, continuous dwell, "not dwelled" negative) **[code]**; a secondary log dates its entry to 25 Aug 2026 and the switch to a long-dwell aggregation to 2 Sep 2026 ([release log](https://keywordseverywhere.com/news/social-algorithm-updates/x-algorithm-open-source/)) **[secondary]**. A post people scroll past in under a second now carries a small explicit cost.

**Links.** There is no URL penalty in the code; "open link" even has a small positive weight **[code]**. Musk said on 29 Jul 2026 that X has not throttled link posts "for over a year", and product head Nikita Bier said the day before that links no longer need to go in replies ([PPC Land](https://ppc.land/x-drops-year-old-link-penalty-musk-tells-zuckerberg-on-platform/)) **[official]**. But measured outcomes still disfavour links: across 18.8M X posts to Dec 2025, link posts had the lowest median engagement (2.25% vs 3.56% text, 3.40% image, 2.96% video) ([Buffer, State of Social Media Engagement 2026](https://buffer.com/resources/state-of-social-media-engagement-2026/)) **[measured]**. The often-cited "94% fewer views" is one creator's A/B test from Oct 2024 (65,400 vs 3,670 views) ([PPC Land, 21 Jan 2026](https://ppc.land/how-xs-algorithm-silently-kills-your-links-without-explicitly-penalizing-them/)) **[anecdotal]**. PPC Land's explanation is plausible and unproven: the model learns that link posts end sessions. Working rule: a link is fine when the link *is* the value (a guide, a release); never make a post whose only content is a link.

**What For You rewards, in one sentence:** posts that a specific viewer is predicted to reply to, quote, send to someone or copy the link of, and that nobody mutes, blocks or marks "not interested". A pre-registered audit of the 2023 engagement ranker found it amplified angry, partisan, out-group-hostile posts that users themselves said they did not want ([Milli et al., PNAS Nexus, Mar 2025](https://academic.oup.com/pnasnexus/article/4/3/pgaf062/8052060)) **[measured]**. Outrage still works mechanically; for a brand it is the fastest route to mutes (-58.8) and a reputation we do not want.

**Premium.** The 2023 code gave verified authors 4x in-network and 2x out-of-network multipliers ([Hootsuite summary of the 2023 code](https://blog.hootsuite.com/twitter-algorithm/)) **[code, historical]**. Buffer measured Premium and non-Premium engagement rates diverging after Jan 2025, with non-Premium falling steadily ([Buffer 2026](https://buffer.com/resources/state-of-social-media-engagement-2026/)) **[measured]**. A brand account should be on Premium; this also unlocks Articles ([help.x.com](https://help.x.com/en/using-x/articles)) **[official]**.

**Engagement bait and spam.** On 16 Jul 2026 X said accounts that solicit engagement ("I'll follow everyone who replies") three or more times are removed from creator revenue sharing and referred to policy; the same applies to reposting others' content with minimal edits ([Social Media Today](https://www.socialmediatoday.com/news/x-updates-its-engagement-bait-detection/825495/)) **[official]**. The repo contains LLM reply-spam classifiers (`grox/flows/reply_spam`, Grok and Gemma models); the prompts are withheld "to reduce gameability" **[code]**. Hashtags: "Please stop using hashtags. The system doesn't need them anymore and they look ugly" (Musk, 17 Dec 2024, [FOX 5](https://www.fox5dc.com/news/hashtags-x-elon-musk-says-please-stop-using-them)) **[official]**; vendor numbers such as "-17% at three tags" have no published method ([example](https://reachmore.co/blogs/do-hashtags-work-on-x-2026)) **[anecdotal]**.

**Crypto specifically.** In Dec 2025 many crypto accounts reported reach collapsing for posts with tickers and hype phrases while X rolled out "Smart Cashtags" against ticker spam ([BeInCrypto](https://beincrypto.com/crypto-x-algorithm-suppression-controversy/); [crypto.news](https://crypto.news/x-smart-cashtags-target-crypto-spam-and-asset-confusion/)) **[anecdotal, widely reported]**. Write like a privacy and freedom account that happens to have a coin, not like a coin account.

---

## 2. Formats that earn reads and follows

- **Text first, image second.** On X, plain text posts had the highest median engagement (3.56%), images 3.40%, video 2.96%, links 2.25% ([Buffer 2026](https://buffer.com/resources/state-of-social-media-engagement-2026/)) **[measured]**. X is the one platform where text beats video.
- **Threads vs long-form posts.** A six-post experiment found long-form posts edged threads on total impressions (11,846 vs 10,783) but variance between posts (169 to 10,889 impressions) dwarfed the format effect; the author's conclusion was that content matters more than format ([Hootsuite experiment](https://blog.hootsuite.com/experiment-x-threads-vs-longform-posts/)) **[measured, small sample]**. Use threads for stories with a reveal per step; use one long post when the piece is a single argument; use an Article for anything with headings or images in sequence.
- **Quote posts weigh the same as replies (5.0)** **[code]**; a vendor dataset found quote-tweet replies out-engage plain replies by about 18% and reach both audiences ([Metricool X statistics](https://metricool.com/x-Twitter-Statistics/)) **[measured, vendor]**. Quote a historical document, a news item or a community member's post and add the "why it matters" line.
- **"Share via copy link" is weighted 20** **[code]**. Content people want to paste into a group chat (a clear explainer, a story, a reference table) is what the ranker values most. This is the strongest structural argument for the owner's "education and value" direction.
- **Hooks.** Craft guides agree on 5–15 words, a specific claim or number, no warm-up ("So I've been thinking..."), and the reader should know within one line who the post is for ([ContentStudio](https://contentstudio.io/blog/social-media-hooks); [HeyOrca](https://www.heyorca.com/blog/the-best-social-media-hooks-for-2026)) **[anecdotal, consistent]**. Thread guides: hook, then the two strongest points at posts 2 and 3, 5–10 posts, each post a complete idea, a recap, one call to action ([Tweet Archivist](https://www.tweetarchivist.com/how-to-write-viral-twitter-threads); [Opentweet](https://opentweet.io/how-to/write-twitter-threads)) **[anecdotal]**.
- **Polls.** No reliable 2026 measurement found; the code has no poll-specific weight **[code]**. Treat polls as an occasional question format, not a reach tool.
- **Replying to your own replies** correlates with about +8% engagement on X, the weakest of all platforms but positive ([Buffer 2026](https://buffer.com/resources/state-of-social-media-engagement-2026/)) **[measured]**; answer within the first hours.
- **Promotion ratios.** The 80/20 rule (80% useful, 20% promotional) and the 4-1-1 rule (four value posts, one soft sell, one hard sell per six) are the standard industry heuristics ([Giraffe Social](https://www.giraffesocialmedia.co.uk/the-80-20-rule-for-social-media-content-what-to-post-and-when/); [SMMU](https://www.thesmmu.com/post/social-media-marketing-content-mix-finding-the-right-balance)) **[convention, not measured]**. The owner's "at most every fifth or sixth post" is exactly 4-1-1.
- **Cadence and timing.** Hootsuite recommends 2–3 posts a day for businesses ([Hootsuite](https://blog.hootsuite.com/how-often-to-post-on-social-media/)) **[official vendor guidance]**. Across 8.7M tweets the best slot was Tuesday 09:00 local, then Wednesday 09:00–10:00; weekday 09:00–11:00 is the reliable window; evenings 18:00–23:00 and Saturdays are worst ([Buffer, 13 Mar 2026](https://buffer.com/resources/best-time-to-post-on-twitter-x/)) **[measured, "local time" means the audience's]**. Derived for a global English audience (my inference, not a source): slot A 13:00–14:00 UTC (09:00 New York, 14:00 Berlin), slot B 07:00–08:00 UTC (Europe morning, Asia evening); check Under the Hood and analytics after four weeks and move the slots.

---

## 3. Accounts that do education and story well

Structures below are my description of their public formats, linked so a planner can check them; no copyrighted text is reproduced.

- **Pete Rizzo, "The Bitcoin Historian" ([@pete_rizzo_](https://x.com/pete_rizzo_))** — "Bitcoin Legends" threads built from archives and IRC logs; the people and drama (Mt. Gox, Silk Road, Ulbricht, Assange) rather than tech ([Untold Stories episode](https://podcasts.apple.com/us/podcast/silk-road-to-satoshi-digging-up-bitcoins-buried-past/id1462346183?i=1000703857839)). Structure: a date or anniversary, one person, what they risked, what it changed, a primary-source screenshot. Directly transferable to "people who fought for freedom".
- **Pessimists Archive ([@PessimistsArc](https://x.com/PessimistsArc))** — "fear of new things in the past": an old newspaper clipping, its year, one framing line ([pessimistsarchive.org](https://pessimistsarchive.org/)). Structure: artefact + date + one dry sentence; the reader supplies the irony. Ideal for "they said this about encryption / cash / the telephone".
- **Naomi Brockwell / NBTV ([@naomibrockwell](https://x.com/naomibrockwell))** — privacy explainers for non-experts; bio line "Dance like no one's watching. Encrypt like everyone is." ([Privacy 101](https://www.nbtv.media/episodes/privacy-101)). Structure: a plain problem statement, three concrete steps, no fear-mongering.
- **Seth for Privacy ([sethforprivacy.com](https://sethforprivacy.com/posts/contributing-to-monero/))** — advises simply "sharing what you're learning", demonstrating privacy on a block explorer side by side. Structure: show, don't assert; one comparison image.
- **EFF ([eff.org](https://www.eff.org/about))** — Deeplinks analysis, Surveillance Self-Defense guides, action campaigns. Structure: the legal or technical fact, who it affects, what to do. Their guides are the kind of content people copy-link into chats.
- **Matthew Green ([@matthew_d_green](https://x.com/matthew_d_green)) and Kim Zetter ([@KimZetter](https://x.com/KimZetter))** — cryptographer and security journalist ([eSecurity Planet list](https://www.esecurityplanet.com/trends/twitter-cybersecurity/)). Structure: a current event, then the mechanism explained in plain words, then the open question that invites expert replies.
- **monero.how ([@monerohow](https://x.com/monerohow))** — tutorials, statistics and charts: one chart, one sentence of what it shows.

Common denominators: one idea per post; a concrete artefact (document, chart, date, name); the "why it matters" sentence written out; the author replies to replies; promotion of their own product is rare and specific.

---

## 4. Mistakes to avoid

1. **Engagement bait** ("repost if you agree", "follow for more", asking for likes): revenue-share removal after three strikes and referral to policy ([Social Media Today](https://www.socialmediatoday.com/news/x-updates-its-engagement-bait-detection/825495/)) **[official]**.
2. **Hashtags**: no classification value, "look ugly" per Musk **[official]**; keep to zero.
3. **Link-only posts**: lowest-engagement format ([Buffer](https://buffer.com/resources/state-of-social-media-engagement-2026/)) **[measured]**; if the link is needed, the post must stand alone without it.
4. **Tickers and hype phrases** ("$SWM to the moon", "100x"): the Dec 2025 crypto reach collapse was reported precisely for these **[anecdotal, widespread]**.
5. **Reposting others' content with minimal edits**: 1.5M stolen posts actioned in one cycle ([Social Media Today](https://www.socialmediatoday.com/news/x-updates-its-engagement-bait-detection/825495/)) **[official]**. Quote and credit instead.
6. **Generic quotes and motivational filler**: nothing to reply to, nothing to copy-link, and they invite "not interested" (-47.52) **[code-based inference]**.
7. **AI-sounding prose**: a vendor study of 3,368 LinkedIn posts found likely-AI posts got 45% less engagement ([SocialNexis / Originality.AI](https://socialnexis.com/guides/ai-posts-engagement-decay-rate)) **[vendor, not peer reviewed]**; audiences say they trust AI-labelled content less. Avoid stacked em dashes, "In today's digital landscape", triplets of adjectives, closing "Let that sink in".
8. **Too many emojis, press-release voice** ("We are thrilled to announce"): no measurement found; judgment call, consistent with every craft guide above and with the owner's complaint. One emoji at most, never as bullets.
9. **Outrage and dunking**: measured to be amplified ([PNAS Nexus](https://academic.oup.com/pnasnexus/article/4/3/pgaf062/8052060)) but it buys mutes and blocks, which carry the largest negative weights **[code]**.
10. **Engagement pods and reply swaps**: no ranking effect by design ([param.rs](https://github.com/xai-org/x-algorithm/blob/main/home-mixer/params/param.rs)) **[code]**.
11. **Posting only promotion**: there is nothing a non-customer can reply to; the 4-1-1 ratio exists for this reason.
12. **Posting into the evening or on Saturday** ([Buffer timing](https://buffer.com/resources/best-time-to-post-on-twitter-x/)) **[measured]**.

---

## 5. Checklist and weekly mix

**Single post (check all before scheduling)**
1. First line names the subject and makes a specific claim; 5–15 words; no warm-up.
2. One idea. If there is a second idea, it is tomorrow's post.
3. A concrete artefact: a name, a date, a number, a document or chart image.
4. The "why this matters for your privacy" sentence is written, not implied.
5. Ends with something a reader can answer (a real question, a request for examples), never "like if you agree".
6. No hashtags, no ticker, no hype words, no "we are thrilled".
7. Zero or one emoji; no em-dash chains; reads aloud like a person.
8. If a link is included, the post is complete without it; otherwise the link goes in the first reply.
9. Network named beside any number or address ("on SWARM mainnet"), per owner rule.
10. Scheduled into slot A or B on a weekday; someone is available to answer replies in the first two hours.
11. Promotion counter: at most one promotional post in any six.

**Thread**
12. Post 1 is a hook with the payoff promised; posts 2 and 3 carry the strongest facts; 5–8 posts total.
13. Each post is a complete sentence-level idea with its own first-line hook; images on at least two posts.
14. Last post: a one-line recap, one question, and (only if relevant) one link.
15. Reply to the first ten replies; quote the best reply the next day as its own post.

**Weekly mix for two posts a day (14 posts)**

| Type | Count | Notes |
|---|---|---|
| Story posts ("why is": people who fought for freedom, history of privacy, cash, cryptography) | 4 | one of them is the week's thread |
| Education posts (how a shielded transaction, key, messenger or browser protection works; what metadata is) | 4 | one chart or comparison image each |
| Questions / conversation starters | 2 | real questions; quote a community reply the next day |
| Reaction to a current privacy or surveillance news item | 2 | quote post with the mechanism explained |
| Promotion (wallet, messenger, browser, release notes, downloads) | 2 | never on consecutive days; counts as the "1 + 1" of 4-1-1 |

This is 12 value posts to 2 promotional, which is 1 in 7 — inside the owner's "at most every fifth or sixth post". Review after four weeks with Under the Hood (10+ posts a month qualifies, [TechCrunch](https://techcrunch.com/2026/08/13/x-open-sources-its-ranking-algorithm-letting-users-see-if-theyve-been-shadowbanned/)) and X analytics; keep the formats whose posts got replies and copy-link shares, drop the rest.

---

### Source list
- X open-source repository and files read 2026-10-06: https://github.com/xai-org/x-algorithm ; https://github.com/xai-org/x-algorithm/blob/main/home-mixer/params/param.rs ; https://github.com/xai-org/x-algorithm/blob/main/docs/BIDIRECTIONAL_BOOST_CHANGE.md
- 2023 weights: https://github.com/twitter/the-algorithm-ml/blob/main/projects/home/recap/README.md
- TechCrunch 13 Aug 2026: https://techcrunch.com/2026/08/13/x-open-sources-its-ranking-algorithm-letting-users-see-if-theyve-been-shadowbanned/
- Musk, Following feed ranked by Grok: https://x.com/elonmusk/status/1993921748597920232
- Links: https://ppc.land/x-drops-year-old-link-penalty-musk-tells-zuckerberg-on-platform/ ; https://ppc.land/how-xs-algorithm-silently-kills-your-links-without-explicitly-penalizing-them/
- Buffer engagement by format and Premium: https://buffer.com/resources/state-of-social-media-engagement-2026/
- Buffer timing: https://buffer.com/resources/best-time-to-post-on-twitter-x/
- Hootsuite frequency: https://blog.hootsuite.com/how-often-to-post-on-social-media/ ; threads vs long-form: https://blog.hootsuite.com/experiment-x-threads-vs-longform-posts/ ; 2023 Premium multipliers: https://blog.hootsuite.com/twitter-algorithm/
- Engagement bait enforcement: https://www.socialmediatoday.com/news/x-updates-its-engagement-bait-detection/825495/
- Hashtags: https://www.fox5dc.com/news/hashtags-x-elon-musk-says-please-stop-using-them ; vendor claim example: https://reachmore.co/blogs/do-hashtags-work-on-x-2026
- Divisive-content audit: https://academic.oup.com/pnasnexus/article/4/3/pgaf062/8052060
- Crypto reach reports: https://beincrypto.com/crypto-x-algorithm-suppression-controversy/ ; https://crypto.news/x-smart-cashtags-target-crypto-spam-and-asset-confusion/
- Articles: https://help.x.com/en/using-x/articles
- Quote posts: https://metricool.com/x-Twitter-Statistics/
- Hooks and threads: https://contentstudio.io/blog/social-media-hooks ; https://www.heyorca.com/blog/the-best-social-media-hooks-for-2026 ; https://www.tweetarchivist.com/how-to-write-viral-twitter-threads ; https://opentweet.io/how-to/write-twitter-threads
- Promotion ratios: https://www.giraffesocialmedia.co.uk/the-80-20-rule-for-social-media-content-what-to-post-and-when/ ; https://www.thesmmu.com/post/social-media-marketing-content-mix-finding-the-right-balance
- AI prose: https://socialnexis.com/guides/ai-posts-engagement-decay-rate
- Example accounts: https://x.com/pete_rizzo_ ; https://podcasts.apple.com/us/podcast/silk-road-to-satoshi-digging-up-bitcoins-buried-past/id1462346183?i=1000703857839 ; https://x.com/PessimistsArc ; https://pessimistsarchive.org/ ; https://x.com/naomibrockwell ; https://www.nbtv.media/episodes/privacy-101 ; https://sethforprivacy.com/posts/contributing-to-monero/ ; https://www.eff.org/about ; https://x.com/matthew_d_green ; https://x.com/KimZetter ; https://www.esecurityplanet.com/trends/twitter-cybersecurity/ ; https://x.com/monerohow
