# Articles

Four long-form pieces, written to be published on Dev.to, Medium, Paragraph and the
crypto blogging sites in the order given in `../medium/README.md`. Each has YAML front matter
(title, description, tags, canonical_url placeholder, published: false) and a one-line
disclosure that the SWARM project published it.

| File | What | Words |
| --- | --- | --- |
| `top-privacy-coins-2026.md` | The privacy-coin landscape in 2026: 16 projects compared on privacy model, default or optional, consensus, allocation and status; the five questions to ask any privacy coin; the regulatory picture; SWARM gets one honest section of the same length as Monero's | about 2,900 |
| `surveillance-money-and-the-case-for-shielded-payments.md` | The coin: why transparent ledgers are surveillance, what a shielded payment hides and does not, the stack, the split, the closed start | about 1,800 |
| `a-browser-that-does-not-phone-home.md` | SWARM Browser: what ungoogled-chromium removes, which defaults are on, the wallet in the toolbar, and the plain list of what is missing | about 1,700 |
| `a-messenger-where-the-money-is-in-the-conversation.md` | SWARM Messenger: Signal's protocol on SWARM's server, sign-in with 24 words, payments inside the chat, what the first release does not do | about 1,500 |

## Open questions to settle before publishing

1. **Messenger calls and groups.** `doc/getting-started.md` says messages and calls are
   end-to-end encrypted and that group chats and settings sync work; the roadmap page lists
   groups and voice and video calls under "planned". The articles, the X calendar and the
   press releases follow getting-started.md. One of the two sources is out of date; fix the
   source, then the texts if needed.
2. **Version numbers.** The messenger page header says 0.1.4 while its download rows say
   0.1.5, and the swarm README lists older versions than the site. The texts use the
   download-row versions (Wallet 0.1.0-mainnet.11, Messenger 0.1.5, Browser 153.0.8010.52-6).
3. **The USD price reading** added to the apps on 5 October is not mentioned anywhere in
   this kit, on purpose (VOICE.md rule 1). If the team wants it mentioned, it needs its own
   wording that names no figure.
4. **Third-party figures** in the comparison article (Zcash shielded share, Monero's Qubic
   incident, Litecoin MWEB usage, Dash CoinJoin share, FATF percentages, the EU application
   date of 10 July 2027) come from the research file and are marked "reported"; check the
   ones you care about against the primary source before publishing.

## Checks

`python tools/check_prose.py articles/*.md` runs the policy's banned phrases, patterns and
SWARM-link rules over the files.
