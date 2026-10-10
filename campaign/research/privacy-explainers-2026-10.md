# Privacy explainer seeds for @swarm_coin (October 2026)

Status: RESEARCH BANK, verified 2026-10-06, nothing posted. Forty seeds for educational X posts. Each seed teaches one idea, carries one concrete number or example, names one common misconception, and links one or two sources (primary or reputable; Wikipedia only paired with a primary). Posts drawn from this bank must teach, not sell: SWARM is mentioned only where the mechanism is literally the one SWARM runs (the Zcash protocol stack, a Signal-based messenger, an ungoogled-chromium browser), and never as a reason to buy anything.

How to use: pick a seed, cut the explanation to post length, keep the number and the misconception, link one source. Where a figure is contested or moving, the seed says so; re-check live figures (shielded-pool size, HIBP totals) on the day of posting. Figures in this file were read on 2026-10-06 unless the seed gives another date.

Writing rules carried over from `campaign/VOICE.md`: plain language, one idea per post, name the network beside every chain number, no "testnet" wording in outward posts, no price talk.

---

## Part 1: Technology (16 seeds)

### 1. A zero-knowledge proof: the Ali Baba cave

**The one idea:** you can prove you know a secret without revealing it.

Picture a ring-shaped cave with a magic door at the far end that only opens to a secret word. Peggy walks in and takes the left or right branch; Victor, who waited outside, then shouts which side she must come out of. If she knows the word she can always comply, because the door lets her cross. If she is bluffing she guesses right half the time. Repeat twenty rounds and a bluffer survives with odds of about one in a million (2^-20). Victor ends up convinced, yet he never hears the word and could not convince anyone else. That is the shape of every zero-knowledge proof: convince, reveal nothing extra. Shielded transactions on the Zcash protocol stack use the same idea to prove "this spend is valid, inputs equal outputs, I own these funds" without publishing sender, receiver or amount.

**Number:** 20 rounds, bluffing odds about 1 in 1,048,576. The cave story is from Quisquater, Guillou et al., CRYPTO 1989, pages 628–631.

**Common misconception:** "zero knowledge" means the transaction is hidden from the network. It means the verifier learns nothing beyond the fact that the statement is true; the network still checks every proof.

**Sources:** https://link.springer.com/chapter/10.1007/0-387-34805-0_60 ; https://en.wikipedia.org/wiki/Zero-knowledge_proof

### 2. What a hash is, and why a SHA-256 checksum catches tampering

**The one idea:** a hash is a fixed-length fingerprint of data that changes completely when one bit changes.

SHA-256 takes any input, a one-line note or a 200 MB installer, and produces 256 bits, usually shown as 64 hexadecimal characters. Two properties matter for everyday use. It is one-way: nobody can run it backwards to recover the file. And it is unforgiving: flip one bit in the input and, on average, about half of the output bits change, so the old and new fingerprints look unrelated. A download page therefore publishes the expected hash; you compute the hash of what you actually got; if the two strings differ, the file is not the one the publisher built, whether that is due to a corrupt download or a swapped binary. Blockchains use the same primitive to chain blocks together and to commit to transactions.

**Number:** SHA-256 output is always 256 bits (64 hex characters) regardless of input size. The algorithm is specified in NIST FIPS 180-4.

**Common misconception:** hashing is a form of encryption. Encryption is reversible with a key; a hash has no key and cannot be reversed.

**Sources:** https://csrc.nist.gov/pubs/fips/180-4/upd1/final ; https://en.wikipedia.org/wiki/SHA-2

### 3. Why 24 words are a whole wallet (BIP-39)

**The one idea:** the recovery phrase is not a password to your wallet; it is the wallet.

A BIP-39 phrase starts as random entropy. For a 24-word phrase that is 256 bits, plus an 8-bit checksum, giving 264 bits; split into 24 chunks of 11 bits, each chunk indexes one of 2,048 words. From those words the wallet derives a seed and, from the seed, every private key, every address and every viewing key it will ever use, in a fixed order. Nothing else is needed: no app, no account, no server. Anyone who reads the words can rebuild the wallet on any device and spend everything. Anyone who loses them has lost the wallet permanently, because there is no company holding a copy. That is why the phrase is written down offline and never typed into a website.

**Number:** 2,048-word list; 24 words encode 256 bits of entropy plus an 8-bit checksum (264 = 24 × 11).

**Common misconception:** the app's PIN or password protects the funds. It only protects the local copy on that device; the words protect the money.

**Sources:** https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki ; https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki

### 4. Public-key cryptography, explained with paint

**The one idea:** two people can agree on a secret in public without anyone listening being able to compute it.

Alice and Bob agree in the open on a common colour, say yellow. Each privately picks a secret colour and mixes it into the yellow, then they swap the mixtures in public. Each now adds their own secret colour to the mixture they received. Both end with the same final shade, because the same three colours went in; an eavesdropper has only the yellow and the two intermediate mixtures, and unmixing paint is hard. Diffie and Hellman published the mathematical version in 1976, and every encrypted chat, every HTTPS connection and every shielded payment starts with a key agreement of this kind. A wallet address contains public key material; a sender uses it to encrypt a note that only the holder of the matching private key can open.

**Number:** "New Directions in Cryptography" appeared in IEEE Transactions on Information Theory in November 1976.

**Common misconception:** public keys must be kept secret too. Publishing the public key is the point; only the private key stays private.

**Sources:** https://ee.stanford.edu/~hellman/publications/24.pdf ; https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

### 5. What end-to-end encryption does and does not protect

**The one idea:** end-to-end encryption hides what you said, not that you said it.

With end-to-end encryption only the two endpoints hold the keys, so the server in the middle relays ciphertext it cannot read. That is a real protection: a breach of the server, a subpoena to the operator or a tap on the wire yields no message content. What remains visible is metadata: which account talked to which, when, how often, how large the messages were, and from which IP address. EFF's examples show why that matters: "you called the suicide prevention hotline from the Golden Gate Bridge" is metadata, and so is a call to a clinic followed by a call to a support group. Good messengers shrink metadata (Signal's sealed sender, minimal server logs), but no app can encrypt the fact that two phones exchanged packets.

