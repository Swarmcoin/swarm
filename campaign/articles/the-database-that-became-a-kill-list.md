---
title: "The database that became a kill list: a record is only as safe as whoever holds it next"
description: "Amsterdam's population register in 1943, the US Census Bureau in 1942 and 1943, Germany's 1983 census ruling, and what a shielded ledger declines to write down. With the limits of SWARM stated plainly."
tags: [privacy, history, cryptography, blockchain]
canonical_url: https://swarm.green/
published: false
lint_judged: ["other-projects: Zcash and Zebra named as the stack attribution; Zcash in the cited ZecHub and ZIP 307 source links"]
---

# The database that became a kill list: a record is only as safe as whoever holds it next

*Published by the SWARM project. SWARM is experimental software; nothing here is financial advice.*

## Plantage Kerklaan 36, 27 March 1943

On the evening of Saturday 27 March 1943, nine members of a Dutch resistance group walked up to the Amsterdam population register at Plantage Kerklaan 36, a former concert hall beside the zoo. They wore police uniforms that a tailor in the group had made. They told the guards they had come to search the building for explosives, and the guards let them in. Two medical students sedated the guards. The others pulled the card files out of their cabinets, threw them on the floor, soaked them and set charges. Five explosions followed, and a fire that could be seen from far away.

The group was led by the sculptor Gerrit van der Veen and the artist and writer Willem Arondeus, and it forged identity cards. In the occupied Netherlands everyone aged 15 and over had to carry one. From January 1941 Jews also had to register as Jews, and their cards were stamped with a large J. A forged card was only as good as the register behind it: one comparison with the card file in the town hall exposed it. So the register had to go.

It mostly did not. Part of the building burned and collapsed; most of it stood. The Anne Frank House puts the result in one line: only 15% of the records were completely lost. The mess helped for a while, and officials who worked with the resistance used it to slip false entries into the files. The Sicherheitsdienst found the group within weeks, through betrayal. Fourteen were sentenced to death in June 1943. Two were spared at the last minute; twelve were shot at the start of July 1943 (the sources give 1 or 2 July). Before he died, Arondeus asked his lawyer, Lau Mazirel, to tell the world that homosexuals were no less brave than anyone else. Van der Veen escaped and was executed in 1944.

Of the roughly 140,000 Jews in the Netherlands, about 104,000 did not survive the persecution, about 74%, the highest share in occupied Western Europe. That is the Anne Frank House's figure, from the historians Pim Griffioen and Ron Zeller. The United States Holocaust Memorial Museum names, among the reasons, the efficiency of the German administration and the cooperation of Dutch administrators and police.

Nobody in Amsterdam had built the register to kill anyone. It was a good register. That was the problem.

## A promise switched off in weeks

The second case is quieter, and it took more than sixty years to confirm.

The US Census Bureau collects detailed answers from every household and is barred by law from releasing anything that identifies a person. In March 1942 the Second War Powers Act suspended that protection. In 2000 the historian Margo Anderson and the statistician William Seltzer showed that the Bureau had released block-by-block data that told officials which neighbourhoods in California, Arizona, Wyoming, Colorado, Utah, Idaho and Arkansas had Japanese American residents, during the roundup for the internment camps. The Bureau's director at the time, Kenneth Prewitt, apologised publicly that year.

The Bureau's own lore held that it had never handed over names. In 2007 Anderson and Seltzer found the memos. On 4 August 1943 the Treasury Secretary, whose department included the Secret Service, asked for the names and locations of all people of Japanese ancestry in the Washington, D.C. area. The Bureau supplied them seven days later. Scientific American reported the find on 30 March 2007.

It was legal. That is the part worth remembering. The confidentiality promise was a law, and a law can be changed in weeks when a government is frightened enough. Every record a census had collected under the old promise was then available under the new rules.

## A court that saw it coming

Forty years later a court drew the conclusion out loud.

West Germany planned a full census for 1983, with questions on work, commuting and housing, and a provision that let the answers be compared with local population registers. Citizens' groups called for a boycott, and people filed constitutional complaints. On 15 December 1983 the Federal Constitutional Court ruled (1 BvR 209/83). It upheld the census itself, struck down the provisions on passing data on, including the comparison with the civil registers, and set out a right it called informational self-determination: the authority of each person, in principle, to decide on the disclosure and use of their own data.

The reasoning, in the court's English translation (paragraph 146), is the most precise description of the problem we know. A legal order is not compatible with that right if citizens can no longer tell "who knows what kind of personal information about them". And people who expect that unusual behaviour may be recorded, stored and passed on will tend not to stand out. The harm is not only what is done with a record. It is what people stop doing because the record exists.

## A register that nobody can burn

Now hold those three cases up against a transparent blockchain.

A transparent ledger is a population register for money. It lists every payment, every address, every amount and the time, and every node keeps a full copy. It is designed so that nobody can alter it and nobody can delete it. That is the point of a blockchain, and it is a real achievement. But read it as the Amsterdam registrars' successors would: it is a register that no resistance group can soak in water, that no court can order partly struck, and that no future law needs to unlock, because it was never locked.

The names are not in it. They do not need to be. Chain analysis has shown since at least 2013 that addresses which pay together belong together, and that one purchase at a shop that knows your name labels the whole cluster. The ledger does not have to record religion or ancestry. It records what you paid for, to whom and when, which says more.

