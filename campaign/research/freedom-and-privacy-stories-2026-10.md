# Freedom and privacy story seeds for @swarm_coin (collected 2026-10-06)

Status: RESEARCH, nothing posted. Every seed below was checked against at least one web source on 2026-10-06; dates and figures come from those sources. Where a story is politically sensitive or a figure is disputed, the "Caution" line says so. Wikipedia links are pointers only; each seed also carries a primary or quality secondary source (court records, EFF, archives, museums, central banks, regulators, major newspapers).

How to use: one seed = one "why is ..." thread or carousel. Keep the hook on the human detail (a name, a date, a number), state the lesson in one line, and link the primary source in the last post. Voice rules in `../VOICE.md`; never use the seeds to attack a named living private person; keep partisan framing out (see cautions).

Groups: A cypherpunks and crypto wars, B whistleblowers and surveillance exposed, C censuses and registries abused, D money and freedom, E thinkers and arguments, F everyday and recent (2025-2026, all re-verified with 2025/2026 sources).

---

## A. Cypherpunks and the crypto wars

### A1. Phil Zimmermann, PGP and the book that beat export control
**Summary.** Phil Zimmermann released Pretty Good Privacy in 1991 as free software; when it spread outside the United States, US Customs opened a criminal investigation (1993) under the Arms Export Control Act, because strong encryption was classed as a munition. In 1995 MIT Press published the complete C source as a printed book, "PGP Source Code and Internals", because books enjoy First Amendment protection and could be exported legally; readers could scan the pages and recompile the program. On 11 January 1996 the Justice Department dropped the investigation without charges after three years. PGP became the most widely used e-mail encryption tool of the decade.
**Lesson.** Code is speech; when a government treats privacy tools as weapons, publishing in the open is the defence.
**Sources.** Zimmermann's own announcement: https://www.mit.edu/~prz/EN/news/PRZ_case_dropped.html ; his 1996 Senate testimony: https://www.mit.edu/~prz/EN/essays/Testimony.html ; The Register interview (2021): https://www.theregister.com/security/2021/06/08/cryptography-whizz-phil-zimmermann-looks-back-at-30-years-of-pretty-good-privacy/1503962 ; pointer: https://en.wikipedia.org/wiki/Phil_Zimmermann
**Caution.** None; well documented. Do not say he was "charged" (he never was).

### A2. Bernstein v. United States: a court says source code is speech
**Summary.** In 1995 mathematics student Daniel J. Bernstein wanted to publish "Snuffle", a small encryption program, plus a paper and instructions; the State Department told him all three were munitions under ITAR and needed an export licence. With the EFF he sued. On 6 May 1999 the Ninth Circuit (176 F.3d 1132) held that software source code is expression protected by the First Amendment and that the export rules were an unconstitutional prior restraint. The case helped force the loosening of US crypto export rules in 1999-2000.
**Lesson.** The right to publish mathematics is a free-speech right, and that is why strong cryptography is legal today.
**Sources.** EFF case page: https://www.eff.org/cases/bernstein-v-us-dept-justice ; opinion text: https://caselaw.findlaw.com/court/us-9th-circuit/1317290.html ; pointer: https://en.wikipedia.org/wiki/Bernstein_v._United_States
**Caution.** The panel opinion was later withdrawn for en banc review and the case ended on mootness after the rules changed; cite it as a landmark panel ruling, not as final Supreme Court law.

### A3. The Clipper chip: government key escrow, broken by one researcher
**Summary.** In April 1993 the Clinton administration announced the Clipper chip, an NSA-designed encryption chip for phones whose keys would be held in escrow by the government, using the classified Skipjack algorithm and a "Law Enforcement Access Field" (LEAF). In 1994 AT&T researcher Matt Blaze showed the LEAF's 16-bit checksum could be brute-forced, letting a user disable the escrow while keeping the encryption. Public opposition from industry and civil-liberties groups followed; by 1996 the programme was dead.
**Lesson.** A backdoor "only for the good guys" is a vulnerability for everyone, and the design that proves it was broken in a year.
**Sources.** EFF retrospective (2015): https://www.eff.org/deeplinks/2015/04/clipper-chips-birthday-looking-back-22-years-key-escrow-failures ; Crypto Museum: https://www.cryptomuseum.com/crypto/usa/clipper.htm ; Matt Blaze's blog: https://www.mattblaze.org/blog/mcconnell_clipper ; pointer: https://en.wikipedia.org/wiki/Clipper_chip
**Caution.** None.

### A4. Diffie, Hellman and the anonymous NSA letter (1976-77)
**Summary.** Whitfield Diffie and Martin Hellman published "New Directions in Cryptography" in IEEE Transactions on Information Theory in November 1976, introducing public-key cryptography to the open world. In July 1977 a letter signed "J. A. Meyer", giving only a home address, warned the IEEE that publishing cryptography research might violate ITAR arms-export law; Science magazine journalists found Meyer was an NSA employee. Hellman presented his students' work himself at a 1977 symposium so that only he, not they, risked prosecution. NSA director Bobby Inman later called the letter a personal initiative.
**Lesson.** Open cryptography was contested from its first year; the people who published anyway gave the world the tools that protect every online payment today.
**Sources.** Stanford Magazine "Keeping Secrets": https://stanfordmag.org/contents/keeping-secrets ; Hellman on the Meyer letter (Cryptome): https://cryptome.org/hellman/hellman-nsa.htm ; NSA FOIA documents: https://cryptome.org/0001/nsa-meyer.htm ; the paper: http://cr.yp.to/bib/1976/diffie.pdf
**Caution.** Whether the NSA ordered the letter is disputed (Inman denied it); say "an NSA employee wrote".

