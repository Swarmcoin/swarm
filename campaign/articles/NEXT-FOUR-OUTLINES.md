# The next four articles: outlines for Marketing Desk approval (2026-10-09)

Status: PROPOSED. Written by the session "Articles Medium and Dev.to" from the pillars in the brief. Nothing is drafted until the Desk approves an outline; each piece then follows the same shape as the first four: story, mechanism, SWARM as the honest example, what is missing, sources. Seeds refer to `../research/freedom-and-privacy-stories-2026-10.md` (letters) and `../research/privacy-explainers-2026-10.md` (numbers).

## 5. The database that became a kill list (a Wednesday thread, expanded)

- Source thread: X calendar `d01-b`, Amsterdam population registry, 27 March 1943 (seed C1; Anne Frank House, Verzetsmuseum, USHMM).
- Story: the Dutch registry recorded religion; the occupiers did not have to find anyone. Van der Veen and Arondeus, dressed as police, drenched and blew up the card files; about 15% burned; twelve were executed on 1 July 1943.
- Mechanism: a record's harm is decided by whoever holds it later. Second case in brief: the US Census Bureau and Japanese Americans, 1942 to 1943, confirmed by Seltzer and Anderson in 2000 and 2007 (seed C3); Germany's 1983 census ruling on informational self-determination (seed C5, Bundesverfassungsgericht English summary).
- Bridge: a transparent ledger is a registry that nobody can burn. What a shielded ledger refuses to write down (seed 7).
- SWARM: one section, the honest example: shielded by default in the wallet, transparent addresses exist, the light-wallet server and the ISP still see the connection, no audit yet.
- Cautions: no politics; the Netherlands death-rate figure only with its source.
- Length about 1,800 words. Publish after the first four, week 5.

## 6. Mining a block at home: what it proves, what it pays, what it does not promise (for the 1 November 2026 opening)

- Story: Adam Back's Hashcash, 1997, built to make spam expensive (seed 13, hashcash.org paper); the first Bitcoin transaction on 12 January 2009 to Hal Finney, who had tweeted "Running bitcoin" the day before (seed A9; source Finney's own post "Bitcoin and Me", 19 March 2013, on the bitcointalk forum, if a 200 link exists, otherwise cited by identifier).
- Mechanism: what a proof-of-work block proves (one hash to verify, trillions to produce); why a reward waits 100 blocks (seed 15, ZIP 213); why "solving equations" is the wrong picture.
- SWARM: Equihash 200,9, 75-second blocks, 6.25 SWM, 80/8/4/8, public mining from 1 November 2026, 15:42 UTC, node software published on swarm.green that day, every miner solo (no pool protocol yet, roadmap "Planned"), Equihash ASICs exist and nothing in the rules keeps them out.
- Mandatory lines, verbatim: "No coins are promised." "SWM has no guaranteed value and can lose value, including all of it." "Please keep ASICs and rented hash power off the network." "Mined, not sold."
- Practical: how to check the genesis hash, how to read the four parts of a reward in the explorer, where immature rewards show in the wallet.
- No hashrate projections, no earnings maths, no hardware recommendations beyond "a CPU you own".
- Length about 1,900 words. Publish in the week of 27 October (before the opening) only if the node download page is live by then; otherwise the week after the opening with what actually happened on 1 November.

## 7. What a block explorer sees, and what it cannot

- Story: the AOL log (seed 23) if not already used in the browser article's final draft; otherwise the Netflix Prize de-anonymisation, 2008: 8 ratings and 14-day dates identify 99% of records (seed 21, arXiv link). Lesson: a public dataset with the names removed is not anonymous; a transparent chain is that dataset with the names left in.
- Mechanism: walk through one transparent transaction in any explorer (addresses, amounts, history, clustering per "A Fistful of Bitcoins", seed 8); then one fully shielded transaction on the Zcash protocol stack: transaction id, block, fee, the proof verified, nothing else (seed 7, zechub.wiki); viewing keys and payment disclosure as the way to prove receipt.
- SWARM: a block on mainnet.explore.swarm.green with its four reward parts; a shielded payment on the same explorer; what the light-wallet server still learns (ZIP 307, seed 9).
- Length about 1,700 words. Pairs with a short X explainer the same week.

## 8. How to verify a download, and why the checksum is not the whole story

- Story: the Clipper chip, 1993 to 1996, the escrow field broken by Matt Blaze in a year (seed A3, EFF retrospective), or shorter: PGP's source code printed as a book in 1995 so it could be exported (seed A1). Lesson: trust in software is checkable, or it is not trust.
- Mechanism: what a hash is (seed 2, FIPS 180-4); the three commands (seed 35: certutil, shasum -a 256, sha256sum); integrity versus authenticity: a swapped page swaps both file and hash, which is what signatures and a second channel are for; Kerckhoffs 1883 on why open source is the precondition (seed 14, petitcolas.net).
- SWARM: every download on swarm.green with its SHA-256; builds unsigned for now, SmartScreen and Gatekeeper warn, the checksum is the verification; signed builds are "in development" on the roadmap; the genesis hash as the chain's checksum; only download from swarm.green.
- Practical: a five-line checklist the reader can keep.
- Length about 1,500 words. Publishes any week; useful before the 1 November node download.

## Order proposed

5 (week 5), 8 (week 6), 7 (week 7), 6 timed to the node download page. Promotion stays at most one piece in five: of these four only the mining piece is about getting SWM, and it carries the disclaimers.