A shielded ledger makes a different choice about what to write down. On the Zcash protocol stack, a fully shielded transaction leaves on the chain a transaction id, the block it is in, the fee and a zero-knowledge proof that the network checked: the inputs exist, nobody spent them before, and nothing was created from nothing. The sender, the receiver, the amount and the memo are written only in encrypted form, readable by whoever holds the matching viewing key. The chain still keeps a permanent record. It is a record that a valid payment happened, not a register of who paid whom.

That is not a promise like the census law. It does not depend on who governs later or on what they are afraid of. The details are not there in the clear to hand over.

## SWARM, honestly

SWARM is a proof-of-work chain built on the Zcash protocol stack as implemented by Zebra, with the consensus rules and the cryptography left unmodified. Here is what that does and does not give you, in the same plain terms we used above.

- **Shielded is the default, not the only option.** SWARM Wallet gives you a shielded address (`swm1…`) by default and tells you which kind of payment you are about to make. Transparent addresses (`s1…` and `s3…`) exist on SWARM mainnet, and a transparent payment is as public as on any transparent chain. The three published project addresses are transparent on purpose, so that anyone can watch what they receive.
- **The connection is not shielded.** A light wallet talks to the SWARM mainnet light-wallet server. That server sees your IP address, which block ranges you download and which transactions you send. The protocol is designed so that it does not learn which shielded notes are yours, because your device does the decryption. Your internet provider sees that you connect to that server and when. Shielding protects what is written on the chain, not the fact that you use SWARM.
- **An encrypted record is still a record.** Shielded notes stay on the chain for good, encrypted. Anyone who later holds your 24 recovery words, or a viewing key derived from them that you have shared, can read your history. The register is not burned; the key to it is in your hands. Keep the words on paper, offline.
- **No audit to point to.** No independent audit of the SWARM-specific changes has been published; the upstream components have their own security records.
- **Experimental.** SWARM mainnet has been live since 2 October 2026, 15:42 UTC. It is new software, and we would rather you read this list here than find it out later.

The code is public at github.com/Swarmcoin. The wallet for Windows, macOS and Linux is at swarm.green/ecosystem/wallet, with a SHA-256 checksum beside every file. Only download from swarm.green.

## What the three cases have in common

None of the people who built these records meant harm. The Amsterdam register was an ordinary piece of good administration. The US Census promised confidentiality and meant it. The German statisticians wanted better planning data. In each case the danger came later, from whoever held the record next, under rules nobody had voted for when the record was made.

The lesson we take is narrow. Not every record can be avoided, and some should not be. But a payment between two people does not need to be written into a permanent public register for the network to check that it is valid. When a system can verify without recording, the record that was never made is the only one nobody can misuse.

## Sources

- The attack on the Amsterdam population register, 27 March 1943, and the 15% figure: Anne Frank House, https://www.annefrank.org/en/timeline/128/the-resistance-attacks-the-population-register-of-amsterdam/
- The registry and identity cards: Verzetsmuseum (Dutch Resistance Museum), https://www.verzetsmuseum.org/en/kennisbank/armed-resistance-1 ; pointer with the identity-card rule, the trial, the executions and Arondeus' message: https://en.wikipedia.org/wiki/1943_Amsterdam_civil_registry_office_bombing
- Registration of Jews from January 1941 and the J stamp: United States Holocaust Memorial Museum podcast "12 Years That Shook the World", episode "Looking Danger in the Eye", https://www.ushmm.org/learn/podcasts-and-audio/12-years-that-shook-the-world/looking-danger-in-the-eye ; pointer for the date of the registration order: https://en.wikipedia.org/wiki/The_Holocaust_in_the_Netherlands
- About 104,000 of 140,000 Jews in the Netherlands did not survive (about 74%): Pim Griffioen and Ron Zeller, Anne Frank House, https://www.annefrank.org/en/anne-frank/go-in-depth/netherlands-greatest-number-jewish-victims-western-europe/
- The administration and the cooperation of Dutch officials: United States Holocaust Memorial Museum, Holocaust Encyclopedia, "The Netherlands", https://encyclopedia.ushmm.org/content/en/article/the-netherlands
- The US Census Bureau, the 2000 block-level finding and the 2007 discovery of the 4 August 1943 request: Scientific American, 30 March 2007, https://www.scientificamerican.com/article/confirmed-the-us-census-b/ ; ACLU, JACL and ADC statement, https://www.aclu.org/press-releases/aclu-jacl-and-adc-alarmed-census-violated-privacy-world-war-ii-urges-congress-ensure
- The census judgment of 15 December 1983, 1 BvR 209/83, English translation: Federal Constitutional Court of Germany, https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/EN/1983/12/rs19831215_1bvr020983en.html
- Clustering of addresses: Sarah Meiklejohn et al., "A Fistful of Bitcoins: Characterizing Payments Among Men with No Names", Internet Measurement Conference 2013, https://cseweb.ucsd.edu/~smeiklejohn/files/imc13.pdf
- What a shielded transaction shows: ZecHub, https://zechub.wiki/using-zcash/transactions
- What a light-wallet server learns: ZIP 307, "Light Client Protocol for Payment Detection", https://zips.z.cash/zip-0307
- SWARM facts, address formats and the three project addresses: https://swarm.green/what-is-swarm and https://swarm.green/verify ; source code: https://github.com/Swarmcoin