### A5. David Chaum: digital cash before the internet was ready
**Summary.** David Chaum described blind signatures in 1982 and patented them in 1983; they let a bank sign a coin without seeing it, so payments could be anonymous but unforgeable. He founded DigiCash in 1989 and launched eCash; in late 1995 Mark Twain Bank in St. Louis became the first bank to issue it. By 1998 the bank had enrolled only about 300 merchants and 5,000 users, DigiCash filed for bankruptcy that year, and the assets passed to eCash Technologies and later InfoSpace (2002).
**Lesson.** Private digital money was invented 27 years before Bitcoin; it failed on adoption, not on cryptography, which is why decentralised designs matter.
**Sources.** Bitcoin Magazine "Genesis Files" on eCash: https://bitcoinmagazine.com/culture/genesis-files-how-david-chaums-ecash-spawned-cypherpunk-dream ; Chaum's eCash 2.0 paper (with SNB co-author): https://chaum.com/wp-content/uploads/2022/11/eCash_2.0_9-7-22-.pdf ; pointer: https://en.wikipedia.org/wiki/DigiCash
**Caution.** Reasons for the failure are contested (Chaum's negotiating style vs. market timing); stick to dates and numbers.

### A6. Two manifestos: Tim May (1988/1992) and Eric Hughes (1993)
**Summary.** Timothy C. May drafted "The Crypto Anarchist Manifesto" in 1988 and circulated it on the cypherpunks list in November 1992, predicting that cryptography would let people transact without revealing identity. On 9 March 1993 Eric Hughes posted "A Cypherpunk's Manifesto", with the lines "Privacy is necessary for an open society in the electronic age. Privacy is not secrecy." and "Cypherpunks write code." The cypherpunks list, founded in 1992 by May, Hughes and John Gilmore, became the forum where Hashcash, b-money and later Bitcoin were announced.
**Lesson.** Privacy as "the power to selectively reveal oneself" was defined in 1993; the technology caught up later.
**Sources.** Hughes' manifesto (archive): https://www.elon.edu/u/imagining/expert_predictions/a-cypherpunks-manifesto/ ; Wired "Crypto Rebels" (1993): https://www.elon.edu/u/imagining/expert_predictions/crypto-rebels-11/ ; pointer: https://en.wikipedia.org/wiki/Timothy_C._May
**Caution.** May held hard-libertarian views; quote the manifesto lines on privacy, do not adopt his politics wholesale.

### A7. Hashcash, b-money, bit gold: the three ideas Bitcoin stood on
**Summary.** Adam Back proposed Hashcash in 1997 as a proof-of-work stamp against spam. In 1998 Wei Dai published "b-money" and Nick Szabo described "bit gold", both proposals for decentralised digital scarcity. The Bitcoin white paper (31 October 2008) cites Hashcash and b-money; bit gold is not cited. Dai later said Satoshi learned of b-money only after reinventing the idea and credited him at Back's suggestion.
**Lesson.** No single inventor: digital cash was a decade-long relay by people who published and refused to give up.
**Sources.** Bitcoin Magazine on Hashcash: https://bitcoinmagazine.com/culture/bitcoin-adam-back-and-digital-cash ; Wei Dai pointer: https://en.wikipedia.org/wiki/Wei_Dai ; History of bitcoin pointer: https://en.wikipedia.org/wiki/History_of_bitcoin
**Caution.** Do not speculate about who Satoshi is.

### A8. Satoshi's headline: 3 January 2009
**Summary.** Bitcoin's genesis block carries the text "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks", a front-page headline from that day's Times about Alistair Darling. It both timestamps the block and states the motive. On 12 January 2009 Satoshi sent 10 BTC to Hal Finney in block 170, the first transaction; the UK announced its second bank rescue package the same month.
**Lesson.** Bitcoin was born as a reply to bail-outs decided over people's heads.
**Sources.** Facsimile of the Times page: https://www.thetimes03jan2009.com/ ; explainer: https://www.lightspark.com/glossary/blockchain-genesis-block ; pointer: https://en.wikipedia.org/wiki/Bitcoin
**Caution.** None.

### A9. Hal Finney: "Running bitcoin"
**Summary.** Hal Finney, a PGP developer and cypherpunk who built the first reusable proof-of-work system in 2004, tweeted "Running bitcoin" on 11 January 2009 and received the first Bitcoin transaction (10 BTC) from Satoshi the next day. Diagnosed with ALS in 2009, he kept coding (including the bcflick wallet-hardening experiment) while paralysed, and wrote "Bitcoin and Me" in 2013. He died on 28 August 2014 and was cryopreserved.
**Lesson.** Privacy tools are built by people, often at great personal cost; Finney worked on them until he could only move his eyes.
**Sources.** CoinGecko profile: https://www.coingecko.com/learn/who-is-hal-finney-first-bitcoin-transaction ; pointer: https://en.wikipedia.org/wiki/Hal_Finney_(computer_scientist)
**Caution.** Do not imply he was Satoshi.

### A10. The Zcash ceremony (23 October 2016)
**Summary.** Zcash's zk-SNARK parameters required a one-time secret ("toxic waste") that, if kept, could forge coins. Zooko Wilcox organised a multi-party ceremony in October 2016 with six participants in different locations; as long as one destroyed their share honestly, the secret could not be reassembled. Participants bought fresh computers in person (a practice Snowden recommended), Peter Todd drove through the desert with his shard, and journalist Morgen Peck's reporting became Radiolab's episode "The Ceremony".
**Lesson.** Trust can be engineered away: good privacy systems are designed so even their makers cannot cheat.
**Sources.** Radiolab transcript: https://radiolab.org/podcast/ceremony/transcript ; Peter Todd's account: https://petertodd.org/2016/cypherpunk-desert-bus-zcash-trusted-setup-ceremony ; archive video: https://archive.org/details/youtube-D6dY-3x3teM
**Caution.** Later Zcash upgrades (Sapling, Halo/Orchard) removed the trusted setup; say "the 2016 ceremony", not "Zcash still relies on it".

---

## B. Whistleblowers and surveillance exposed

### B1. Edward Snowden, June 2013
**Summary.** On 5 June 2013 The Guardian published a secret FISA court order requiring Verizon to hand over the call records of millions of Americans; on 6 June The Guardian and Washington Post revealed PRISM, which drew data from Microsoft, Google, Apple and others; on 9 June Edward Snowden identified himself from Hong Kong. The disclosures led to the USA Freedom Act (2015) ending bulk domestic phone-record collection and to a rapid spread of end-to-end encryption.
**Lesson.** Mass surveillance was not a conspiracy theory; one person's documents proved it and changed the law.
**Sources.** Government Accountability Project timeline: https://whistleblower.org/snowden-timeline/ ; NBC timeline: https://www.nbcnews.com/feature/edward-snowden-interview/edward-snowden-timeline-n114871 ; pointer: https://en.wikipedia.org/wiki/Timeline_of_Snowden_disclosures
**Caution.** Snowden lives in Russia and took Russian citizenship; politically polarising, keep to the documents and legal outcomes.

### B2. The 1971 Media, Pennsylvania burglary that exposed COINTELPRO
**Summary.** On 8 March 1971, the night of the Ali-Frazier fight, eight activists calling themselves the Citizens' Commission to Investigate the FBI broke into the FBI office in Media, Pennsylvania and took more than 1,000 documents. Mailed to journalists, they revealed the FBI's secret COINTELPRO programme against civil-rights, anti-war and Black groups. Washington Post reporter Betty Medsger broke the story; the burglars were never caught and seven revealed themselves to her in 2014 in "The Burglary".
**Lesson.** Secret surveillance programmes were uncovered only because citizens took evidence out of a locked office.
**Sources.** Medsger collection, Bryn Mawr archives: https://archives.tricolib.brynmawr.edu/repositories/8/resources/10549 ; PBS NewsHour: https://www.pbs.org/newshour/show/unlikely-group-changed-face-fbi-retold-burglary ; pointer: https://en.wikipedia.org/wiki/Citizens'_Commission_to_Investigate_the_FBI
**Caution.** It was a crime; frame as civil disobedience with consequences, not a how-to.

### B3. The Church Committee (1975-76) and the letter to Martin Luther King
**Summary.** The Senate Select Committee chaired by Frank Church reviewed 110,000 documents and 800 witnesses and published a 2,702-page final report in 1976. It confirmed that COINTELPRO went far beyond the Media documents, that the NSA had intercepted Americans' telegrams, and that the FBI wiretapped and bugged Martin Luther King Jr. and sent him an anonymous letter urging him to kill himself. The findings led to the Foreign Intelligence Surveillance Act (1978).
**Lesson.** "If you have nothing to hide" fails the moment the watcher decides who is dangerous.
**Sources.** Senate citations list: https://www.senate.gov/about/resources/pdf/church-committee-full-citations.pdf ; Georgetown 50-year retrospective: https://college.georgetown.edu/news-story/why-the-church-committee-report-still-matters-50-years-later/
**Caution.** None.

### B4. Daniel Ellsberg and the Pentagon Papers
**Summary.** In 1971 RAND analyst Daniel Ellsberg gave the New York Times and Washington Post a 7,000-page secret history of the Vietnam War. In January 1973 he was charged under the Espionage Act with a maximum exposure of 115 years. On 11 May 1973 Judge William Byrne dismissed all charges because the government had burgled his psychiatrist's office, wiretapped him illegally and lost evidence.
**Lesson.** The state's answer to a leak was to spy on the leaker's therapist; privacy of the mind is the first casualty.
**Sources.** Trial chronology: https://famous-trials.com/ellsberg/277-chronology ; Free Speech Center: https://firstamendment.mtsu.edu/article/daniel-ellsberg/ ; pointer: https://en.wikipedia.org/wiki/Daniel_Ellsberg
**Caution.** None.

### B5. The Stasi: 189,000 informants and jars of smell
**Summary.** East Germany's Ministry for State Security employed about 91,000 full-time staff and ran roughly 189,000 unofficial informants in a country of 16 million, about one watcher per 57 citizens. It kept "smell samples" of suspects on cloth in sealed glass jars for tracker dogs, some taken by stealing underwear from homes. After 1990 the files (over 111 km of paper) were opened to citizens; the Stasi Records Archive joined the Federal Archives in 2021 and the jars are displayed in the Stasi Museum, Berlin.
**Lesson.** Total surveillance is not abstract: it is your neighbour, your spouse, and a jar with your scent in it.
**Sources.** German History in Documents and Images: https://germanhistorydocs.org/en/a-new-germany-1990-2023/individual-odor-samples-preserved-by-the-stasi-1990s ; Deutsches Spionagemuseum: https://www.deutsches-spionagemuseum.de/en/sammlung/odour-capture ; Harvard Magazine: https://www.harvardmagazine.com/2008/07/Harvard-author-spying-techniques-east-germany
**Caution.** Informant counts vary by year and definition (174,000-189,000); say "about 189,000 at its peak".

### B6. The Rosenholz files
**Summary.** The Rosenholz files are 381 CD-ROMs holding about 280,000 index-card records on sources, targets and officers of the Stasi's foreign arm (HVA). They reached the CIA in the chaos of reunification under circumstances still unclear, were used by the US alone, and were returned to Germany only in 2003 after years of negotiation; they have been requestable at the BStU since March 2004 and helped unmask NATO spy Rainer Rupp in 1993.
**Lesson.** Surveillance archives outlive the regime that built them and change hands; the data you give up is never only held by one state.
**Sources.** Macrakis et al., chapter in "East German Foreign Intelligence": https://www.taylorfrancis.com/chapters/mono/10.4324/9780203873021-13/ ; H-Net review: https://www.h-net.org/reviews/showrev.php?id=13987 ; pointer: https://en.wikipedia.org/wiki/Rosenholz_files
**Caution.** How the CIA obtained them is disputed (purchase vs. defector); say "under unclear circumstances".

### B7. Mark Klein and Room 641A
**Summary.** In January 2006 retired AT&T technician Mark Klein walked into the EFF's offices with documents showing that at 611 Folsom Street, San Francisco, fibre-optic splitters copied internet traffic into a locked NSA room, 641A. The EFF filed Hepting v. AT&T; Congress responded in 2008 with retroactive immunity for the telecoms. Klein died in 2025 aged 79.
**Lesson.** The copy of your traffic was made at the cable, not at your device; only encryption travels with the data.
**Sources.** EFF/Boing Boing account (2026): https://boingboing.net/2026/04/30/how-a-retired-technician-handed-eff-the-proof-of-nsa-mass-spying.html ; MIT Press Reader: https://thereader.mitpress.mit.edu/the-whistleblower-who-uncovered-the-nsas-big-brother-machine/ ; Hepting pointer: https://en.wikipedia.org/wiki/Hepting_v._AT%26T
**Caution.** None.

### B8. Katharine Gun and the UN spying memo (2003)
**Summary.** On 31 January 2003 GCHQ translator Katharine Gun saw an NSA e-mail from Frank Koza asking for a surveillance "surge" against six UN Security Council members (Angola, Bulgaria, Cameroon, Chile, Guinea, Pakistan) ahead of the Iraq vote. She leaked it to The Observer, which published on 2 March 2003. Charged under the Official Secrets Act in November 2003, she saw the case dropped in February 2004 after her defence demanded the Attorney General's legal advice on the war.
**Lesson.** Surveillance is used to bend votes, not only to catch criminals.
**Sources.** Al Jazeera, 25 Feb 2004: https://www.aljazeera.com/news/2004/2/25/uk-whistleblower-case-is-dropped ; Just Security analysis: https://www.justsecurity.org/64979/iraq-dirty-tricks-tale-gets-star-treatment-but-big-questions-remain/ ; pointer: https://en.wikipedia.org/wiki/Katharine_Gun
**Caution.** Iraq war context is politically charged; keep to the memo and the prosecution.

---

## C. Censuses and registries that were abused

### C1. The Amsterdam registry attack, 27 March 1943
**Summary.** The Dutch population registry recorded religion, which let the German occupiers identify Jews with deadly precision. On 27 March 1943 a resistance group led by sculptor Gerrit van der Veen and artist Willem Arondeus, dressed as police, overpowered the guards at the Amsterdam registry, drenched the card files and set explosives. Only about 15 percent of the records were destroyed; twelve participants, including Arondeus, were executed on 1 July 1943; van der Veen was shot in 1944. Arondeus' last message asked that people be told homosexuals were not cowards.
**Lesson.** A well-kept database became a kill list; the people who tried to destroy it are heroes today.
**Sources.** Anne Frank House timeline: https://www.annefrank.org/en/timeline/128/the-resistance-attacks-the-population-register-of-amsterdam/ ; Verzetsmuseum: https://www.verzetsmuseum.org/en/kennisbank/armed-resistance-1 ; USHMM podcast: https://www.ushmm.org/learn/podcasts-and-audio/12-years-that-shook-the-world/looking-danger-in-the-eye ; pointer: https://en.wikipedia.org/wiki/1943_Amsterdam_civil_registry_office_bombing
**Caution.** None; use the Netherlands' roughly 75 percent Jewish death rate only with a source if quoted.

### C2. IBM, Hollerith machines and the Nazi censuses
**Summary.** Edwin Black's "IBM and the Holocaust" (2001) documented how IBM's German subsidiary Dehomag supplied Hollerith punch-card machines used for the 1933 Prussian census and the 1939 Reich census, which recorded Jewish ancestry, and how Hollerith departments operated in concentration camps. Black argues the machines made the identification and logistics of persecution far faster.
**Lesson.** Data processing is neutral until a regime asks it who to find.
**Sources.** Pointer: https://en.wikipedia.org/wiki/IBM_and_the_Holocaust ; FindLaw review: https://supreme.findlaw.com/legal-commentary/ibm-and-the-holocaust.html ; historiography overview: https://explaininghistory.org/2025/09/30/ibm-and-the-holocaust-technology-as-a-force-multiplier-for-genocide/
**Caution.** DISPUTED. Historians Peter Hayes and Omer Bartov criticised the book as sloppy and speculative in its strongest claims (e.g., that camps "could not have processed" prisoners without IBM). State only the documented parts: Dehomag machines tabulated the censuses; camps had Hollerith departments. Do not claim IBM "ran the Holocaust".

### C3. The US census and Japanese-American internment (confirmed 2007)
**Summary.** In 2000 historian Margo Anderson and statistician William Seltzer showed the Census Bureau had supplied block-level data on Japanese Americans in 1942 to aid internment. In 2007 they found documents proving the Bureau also handed the Secret Service, on 4 August 1943, the names, addresses and citizenship status of Japanese Americans in the Washington, D.C. area. It was legal at the time because the Second War Powers Act (1942) had suspended census confidentiality; the Bureau formally apologised in 2000.
**Lesson.** A confidentiality promise is only as strong as the law in a crisis, and that law was switched off in weeks.
**Sources.** Scientific American: https://www.scientificamerican.com/article/confirmed-the-us-census-b/ ; Snopes fact check with the Seltzer-Anderson papers: https://www.snopes.com/fact-check/census-bureau-japanese-americans/ ; ACLU/JACL statement: https://www.aclu.org/press-releases/aclu-jacl-and-adc-alarmed-census-violated-privacy-world-war-ii-urges-congress-ensure
**Caution.** None if dated precisely (2000 for aggregates, 2007 for names).

### C4. Rwanda's ethnic ID cards (1933-1994)
**Summary.** In 1933 the Belgian colonial administration made every Rwandan carry an identity card marked Hutu, Tutsi or Twa, freezing categories that had been fluid. Independent Rwanda kept the ethnic line on the card. In April-July 1994 the card was the tool used at roadblocks: a "Tutsi" entry meant death. Ethnicity was removed from Rwandan ID cards only in 1997.
**Lesson.** An identity field added for administration sixty years earlier became the sorting mechanism of a genocide.
**Sources.** Prevent Genocide International, "Indangamuntu 1994": http://www.preventgenocide.org/edu/pastgenocides/rwanda/indangamuntu.htm ; Fussell, "Group Classification on National ID Cards": https://www.researchgate.net/publication/242603138 ; LSE International History: https://blogs.lse.ac.uk/lseih/2024/11/08/30-years-since-the-rwandan-genocide/
**Caution.** Handle with care; do not use for crypto point-scoring; credit the many causes (militias, radio, planning).

### C5. Germany's 1983 census boycott and "informational self-determination"
**Summary.** West Germany's planned 1983 "total census" asked about nationality, work and commuting, with data to be shared with local registries. Citizens' initiatives called for a boycott and several people lodged constitutional complaints. On 15 December 1983 the Federal Constitutional Court struck down parts of the Census Act and created the right to informational self-determination from Articles 1(1) and 2(1) of the Basic Law, stating that a society in which citizens cannot know who knows what about them is incompatible with that right.
**Lesson.** Privacy is a precondition of democracy, says Germany's highest court: people who fear being recorded stop exercising their freedoms.
**Sources.** Court's English summary: https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/EN/1983/12/rs19831215_1bvr020983en.html ; Deutschlandmuseum: https://www.deutschlandmuseum.de/en/history/calendar/1983-04-13-stop-the-census/
**Caution.** None.

---

## D. Money and freedom

### D1. Executive Order 6102: the 1933 gold call-in
**Summary.** On 5 April 1933 President Roosevelt ordered Americans to deliver gold coin, bullion and certificates to the Federal Reserve by 1 May 1933 at $20.67 per ounce, with exemptions for $100 in coin, jewellery and rare coins; violations carried up to $10,000 or ten years. The Gold Reserve Act of 30 January 1934 then set the price at $35, a 69 percent devaluation of the dollar against gold. Private gold ownership was fully legal again only on 31 December 1974.
**Lesson.** Even the world's richest democracy has confiscated its citizens' savings by decree; hard assets you cannot hide are assets you can lose.
**Sources.** Federal Reserve History on the Gold Reserve Act: https://www.federalreservehistory.org/essays/gold-reserve-act ; pointer: https://en.wikipedia.org/wiki/Executive_Order_6102
**Caution.** Few prosecutions occurred and compliance is debated; do not claim "all gold was seized".

### D2. The Bank Secrecy Act and California Bankers Assn v. Shultz (1970-74)
**Summary.** The Bank Secrecy Act of 1970 required banks to record customers' transactions and report cash movements above thresholds. Banks, the ACLU and depositors challenged it; on 1 April 1974 the Supreme Court upheld it (416 U.S. 21). Justice Douglas dissented that the grant of power to the Treasury was "too broad to pass constitutional muster", and Justice Marshall argued bank records are an extension of private property. Two years later, United States v. Miller (1976) held customers have no Fourth Amendment interest in their bank records at all.
**Lesson.** Financial privacy in the US was lost in a 1974 ruling, not in the digital age; every "know your customer" rule descends from it.
**Sources.** Opinion (Library of Congress scan): https://tile.loc.gov/storage-services/service/ll/usrep/usrep416/usrep416021/usrep416021.pdf ; FindLaw: https://caselaw.findlaw.com/court/us-supreme-court/416/21.html ; pointer: https://en.wikipedia.org/wiki/California_Bankers_Ass%27n_v._Shultz
**Caution.** None.

### D3. Operation Choke Point (2013-2017)
**Summary.** From 2013 the US Department of Justice, with the FDIC, pressured banks to drop merchants in categories labelled "high risk", including payday lenders, firearms and ammunition dealers and coin dealers, by threatening subpoenas and examinations. House Oversight staff reports in May and December 2014 documented the campaign and FDIC officials' personal animus; the DOJ formally ended it in August 2017.
**Lesson.** When regulators can de-bank a legal industry without a law or a court, access to money becomes a political favour.
**Sources.** House Oversight staff report (Dec 2014): https://oversight.house.gov/wp-content/uploads/2014/12/Staff-Report-FDIC-and-Operation-Choke-Point-12-8-2014.pdf ; Administrative Law Review analysis (Stevenson, 2023): https://administrativelawreview.org/wp-content/uploads/sites/2/2023/07/ALR-75.2_Stevenson.pdf
**Caution.** Partisan topic (the reports were Republican-led; Stevenson argues the programme was narrower than critics claim). Cite the documents, avoid "Obama did X" framing; the later "Choke Point 2.0" crypto label is an allegation, not a finding.

### D4. Canada 2022: 280 frozen accounts, ruled unlawful (2024, upheld 2026)
**Summary.** On 14 February 2022 Canada invoked the Emergencies Act against the trucker convoy; banks froze about 280 accounts on police-supplied lists, without court orders. On 23 January 2024 Federal Court Justice Richard Mosley ruled the invocation unreasonable and found the financial orders violated Charter section 8 by permitting unreasonable search and seizure of financial information and the freezing of accounts; he called the RCMP's lack of any standard before naming people "nothing short of alarming". On 16 January 2026 the Federal Court of Appeal unanimously upheld the ruling; the government announced in March 2026 it would seek leave to appeal to the Supreme Court.
**Lesson.** Account freezes without a judge happened in a G7 democracy and two courts later said they were unlawful; the money was still frozen when it mattered.
**Sources.** CBC on the 2024 ruling: https://www.cbc.ca/news/politics/emergencies-act-federal-court-1.7091891 ; CBC on the 2026 appeal ruling: https://www.cbc.ca/news/politics/convoy-protest-emergencies-act-appeal-9.7046769 ; Torys summary: https://www.torys.com/en/our-latest-thinking/publications/2024/01/federal-court-finds-emergencies-act-orders-exceed-governments-powers ; National Observer on the Supreme Court appeal: https://www.nationalobserver.com/2026/03/17/news/feds-appeal-use-emergencies-act-during-freedom-convoy-supreme-court
**Caution.** Politically polarising; the Rouleau public inquiry (2023) reached the opposite conclusion on the invocation. Report both the inquiry and the courts, do not endorse the protest.

### D5. Hong Kong 2019: cash for a single ride
**Summary.** During the 2019 protests, Hong Kong demonstrators queued at MTR ticket machines to buy single-journey tickets with cash rather than tap their Octopus cards, because card trip histories could place them at a protest; others left cash and spare clothes for strangers. Octopus cards are mostly anonymous but can be linked to credit cards, and police had used card data in earlier cases.
**Lesson.** When a payment leaves a trail, people under pressure go back to cash; privacy is what makes money usable in a crisis.
**Sources.** Hong Kong Free Press explainer: https://hongkongfp.com/2019/09/22/explainer-communist-partys-railway-hong-kongs-respected-mtr-fell-afoul-protesters/ ; BuzzFeed News: https://www.buzzfeednews.com/article/rosalindadams/hong-kong-mtr-protests ; pointer: https://en.wikipedia.org/wiki/Tactics_and_methods_surrounding_the_2019%E2%80%932020_Hong_Kong_protests
**Caution.** Politically sensitive (PRC); keep to the payment behaviour.

### D6. India's demonetisation, 8 November 2016
**Summary.** At 20:00 on 8 November 2016 India announced that Rs 500 and Rs 1,000 notes, about 86 percent of currency in circulation by value, would cease to be legal tender at midnight. Weeks of queues followed; reports counted over 80 deaths linked to the rush. The RBI's 2017-18 annual report found 99.3 percent of the Rs 15.41 trillion withdrawn had come back to banks, undermining the "black money" rationale.
**Lesson.** The state can switch off the money in your pocket overnight, and the people it hurts most are those with only cash.
**Sources.** The Wire on the RBI report: https://m.thewire.in/article/banking/rbi-says-99-3-of-scrapped-money-returned-to-the-banking-system ; Al Jazeera: https://www.aljazeera.com/amp/economy/2018/8/30/indias-banknote-recall-failed-to-uncover-black-money ; pointer: https://en.wikipedia.org/wiki/2016_Indian_banknote_demonetisation
**Caution.** Death figures are from press tallies, not official counts; say "reports counted".

### D7. Cyprus 2013: the bail-in
**Summary.** In March 2013 Cyprus accepted a 10 billion euro Troika bailout on condition that uninsured depositors absorb bank losses. Laiki Bank was wound down and about 47.5 percent of Bank of Cyprus deposits above 100,000 euros were converted into shares; roughly 8 billion euros of deposits were seized. Capital controls, including ATM limits of a few hundred euros a day, were imposed for two years.
**Lesson.** A bank deposit is a loan to the bank; in 2013 Europe showed it can be written down by decree.
**Sources.** Global Banking and Finance Review, "Bailing in depositors: lessons from Cyprus": https://www.globalbankingandfinance.com/bailing-in-depositors-lessons-from-cyprus ; Bellwether Research timeline: https://thebellwetherresearch.com/articles/cyprus-financial-crisis-2013.html ; pointer: https://en.wikipedia.org/wiki/Economy_of_Cyprus
**Caution.** Many large depositors were Russian; avoid nationality framing.

### D8. Greece 2015: 60 euros a day
**Summary.** After the Eurogroup refused to extend Greece's bailout, the government closed banks on 28 June 2015 and capped ATM withdrawals at 60 euros a day; banks reopened on 20 July, the weekly cap became 420 euros, and controls were fully lifted only on 1 September 2019.
**Lesson.** Four years of rationed access to your own salary, inside the euro area.
**Sources.** Al Jazeera, 29 June 2015: https://www.aljazeera.com/amp/economy/2015/6/29/greece-closes-banks-temporarily-as-crisis-deepens ; VOA on the end of controls (2019): https://www.voanews.com/a/europe_greece-ends-crisis-era-capital-controls/6174987.html ; pointer: https://en.wikipedia.org/wiki/Capital_controls_in_Greece
**Caution.** None.

### D9. Argentina's corralito, 1 December 2001
**Summary.** Economy minister Domingo Cavallo froze bank accounts on 1 December 2001, allowing 250 pesos (then 250 US dollars) a week in cash withdrawals to stop a run. Pot-banging protests (cacerolazos) and riots followed; President de la Rúa resigned on 20 December. In 2002 dollar deposits were forcibly converted to pesos at 1.40 while the market rate fell past 3, wiping out most of savers' value.
**Lesson.** "Your dollars are safe in the bank" lasted until the day the bank was told to stop paying them.
**Sources.** Buenos Aires Times retrospective: https://www.batimes.com.ar/news/argentina/argentines-recall-nations-worst-ever-crisis-20-years-on.phtml ; Warwick working paper on default and devaluation: https://warwick.ac.uk/fac/soc/pais/research/csgr/research/keytopic/global/millerapril04.pdf ; pointer: https://en.wikipedia.org/wiki/Corralito
**Caution.** Pesification rates varied by account type; say "about 1.40".

### D10. Venezuela: hyperinflation and the dollar as "escape valve"
**Summary.** The IMF estimated Venezuelan inflation at about 1.37 million percent for 2018 and projected 10 million percent for 2019; the bolivar lost over 99 percent of its value and was redenominated twice (2008, 2018) with a third in 2021. An Ecoanalítica survey of 12,600 transactions in seven cities found more than 56 percent were paid in foreign currency in October 2019 (86 percent in Maracaibo). In November 2019 President Maduro himself called dollarisation an "escape valve".
**Lesson.** People do not wait for permission to leave a failing currency; they move to whatever money they can hold themselves.
**Sources.** Ecoanalítica report: https://www.ecoanalitica.net/wp-content/uploads/WR_39_2019_14_11_eng.pdf ; Bloomberg on the IMF estimate: https://www.bloomberg.com/news/articles/2018-10-09/venezuela-s-2018-inflation-to-hit-1-37-million-percent-imf-says ; CNBC 2019: https://www.cnbc.com/2019/08/02/venezuela-inflation-at-10-million-percent-its-time-for-shock-therapy.html
**Caution.** Inflation estimates differ widely (IMF vs. Hanke's 80,000 percent for 2018); always name the source of the number.

### D11. Nigeria 2023: a cash shortage by design
**Summary.** In October 2022 the Central Bank of Nigeria announced redesigned 200, 500 and 1,000 naira notes with a 31 January 2023 deadline to swap old notes, weeks before the February election. New notes were scarce; people slept outside banks, protests turned violent and bank branches were attacked. Three state governors sued; on 3 March 2023 the Supreme Court held the policy unconstitutional as executed and kept the old notes legal tender until 31 December 2023.
**Lesson.** A "cashless" push imposed from above left millions unable to buy food; the court, not the central bank, restored their money.
**Sources.** Africanews on the Supreme Court ruling: https://www.africanews.com/2023/03/03/supreme-court-faults-president-buhari-on-naira-redesign-policy/ ; Quartz: https://qz.com/nigeria-naira-banknotes-supreme-court-ruling-1850177575 ; pointer: https://en.wikipedia.org/wiki/2023_Nigerian_currency_crisis
**Caution.** The policy's stated aims (vote-buying, counterfeiting) were legitimate; present the execution failure, not a conspiracy.

### D12. The WikiLeaks banking blockade (2010-12) and Bitcoin
**Summary.** Within days of Cablegate, PayPal (3-4 December 2010), then Visa and MasterCard (7 December), Bank of America and Western Union stopped processing donations to WikiLeaks without any court order. WikiLeaks said the blockade destroyed 95 percent of its revenue; its reserves fell from about $992,000 to under $124,000 by mid-2012. It began accepting Bitcoin in June 2011; Satoshi had posted in December 2010 asking WikiLeaks not to use Bitcoin yet because the project was too young.
**Lesson.** Payment companies can un-person an organisation in a week; neutral money is the answer to that power, whatever you think of the target.
**Sources.** WikiLeaks blockade page: https://wikileaks.org/Banking-Blockade.html ; Forbes, 7 Dec 2010: https://www.forbes.com/sites/andygreenberg/2010/12/07/visa-mastercard-move-to-choke-wikileaks/ ; Forbes 2012 on Bitcoin: https://www.forbes.com/sites/jonmatonis/2012/08/20/wikileaks-bypasses-financial-blockade-with-bitcoin/
**Caution.** WikiLeaks/Assange are polarising; the Satoshi "hornet's nest" post is from the bitcointalk forum (Dec 2010), link it directly if quoted.

### D13. Wörgl 1932: the town that printed its own money, and the bank that stopped it
**Summary.** On 31 July 1932, in the Depression, mayor Michael Unterguggenberger of Wörgl, Austria issued "labour certificates", local scrip that lost 1 percent of face value each month unless stamped, following Silvio Gesell's ideas. Unemployment fell and the town built roads, a bridge and a ski jump while the rest of Austria stagnated; Irving Fisher and French premier Daladier took note. On 1 September 1933 the Austrian National Bank had the scrip banned to protect its currency monopoly.
**Lesson.** A working alternative currency was shut down not because it failed but because it worked without the central bank.
**Sources.** Lietaer's annotated account: https://bernard-lietaer.org/wp-content/uploads/2022/07/2010-The-Worgl-Experiment-Austria-1932-1933-Lietaer-annotated.pdf ; Mises Institute critique: https://mises.org/library/free-money-miracle ; pointer: https://en.wikipedia.org/wiki/Worgl_Experiment
**Caution.** The economic "miracle" is disputed by both Austrian and mainstream economists; present the dates and the ban as fact, the effects as "reported".

### D14. Afghan women paid in Bitcoin (2013-2021)
**Summary.** Afghan entrepreneur Roya Mahboob, co-founder of the Digital Citizen Fund, began paying her female staff and students in Bitcoin from about 2013 because many could not open bank accounts and male relatives took cash wages; from 2016 her curriculum taught thousands of girls in Herat to use wallets. After the Taliban took Kabul in August 2021, several of these women used their holdings to fund their escape, as reported in 2021.
**Lesson.** Money a woman can hold on her phone, that no one else can see or seize, is freedom in the most literal sense.
**Sources.** Bitcoin Magazine: https://bitcoinmagazine.com/culture/bitcoin-financial-freedom-in-afghanistan ; IBTimes: https://www.ibtimes.com/afghan-tech-entrepreneur-uses-bitcoin-empower-women-2575881 ; pointer: https://en.wikipedia.org/wiki/Roya_Mahboob
**Caution.** Figures ("thousands") come from Mahboob and advocacy press; "Code to Inspire" is Fereshteh Forough's separate Herat coding school, which also used crypto payments; do not merge the two.

---

## E. Thinkers and arguments

### E1. Warren and Brandeis, "The Right to Privacy" (15 December 1890)
**Summary.** Boston lawyers Samuel Warren and Louis Brandeis published "The Right to Privacy" in the Harvard Law Review on 15 December 1890, arguing that "instantaneous photographs and newspaper enterprise have invaded the sacred precincts of private and domestic life" and that the common law should recognise a "right to be let alone". It is widely considered the founding text of privacy law in the United States.
**Lesson.** Every new recording technology has triggered a privacy fight; the 1890 version was the Kodak camera.
**Sources.** Full text: https://en.wikisource.org/wiki/The_Right_to_Privacy ; Brandeis School of Law collection: https://law.louisville.edu/lawlibrary/special-collections/louis-d-brandeis-collection/writings-louis-d-brandeis/right-privacy
**Caution.** None.

### E2. Brandeis' Olmstead dissent (1928) and Katz (1967)
**Summary.** In Olmstead v. United States (4 June 1928) the Supreme Court held 5-4 that warrantless wiretapping of a bootlegger did not violate the Fourth Amendment because nothing physical was searched. Justice Brandeis dissented that the framers "conferred, as against the Government, the right to be let alone, the most comprehensive of rights", and warned that future technology would allow the government to reach into the home without entering it. Katz v. United States (1967) overruled Olmstead and adopted his view.
**Lesson.** The argument that surveillance of signals is not a "search" was wrong in 1928 and took 39 years to overturn.
**Sources.** National Constitution Center: https://constitutioncenter.org/blog/olmstead-case-was-a-watershed-for-supreme-court ; pointer with opinion links: https://en.wikipedia.org/wiki/Olmstead_v._United_States
**Caution.** None.

### E3. Orwell's Nineteen Eighty-Four and where it came from
**Summary.** George Orwell wrote Nineteen Eighty-Four on the island of Jura while ill with tuberculosis; it was published on 8 June 1949. Room 101 took its name from a BBC conference room where he endured meetings during his 1941-43 propaganda work; the Ministry of Truth was modelled on Senate House, London, wartime home of the Ministry of Information. The book gave English "Big Brother", "thought police" and "doublethink".
**Lesson.** The telescreen was fiction in 1949; the author built it from real offices he had worked in.
**Sources.** Orwell Foundation: https://www.orwellfoundation.com/the-orwell-foundation/orwell/books-by-orwell/nineteen-eighty-four/ ; Camden New Journal on Senate House: https://www.camdennewjournal.co.uk/article/prophet-warning
**Caution.** The Room 101 origin is Orwell biographers' account, not documented by Orwell himself; say "reportedly".

### E4. Bentham's Panopticon (1787) and Foucault (1975)
**Summary.** Jeremy Bentham described the Panopticon in letters written in 1787: a circular prison with a central tower from which a guard could see every cell while remaining unseen, so inmates would behave as if always watched. Michel Foucault's "Discipline and Punish" (1975) made it the model of modern disciplinary power: surveillance that is "visible and unverifiable" makes people police themselves.
**Lesson.** You do not need to be watched all the time; you only need to believe you might be.
**Sources.** The Conversation on Discipline and Punish at 50: https://theconversation.com/a-dark-masterpiece-foucaults-discipline-and-punish-at-50-246245 ; PolSci Institute summary: https://polsci.institute/western-political-thought/panopticon-jeremy-bentham-surveillance-control/
**Caution.** None.

### E5. Hannah Arendt: the private realm as shelter
**Summary.** In "The Human Condition" (1958) Hannah Arendt argued that a private realm hidden from public view is necessary for a person to have depth, and that the modern "social" realm erodes both private and public life. In "The Origins of Totalitarianism" (1951) she described how terror leaves "no space for private life" and how organised loneliness prepares people for total domination.
**Lesson.** Without a private space there is no self to bring into public life; totalitarianism starts by abolishing it.
**Sources.** Aeon essay on Arendt and loneliness: https://aeon.co/essays/for-hannah-arendt-totalitarianism-is-rooted-in-loneliness ; The Human Condition (text): https://www.frontdeskapparatus.com/files/arendt.pdf
**Caution.** Quote only lines verifiable in the text; Arendt is often misquoted online.

### E6. UDHR Article 12 (10 December 1948)
**Summary.** Article 12 of the Universal Declaration of Human Rights, adopted by the UN General Assembly on 10 December 1948, states: "No one shall be subjected to arbitrary interference with his privacy, family, home or correspondence, nor to attacks upon his honour and reputation. Everyone has the right to the protection of the law against such interference or attacks." Correspondence includes letters, calls and, by modern reading, messages.
**Lesson.** Privacy is not a niche preference; it has been a universal human right on paper since 1948.
**Sources.** OHCHR text: https://www.ohchr.org/sites/default/files/UDHR/Documents/UDHR_Translations/eng.pdf ; Utrecht University explainer: https://www.uu.nl/en/education/universal-declaration-of-human-rights-75-years/udhr-in-words-and-images/udhr-articles-1-30/article-12-privacy
**Caution.** None.

### E7. Glenn Greenwald's challenge: "send me your passwords" (TEDGlobal, October 2014)
**Summary.** In his TED talk "Why privacy matters" (Rio de Janeiro, October 2014) Glenn Greenwald answered "I have nothing to hide" with a standing offer: e-mail him all your e-mail and social-media passwords so he can browse. "I've not had one single person send me them." He also quoted Google's Eric Schmidt ("if you have something you don't want anyone to know, maybe you shouldn't be doing it") and noted Schmidt's company had blacklisted CNET for publishing his own public data.
**Lesson.** Everyone has something to hide; the people who deny it still lock their doors.
**Sources.** TED: https://www.ted.com/talks/glenn_greenwald_why_privacy_matters ; The Intercept: https://theintercept.com/2014/10/10/privacy-matters-ted-talk/
**Caution.** Greenwald is politically polarising; cite the argument, not the person.

### E8. Daniel Solove, "I've Got Nothing to Hide" (2007)
**Summary.** Law professor Daniel Solove's essay in the San Diego Law Review (vol. 44, 2007) dissects the "nothing to hide" argument: it assumes privacy is only about hiding bad things, ignores aggregation (harmless facts combine into a profile), exclusion (you cannot see or correct what is held about you) and the chilling of lawful behaviour. The essay became the 2011 book "Nothing to Hide".
**Lesson.** The harm of surveillance is not exposure of a secret; it is power over you built from facts you never chose to share.
**Sources.** GWU scholarship copy: https://scholarship.law.gwu.edu/cgi/viewcontent.cgi?article=1159&context=faculty_publications ; pointer: https://en.wikipedia.org/wiki/Nothing_to_Hide_(book)
**Caution.** None.

### E9. Bruce Schneier, "The Eternal Value of Privacy" (Wired, 18 May 2006)
**Summary.** Schneier argued privacy is a basic human need, not a cover for wrongdoing, and quoted the line attributed to Cardinal Richelieu: give me six lines by the most honest man and I will find something to hang him. "Watch someone long enough, and you'll find something to arrest, or just blackmail, with."
**Lesson.** The question is not whether you have something to hide but whether someone with power over you wants to find it.
**Sources.** Schneier's archive: https://www.schneier.com/essays/archives/2006/05/the_eternal_value_of.html
**Caution.** The Richelieu quote is attributed, not documented; say "attributed to".

### E10. Jonathon Penney: the measurable chilling effect (2016)
**Summary.** Jonathon Penney's study "Chilling Effects: Online Surveillance and Wikipedia Use" (Berkeley Technology Law Journal 31:1, 2016) examined traffic to 48 Wikipedia articles on terrorism-related topics and found an immediate drop of about 20 percent after the June 2013 Snowden revelations, with a sustained decline afterwards (press summaries cite "nearly 30 percent").
**Lesson.** When people learn they are watched, they stop reading; surveillance costs knowledge even when it never arrests anyone.
**Sources.** Paper: https://digitalcommons.schulichlaw.dal.ca/scholarly_works/268/ ; SSRN: https://www.ssrn.com/abstract=2769645 ; BTLJ note: https://btlj.org/2016/05/5075/
**Caution.** Quote the paper's own figures; press versions round differently.

### E11. Cambridge Analytica (March 2018)
**Summary.** On 17 March 2018 whistleblower Christopher Wylie told The Observer and the New York Times how Cambridge Analytica had obtained Facebook profile data via a personality-quiz app; Facebook later put the number at up to 87 million users. In July 2019 the US FTC fined Facebook a record $5 billion for privacy violations. Cambridge Analytica closed in May 2018.
**Lesson.** Data collected "for research" was used to target voters; consent you gave once did not travel with the data.
**Sources.** CNBC on the FTC fine: https://www.cnbc.com/2019/07/12/ftc-fines-facebook-5-billion-for-privacy-lapses.html ; Hu, "Cambridge Analytica's black box" (Big Data & Society, 2020): https://journals.sagepub.com/doi/full/10.1177/2053951720938091
**Caution.** The effectiveness of the targeting on election outcomes is disputed; do not claim it "won" any vote.

---

## F. Everyday and recent (all verified with 2025-2026 sources)

### F1. Sweden: the cashless pioneer asks for cash back
**Summary.** Sweden is the most cashless economy in Europe: the Riksbank's Payments Report 2025 says about 10 percent of in-store purchases are made in cash. In December 2024 a government "Cash Inquiry" proposed obliging sellers of essential goods (food, pharmacies, fuel, healthcare) to accept cash, and in 2025 the Riksbank backed legislation. Governor Erik Thedéen: "People should always be able to pay for food, healthcare and medicines both digitally and with cash." The stated reasons are inclusion and emergency preparedness, since cash works without power or networks.
**Lesson.** The country that nearly abolished cash concluded that money which needs a server is a national-security risk.
**Sources.** Riksbank Payments Report 2025: https://www.riksbank.se/globalassets/media/rapporter/betalningsrapport/2025/engelsk/payments-report-2025.pdf ; Riksbank page "Cash use continues to decline": https://www.riksbank.se/en-gb/payments--cash/payments-in-sweden/payments-report-2025/trends-on-the-payments-market/the-swedish-payments-market-is-almost-entirely-digital/cash-use-continues-to-decline/ ; Central Banking: https://www.centralbanking.com/central-banks/currency/7972908/riksbank-everyone-should-be-able-to-pay-in-cash
**Caution.** "Reversal" is an interpretation; the Riksbank frames it as securing a cash floor, not reversing digitalisation.

### F2. EU AMLR: 10,000 euro cash cap and the end of anonymous crypto accounts (10 July 2027)
**Summary.** Regulation (EU) 2024/1624 (AMLR) applies from 10 July 2027. Article 80 caps cash payments to businesses at 10,000 euros EU-wide (member states may set lower limits). Crypto-asset service providers may not offer anonymous accounts or wallets, and may not handle "anonymity-enhancing coins" (privacy coins); identity checks apply to occasional crypto transactions from 1,000 euros. The new authority AMLA will directly supervise up to 40 large cross-border entities from 2027-28.
**Lesson.** From 2027 Europe's exchanges are forbidden to touch private coins; privacy will have to live in self-custody.
**Sources.** The Defiant: https://thedefiant.io/news/regulation/eu-aml-rules-to-ban-anonymous-accounts-privacy-coins ; Tech Law Policy explainer (June 2025): https://techlawpolicy.com/2025/06/eu-vs-crypto-anonymity-what-you-need-to-know/ ; cash cap (Crypto Briefing): https://cryptobriefing.com/eu-impose-10-000-euros-cash-cap-july-2027-new-aml-regulation/ ; EVZ country overview: https://www.evz.de/en/topics/banking-finance/cash-payment-limits/ ; regulation text: EUR-Lex 32024R1624
**Caution.** The ban hits regulated service providers, not holding or peer-to-peer use; "EU bans privacy coins" is an over-statement, say "bans them from exchanges".

### F3. Chat control: the EU almost mandated scanning of encrypted messages
**Summary.** The Commission's Child Sexual Abuse Regulation (proposed 11 May 2022) would have let authorities order messaging services to scan private messages, including end-to-end encrypted ones. In July 2025 the Danish Council presidency revived mandatory detection orders; Germany joined a blocking minority and the plan was pulled from a vote in October 2025. On 26 November 2025 the Council agreed a position centred on voluntary detection and risk mitigation, dropping mandatory scanning but adding age-verification duties; trilogues with Parliament follow.
**Lesson.** Encryption survived in Europe in 2025 by a handful of votes; the proposal will be back.
**Sources.** eucrim on the Council position: https://eucrim.eu/news/csa-regulation-council-position-reached/ ; EDRi document pool: https://edri.org/our-work/csa-regulation-document-pool/ ; TechRadar: https://www.techradar.com/vpn/vpn-privacy-security/chat-control-eu-lawmakers-finally-agree-on-the-voluntary-scanning-of-your-private-chats ; pointer: https://en.wikipedia.org/wiki/Chat_Control
**Caution.** Child-protection framing is sensitive; acknowledge the aim, criticise the method.

### F4. UK Online Safety Act: age checks and a 1,400 percent VPN spike (July 2025)
**Summary.** Age-verification duties under the UK Online Safety Act took effect on 25 July 2025, requiring adult and some social sites to verify ages with ID, face estimation or bank data. Proton VPN reported an hourly sign-up rise of 1,400 percent on the day and sustained increases of about 1,800 percent; NordVPN reported a 1,000 percent purchase spike; VPN apps filled half of the UK App Store's top ten free apps.
**Lesson.** Tell people to upload ID to read the internet and they will route around you within hours.
**Sources.** ITV News: https://www.itv.com/news/2025-07-28/vpn-downloads-spike-as-uk-introduces-age-checks-for-adult-online-content ; Tom's Guide on Proton's numbers: https://www.tomsguide.com/uk/computing/vpns/major-vpn-provider-sees-a-huge-spike-in-sign-ups-as-age-verification-law-comes-into-effect-in-the-uk ; Slashdot roundup: https://news.slashdot.org/story/25/07/27/1957211/vpn-downloads-surge-in-uk-as-new-age-verification-rules-take-effect
**Caution.** VPN figures are company-reported.

### F5. Flock cameras: towns pull the plug (2025-26)
**Summary.** Flock Safety's automatic licence-plate readers photograph every passing car and share hits across a national network. From 2025 revelations that federal agencies, including Border Patrol, had searched local data without local consent, plus cases of officers using ALPRs to stalk ex-partners, triggered cancellations; the ACLU's "Get the Flock Out" campaign and local votes have led dozens of cities in over 20 states to cancel, reject or deactivate systems, with a 2026 tracker counting well over 50 jurisdictions.
**Lesson.** A camera that logs everyone to find someone builds a movement database by default; local councils are the ones switching it off.
**Sources.** ACLU campaign: https://www.aclu.org/campaigns-initiatives/get-the-flock-out ; Houston Chronicle map (2026): https://www.houstonchronicle.com/projects/2026/flock-camera-votes-map/ ; NewsNation: https://www.newsnationnow.com/politics/flock-contract-cancellations-grow/ ; Newsweek map: https://www.newsweek.com/map-cities-rejected-deactivated-flock-cameras-12253499
**Caution.** Cancellation counts differ by tracker (54 to "over 200" depending on definition and date); cite the tracker you use.

### F6. Period-tracking apps after Dobbs (2022)
**Summary.** After the US Supreme Court's Dobbs decision (24 June 2022) ended the federal right to abortion, privacy groups warned that period and fertility apps, search and location data could be subpoenaed in states that criminalised abortion. The FTC had already settled with Flo Health (finalised 22 June 2021) for sharing users' health data with Facebook, Google and analytics firms despite privacy promises; in July 2022 the FTC pledged to pursue misuse of health and location data, and several apps added anonymous modes.
**Lesson.** Data that felt harmless when collected became evidence when the law changed; collect less, encrypt the rest.
**Sources.** Engadget on the FTC pledge: https://www.engadget.com/ftc-responds-abortion-data-privacy-legal-authorities-030247915.html ; Flo settlement (National Law Review): https://natlawreview.com/article/privacy-tip-267-fertility-tracking-app-settles-ftc ; Columbia STLR blog: https://journals.library.columbia.edu/index.php/stlr/blog/view/660
**Caution.** Abortion is politically charged; keep to the data-protection point.

### F7. Tornado Cash: sanctions imposed 2022, lifted 21 March 2025
**Summary.** OFAC sanctioned the Tornado Cash smart contracts on 8 August 2022, the first time code rather than people was listed. Six users backed by Coinbase sued; in November 2024 the Fifth Circuit held immutable smart contracts are not "property" that can be sanctioned, and on 21 March 2025 Treasury removed Tornado Cash from the SDN list. Developer Roman Semenov remained listed.
**Lesson.** A US court said open-source code cannot be sanctioned; the case is the legal floor under every privacy protocol.
**Sources.** Venable analysis (April 2025): https://www.venable.com/insights/publications/2025/04/a-legal-whirlwind-settles-treasury-lifts-sanctions ; DeFi Education Fund: https://www.defieducationfund.org/treasury-department-officially-delists-sanctions-on-tornado-cash/ ; Potomac Law: https://www.potomaclaw.com/news-US-Sanctions-on-Crypto-Company-Withdrawn-Following-Ruling-on-Statutory-Authority
**Caution.** Treasury framed the delisting as discretionary after "review", and North Korea's Lazarus Group did launder through the mixer; state both.

### F8. Roman Storm: partial verdict, 6 August 2025
**Summary.** Tornado Cash co-founder Roman Storm went on trial in Manhattan on 14 July 2025. On 6 August 2025, after four days of deliberation and an Allen charge from Judge Katherine Polk Failla, the jury convicted him of conspiracy to operate an unlicensed money-transmitting business (max. five years) and hung on money laundering and sanctions conspiracy. Prosecutors have not dropped the hung counts; a retrial date has been reported for 2027 while an acquittal motion is pending.
**Lesson.** A developer was convicted for writing software others used; whether code authors are "money transmitters" is now the central legal fight for privacy tech.
**Sources.** CryptoSlate: https://cryptoslate.com/jury-convicts-roman-storm-on-unlicensed-money-transmission-hung-on-laundering-not-guilty-on-sanctions/ ; Bitcoin Magazine: https://bitcoinmagazine.com/news/tornado-cash-trial-concludes-roman-storm-found-guilty-of-one-of-three-counts ; Kelman Law analysis: https://kelman.law/roman-storms-tornado-cash-verdict-what-it-means-for-crypto/
**Caution.** Live case; re-check the docket (S.D.N.Y. 1:23-cr-00430) before posting any status line; say "hung" not "acquitted" on the two counts.

### F9. Samourai Wallet: guilty pleas and prison (2025)
**Summary.** Keonne Rodriguez and William Lonergan Hill, developers of the Samourai Wallet Bitcoin mixer, were arrested in April 2024. In July 2025 both pleaded guilty to conspiracy to operate an unlicensed money-transmitting business; Rodriguez was sentenced to five years on 6 November 2025 and Hill to four years on 19 November 2025, each with three years' supervised release, $250,000 fines and about $238 million in forfeiture combined. Prosecutors said the service processed more than $237 million in criminal proceeds.
**Lesson.** Non-custodial privacy software was prosecuted as money transmission; the line between tool-maker and operator is being drawn in court.
**Sources.** IRS-CI press release: https://www.irs.gov/compliance/criminal-investigation/founders-of-samourai-wallet-cryptocurrency-mixing-service-sentenced-to-five-and-four-years-in-prison ; The Record: https://therecord.media/samourai-wallet-crypto-mixer-founders-sentenced ; pointer: https://en.wikipedia.org/wiki/Samourai_Wallet
**Caution.** They admitted knowingly serving criminal users; do not paint them as innocent, frame the legal theory as the issue.

### F10. Dubai bans privacy coins from licensed venues (effective 12 January 2026)
**Summary.** Dubai's Virtual Assets Regulatory Authority first prohibited "anonymity-enhanced cryptocurrencies" in its February 2023 rulebook. Updated rules effective 12 January 2026 reinforced a categorical ban on issuing, listing or facilitating Monero, Zcash and similar coins, and on mixers, for all licensed providers in Dubai including the DIFC; platforms set deadlines around 31 March 2026 for users to withdraw or convert. Self-custody is not banned.
**Lesson.** The world's most crypto-friendly hub drew the line at privacy; privacy coins will be held, not traded, in Dubai.
**Sources.** Elliptic on the 2023 rulebook: https://www.elliptic.co/blog/analysis/crypto-regulatory-affairs-dubai-s-vara-rolls-out-digital-asset-regs-includes-privacy-coin-ban ; Bankless Times (12 Jan 2026): https://www.banklesstimes.com/articles/2026/01/12/dubai-bans-privacy-tokens-tightens-stablecoins-rules/ ; Bitcoin.com News: https://news.bitcoin.com/from-surge-to-shutdown-dubai-blocks-privacy-coins-in-2026/
**Caution.** Confirm the exact VARA rulebook citation before quoting; secondary press only so far.

### F11. Dash adopts Zcash's Orchard (July 2026)
**Summary.** In February 2026 Dash announced it would integrate Zcash's Orchard shielded pool (Halo 2, no trusted setup) into its Evolution chain; shielded transactions went live on the Dash Evolution mainnet in July 2026 (Dash's announcement of 4 August 2026 describes a five-month build, February to July). Dash reports about one-second settlement and 20-second wallet sync, and says it shipped a version without the inflation bug found in an earlier Orchard implementation.
**Lesson.** Zcash's cryptography is becoming the shared standard for shielded value across chains; the market is choosing shielded pools.
**Sources.** Dash announcement: https://www.dash.org/news/shielded-transactions-are-live-on-the-dash-evolution-mainnet/ ; Cryptopolitan: https://www.cryptopolitan.com/dash-launch-zcash-orchard-technology/ ; BingX (Feb 2026 plan): https://bingx.com/en/news/post/dash-evolution-to-add-zcash-s-orchard-pool-march-launch-after-audits
**Caution.** Technical claims are Dash's own; the "inflation bug" reference should be checked against the Zcash disclosure before repeating. Relevant to SWARM since SWARM also uses Orchard-class shielded pools; never say "a copy of Zcash".

### F12. Canada's account freezes ruled unlawful (see D4)
Cross-reference for recency: Federal Court of Appeal, 16 January 2026; Supreme Court leave sought March 2026. Use D4 text.

---

## Notes for the writers
- Numbers that differ between sources (Stasi informants, Venezuelan inflation, Flock cancellations, Indian demonetisation deaths) must be attributed to a named source in the post.
- Live legal cases (Storm, Canada at the Supreme Court) need a date check on the day of posting.
- Politically charged items (Snowden, Canada 2022, Hong Kong, Choke Point, Dobbs, chat control) go out as privacy stories with both sides' stated aims named; no partisan endorsement.
- The disputed item (IBM and the Holocaust) should only be used with the caution wording in C2.
- Do not post any of this; it is a research collection for the owner's review.