**Number:** three fields, sender, receiver, time, are enough to build a social graph; none of them is message content.

**Common misconception:** "encrypted" equals "anonymous". Encryption protects content; anonymity would require hiding who is talking, which is a separate and harder problem.

**Sources:** https://ssd.eff.org/module/why-metadata-matters ; https://ssd.eff.org/module/what-should-i-know-about-encryption

### 6. The Signal double ratchet in one paragraph

**The one idea:** every message gets a fresh key, and stolen keys stop working almost immediately.

Signal's double ratchet runs two gears at once. The symmetric ratchet turns one step per message: each message key is derived from a chain key, the chain key is advanced, and the old one is thrown away, so a key captured later cannot decrypt earlier messages (forward secrecy). The Diffie-Hellman ratchet turns once per round trip: every reply carries a new public key, and both sides mix the new shared secret into their chains, so an attacker who copied the state at one moment is locked out again after the next exchange (post-compromise security, sometimes called self-healing). The two ratchets together are why a Signal-protocol chat has no single long-lived key to steal. SWARM's messenger inherits this from Signal's code; the design belongs to Perrin and Marlinspike.

**Number:** specification revision 1, dated 20 November 2016; two ratchets, one key per message.

**Common misconception:** a chat is protected by one key agreed at the start. In the double ratchet that key is used once and replaced.

**Sources:** https://signal.org/docs/specifications/doubleratchet/ ; https://signal.org/docs/specifications/x3dh/

### 7. What a block explorer shows: transparent chain vs shielded pool

**The one idea:** on a transparent chain the explorer shows everything; in a shielded pool it shows that something valid happened.

Open any Bitcoin-style transaction in an explorer and you see the sending addresses, the receiving addresses, the exact amounts, the time and every prior transaction those addresses took part in. The whole history is indexed and searchable by anyone, free. Open a fully shielded transaction on the Zcash protocol stack and the explorer shows a transaction ID, the block, the fee and the fact that the zero-knowledge proof verified. Sender, receiver, amount and memo are encrypted; only the holder of the right viewing key can decode them. On Zcash itself both kinds coexist: on 6 October 2026 zecstats.org showed 11.97 million ZEC in the transparent pool and 4.94 million ZEC (29.1 percent of supply) in shielded pools.

**Number:** 29.1 percent of ZEC shielded on 2026-10-06 (moving figure, re-check before posting).

**Common misconception:** an explorer "proves" a shielded payment reached someone. It proves a valid transaction exists; the recipient proves receipt with a viewing key or a payment disclosure, not with the explorer.

**Sources:** https://zecstats.org/shielded ; https://zechub.wiki/using-zcash/transactions

### 8. What chain analysis actually does

**The one idea:** chain analysis does not break cryptography; it exploits habits.

The 2013 paper "A Fistful of Bitcoins" (Meiklejohn et al., Internet Measurement Conference) laid out the two workhorse heuristics still used today. Common-input ownership: if several addresses are spent together as inputs of one transaction, one party controlled all of them, so they are merged into a cluster. Change detection: a fresh output that fits the pattern of change is assigned to the sender's cluster too. The authors then bought and sold at exchanges and merchants to attach names to clusters, and found that the clusters covered a large, active part of the economy. Satoshi's own white paper warned in 2008 that multi-input transactions "necessarily reveal that their inputs were owned by the same owner". A new address per payment does not undo this; the next spend links it again.

**Number:** two heuristics, published 2013; the warning about linked inputs is in section 10 of the 2008 white paper.

**Common misconception:** "I use a new address each time, so I am anonymous." Clustering follows the money, not the label.

**Sources:** https://cseweb.ucsd.edu/~smeiklejohn/files/imc13.pdf ; https://bitcoin.org/bitcoin.pdf

### 9. What your ISP and a light-wallet server see when you use a wallet

**The one idea:** encryption on the wire still leaks who you talk to, when, and how much.

Your internet provider sees your IP address, the IP addresses you connect to, the timing and the volume of traffic. It usually also sees the hostname: in TLS 1.3 the certificate is encrypted, but the Server Name Indication in the first handshake message is still plaintext unless Encrypted Client Hello is in use. So "connected to a wallet server at 02:13 and again at 02:15" is visible even though the content is not. The light-wallet server (lightwalletd in the Zcash design) sees more: your IP, which block ranges you fetched, which transactions you broadcast and which memo ciphertexts you asked for. ZIP 307's stated goal is narrower: the server must not learn which shielded notes are yours, because trial decryption happens on your device.

**Number:** one plaintext field (SNI) in the first TLS packet is enough to name the service; the fix, ECH, is still being deployed.

**Common misconception:** HTTPS hides which site or service you use. It hides what you said to it.

**Sources:** https://blog.cloudflare.com/encrypted-client-hello/ ; https://zips.z.cash/zip-0307

### 10. What Tor does and does not hide

**The one idea:** Tor separates "who you are" from "where you go", for one application at a time.

Tor routes your connection through three volunteer relays, each knowing only the previous and next hop. The site you visit sees the exit relay's address, not yours; your provider sees that you connected to Tor, not where. That is the protection. The limits are just as concrete. Your provider can tell you are using Tor unless you use a bridge. The exit relay sees unencrypted traffic, so HTTP without TLS is readable there. Logging into an account that carries your name identifies you regardless of the route. Only traffic from the Tor-enabled application is protected; other apps on the same machine go out in the clear. And an observer who can watch both ends can correlate timing; the project says so in its own documentation.

**Number:** three relays per circuit; one application protected at a time.

**Common misconception:** Tor makes a device anonymous. It makes one connection path hard to trace; identity leaks through logins, plugins and other apps are untouched.

