---
title: "How to verify a download, and why the checksum is not the whole story"
description: "PGP's source code printed as a book in 1995, what a SHA-256 hash is, the one command per system that checks a file, the difference between integrity and authenticity, and how to check SWARM's downloads and its chain."
tags: [security, privacy, opensource, tutorial]
canonical_url: https://swarm.green/
published: false
lint_judged: ["security-claims: 'Secure Hash Standard', the title of NIST FIPS 180-4 in Sources, not a claim about SWARM", "other-projects: Zcash and Zebra named as the stack attribution"]
---

# How to verify a download, and why the checksum is not the whole story

*Published by the SWARM project. SWARM is experimental software; nothing here is financial advice.*

## A program printed as a book

In June 1991 Pretty Good Privacy, a program Phil Zimmermann had written and released as free software, was posted to USENET. PGP let anyone encrypt e-mail with the kind of cryptography that, until then, governments had kept for themselves. It soon spread outside the United States, and in 1993 US Customs opened a criminal investigation. Strong encryption was classed as a munition under the Arms Export Control Act, and exporting it without a licence was treated like exporting arms.

Zimmermann's answer was a book. In 1995 MIT Press published "PGP Source Code and Internals": the complete C source of the program, printed on paper. Books are protected speech in the United States and could leave the country legally. A reader abroad could cut off the covers, scan the pages and turn them back into a working program. On 11 January 1996 the US Attorney's office in San Jose wrote to his lawyer that he would not be prosecuted and that the investigation was closed. He was never charged.

The same years produced the opposite idea. On 16 April 1993 the White House announced the Clipper chip, an encryption chip for phones built around a classified algorithm, whose keys the government would hold in escrow; in 1994 Matt Blaze, then at AT&T, showed that its law-enforcement field could be defeated, and by 1996 the proposal was dead.

Put the two side by side and the lesson is about trust. Clipper asked people to trust a design nobody outside could read. PGP put every line on paper and let anyone check it. Trust in software is either something you can check, or it is not trust.

## What a hash is

Checking starts with a hash. SHA-256, specified by NIST in FIPS 180-4, takes any input, a one-line note or a 200 MB installer, and produces 256 bits, usually written as 64 hexadecimal characters.

Two properties make it useful for downloads. It is one-way: nobody can run it backwards to rebuild the file. And it is unforgiving: change one bit of the input and, on average, about half of the output bits change, so the two strings look unrelated. Nobody has found two different files with the same SHA-256.

A hash is not encryption. Encryption can be reversed with a key; a hash has no key and cannot be reversed. It is a fingerprint, and the fingerprint is the whole point.

So a publisher lists the expected hash next to the file. You compute the hash of what actually arrived on your disk. If the two strings match, every byte is the byte the publisher hashed. If one character differs, something changed on the way: a broken download, a faulty mirror, or a file someone swapped.

## The three commands

One command per system. Replace `<file>` with the path of what you downloaded.

```
Windows (Command Prompt or PowerShell):  certutil -hashfile <file> SHA256
macOS (Terminal):                        shasum -a 256 <file>
Linux:                                   sha256sum <file>
```

In PowerShell, `Get-FileHash <file>` gives the same result. On Linux, if the publisher offers a file of checksums, `sha256sum -c` with that file prints OK or FAILED for each line, which saves reading 64 characters by eye.

Compare every character, not the first few and the last few. An attacker who can make two hashes share a beginning and an end has not achieved much; an attacker who can make all 64 characters match has broken SHA-256, and nobody has publicly done so.

## Integrity is not authenticity

Here is the part most guides leave out. A matching checksum proves integrity: the file is the one whose hash is printed on the page. It does not prove authenticity: that the page is the one the real publisher wrote.

If someone takes over a download page, they swap both the file and the hash. Your check then passes, perfectly, on the wrong file. A checksum catches a corrupt download and a swapped file on a mirror. It does not catch a swapped page.

Two things close that gap.

- **A signature.** The publisher signs the release with a private key that never touches the web server. Your system, or a tool like GnuPG, checks the signature against a public key you already trust. A thief who changes the page cannot produce a valid signature. This is what Windows SmartScreen and macOS Gatekeeper look for, among other things, when they decide whether to warn you.
- **A second channel.** The publisher posts the same hash somewhere else, under separate control, such as a source repository or an account you already follow. An attacker now has to change two places at once.

## Why the code has to be readable

There is a third layer, and it is older than computers. In January and February 1883 Auguste Kerckhoffs published "La cryptographie militaire" in the Journal des sciences militaires. His second principle, in Fabien Petitcolas's translation: "The system must not require secrecy and can be stolen by the enemy without causing trouble." Only the key may be secret.

