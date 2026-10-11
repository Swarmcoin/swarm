# Pitch emails (final text)

Status: final, PROPOSED for sending. Nothing is sent before the owner's word for that batch
(dates and gates in `sequence.md`). The sender is the person named in owner item 318, written
here as [Name]; the address is swarmofficial@atomicmail.io.

How to use:
- Plain text, no attachments, no tracking links. Where a release goes with the mail, it is
  pasted below the signature as plain text; the mail says so in a bracketed line.
- "[personal line]" is the first line after the greeting in A1, B and C. Take it from
  `tracker.csv`, column personal_line, and log the send there.
- One mail per person. Never the same mail to two people at one outlet without saying so.
- Never offer anything for coverage, never discuss what SWM is worth (the project does not
  promise a price), never claim an audit. Answer every reply in writing within 24 hours.
- Lint: this whole file is linted. The only expected error is section D, which names the
  upstream project by necessity and is marked as such.

Every mail that mentions mining carries these two lines at the foot, exactly:

No coins are promised.
Please keep ASICs and rented hash power off the network.

---

## A0. Embargo ask (Mon 20 Oct 2026, 14:00 UTC)

Rows: DL News (Mathew Di Salvo, with tips@dlnews.com in copy), Decrypt (editor@decrypt.co),
The Block (Brian Danga).

Subject: Embargo request: SWARM press release for Monday 26 October 2026, 10:00 UTC

Hi [first name],

Would you take our first press release under embargo until Monday 26 October 2026, 10:00 UTC?
The story in one line: SWARM is private money you can mine yourself, a proof-of-work coin
whose payments stay encrypted on the chain, with a messenger that pays inside the
conversation, and public mining opens on 1 November. If you say yes, the embargoed release
reaches you today or tomorrow as plain text in a mail. Before the embargo lifts we will also
answer the hard questions in writing: the 30-day closed start, the permanent 20% allocation,
what optional privacy does not hide, and why no independent audit has been published yet.
If it is not for you, no reply is needed, and the release reaches you on the 26th with
everyone else.

[Name], SWARM · swarmofficial@atomicmail.io · x.com/swarm_coin

No coins are promised.
Please keep ASICs and rented hash power off the network.

---

## A1. Release 1 cover mail for crypto reporters (Mon 26 Oct 2026, 10:00 UTC)

Rows: every priority-1 and priority-2 row of segment A (crypto media) in `media-list.csv`:
DL News, Blockworks (once a reporter is found), Decrypt, The Defiant, CoinDesk (news@ and one
masthead reporter, as two separate mails), The Block (Naga Avan-Nomayo, Brian Danga),
Cointelegraph (editor@ only), BeInCrypto, Crypto Briefing, Protos. Reporters who accepted
the embargo already have the release; they get a two-line note that the embargo has lifted.

Subject: Money has become a record of you: SWARM opens public mining on 1 November (release below)

Hi [first name],

[personal line]

Every card payment, bank transfer and payment-app transaction leaves a record of who paid
whom, how much and when, and a public blockchain makes that record visible to everyone,
forever. SWARM (SWM) is a proof-of-work cryptocurrency built against that record: its
shielded payments keep the sender, the receiver and the amount encrypted on the chain while
every node still verifies them.

Three facts:

1. The mainnet has run since 2 October 2026, 15:42 UTC. Public mining opens on 1 November
   2026, 15:42 UTC, when SWARM Node is published for Windows, Linux and macOS (Apple silicon
   and Intel).
2. Every block pays 80% to its miner and 20% to three published project addresses (8% Core
   Development, 4% Grants & Ecosystem, 8% Community & Development Reserve), fixed in the
   genesis rules for the life of the chain. Until 31 October only the project's own machines
   mine: about 33,408 blocks and about 208,800 SWM, about 0.99% of the cap, each block split
   like every other and visible in the explorer.