**Sources:** https://support.torproject.org/about/ ; https://support.torproject.org/faq/

### 11. What a browser leaks, and what ungoogled-chromium turns off

**The one idea:** a stock browser reports on you by design, mostly to the vendor.

Before you type anything, a browser can leak: the Referer header (which page you came from), client hints (browser version, platform, device model on request), your local network address through WebRTC (now mitigated by mDNS in most builds), a fingerprint from fonts, screen, canvas and audio that EFF's Cover Your Tracks test shows is often unique, and, in Chrome, Safe Browsing lookups and other background requests to Google services. ungoogled-chromium, the base of SWARM's browser, removes the vendor channel: it disables functionality tied to Google domains (Google Host Detector, URL Tracker, Cloud Messaging, Hotwording), disables Safe Browsing, rewrites Google hostnames in the source to a non-existent domain and blocks them at runtime, and strips pre-built binaries. It does not by itself stop fingerprinting or referrers; those need settings or extensions.

**Number:** the ungoogled-chromium README lists four core removals and about ten opt-in switches, all off by default.

**Common misconception:** incognito or private mode stops tracking. It discards local history; fingerprinting and network requests are unchanged.

**Sources:** https://github.com/ungoogled-software/ungoogled-chromium ; https://coveryourtracks.eff.org/

### 12. Why "delete" rarely deletes

**The one idea:** delete removes the signpost, not the data.

When you delete a file, the operating system marks the space as free and drops the directory entry; the bytes stay until something overwrites them, which on a modern SSD the user does not control because the drive remaps blocks for wear levelling. Copies also live on: cloud sync, backups, the recipient's device, the server's own backups and logs. NIST's media sanitisation guideline (SP 800-88, revision 2 published 26 September 2025) therefore distinguishes three levels: Clear (ordinary tools cannot retrieve the data), Purge (laboratory recovery infeasible, for example by cryptographic erase) and Destroy (the medium is unusable). "Empty trash" does not reach Clear. For messages the honest statement is: a disappearing message is deleted from cooperating devices; a screenshot or an uncooperative server is outside anyone's control.

**Number:** three sanitisation levels; revision 2 dated 2025-09-26.

**Common misconception:** emptying the recycle bin or deleting a chat removes the information from the world.

**Sources:** https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-88r2.pdf ; https://www.nist.gov/news-events/news/2025/09/guidelines-media-sanitization-nist-publishes-sp-800-88r2

### 13. What a proof-of-work block actually proves

**The one idea:** a valid block proves that someone spent real computing effort on exactly this content.

Miners take the block header, which commits to all transactions in the block and to the previous block, and search for a nonce such that the header's hash falls below a target. There is no shortcut: the only way to find one is to try, on average, a predictable number of hashes. The idea comes from Adam Back's Hashcash (2002), designed to make spam expensive. In a currency it does three things: it makes rewriting history cost as much as writing it, it lets anyone verify the work with one hash, and it ties block production to a schedule by adjusting the target. It does not prove the transactions are honest; the validity rules do that. Bitcoin aims for a block every ten minutes; Zcash-family chains every 75 seconds.

**Number:** verification costs one hash; production costs on the order of the difficulty, trillions of hashes on Bitcoin.

**Common misconception:** miners "solve complex equations". They repeat one simple operation until luck and effort produce a small enough number.

**Sources:** https://bitcoin.org/bitcoin.pdf ; http://www.hashcash.org/papers/hashcash.pdf

### 14. Why open source matters for crypto software: Kerckhoffs, 1883

**The one idea:** a system is only secure if it stays secure when everyone knows how it works.

Auguste Kerckhoffs published "La cryptographie militaire" in the Journal des sciences militaires in January and February 1883. His second principle, in Petitcolas's translation, reads: "The system must not require secrecy and can be stolen by the enemy without causing trouble." Only the key may be secret. The reason is practical: designs leak, staff change sides, hardware is captured; a design that collapses when read is a design that will collapse. For wallet and messenger software this is the case for open source. If the code is public, the claim "we cannot read your messages" can be checked instead of trusted, the build can be reproduced, and a hidden key-exfiltration path has nowhere to hide. Closed-source privacy software asks you to take the one thing the field says not to take: its word.

**Number:** 1883; six principles; the second is the one that survived.

**Common misconception:** publishing the code helps attackers. It helps everyone equally, and defenders outnumber attackers when the code is widely read.

**Sources:** https://www.petitcolas.net/kerckhoffs/ ; https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle

### 15. Coinbase maturity: why a mining reward waits 100 blocks

**The one idea:** a freshly mined reward cannot be spent until the block is buried deep enough that it will not disappear.

The first transaction in each block, the coinbase, creates the reward out of nothing. If a chain reorganisation later drops that block, the reward vanishes with it. If it had already been spent, every downstream payment would unravel too, so the consensus rule says a coinbase output may not be spent until 100 blocks have been mined on top of it. Bitcoin's source carries it as `COINBASE_MATURITY = 100`; the Zcash protocol applies the same rule, and since shielded coinbase (ZIP 213) it applies to transparent coinbase outputs. At 10-minute blocks that is roughly 16.7 hours; at 75-second blocks, about two hours. Wallets show these funds as "immature", which is not an error.

**Number:** 100 blocks; about 2 hours 5 minutes on a 75-second chain, about 16 h 40 min on Bitcoin.

**Common misconception:** an immature reward means the pool or node has failed to pay. It means the chain has not yet guaranteed the block.

**Sources:** https://zips.z.cash/zip-0213 ; https://en.bitcoin.it/wiki/Protocol_rules

### 16. What a 2-of-3 multisig is

**The one idea:** money that needs two of three keys to move survives one lost key and one stolen key.

