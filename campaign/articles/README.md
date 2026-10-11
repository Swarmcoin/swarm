# Articles

Four long-form pieces, written to be published on Dev.to, Medium, Paragraph and the
crypto blogging sites in the order given in `../medium/README.md`. Each has YAML front matter
(title, description, tags, canonical_url placeholder, published: false) and a one-line
disclosure that the SWARM project published it.

Story-first rewrite 2026-10-09; sources that block robots are cited by identifier.

| File | What | Words |
| --- | --- | --- |
| `top-privacy-coins-2026.md` | The privacy-coin landscape in 2026. Opens with Hong Kong 2019 (cash for a single MTR ride) and Bitcoin's open privacy sentence; then 16 projects compared on privacy model, default or optional, consensus, allocation and status; the five questions; the regulatory picture; SWARM gets one honest section of the same length as Monero's | about 3,400 |
| `surveillance-money-and-the-case-for-shielded-payments.md` | The coin. Opens with Venmo's public-by-default feed; the Bank Secrecy Act and Shultz; chain analysis; why new addresses and mixers fall short; what a shielded payment hides and does not; the stack, the split, the closed start, the two wallets | about 2,250 |
| `a-browser-that-does-not-phone-home.md` | SWARM Browser. Opens with AOL user No. 4417749; what a browser sends before you type; what ungoogled-chromium removes; which defaults are on; the wallet in the toolbar; how to tell a real site from a copy; the plain list of what is missing | about 1,950 |
| `a-messenger-where-the-money-is-in-the-conversation.md` | SWARM Messenger. Opens with the Stanford metadata study and Hayden's 2014 line; what end-to-end encryption hides; the double ratchet; chat control; Signal's protocol on SWARM's server, sign-in with 24 words, payments inside the chat. Carries owner item 316 markers | about 2,100 |
| `the-database-that-became-a-kill-list.md` | DRAFT, Desk-approved outline 5, 2026-10-09. Opens with the Amsterdam population register attack of 27 March 1943; the US Census Bureau and Japanese Americans (2000 block data, 2007 names); Germany's 1983 census ruling on informational self-determination; a transparent ledger as a register nobody can burn; one honest SWARM section | about 1,900 |
| `how-to-verify-a-download.md` | DRAFT, Desk-approved outline 8, 2026-10-09. Opens with PGP's source printed as a book in 1995 and the investigation closed on 11 January 1996, with the Clipper chip in two sentences; what a SHA-256 is; the three commands; integrity versus authenticity; Kerckhoffs 1883; SWARM's checksums, unsigned builds and genesis hash; a five-line checklist | about 1,600 |
| `what-a-block-explorer-sees.md` | DRAFT, Desk-approved outline 7, 2026-10-09. Opens with the Netflix Prize de-anonymisation; a transparent payment in an explorer and address clustering; a fully shielded transaction, viewing keys and payment disclosures; SWARM mainnet block 8,100 and its four reward parts, read on 9 October 2026; what the light-wallet server and the ISP still see | about 1,850 |
| `NEXT-FOUR-OUTLINES.md` | Outlines for the next four, PROPOSED | about 900 |

Each article ends with a Sources section.

## Open questions to settle before publishing

1. **Owner item 316: messenger calls, groups and version.** `doc/getting-started.md` says
   messages and calls are end-to-end encrypted and that group chats and settings sync work;
   the roadmap page lists groups and voice and video calls under Planned. The messenger
   article now follows the Marketing Desk default of 2026-10-09, not getting-started.md:
   calls and groups are written as Planned, and the first release as one-to-one chat with
   photos, files and payments. The messenger page header says 0.1.4 while its download rows
   say 0.1.5; the article uses 0.1.5. Every affected sentence carries an
   `<!-- OWNER ITEM 316 ... -->` marker; confirm with the owner, then delete the markers.
2. **The same header-versus-rows pattern on the wallet page.** The header says
   0.1.0-mainnet.10, the download rows 0.1.0-mainnet.11. The texts use the rows.
3. **The USD price reading** in the apps is left out of every article on purpose
   (VOICE.md rule 1).
4. **Third-party figures** in the comparison article (Monero's Qubic incident, Litecoin MWEB
   usage, Dash CoinJoin share, the listed company's Zcash holding, FATF percentages) are marked
   "reported" or carry their date; the Zcash shielded share is now the zecstats.org reading of
   6 October 2026. Check the ones you care about against the primary source before publishing.

## Checks

`python tools/check_prose.py articles/*.md` runs the policy's banned phrases, patterns and
SWARM-link rules over the files.
