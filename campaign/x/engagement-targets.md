# Engagement targets on X

Who @swarm_coin talks to, why, and how. The agent reads these accounts (tiers below mirror
`agent/policy.yaml`) and *proposes* replies into the review queue; a human approves them.
Replies to people who mention us are the only replies the agent sends on its own, because
X's automation rules allow automated replies only to people who opted in by mentioning you.

## The rule of thumb

We reply when we can add something true and useful that the thread does not already have:
a fact about shielded transactions, a correction, a pointer to a specification, a thank-you
for work we build on. We never reply to say "SWARM does this too". A good week is ten
replies people were glad to read; a bad week is fifty they scrolled past.

## Tier 1: the ecosystem we build on (read daily; reply generously, never promote)

| Handle | Why | How we engage |
| --- | --- | --- |
| @zcash | The protocol SWARM runs | Amplify protocol news; answer questions about shielded tech when asked in their threads; never compare ZEC and SWM |
| @ElectricCoinCo | Maintains the Zcash protocol; cool towards forks | Credit their work; never pitch; answer only direct questions. Their page shows no posts to a logged-out browser (checked 9 Oct 2026); read logged in or via the API |
| @ZcashFoundation | Maintains Zebra, the node we fork | Thank, credit, report upstream-relevant findings |
| @ZingoLabs | zingolib and Zaino, our wallet SDK and indexer | Technical questions and credit; integration conversations in public |
| @zooko | Endorsed the Ycash friendly fork in 2019 | Plain, respectful; answer if addressed |
| @ZcashCommGrants, @ZecHub, @zodl_app (formerly @zashi_app, moved February 2026), @ShieldedLabs | Zcash community infrastructure | Read; reply only with facts about the stack |
| @signalapp | Protocol and code the messenger forks | Credit only; do not expect a reply |
| @ungoogled (ungoogled-chromium) | Base of the browser | Credit; report findings upstream |

## Tier 2: privacy advocates and journalists (read daily; reply when we know the answer)

| Handle | Why | How we engage |
| --- | --- | --- |
| @naomibrockwell | Largest privacy-tech channel; has covered Zcash and Monero | Answer questions in her threads with facts; pitch the apps for review by email, not in replies |
| @TechloreInc (not @techlore, which is an unrelated account dormant since 2014) | Privacy education; cautious on crypto | Facts only; the browser and messenger are the relevant topics |
| @privacy_guides | Recommends Monero only; sceptical of new coins | Never pitch; answer factual questions; a user may suggest the apps on their forum |
| @sethforprivacy, @optoutpod | Privacy-crypto podcast; Monero-aligned, fair | Engage on substance: default-vs-optional privacy, what servers learn; accept criticism |
| @MoneroTalk, @DouglasTuman | Hosts non-Monero guests | Same; expect adversarial questions about a Zcash fork and answer them plainly |
| @The_HatedOne_ | Privacy-maximalist channel | Facts when asked |
| Mathew Di Salvo (DL News) | Writes the privacy-coin beat | Reply with facts and a source when he asks the ecosystem something; pitch by email |
| @a_greenberg, @CamiRusso, @Blockworks (not @Blockworks_, which does not exist), @DecryptMedia | Journalists and desks that cover privacy and altcoins | Reply only with a verifiable fact or a correction |
| @torproject (and EFF, which left X on 9 April 2026 and posts on Bluesky and Mastodon instead) | Movement, not partners | Credit their work; never tag them for attention |

## Tier 3: peer privacy projects (read twice a week; be generous)

| Handle | Why | How we engage |
| --- | --- | --- |
| @monero | The flagship; community hostile to Zcash-stack coins | Never promote in their threads; congratulate on milestones (FCMP++); compare designs only when asked |
| @firoorg, @zano_project, @pirate_chain, @beamprivacy, @grincoin, @railgun_project, @secretnetwork | Peers in the same argument | Congratulate releases; share technical reading; no comparisons that favour us |

## Tier 4: mining (from 25 October; the agent does not read these, a human does)

| Who | Why | How |
| --- | --- | --- |
| @MiningPoolStats | The index miners read; add SWARM through their new-coin contact | Human task, see `../forums/README.md` |
| @2MinersPool, @f2pool_official, @LuxorTechnology, @WoolyPooly, @herominers, @K1Pool | Equihash pools | Answer their technical questions in public; point to privacy-zebra and swarm-node |
| r/gpumining, r/CryptoMining | Miner communities | Expect "ASIC or GPU?" at once: Equihash 200,9, ASICs exist, nothing keeps anyone out |

## What we do not do

- No following campaigns. Following is a human decision, a few accounts a week at most.
- No likes in bulk. The agent likes only friendly posts that mention us, under a daily cap.
- No replies to price talk, listing questions, giveaways, scams or politics. The policy
  filters those before the agent sees them.
- No tagging people who did not ask. No "@naomibrockwell check this out".
- No arguing. One factual answer, then stop.

## Mentions and search queries the agent reads each cycle

The queries live in `agent/policy.yaml` under `search_queries`: mentions of swarm_coin and
swarm.green, the product names, and general conversations about shielded payments and
privacy coins. Only the first two can lead to a direct reply (if the post mentions us); the
rest produce proposals.

## Handle checks

Handles were last verified against the live public pages on 9 October 2026 (logged out, built-in browser). Verify a handle before the first reply to it; accounts move and die. Known: @zashi_app became @zodl_app; @techlore is not Techlore; @Blockworks_ never existed; @EFF stopped posting on X in April 2026. `x.com/search` needs a login, so the topic queries in `agent/policy.yaml` run only through the API.