A multisignature output is locked to several public keys and a threshold. With 2-of-3, any two of the three private keys can sign a spend; one key alone cannot. Keep the keys in different places (a hardware device, a laptop, a backup in a vault) and two separate failures are survivable: a thief with one key cannot spend, and a user who loses one key still has two. Bitcoin standardised the construction in BIP-11 (Gavin Andresen, 2011) using `OP_CHECKMULTISIG`, and the same idea is used for project treasuries and exchange cold storage. It is a custody tool, not a privacy tool: on a transparent chain a multisig spend is visible like any other, and the script pattern often reveals that multisig was used.

**Number:** 2 signatures out of 3 keys; BIP-11 dated 2011.

**Common misconception:** multisig hides the owners. It distributes control; it does not hide anything.

**Sources:** https://github.com/bitcoin/bips/blob/master/bip-0011.mediawiki ; https://en.bitcoin.it/wiki/Multi-signature

---

## Part 2: Data and metadata (10 seeds)

### 17. The Stanford phone-metadata study (2016)

**The one idea:** phone metadata alone, no content, is enough to infer medical conditions, purchases and relationships.

Jonathan Mayer, Patrick Mutchler and John Mitchell collected call and text metadata from volunteers through an Android app and published the results in PNAS in May 2016. Their findings: the metadata is densely interconnected, numbers are trivially re-identified using public directories and social media, and automated inference recovers locations and relationships. The case studies are what people remember: one participant's calls to a cardiology group, a medical laboratory, a pharmacy and a device hotline indicated a heart condition; another's calls pointed to a firearm purchase; another's, to a hardware store, a hydroponics supplier and a head shop. Nothing in any of those calls was recorded. The paper was written to test the legal claim that metadata is less sensitive than content.

**Number:** published in PNAS vol. 113, no. 20, pp. 5536–5541 (2016).

**Common misconception:** "just metadata" is harmless because nobody heard the call.

**Sources:** https://www.pnas.org/doi/10.1073/pnas.1508081113 ; https://www.pnas.org/doi/10.1073/pnas.1605356113

### 18. "We kill people based on metadata" (Hayden, 2014)

**The one idea:** the people who collect metadata say it is decisive; that is the strongest argument for protecting it.

In April 2014, at a Johns Hopkins University Foreign Affairs Symposium debate with law professor David Cole, former NSA and CIA director Michael Hayden said: "We kill people based on metadata." Cole reported the line in the New York Review of Books on 10 May 2014, alongside former NSA general counsel Stewart Baker's statement that metadata "absolutely tells you everything about somebody's life". Hayden added that the United States does not do this with the domestic telephone records programme; the remark was about overseas targeting. The quotation is worth stating exactly, with that qualification, because it is often shortened into something he did not say. The lesson is narrow and strong: metadata is treated as actionable intelligence by the agencies that have the most of it.

**Number:** debate April 2014; published 10 May 2014.

**Common misconception:** Hayden was describing the bulk domestic programme. He explicitly excluded it; the point stands for what metadata can support.

**Sources:** https://www.nybooks.com/online/2014/05/10/we-kill-people-based-metadata/ ; https://www.justsecurity.org/10311/michael-hayden-kill-people-based-metadata/

### 19. The Target pregnancy-prediction story (NYT, 2012)

**The one idea:** purchase records can infer a condition before the shopper tells anyone; the famous anecdote is weaker than the method.

Charles Duhigg's New York Times Magazine piece (February 2012) described how Target statistician Andrew Pole built a "pregnancy prediction" score from about 25 products, such as unscented lotion and supplements, and could estimate a due date closely enough to time coupons. That part is documented from Target's own analytics work. The widely retold scene, a father complaining that his teenage daughter received baby coupons and later learning she was pregnant, is a second-hand anecdote told to Duhigg by a Target employee, and later commentators have questioned whether it happened as told. State it as "a story Target staff told" and lead with the verified part: retailers score customers on life events from receipts, then disguise the targeting by mixing in unrelated offers.

**Number:** roughly 25 products in the model; published 16 February 2012 (magazine dated 19 February).

**Common misconception:** the teenager story is a confirmed case. The scoring method is confirmed; the anecdote is not.

**Sources:** https://www.nytimes.com/2012/02/19/magazine/shopping-habits.html ; https://www.kdnuggets.com/2014/05/target-predict-teen-pregnancy-inside-story.html

### 20. The Strava heat map that revealed military bases (2018)

**The one idea:** aggregated, anonymised fitness data can disclose exactly what each individual record did not.