A hash proves you got the file the publisher built. It says nothing about what that file does. For that, the source has to be public, the build has to be something others can repeat, and people other than the authors have to read it. Clipper failed that test by design. PGP passed it by printing itself.

## SWARM: what you can check today

Here is how this applies to our own downloads, including what is missing.

**Every file has a SHA-256.** Every download in the Ecosystem on swarm.green, SWARM Wallet, SWARM Messenger and SWARM Browser, is listed with its SHA-256 beside it, and the wallet page links a SHA256SUMS file for `sha256sum -c`. The files themselves are served from a separate download server of ours, so the page that shows the hash and the server that sends the file are two different machines. That is a modest separation, not a signature: both are run by the same project.

**Builds are unsigned for now.** Windows may show a SmartScreen notice for a new publisher before the first start; the macOS builds are not signed with an Apple Developer ID and not notarized, so macOS refuses them until you allow them under System Settings, Privacy & Security. Until builds are signed, the checksum is the verification, and the warning is accurate: the operating system cannot confirm who made the file. Signed macOS builds are listed as in development on our roadmap; we give no date.

**The source is public.** The code is at github.com/Swarmcoin. The chain is built on the Zcash protocol stack as implemented by Zebra, with the consensus rules and the cryptography left unmodified. No independent audit of the SWARM-specific changes has been published; the upstream components have their own security records.

**The chain has a checksum too.** A blockchain is identified by its first block. The hash of SWARM mainnet's genesis block is:

```
01b76d8a0f18c502b23ab6605e26296d189aa5770fc4a34155e5c7b250a0eff2
```

It is published on swarm.green/verify with the launch time, 2 October 2026, 15:42 UTC, the public endpoints and the three project addresses. Software that syncs the chain itself reports the hash of block 0; if it reports anything else, it is on a different chain, whatever its name says. The node software will be published on swarm.green from 1 November 2026, 15:42 UTC, and the same two checks apply to it: the SHA-256 of the file and the genesis hash it reports. No coins are promised. SWM has no guaranteed value and can lose value, including all of it. Please keep ASICs and rented hash power off the network.

**Only download from swarm.green.** Not from a link in a reply, an advert, a direct message or a file-sharing site. A copy can imitate our page perfectly; it cannot imitate the domain. We never ask for recovery words, private keys or a payment.

## A checklist to keep

1. Get the file from the publisher's own domain, reached from a bookmark you made yourself, not from a link someone sent you.
2. Run one command: `certutil -hashfile <file> SHA256`, `shasum -a 256 <file>` or `sha256sum <file>`.
3. Compare all 64 characters with the hash on the page. One difference: delete the file.
4. Where the publisher offers a signature or a second place with the same hash, check that too; a checksum alone does not catch a swapped page.
5. For a blockchain, check the genesis hash your software reports against the one the project published.

## Sources

- The PGP investigation closed on 11 January 1996: the announcement by Zimmermann's lawyer, Philip L. Dubois, 12 January 1996, https://www.mit.edu/~prz/EN/news/PRZ_case_dropped.html ; Zimmermann's testimony to the US Senate, 1996, https://www.mit.edu/~prz/EN/essays/Testimony.html ; pointer for the 1993 investigation and the book: https://en.wikipedia.org/wiki/Phil_Zimmermann
- The book: Philip R. Zimmermann, "PGP Source Code and Internals", MIT Press, 1995, ISBN 0-262-24039-4 (cited by identifier)
- The Clipper chip: EFF, "On the Clipper Chip's Birthday, Looking Back on Decades of Key Escrow Failures", 16 April 2015, https://www.eff.org/deeplinks/2015/04/clipper-chips-birthday-looking-back-22-years-key-escrow-failures ; Matt Blaze, "Protocol Failure in the Escrowed Encryption Standard", 1994, https://www.mattblaze.org/papers/eesproto.pdf
- SHA-256: NIST FIPS 180-4, Secure Hash Standard, https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf
- The commands: Microsoft, certutil, https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil ; GNU Coreutils manual, section "sha2 utilities" (sha256sum, cited by identifier); macOS `shasum` manual page (cited by identifier)
- Kerckhoffs' principles, 1883, with Fabien Petitcolas's English version: https://www.petitcolas.net/kerckhoffs/
- SWARM downloads and checksums: https://swarm.green/ecosystem ; genesis hash and launch facts: https://swarm.green/verify ; signed macOS builds under In development: https://swarm.green/roadmap ; source code: https://github.com/Swarmcoin