3. The apps exist: SWARM Wallet (Windows, macOS, Linux, Android); SWARM Messenger
   (end-to-end encrypted messages between wallets, payments inside the chat, sign-in with the
   wallet's 24 words); SWARM Browser (Windows pre-release, the open-source Chromium code with
   Google's services removed, the wallet in the toolbar).

What is unfinished: no independent audit of the SWARM-specific changes has been published;
builds are not signed with a vendor certificate; the browser has no tracker blocking yet; the
messenger has no phone app. Shielding protects what is written to the chain, not the fact
that a computer connects to the network.

If it helps, I can arrange a call with the founding team. We answer every question in
writing within 24 hours, including the hard ones: the closed start, the 20%, what optional
privacy leaks, what the light-wallet server learns.

Facts on one page: https://swarm.green/what-is-swarm
Verify the chain: https://swarm.green/verify
Explorer (mainnet): https://mainnet.explore.swarm.green

Thanks for reading,
[Name], SWARM · swarmofficial@atomicmail.io · x.com/swarm_coin

No coins are promised.
Please keep ASICs and rented hash power off the network.

[Paste below the signature: press-release-1-mainnet-live.md, from the line FOR IMMEDIATE
RELEASE to the end of the disclaimer, as plain text. Not the status lines above it.]

Embargo-lifted note, for those who accepted the embargo (same minute):

Subject: Re: Embargo request: SWARM press release for Monday 26 October 2026, 10:00 UTC

Hi [first name], the embargo on the SWARM release has lifted as of 10:00 UTC today. The
release you have is final; the questions you sent are answered in the thread below.

[Name], SWARM · swarmofficial@atomicmail.io · x.com/swarm_coin

---

## B. Review request: FOSS and privacy-tech media, YouTube reviewers (Tue 27 Oct 2026, 14:00 UTC)

Rows: It's FOSS News (through its form), CyberInsider (the browser only), Naomi Brockwell /
NBTV, Techlore, The Hated One (after the hand check), The Register (Liam Proven), TechCrunch,
Wired (Andy Greenberg). Privacy Guides only as a factual tool entry, and only if the owner
wants it.

Subject: Two open-source apps for review: a browser with Google's services removed and a messenger that pays inside the chat

Hi [first name],

[personal line]

SWARM Browser 153.0.8010.52-6 (Windows pre-release) is built from the open-source Chromium
code with Google's services removed and privacy defaults switched on, with a wallet in the
toolbar. Missing today, and said on the download page: tracker blocking, builds signed with a
vendor certificate, and builds for macOS and Linux.

SWARM Messenger 0.1.5 (Windows, macOS, Linux) is built on the open-source code of a widely
used end-to-end encrypted messenger and runs on SWARM's own server. You sign in with a
wallet's 24 words instead of a phone number; messages between wallets are end-to-end
encrypted; a payment happens inside the chat. It is a first release: no phone app, builds not
signed with a vendor certificate.

Both belong to SWARM, a privacy coin that is mined, not sold; the apps stand or fall on their
own. No independent audit of the SWARM-specific changes has been published.

Downloads with SHA-256 checksums: https://swarm.green/ecosystem
Code: https://github.com/Swarmcoin

If you try them, criticism is the most useful thing you can send us. We answer technical
questions in writing within 24 hours and can put you in touch with the people who built
them. Nothing is attached to this mail and nothing is offered for a review.

[Name], SWARM · swarmofficial@atomicmail.io · x.com/swarm_coin

---

## C. Podcast and channel pitch (Tue 27 to Fri 30 Oct 2026, 14:00 UTC, one or two a day)

Rows: Monerotopia (Douglas Tuman), Closed Network Privacy Podcast (Simon Walsh), Opt Out (after
the hand check), Red Panda Mining, Juraj Bednar (Option Plus), The Hobbyist Miner, Rabid Mining
(after the hand check), Privacy Interviews (the apps and the format only). Day per row in
`tracker.csv`.

Subject: A privacy coin that will answer the hard questions on your show

Hi [first name],

[personal line]

We built SWARM (SWM), a proof-of-work cryptocurrency whose shielded payments keep the sender,
the receiver and the amount encrypted on the chain, and we would like to be interviewed by
someone who will not be kind about it.

The questions we expect, and will answer plainly:
- Why the first 30 days are mined by the project's own machines alone, and what that
  produces: about 0.99% of the cap, block by block in the explorer.
- Whether a permanent 20% of every block to three project addresses is a tax on miners. We
  call it a permanent allocation, and we say who holds the keys.
- What optional privacy leaks when people pay from transparent addresses.
- What the light-wallet server learns about a wallet that connects to it.
- Hardware: specialised machines for this proof of work exist, and nothing in the rules keeps
  them out.
- Why no independent audit of the SWARM-specific changes has been published yet.

What we think is worth your audience's time: a messenger where the payment happens inside the
encrypted chat and the identity is the wallet, not a phone number; a browser with Google's
services removed and the wallet in the toolbar; and a project that lists what is missing on
every download page.

Public mining opens on 1 November 2026, 15:42 UTC. Any recording date before or after works,
and we send written answers ahead if you want them.

https://swarm.green · https://github.com/Swarmcoin

[Name], SWARM · swarmofficial@atomicmail.io · x.com/swarm_coin

No coins are promised.
Please keep ASICs and rented hash power off the network.

---

## D. Upstream-community courtesy note (Mon 26 Oct 2026, 10:00 UTC)

lint: names the upstream project by necessity; owner item 445 decides whether it is sent

Rows: ZecHub (no email: a Discord message or a GitHub note from the owner's account). The
forum introduction itself belongs to the session Reddit and Forums (`../forums/`); this note
is only the courtesy mail. Keep it short.

Subject: A courtesy note from SWARM, a new network built on Zcash code

Hello,

We are the team behind SWARM (SWM), a new proof-of-work network that runs the Zcash
protocol as implemented by Zebra. We changed the network definition, the genesis, the address
prefixes, the emission schedule and the block allocation; the consensus rules and the
cryptography are upstream's, unmodified. We owe the project to the Electric Coin Company, the
Zcash Foundation and Zingo Labs, and we say so on swarm.green/verify and in the repository.
We would like to hear where we are wrong, here or in the forum thread [link]. If anything we
write is useful upstream, it is yours.

[Name], SWARM · swarmofficial@atomicmail.io · x.com/swarm_coin

---

## E. Pool operators (Fri 30 Oct 2026, 14:00 UTC)

Rows: f2pool (business@), Luxor (only if a written route opens), WoolyPooly and HeroMiners
(chat, from the owner's account), K1Pool (contact@). Not 2Miners (paid; owner decision).
Not MiningPoolStats yet (E2 on 1 November).

Subject: SWARM (SWM), Equihash 200,9: public mining opens 1 November 2026, 15:42 UTC

Hello,

SWARM (SWM) opens public mining on 1 November 2026, 15:42 UTC. A technical summary for pool
operators:

- Proof of work: Equihash 200,9; 75-second block target.
- Block reward 6.25 SWM, halving every 1,680,000 blocks; at most 20,999,987.3152 SWM.
- Every coinbase carries three fixed outputs to published project addresses: 8% Core
  Development, 4% Grants & Ecosystem, 8% Community & Development Reserve. The miner's 80%
  goes to the payout address. Coinbase maturity 100 blocks.
- Addresses: transparent s1 (P2PKH) and s3 (P2SH); shielded swm1.
- Explorer (mainnet): https://mainnet.explore.swarm.green
- Genesis hash, endpoints and the three published addresses: https://swarm.green/verify
- Code: https://github.com/Swarmcoin

We are not asking you to promote anything, only to add the coin if your miners ask for it.
Technical questions to this address; we answer in writing within 24 hours.

[Name], SWARM · swarmofficial@atomicmail.io · x.com/swarm_coin

No coins are promised.
Please keep ASICs and rented hash power off the network.

---

## E2. MiningPoolStats add-coin note (Sun 1 Nov 2026, evening, about 20:00 UTC)

Row: MiningPoolStats. Route: the Quick Message to MiningPoolStats form (footer email icon, a
modal on the homepage) with three fields: sender, subject, message. The sender fills it by
hand; agents do not fill forms. Only after the first public block is in the explorer.

Sender: swarmofficial@atomicmail.io

Subject: Add coin: SWARM (SWM), Equihash 200,9, public mining since 1 November 2026

Message:

SWARM (SWM) opened public mining on 1 November 2026, 15:42 UTC. Algorithm Equihash 200,9;
block target 75 seconds; block reward 6.25 SWM, halving every 1,680,000 blocks; at most
20,999,987.3152 SWM. Every block pays 80% to the miner and 20% to three published project
addresses, fixed in the genesis rules. Website https://swarm.green · Explorer (mainnet)
https://mainnet.explore.swarm.green · Code https://github.com/Swarmcoin · X
https://x.com/swarm_coin. Pools: [the pools that have added SWM by then, or: none yet; solo
mining with SWARM Node]. No coins are promised.
Please keep ASICs and rented hash power off the network.
[Name], SWARM

---

## R2. Release 2 cover (Sun 1 Nov 2026, 16:00 UTC)

Rows: everyone who replied or published, then rows never sent before. Rows that never
answered at all get release 2 once, through F2 on 2 November, not twice.

Subject: SWARM opened public mining at 15:42 UTC today (release below)

Hi [first name],

Thank you for [your reply / your piece, link]. At 15:42 UTC today SWARM ended its 30-day
closed start and opened mining to everyone; the first public block, number [HEIGHT-OPEN], is
in the explorer at https://mainnet.explore.swarm.green, and release 2 is below. Questions are
answered in writing within 24 hours.

[Name], SWARM · swarmofficial@atomicmail.io · x.com/swarm_coin

No coins are promised.
Please keep ASICs and rented hash power off the network.

[Paste below the signature: press-release-2-mining-open.md, from FOR IMMEDIATE RELEASE to the
end of the disclaimer, with the three blanks filled from the explorer.]

---

## F1. Follow-up 1 (Thu 29 Oct 2026, 14:00 UTC)

Rows: every A, B and D row sent on 26 or 27 October with no reply.

Subject: Re: [original subject]

Hi [first name], one follow-up in case the first mail was buried. The short version: SWARM's
mainnet has run since 2 October and public mining opens on 1 November 2026, 15:42 UTC, with
the facts on one page at https://swarm.green/what-is-swarm. We answer any question in writing
within 24 hours, including the hard ones. If it is not for you, no reply is needed.

[Name], SWARM · swarmofficial@atomicmail.io · x.com/swarm_coin

No coins are promised.
Please keep ASICs and rented hash power off the network.

---

## F2. Follow-up 2, the last mail (Mon 2 Nov 2026, 14:00 UTC)

Rows: every row with no reply at all. After this, stop.

Subject: Re: [original subject] (last mail)

Hi [first name], this is the last mail from us on this. SWARM opened public mining yesterday,
1 November 2026, at 15:42 UTC; the first public blocks are in the explorer at
https://mainnet.explore.swarm.green, and release 2 is below. We will not write again unless
you ask, and any question is still answered in writing within 24 hours.

[Name], SWARM · swarmofficial@atomicmail.io · x.com/swarm_coin

No coins are promised.
Please keep ASICs and rented hash power off the network.

[Paste below the signature: press-release-2-mining-open.md, from FOR IMMEDIATE RELEASE to the
end of the disclaimer, blanks filled.]

---

## G. Thank-you and correction notes (3 to 6 Nov 2026)

Rows: everyone who published. A correction goes out in writing within 24 hours of reading the
piece, and only for a fact, never for an opinion.

Thank-you:

Subject: Thank you for your piece on SWARM

Hi [first name], thank you for [title of the piece] ([link]). If a later piece needs a fact
from us, we answer in writing within 24 hours.

[Name], SWARM · swarmofficial@atomicmail.io · x.com/swarm_coin

Correction:

Subject: One factual correction to [title of the piece]

Hi [first name], thank you for [title of the piece] ([link]). One fact needs a correction:
the piece says [the sentence, copied exactly], and the correct fact is [the fact], with the
source at [a page on swarm.green or the explorer]. Everything else is yours to judge; we are
not asking for any other change.

[Name], SWARM · swarmofficial@atomicmail.io · x.com/swarm_coin

---

## H. Invitation to the critic for the X Space "Ask us anything hard", Thursday 29 October 2026 23:00 UTC (19:00 Santo Domingo)

The owner picks the name and sends (Owner Checklist item 318); the Spaces plan of Launch
Campaign Control records both. Send the first draft; the second only if the first is declined
or unanswered.

### H1. Cas Piancey, Protos (first choice)

Route: editorial@protos.com (the masthead prints per-journalist addresses as first name at
protos.com; his own is not printed, so the sender confirms it by hand before using it).

Subject: An invitation to question SWARM live for 60 minutes: X Space, Thursday 29 October, 23:00 UTC

Hi Cas,

We would like to invite you to question the SWARM project live for 60 minutes in an X Space
on Thursday 29 October 2026 at 23:00 UTC, which is 23:00 in London. The subjects we want you
to press us on are the 30-day closed start, the permanent 20% allocation to three project
addresses, custody of the keys to those addresses, who the team is, the hardware question and
the independent audit that has not been published. Your questions are not screened or agreed
in advance. Nothing is paid and no coins are involved, in either direction. The Space is
recorded, and you keep every right to publish your own account of it, however critical. If
it is not for you, a one-line no is plenty, and the offer of written answers stands either
way.

[Name], SWARM · swarmofficial@atomicmail.io · x.com/swarm_coin

### H2. Douglas Tuman (fallback)

Route: the guest form at https://www.monerotalk.live/contact (filled by the sender), or
monerotopia@protonmail.com.

Subject: An invitation to question SWARM live for 60 minutes: X Space, Thursday 29 October, 19:00 New York

Hi Douglas,

You give guests from outside your own community a hard time on your show, and we would like
you to do the same to us, live, for 60 minutes in an X Space on Thursday 29 October 2026 at
23:00 UTC, which is 19:00 in New York. Please press us on the 30-day closed start, the
permanent 20% allocation to three project addresses, custody of the keys to those addresses,
who the team is, the hardware question and the independent audit that has not been
published. Your questions are not screened or agreed in advance. Nothing is paid and no coins
are involved, in either direction. The Space is recorded, and you keep every right to publish
your own account of it, on your show or anywhere else. If it is not for you, a one-line no is
plenty.

[Name], SWARM · swarmofficial@atomicmail.io · x.com/swarm_coin
