# X profile set for @swarm_coin

Status: **PROPOSED** (every field, image choice and post on this page). Written 2026-10-09 for
the session "X Calendar and Scheduling". The owner pastes these into the X account before the
first post. The owner saves the profile and publishes the thread; an agent never does.

Rules this page follows: `campaign/VOICE.md`. Character counts are Python `len()` of the exact
text. X counts every link as 23 characters, so the count X shows for post 10 is lower.

## A. Name field (X limit 50)

| Option | Text | Characters |
| --- | --- | --- |
| Proposed | `SWARM` | 5 |
| Alternative | `SWARM ⬢ private money` | 21 (one hexagon only) |

## B. Bio (X limit 160)

Kept from the earlier version: it carries two lines we repeat (mined, not sold; we never ask for
recovery words), and it has no call to buy and no figure.

```
Private, proof-of-work money you can run yourself. SWM is mined, not sold. Nobody promises you a price. We never DM first or ask for recovery words.
```

Characters: **148 of 160**.

## C. Location field (X limit 30)

```
Official links: swarm.green
```

Characters: **27 of 30**.

## D. Website field

```
https://swarm.green
```

## E. Images

| Slot | File | Note |
| --- | --- | --- |
| Header (1500 x 500) | `D:/privacy/docs/x/profile/swarm-x-header-mainnet-1500x500.png` | its text reads "MAINNET LIVE · NO PREMINE · MINED, NOT SOLD" |
| Avatar (400 x 400) | `D:/privacy/docs/x/profile/swarm-x-avatar-400.png` | network-neutral |
| Never use | `D:/privacy/docs/x/profile/swarm-x-header-1500x500.png` | carries the pill of the old pre-mainnet network; must never be uploaded |

Birthday, professional category and extra links: leave empty.

## F. Pinned thread (replaces the stale X-001 of 27 September 2026)

10 posts. Post 1 goes out as a normal post; posts 2 to 10 are replies, each to the one before.
No post numbers, so that every post about mining, rewards or the waiting list ends with the
disclaimer. No hashtags, no emoji. Links only in the last post.

Corrections against the stale version: mainnet live since 2 October 2026, 15:42 UTC (not
26 September); the closed-start dates; the build-base sentence; all four apps; one clause of the
old "what we never do" post removed (owner instruction); the contracts sentence removed.

Open for the planner: post 4 uses the site's own wording (`facts/llms-full.txt`, "What it is
built on") instead of the VOICE sentence that names the upstream protocol stack and its
implementation, because the campaign lint (`scripts/campaign/campaign.json`, rule
`other-projects`) rejects those names in outward copy. The VOICE variant is kept outside this
file until the planner decides which rule wins.

| Post | Characters |
| --- | --- |
| 1 | 250 |
| 2 | 280 |
| 3 | 241 |
| 4 | 226 |
| 5 | 212 |
| 6 | 234 |
| 7 | 264 |
| 8 | 273 |
| 9 | 264 |
| 10 | 272 |

Post 1 (250 characters)

```
SWARM is private money you can run yourself: proof of work, at most 20,999,987 SWM, no premine, shielded payments that encrypt sender, receiver and amount. Mainnet has been live since 2 October 2026, 15:42 UTC. Mined, not sold. No coins are promised.
```

Post 2 (280 characters)

```
Public ledgers keep every payment forever, and software reads them at scale. On SWARM each payment is transparent or shielded, your choice. Shielded means sender, receiver and amount are encrypted on the chain. Privacy was normal for cash; it should stay normal for digital money.
```

Post 3 (241 characters)

```
What shielding does not do: it hides what is written to the chain, not the fact that you use SWARM. Your ISP and the light-wallet server can still see that. Privacy on a young network is also weaker: fewer shielded payments to blend in with.
```

Post 4 (226 characters)

```
The chain is built on an open-source protocol stack that has secured real value for years. Consensus rules and cryptography are unmodified; we invented no cryptography. What SWARM adds: its network, its economics and its apps.
```

Post 5 (212 characters)

```
Equihash 200,9, a block every 75 seconds, 6.25 SWM per block, halving about every four years, 20,999,987 SWM at most. The genesis block holds no coins; every SWM that exists has been mined. No coins are promised.
```

Post 6 (234 characters)

```
Every block pays 80% to the miner and 20% to three published addresses: 8% Core Development, 4% Grants & Ecosystem, 8% Community & Development Reserve. For the whole life of the chain, block by block, in public. No coins are promised.
```

Post 7 (264 characters)

```
The closed start. Until 31 October 2026, 15:42 UTC only our own machines mine. For the next 24 hours the waiting list can mine too. From 1 November 2026, 15:42 UTC mining is open to everyone, and SWARM Node (node and CPU miner) is published. No coins are promised.
```

Post 8 (273 characters)

```
SWARM Wallet: Windows, macOS, Linux, Android APK. SWARM Messenger: end-to-end encrypted, sign in with 24 words, pay inside the chat; desktop only. SWARM Browser: ungoogled Chromium with the wallet in the toolbar, Windows pre-release. Builds are unsigned: check the SHA-256.
```

Post 9 (264 characters)

```
The uncomfortable parts. 20% of every block goes to the project for the whole schedule. Equihash hardware exists. Please keep ASICs and rented hash power off the network. No independent audit of the SWARM-specific changes has been published. No coins are promised.
```

Post 10 (272 characters)

```
We never sell you coins. Nobody promises you a price. We never DM first. We never ask for recovery words, private keys or a payment. New software breaks. https://swarm.green https://mainnet.explore.swarm.green https://github.com/Swarmcoin Mail: swarmofficial@atomicmail.io
```

## G. Official-links line

One line to paste as a reply, or into the location or bio of any other profile:

```
swarm.green · wallet.swarm.green · chat.swarm.green · mainnet.explore.swarm.green · x.com/swarm_coin · github.com/Swarmcoin. Anything else is not us.
```

## H. Check before saving (owner)

- [ ] Name reads `SWARM` (or the alternative with exactly one hexagon).
- [ ] Bio and location read exactly as written above, character for character.
- [ ] Website reads `https://swarm.green`.
- [ ] Header is `swarm-x-header-mainnet-1500x500.png` and shows "MAINNET LIVE · NO PREMINE · MINED, NOT SOLD"; never `swarm-x-header-1500x500.png`.
- [ ] Avatar is `swarm-x-avatar-400.png`.
- [ ] The owner publishes the thread (post 1, then each next post as a reply); an agent never publishes it.
- [ ] Right after the thread is out: profile > post 1 > Pin.