In November 2017 Strava published a global heat map built from about three trillion GPS points (Strava's figure; some reports quote 13 trillion, which was the count of rasterised pixels). In January 2018 Nathan Ruser, a student at the Australian National University, noticed that in Afghanistan, Syria and Djibouti the glowing jogging loops were almost all foreign soldiers, so the map outlined bases that do not appear on commercial satellite imagery, including patrol routes. No single runner's identity was on the map; the collective pattern was the leak. Strava's response was to tell users to review their privacy settings, and militaries restricted fitness trackers. The case is the standard example of aggregation risk: anonymising each row does not anonymise the shape of the whole.

**Number:** about 3 trillion GPS points; discovered 27–28 January 2018.

**Common misconception:** the data was stolen. It was published deliberately as a feature, with each user's data "anonymised".

**Sources:** https://techcrunch.com/2018/01/28/strava-exposes-military-bases/ ; https://www.theguardian.com/world/2018/jan/28/fitness-tracking-app-gives-away-location-of-secret-us-army-bases

### 21. The Netflix Prize de-anonymisation (2008)

**The one idea:** a few public data points re-identify records in a "scrubbed" dataset.

For its 2006 recommendation contest, Netflix released about 100 million ratings from roughly 500,000 subscribers with names removed. Arvind Narayanan and Vitaly Shmatikov (IEEE Security and Privacy, 2008) showed that knowing a handful of a person's ratings, even approximately, is enough to find their row: with 8 ratings, two of which may be wrong, and dates known to within 14 days, 99 percent of records were uniquely identified; with only 2 ratings and 3-day date accuracy, 68 percent. They matched rows against public IMDb reviews and recovered apparent political and other sensitive preferences. The planned sequel contest was cancelled in 2010 after an FTC inquiry and a lawsuit. The finding generalises to any sparse, high-dimensional data: transactions, locations, listening histories.

**Number:** 8 ratings plus 14-day dates re-identify 99 percent of records.

**Common misconception:** removing names anonymises a dataset. Names were never the identifying part; the pattern was.

**Sources:** https://arxiv.org/abs/cs/0610105 ; https://dl.acm.org/doi/10.1109/SP.2008.33

### 22. Latanya Sweeney's 87 percent (2000)

**The one idea:** ZIP code, birth date and sex identify most Americans uniquely.

Latanya Sweeney's 2000 working paper "Simple Demographics Often Identify People Uniquely" used 1990 census data to show that 87 percent of the US population could be identified by the combination of five-digit ZIP code, full date of birth and sex, three fields that "anonymised" medical and marketing datasets routinely kept. The figure is contested in the sense that it moves with the data: Philippe Golle recomputed it on the 2000 census and found 63 percent, still a majority. Earlier, in 1997, Sweeney had linked an anonymised hospital dataset to a voter roll to find the governor of Massachusetts's records. The method, matching quasi-identifiers across datasets, is what k-anonymity and modern de-identification rules were built to resist.

**Number:** 87 percent (1990 census, Sweeney); 63 percent (2000 census, Golle 2006).

**Common misconception:** data without names or ID numbers is anonymous.

**Sources:** https://dataprivacylab.org/projects/identifiability/paper1.pdf ; https://www.privacylives.com/wp-content/uploads/2010/01/golle-reidentification-deanonymization-2006.pdf

### 23. The AOL search-log release (2006)

**The one idea:** search queries are a diary; a user number is not a disguise.

On 4 August 2006 AOL's research arm published about 20 million search queries from 657,000 users over three months, with each user replaced by a number. Five days later the New York Times identified user No. 4417749 as Thelma Arnold, a 62-year-old widow in Lilburn, Georgia, from her own queries: landscapers in Lilburn, homes sold in her subdivision, people with her surname, and medical searches she had made for friends. AOL withdrew the file within days, but copies persist. The lesson is twofold: queries contain names, places and conditions that re-identify the searcher, and a search engine or wallet server that logs "pseudonymous" requests holds the same kind of diary.

**Number:** 20 million queries, 657,000 users, released 4 August 2006; identified 9 August 2006.

**Common misconception:** replacing identities with random numbers anonymises logs.

**Sources:** https://www.nytimes.com/2006/08/09/technology/09aol.html ; https://en.wikipedia.org/wiki/AOL_search_log_release

### 24. Location-data brokers and the FTC (Kochava, X-Mode, 2022–2024)

**The one idea:** phone location data is bought, resold and tied to individuals, and it took enforcement actions to restrict even its most sensitive uses.

On 29 August 2022 the FTC sued Kochava for selling location data from hundreds of millions of devices that could trace people to reproductive-health clinics, shelters and places of worship; a court let the amended complaint proceed in February 2024, and a settlement was reported in 2026 (confirm current status before posting). On 9 January 2024 the FTC announced its first ban on selling sensitive location data: X-Mode Social and its successor Outlogic, which had collected precise locations through SDKs embedded in more than 300 apps and sold them with advertising identifiers; the order was finalised in April 2024. The mechanism to teach is the SDK: a weather or prayer app includes a library, the library reports location, and the app developer is paid.

**Number:** more than 300 apps carried X-Mode's SDK; first FTC sensitive-location ban dated 9 January 2024.

**Common misconception:** location data is sold only in aggregate. It was sold per device, with identifiers that let buyers tie it to a person.

**Sources:** https://www.ftc.gov/news-events/news/press-releases/2024/01/ftc-order-prohibits-data-broker-x-mode-social-outlogic-selling-sensitive-location-data ; https://www.ftc.gov/news-events/news/press-releases/2022/08/ftc-sues-kochava-selling-data-tracks-people-reproductive-health-clinics-places-worship-other

### 25. The 2024 National Public Data breach, with the numbers checked

**The one idea:** a background-check broker you never heard of held your identity data, and the headline number was rows, not people.

National Public Data, a Florida background-check aggregator, was breached in late 2023; the data was offered for sale in April 2024 and leaked in full in August 2024. Headlines said "2.9 billion people". Troy Hunt, who runs Have I Been Pwned, analysed the files: 2.9 billion is the row count, with heavy duplication, many deceased people and no email addresses in the main set; a later partial set contained 134 million unique email addresses, 87 percent of which were already in HIBP from other breaches. What was real and serious: names, addresses, dates of birth and Social Security numbers for a large share of the US population. NPD confirmed the breach in August 2024 and filed for bankruptcy in October 2024. Use the smaller, verified numbers.

**Number:** 134 million unique email addresses (verified); "2.9 billion" is rows, not people.

**Common misconception:** 2.9 billion people were exposed. The figure is contested; the row count exceeds the population of the affected countries.

**Sources:** https://www.troyhunt.com/inside-the-3-billion-people-national-public-data-breach/ ; https://haveibeenpwned.com/Breach/NationalPublicData

### 26. Mozilla's 2023 verdict: cars are the worst product category for privacy

**The one idea:** a modern car is a data-collection device with wheels.

In September 2023 Mozilla's *Privacy Not Included team reviewed 25 car brands and gave every one its warning label, calling cars "the worst product category we have ever reviewed for privacy". The numbers from the report: 84 percent of brands say they share personal data with service providers, data brokers or other businesses; 76 percent say they can sell it; 56 percent say they will hand it to government or law enforcement on a "request", not necessarily a warrant. Nissan's policy listed "sexual activity" among data it may collect, and several brands mentioned genetic information. The researchers could not confirm that any brand met Mozilla's minimum security standards. The point for a privacy audience: the telematics unit, the app and the dealer's systems all keep records that outlive the drive.

**Number:** 25 of 25 brands failed; 56 percent share with authorities on request.

**Common misconception:** the car only knows where it has been. Policies cover in-car behaviour, app usage and data bought from third parties.

**Sources:** https://www.mozillafoundation.org/en/privacynotincluded/articles/its-official-cars-are-the-worst-product-category-we-have-ever-reviewed-for-privacy/ ; https://www.securityweek.com/25-major-car-brands-get-failing-marks-from-mozilla-for-security-and-privacy/

---

## Part 3: Money (8 seeds)

### 27. What a bank statement reveals, and who may read it

**The one idea:** your bank is required by law to watch you and to report without telling you.

A statement lists counterparties, amounts, dates, merchants and locations; together they show where you live, work, worship, shop and travel. In the United States the Bank Secrecy Act of 1970 obliges banks to keep these records and to file reports. A Currency Transaction Report goes to FinCEN for cash transactions above $10,000 in a day, a threshold unchanged since 1970. A Suspicious Activity Report is filed for transactions of $5,000 or more at a bank that staff judge suspicious, and the customer may not be told it exists. Readers of your statement therefore include bank staff, compliance contractors, FinCEN, and law-enforcement agencies that query it. Most countries have an equivalent regime. None of this requires a warrant naming you.

**Number:** CTR threshold $10,000 (since 1970); SAR threshold $5,000 for banks.

**Common misconception:** bank records are private between you and the bank.

**Sources:** https://www.fincen.gov/resources/statutes-and-regulations/bank-secrecy-act ; https://en.wikipedia.org/wiki/Bank_Secrecy_Act

### 28. How payment apps share data: Venmo's public-by-default feed

**The one idea:** a payment app can publish your transactions to the world, and did.

Venmo launched with a social feed in which every payment, with names, timestamps and the message, was public by default; only the amount was hidden. In 2018 researcher Hang Do Thi Duc pulled 207,984,218 public transactions from 2017 through the open API for her project "Public By Default" and reconstructed drug purchases, break-ups and a family's daily routine. In February 2018 the FTC settled with PayPal over Venmo misleading users about privacy settings: limiting the audience for future payments did not make them private unless a second setting was also changed. Friends lists became hideable only in 2021 after pressure from EFF and Mozilla. Beyond the feed, every card and app payment is visible to the processor, the network and the merchant, who may share it with "partners".

**Number:** 207,984,218 public Venmo transactions in 2017.

**Common misconception:** payment apps show your activity only to friends. The default audience was everyone with the API.

**Sources:** https://money.cnn.com/2018/07/17/technology/venmo-payments-public/index.html ; https://www.ftc.gov/news-events/news/press-releases/2018/02/paypal-settles-ftc-charges-venmo-failed-disclose-information-consumers-about-ability-transfer-funds

### 29. Why a transparent blockchain is worse than a bank for privacy

**The one idea:** a bank shows your records to a few parties under rules; a transparent chain shows them to everyone, forever, with no rules.

A bank statement is read by the bank, its contractors and regulators. A transaction on a transparent chain is a public record: anyone, anywhere, can read the addresses and amounts, link them to earlier and later transactions, and keep doing so years later with better tools. Nothing is ever deleted. The 2008 white paper acknowledged this and proposed one mitigation, a new key pair per transaction, while noting that linking is "still unavoidable with multi-input transactions". Chain-analysis firms now sell the resulting graphs to exchanges, governments and private clients. If one address is ever tied to a name, through an exchange account, a donation page or a delivery, the whole cluster inherits that name retroactively.

**Number:** zero deletions, unlimited readers; mitigation proposed in 2008, section 10 of the white paper.

**Common misconception:** "pseudonymous" means private. It means the label is missing until someone attaches it, and then it applies to the entire history.

**Sources:** https://bitcoin.org/bitcoin.pdf ; https://cseweb.ucsd.edu/~smeiklejohn/files/imc13.pdf

### 30. What a mixer does, and why it is not a shielded pool

**The one idea:** a mixer is a service that shuffles coins on a transparent ledger; a shielded pool is a ledger rule that never records who paid whom.

A mixer or tumbler takes deposits from many users and pays out to new addresses, hoping to break the link. Deposits and withdrawals are still public, so amounts, timing and address reuse can re-link them; the operator, if there is one, may keep logs; and governments treat mixers as suspicious by category. Tornado Cash was sanctioned by the US Treasury on 8 August 2022, with the claim that it had been used to launder more than $7 billion, and delisted on 21 March 2025 after litigation. A shielded pool is different in kind: in a shielded transaction the sender, receiver and amount are never written to the chain; validity is proven with a zero-knowledge proof; there is no operator and nothing to subpoena. The privacy is a property of the protocol, not a service layered on top.

**Number:** sanctioned 2022-08-08, delisted 2025-03-21.

**Common misconception:** a shielded pool is a built-in mixer. A mixer obscures a public record; a shielded pool never creates one.

**Sources:** https://home.treasury.gov/news/press-releases/jy0916 ; https://home.treasury.gov/news/press-releases/sb0057

### 31. Default privacy vs optional privacy: Monero and Zcash by the numbers

**The one idea:** privacy you must opt into is used by a minority, and a small crowd is easier to pick out.

Monero makes every transaction private by protocol: ring signatures (a ring of 16 possible senders), stealth addresses and RingCT hide sender, receiver and amount with no user action, so the anonymity set is the whole network. Zcash offers both transparent and shielded transactions, and for most of its history most coins stayed transparent. On 6 October 2026 zecstats.org showed 4.94 million ZEC (29.1 percent of supply) in shielded pools against 11.97 million transparent; the share was about 26 percent in mid-2026 and has been rising. A SWARM post should state both sides honestly: optional privacy lets transparent exchanges and auditors interoperate, and it leaves the shielded share to depend on wallet defaults and user habits.

**Number:** 29.1 percent of ZEC shielded on 2026-10-06 (moving; re-check); Monero 100 percent by construction.

**Common misconception:** optional and default privacy give the same protection to someone who opts in. The size of the crowd you hide in is part of the protection.

**Sources:** https://www.getmonero.org/get-started/what-is-monero/ ; https://zecstats.org/shielded

### 32. CBDC programmability and expiry: e-CNY coupons and the digital euro

**The one idea:** central-bank digital money can carry rules; whether it will is a policy choice you should read, not assume.

In October 2020 Shenzhen's Luohu district distributed 50,000 e-CNY "red packets" of 200 yuan each by lottery; the money could be spent at 3,389 designated shops only from 12 to 18 October and then expired. About 92 percent was spent in the window. That is programmability in practice: money with a deadline and a merchant list. The European Central Bank's digital-euro FAQ states a different design: offline payments with "cash-like" privacy where only payer and payee know the details, an online mode in which the Eurosystem "would not be able to directly link" transactions to individuals, anti-money-laundering checks performed by the distributing bank, and an explicit statement that the digital euro would not be "programmable money". Both are claims by issuers; the code is what counts.

**Number:** 200 yuan per packet, valid 12–18 October 2020; digital euro targeted for 2029.

**Common misconception:** CBDCs are the same as bank deposits in an app. A CBDC is a central-bank liability whose rules are set by the issuer directly.

**Sources:** https://www.ledgerinsights.com/china-central-bank-digital-currency-cbdc-ecny-giveaway-results/ ; https://www.ecb.europa.eu/euro/digital_euro/faqs/html/ecb.faq_digital_euro.en.html

### 33. Cash is declining, unevenly: ECB SPACE 2024 and the Riksbank

**The one idea:** cash is still the most used payment instrument in euro-area shops by count, yet in Sweden it is nearly gone; both trends are measured, not felt.

The ECB's SPACE 2024 study found cash used in 52 percent of point-of-sale transactions in the euro area by number, down from 59 percent in 2022, and 39 percent by value, with cards at 45 percent by value. Cash remains the tool for small purchases and for people without accounts. Sweden is the other end of the curve: the Riksbank's Payments Report 2025 puts cash at about one in ten in-store purchases, and notes that many small businesses have stopped accepting it. The privacy relevance is direct: cash is the only widely accepted payment that leaves no third-party record, and each percentage point lost moves everyday life into logged systems. The decline is a fact; whether it is a problem is the debate.

**Number:** euro area 52 percent of POS transactions in cash (2024); Sweden about 10 percent.

**Common misconception:** nobody uses cash any more. Half of euro-area shop payments still do; the value share is where cash is losing.

**Sources:** https://www.ecb.europa.eu/stats/ecb_surveys/space/html/ecb.space2024~19d46f0f17.en.html ; https://www.riksbank.se/globalassets/media/rapporter/betalningsrapport/2025/engelsk/payments-report-2025.pdf

### 34. The EU anti-money-laundering regulation: €10,000 cash cap and no anonymous accounts from 10 July 2027

**The one idea:** from 2027 a single EU regulation caps cash and bans anonymous accounts at regulated firms; it binds businesses, not the existence of private tools.

Regulation (EU) 2024/1624 applies from 10 July 2027. Article 80 forbids traders in goods and services from making or accepting cash payments above €10,000, or the equivalent, in one or linked operations; member states may set lower caps. Article 79 prohibits credit and financial institutions and crypto-asset service providers from keeping anonymous accounts, anonymous passbooks or safe-deposit boxes, and from offering accounts that allow anonymisation of the holder or increased obfuscation of transactions, including through anonymity-enhancing coins. Read precisely: it regulates obliged entities, banks, exchanges and custodians. It does not outlaw cash, self-custody or open-source software, and some national caps are already lower. Cite the regulation, not a summary, when posting.

**Number:** €10,000 cap; applies from 10 July 2027; Articles 79, 80 and 90.

**Common misconception:** the AMLR bans privacy coins in Europe. It bans regulated service providers from handling them anonymously; it does not reach the protocol or the user.

**Sources:** https://eur-lex.europa.eu/eli/reg/2024/1624/oj/eng ; https://anti-money-laundering.eu/article-80-amlr/

---

## Part 4: Practical (6 seeds)

### 35. How to verify a download checksum on Windows, macOS and Linux

**The one idea:** one command tells you whether the file you have is the file that was published.

The publisher lists a SHA-256 hash next to the download. Compute yours and compare every character. Windows, in Command Prompt or PowerShell: `certutil -hashfile <file> SHA256`. macOS, in Terminal: `shasum -a 256 <file>`. Linux: `sha256sum <file>`, or put the published hash in a file and run `sha256sum -c <file>.sha256`, which prints OK or FAILED. A match proves integrity: the bytes are unchanged. It does not prove authenticity: if an attacker replaced both the file and the hash on the same page, both match. For that, publishers sign releases (GPG or code-signing certificates) and post the hash in a second place, such as a repository or a social account. Checksums catch corrupt and swapped downloads; signatures catch swapped pages.

**Number:** 64 hex characters; every one must match.

**Common misconception:** a matching checksum proves the file is safe. It proves it is the file the publisher of that hash intended; trust in the publisher is a separate step.

**Sources:** https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil ; https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html

### 36. How to store a recovery phrase, and why not as a photo

**The one idea:** the phrase must survive fire and theft, which means offline, duplicated and never digital.

Write the 24 words by hand on paper or stamp them into metal; check them by restoring a wallet before you move funds in. Keep two copies in two places, so one fire, flood or burglary does not take both. Never photograph the phrase: a photo is synced to the cloud by default on most phones, included in backups, visible to any app with photo permission, and indexed by image recognition that can read text. Never type it into a website or a chat, including one that claims to be support; a real wallet asks for the phrase only when restoring on the device. Never store it in the same place as the device. The phrase is the wallet (seed 3); treat it like the cash it controls.

**Number:** two copies, two locations, zero photos.

**Common misconception:** a password manager or encrypted note is "safe enough". It puts the phrase on an internet-connected device under one password.

**Sources:** https://bitcoin.org/en/secure-your-wallet ; https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki

### 37. How to check that a site is the real one

**The one idea:** read the domain, not the page; arrive by bookmark, not by link.

Phishing pages copy the look of a wallet, exchange or project site perfectly; what they cannot copy is the domain name. Before entering anything, read the address bar from the end of the host backwards: the registrable part just before the first slash is what matters, so `swarm.green.example.com` belongs to example.com, not to swarm.green. Watch for swapped letters, extra words and lookalike characters. The padlock means only that the connection to that domain is encrypted; a phishing site has a padlock too. Reach money sites from a bookmark you made yourself or by typing the address; never from a link in an email, a reply or an advert, and never from a search result, where lookalike adverts sit above the real result. EFF's phishing guide says the same in one line: go to the login page yourself.

**Number:** one field to check, the domain; one habit, the bookmark.

**Common misconception:** HTTPS means the site is genuine. It means the connection is private to whoever owns that domain.

**Sources:** https://ssd.eff.org/module/how-avoid-phishing-attacks ; https://en.wikipedia.org/wiki/IDN_homograph_attack

### 38. How to read a privacy policy in two minutes

**The one idea:** you cannot read them all, so search them for the four words that matter.

McDonald and Cranor (2008) estimated that reading every privacy policy an American encounters would take about 244 hours a year, roughly ten minutes per policy, so nobody does. Use search instead. Open the policy and look for "share" and "partners": who receives the data, and is "partners" defined? Look for "sell": many policies say they do not sell data but share it for "advertising measurement", which is the same flow under another name. Look for "retain" and "delete": how long is data kept after you close the account, and is deletion offered at all? Finally look for "law enforcement" or "request": does the company require a warrant, or hand over data on a request? Four searches, two minutes, and you know what the service is for.

**Number:** 244 hours per year to read them all; about 10 minutes per policy.

**Common misconception:** "we do not sell your data" means it stays with the company. Sharing for advertising, analytics and "partners" is usually covered elsewhere in the same document.

**Sources:** https://lorrie.cranor.org/pubs/readingPolicyCost-authorDraft.pdf ; https://cyberlaw.stanford.edu/content/files/bitstream/handle/1811/72839/isjlp_v4n3_543.pdf

### 39. How to check your own exposure with Have I Been Pwned

**The one idea:** the breaches you are already in are public knowledge; look them up before an attacker does.

Have I Been Pwned, run by Troy Hunt since 2013, indexes credentials from published breaches. On 6 October 2026 it listed 1,039 breached sites and 17.8 billion pwned addresses. Enter an email address and it returns which breaches contained it and what data types leaked (passwords, phone numbers, addresses). The practical response is specific: change the password on each listed service, and anywhere you reused it; turn on two-factor authentication; expect targeted phishing that quotes real details from those breaches. The Pwned Passwords feature lets you check a password without sending it: the client sends only the first five characters of its hash and compares locally. Set up the notification service once; new breaches then find you.

**Number:** 17.8 billion pwned addresses across 1,039 sites (2026-10-06, moving figure).

**Common misconception:** "I was not notified, so I was not breached." Most breached companies notify late or never; the index is the notification.

**Sources:** https://haveibeenpwned.com/ ; https://haveibeenpwned.com/About

### 40. How to set up a separate browser profile for money

**The one idea:** one browser profile for wallets and banking, with nothing else in it, removes most of the attack surface you carry around all day.

Chrome, Chromium-based browsers and Firefox all support profiles: separate stores of bookmarks, history, cookies, extensions and settings. Create one named "money". Install no extensions, because every extension can read every page, and extension hijacks are a recurring theft route. Do not sign the profile into a vendor account or sync it. Add bookmarks only for the few sites you use for money, typed in by hand once and checked (seed 37). Use it for nothing else: no search, no social media, no email. In Chrome, use the profile menu; in Firefox, open `about:profiles`. The everyday profile keeps its conveniences; the money profile keeps its silence. Cost: one minute to switch; benefit: a leak in a shopping extension cannot see your wallet page.

**Number:** zero extensions in the money profile.

**Common misconception:** a private or incognito window is isolation enough. It shares the extensions and the browser process; it only forgets afterwards.

**Sources:** https://support.google.com/chrome/answer/2364824 ; https://support.mozilla.org/en-US/kb/profile-manager-create-remove-switch-firefox-profiles

---

## Verification notes (2026-10-06)

- All source URLs were located by web search or fetched on 2026-10-06. Two pages could not be fetched directly for content (the Mozilla Foundation article returned 403 after a confirmed 301 from the old foundation.mozilla.org path; the Guardian blocks fetching). For both, the facts were confirmed through the secondary sources listed beside them. The Firefox support page returned a client-side challenge; its URL is the canonical one.
- Contested or moving figures are flagged in the seed: Sweeney 87 vs Golle 63 percent; Strava 3 trillion points vs 13 trillion pixels; National Public Data 2.9 billion rows vs 134 million emails; Zcash shielded share (29.1 percent on 2026-10-06); HIBP totals; the Target anecdote; Kochava settlement status (reported 2026, confirm).
- Hayden's exact wording, "We kill people based on metadata.", is as reported by David Cole (NYRB, 10 May 2014) and the Just Security transcript; the debate was at Johns Hopkins in April 2014. Hayden's qualification about the domestic programme should accompany the quote.
- AMLR dates and articles are from the EUR-Lex text: application from 10 July 2027 (Article 90), cash cap in Article 80, anonymous instruments in Article 79.
- Nothing here has been posted. Posting runs through the owner via the Metricool route; agents draft only.
