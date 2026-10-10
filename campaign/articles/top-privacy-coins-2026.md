---
title: "The privacy coin landscape in 2026: who still hides what, and how"
description: "A comparison of the privacy coins and privacy platforms still running in October 2026: what each hides, whether by default, who is paid from the issuance, and what regulators have scheduled."
tags: [privacy, cryptocurrency, zcash, monero]
canonical_url: https://swarm.green/
published: false
lint_judged: ["privacy-claims: 'anonymity set' as the technical term and 'anonymity-enhancing coins' as the regulations' own term, in quotation marks with the EU AMLR, FATF and VARA as sources", "security-claims: 'audited' in question 5, the question whether code was audited", "retired-words rule: 'snapshot' in Secret Network's token migration reported as news with its date", "other-projects: Zcash, Monero and the other compared projects named as reported facts in the comparison"]
---

*Disclosure: this article is published by the SWARM project, whose coin is one of the sixteen compared below. We describe every other project in the terms its own documentation uses, and hold SWARM to the same standard.*

## Cash for a single ride

In the autumn of 2019, during the protests in Hong Kong, an odd queue formed in MTR stations. People lined up at the ticket machines to buy single-journey tickets with coins and notes, although most carried an Octopus card that would have taken them through the gates. Some left cash at the machines for strangers.

The reason was the card's memory. An Octopus card can be used without a name, but many are linked to a credit card, and every card keeps a record of where it entered and left the network. Hong Kong Free Press and BuzzFeed News both described the same choice: a paper ticket bought with cash leaves no trip history, and a trip history can place a person at one station at one hour.

Nothing about the queue was dramatic. It was people paying for a train ride the slow way because the fast way wrote everything down.

The lesson fits in one line: when a payment leaves a trail, people under pressure go back to cash. Online there is no cash to go back to.

## What Bitcoin fixed, and the sentence it left open

On 3 January 2009 the first Bitcoin block was mined with a line of text inside it: "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks", the front-page headline of that day's London Times. It dated the block and stated the motive. What followed solved a problem that had looked unsolvable: money with a fixed supply, 21 million coins at most, issued by proof of work on a published schedule, with no bank and no government deciding how much exists.

Privacy was left open, and the white paper says so. Section 10 of the 2008 paper offers one defence: "a new key pair should be used for each transaction to keep them from being linked to a common owner." The next sentence admits its limit: "Some linking is still unavoidable with multi-input transactions, which necessarily reveal that their inputs were owned by the same owner." In 2013 the paper "A Fistful of Bitcoins" turned that limit into the first published method for clustering Bitcoin addresses, and chain analysis has been an industry ever since.

A privacy coin is the attempt to finish that sentence: scarce money that works like the cash queue, online.

## What "privacy coin" means

A privacy coin is a cryptocurrency whose chain does not record who paid whom, or how much. The ledger still proves that every payment was valid and that no coin was spent twice or created from nothing; it leaves out the sender, the receiver and the amount. A coin that routes traffic over Tor but writes every address and amount to the chain is not a privacy coin, and we have left that category out.

The projects that remain split along one line: is privacy mandatory or optional? On Monero and Pirate Chain every transaction is shielded, so the anonymity set is the whole chain. On Zcash, Dash, Firo, Litecoin and Decred, shielding is a choice, and the shielded minority sits beside a transparent majority that leaks information about it. Optional privacy is weaker as a property of the population. It is also why those coins remain on regulated exchanges while the mandatory ones have been removed from several.

## What changed in 2025 and 2026

Three things changed in 2025 and 2026. Institutional attention went to Zcash: a Grayscale ETF filing, a listed company reportedly holding about 1.8% of supply, a Foundry mining pool. Zcash's Orchard shielded pool became a shared library: Dash shipped it, Pirate Chain is testing it, and SWARM's shielded pool, called Ironwood, is built on its design. And the regulatory calendar acquired a date: from 10 July 2027, EU exchanges may not serve "anonymity-enhancing coins".

## The field at a glance

| Coin | Privacy model | Default or optional | Consensus | Supply and allocation | Status, October 2026 |
| --- | --- | --- | --- | --- | --- |
| Monero | RingCT (ring 16), stealth addresses, Bulletproofs+ | Mandatory | PoW RandomX (CPU) | About 18.4M plus tail emission; no premine, no dev share | FCMP++ stressnet since 5 October 2026 |
| Zcash | zk-SNARKs (Halo 2, Orchard) | Optional; 29.1% of supply shielded on 6 October 2026 ([zecstats.org](https://zecstats.org/shielded), a moving figure) | PoW Equihash (ASIC) | 21M cap; Founders' Reward 2016 to 2020, then dev fund | NU7 mainnet 5 November 2026 |
| Dash | Optional CoinJoin; Orchard pool since Evolution 4.0 | Optional | PoW X11 plus masternodes; 10% treasury | About 18.9M cap; 2014 instamine | Repositioning |
| Firo | Lelantus Spark | Optional | PoW FiroPoW plus masternodes | 21.4M cap; about 15% dev fund | Hard fork after Spark bug, 2026 |
| Litecoin MWEB | Mimblewimble extension block | Opt-in; about 350k LTC inside (reported) | PoW Scrypt | 84M cap; no premine | No exchange MWEB deposits |
| Decred | StakeShuffle, peer-to-peer | Opt-in | Hybrid PoW/PoS; 10% treasury | 21M cap; 8% premine | dcrd 2.0 |
| Grin | Mimblewimble, interactive | Default | PoW Cuckatoo32 | 1 GRIN per second forever; no premine | Node 5.1.2 |
| Beam | Mimblewimble plus LelantusMW | Default | PoW BeamHash III | 262.8M cap; 20% treasury for 5 years | Quiet |
| Pirate Chain | Sapling z-addresses only | Mandatory | PoW Equihash plus Komodo dPoW | 200M cap, about 196M issued; no premine | Orchard in public testing |
| Zano | CryptoNote lineage, confidential assets | Default | Hybrid PoW/PoS | About 17.5M, uncapped; 3.6M premine | HF6 August 2026 |
| Horizen | L3 on Base, selective disclosure | Opt-in | Base | 21M cap | L1 deprecated |
| Secret Network | TEE (SGX) contract state | Default for contracts | PoS; SCRT moving to Arbitrum | Inflationary | Pivoted to SecretAI |
| Aztec | zk-rollup, Noir | Per contract | Decentralised sequencers | AZTEC token; community sale 2026 | L2 going live |
| Railgun | Shielded balances as Ethereum contracts | Opt-in | Host chain | RAIL governance token | Alive |
| Oasis | Sapphire confidential EVM (TEE) | Per contract | PoS | 10B cap; large insider allocation | Sapphire 1.0 |
| SWARM | Zcash stack, shielded pool Ironwood (Orchard design) | Optional; wallet defaults to shielded | PoW Equihash 200,9 (ASIC) | 20,999,987.3152 cap; no premine; 20% of each block to 3 funds, permanently | Mainnet since 2 October 2026; closed start until 1 November 2026 |

Figures marked "reported" come from third-party trackers read on 6 October 2026 and will have moved.

## Monero

Monero remains the reference implementation of the mandatory model. Every output is hidden behind a stealth address, every amount behind a Bulletproofs+ range proof, and every spend behind a ring signature that mixes the real input with 15 decoys. Nothing is optional, so the anonymity set is every Monero transaction ever made. Issuance is proof of work on RandomX, designed for CPUs, with a tail emission of 0.6 XMR per 2-minute block that never ends. There was no premine and there is no developer share; the project runs on donations.

Its weaknesses are the known ones. Rings are a decoy scheme, and decoy selection has been the target of statistical heuristics for years. The planned fix, FCMP++, replaces the 16-member ring with a membership proof over the whole output set; a stressnet forked on 5 October 2026 and there is no mainnet date. Transactions are large compared with zk-SNARK designs. And in August 2025 the Qubic pool reportedly claimed a majority of hashrate and produced a 6-block reorganisation, a reminder that CPU-friendly mining is not automatically distributed mining.

The other cost of the mandatory model is market access. Monero has been removed from several regulated exchanges, and it is the coin regulators mean by "anonymity-enhancing".

Official site: [getmonero.org](https://www.getmonero.org/).

## Zcash

Zcash is the origin of the zero-knowledge approach. A shielded transaction carries a zk-SNARK that proves validity without revealing sender, receiver or amount, and since the Orchard pool and Halo 2 there is no trusted setup. Privacy is optional: transparent addresses exist and most of the supply has historically sat in them. On 6 October 2026 [zecstats.org](https://zecstats.org/shielded) showed 29.1% of supply in shielded pools, a share that has been rising through 2026; it is a moving figure.

Funding is the other thing Zcash is known for. From 2016 to 2020, 20% of every block reward went to the Founders' Reward, about 10% of eventual supply. A development fund renewed by community decision replaced it; the NU6.1 upgrade in November 2025 set 8% for Zcash Community Grants plus a coinholder-controlled fund. The weight of the Electric Coin Company and the Zcash Foundation is a centralisation concern the project discusses openly. Mining is Equihash, ASIC territory for years.

2025 and 2026 were Zcash's strongest years since launch: the Zashi wallet made shielded-by-default usable, Foundry opened a pool, Grayscale filed for an ETF, and NU7 is scheduled for mainnet on 5 November 2026 with 25-second blocks. The open problem is unchanged: a transparent pool beside a shielded one leaks information whenever value crosses between them.

Official site: [z.cash](https://z.cash/).

## The optional-privacy bloc: Dash, Firo, Litecoin MWEB, Decred

These four treat privacy as a feature rather than the product, and have paid for it in adoption while being rewarded in listings.

**Dash** has offered CoinJoin for most of its life; fewer than 1% of transactions use it. More interesting is that Evolution 4.0, released in July 2026, added an Orchard shielded pool, the same construction Zcash uses. Dash is X11 proof of work with masternodes and a 10% treasury, still carries the 2014 instamine controversy, and is delisted in Japan and South Korea.

**Firo** has the most original cryptography in the group, Lelantus Spark, extended in 2026 with Spark Names and Spark Assets. The same year a Spark vulnerability forced a mandatory hard fork, which the project disclosed; novel cryptography carries novel risk, however good the team. Firo runs FiroPoW with masternodes and about a 15% development share.

**Litecoin's MWEB** is a Mimblewimble extension block on an otherwise transparent chain. It is opt-in, reportedly holds about 350,000 LTC, and its transaction count is up roughly 10 times since mid-2024. Litecoin has no premine, but exchanges do not accept deposits from MWEB addresses, so the privacy ends at the on-ramp.

**Decred** uses StakeShuffle mixing, which dcrd 2.0 made peer-to-peer instead of server-mediated. Mixing is opt-in. Decred is hybrid proof of work and proof of stake with a 10% treasury and an 8% premine.

Official sites: [dash.org](https://www.dash.org/), [firo.org](https://firo.org/), [litecoin.org](https://litecoin.org/), [decred.org](https://decred.org/).

## Mimblewimble coins: Grin and Beam

Mimblewimble hides amounts with commitments and has no addresses; transactions are built interactively, and the chain stores a compact, cut-through history. Both coins are confidential by default.

**Grin** is the purist implementation: 1 GRIN per second forever, no premine, no company, donations only. Node 5.1.2 added Tor bridges and view keys. The interactive flow remains awkward, the team is tiny, and supply grows without bound, though the inflation rate falls yearly.

**Beam** added LelantusMW to break the transaction graph and governs through the BeamX DAO; its cap is 262.8M with a 20% treasury for the first 5 years. Both share Mimblewimble's structural weakness: anyone watching the network at broadcast can link inputs to outputs before cut-through hides them.

Official sites: [grin.mw](https://grin.mw/), [beam.mw](https://beam.mw/).

## Mandatory zero knowledge: Pirate Chain

Pirate Chain took the Zcash Sapling pool and removed the option: only z-addresses exist, so every transaction is shielded. It is Equihash proof of work, additionally notarised to another chain by Komodo's delayed proof of work. There was no premine. The cap is 200M and about 196M is already issued, so the subsidy is close to vanishing and long-term security depends on fees and on the dPoW arrangement. Orchard support is in public testing in 2026. Pirate shows that the Zcash cryptography can be run as a mandatory system; it is also small.

Official site: [piratechain.com](https://piratechain.com/).

## The pivots and the platforms

**Horizen** voted in February 2025 to deprecate its L1; ZEN is now an ERC-20 on Base with an L3 offering selective disclosure since December 2025. **Secret Network** is moving SCRT to an Arbitrum ERC-20, with a snapshot on 1 September 2026, and refocusing on SecretAI; its privacy comes from Intel SGX enclaves, which carry side-channel history. **Oasis** offers Sapphire, a confidential EVM also built on trusted hardware, with a 10B cap and a large insider allocation. **Aztec** is a zk-rollup on Ethereum with private and public state and the Noir language; Ignition started in November 2025, execution is rolling out through 2026, and a community sale closed in February 2026. **Railgun** is a set of contracts holding zk-SNARK-shielded balances on Ethereum and its L2s, with deposit screening and host-chain gas costs.

These are privacy platforms, not currencies, and should be judged as such. **Zano** is the exception: a CryptoNote-lineage chain with confidential assets and Zarcanum private proof of stake, private by default, with a 3.6M premine, no supply cap and an EVM layer planned for late 2026.

Official sites: [horizen.io](https://www.horizen.io/), [scrt.network](https://scrt.network/), [oasisprotocol.org](https://oasisprotocol.org/), [aztec.network](https://aztec.network/), [railgun.org](https://www.railgun.org/), [zano.org](https://zano.org/).

## SWARM

SWARM is a Zcash-stack coin; SWARM mainnet has been live since 2 October 2026, 15:42 UTC. It runs the Zcash protocol as implemented by the Zebra node: consensus rules and Equihash 200,9 are unmodified, and its shielded pool, called Ironwood, keeps sender, receiver and amount encrypted on chain; SWARM adds its network, its economics and its apps. Shielding is optional; SWARM Wallet defaults to a shielded address and labels every payment before sending.

Economics differ: 75-second blocks pay 6.25 SWM, halving every 1,680,000 blocks, for a cap of 20,999,987.3152 SWM. The genesis block holds no coins. Every block pays 80% to the miner and 20% to three published multisig addresses: 8% Core Development, 4% Grants & Ecosystem, 8% Community & Development Reserve. Unlike Zcash's Founders' Reward, the allocation never ends, and SWARM says so.

The start is closed: until 31 October 2026, 15:42 UTC only the project's own machines mine, about 0.99% of the cap; the waiting list gets 24 hours; public mining opens on 1 November 2026, 15:42 UTC. Equihash ASICs exist and nothing in the rules keeps them out. Please keep ASICs and rented hash power off the network. No coins are promised.

What is missing: no independent audit of the SWARM-specific changes has been published; the upstream components have their own security records. Builds are unsigned, and shielding hides what is written to the chain, not that a wallet uses SWARM from its ISP or light-wallet server.

Official site: [swarm.green](https://swarm.green/); SWARM mainnet explorer: [mainnet.explore.swarm.green](https://mainnet.explore.swarm.green/).

## How to read a privacy claim

Five questions sort most claims.

**1. Default or optional?** If users can choose, most will not, and the shielded minority inherits the leaks of the transparent majority. Ask what share of transactions is private.

**2. What does the chain record?** "Confidential amounts" is not "hidden participants". Mimblewimble hides amounts but exposes the graph at broadcast; rings hide the real spend among decoys; zk-SNARKs hide all three but reveal fee and size. Read the project's own table of what a transaction reveals.

**3. What does the server or the ISP learn?** Nearly every privacy coin is used through a light wallet. The server sees which encrypted outputs a wallet fetched and when; the ISP sees that the wallet talked to it. None of the coins above hide that.

**4. Who gets a share of the issuance?** Monero, Grin, Pirate Chain and Litecoin pay nothing to a team; Zcash, Dash, Firo, Decred, Beam, Zano and SWARM all carry a founder, treasury or development allocation. None is disqualifying, but the figure belongs on the front page, with the addresses.

**5. Has this specific code been audited?** "Built on audited cryptography" describes the upstream, not the project built on it. Firo's 2026 hard fork shows that even reviewed schemes break. Ask for the report, its date and its scope.

## The regulatory picture

The hard date is **10 July 2027**. From then, Article 79 of the EU Anti-Money Laundering Regulation (Regulation (EU) 2024/1624) prohibits credit institutions, financial institutions and crypto-asset service providers from keeping anonymous accounts, including accounts that allow anonymisation "including through anonymity-enhancing coins". The date is often misreported as 1 July. It removes EU fiat on- and off-ramps for such assets; it does not criminalise self-custody or peer-to-peer use. MiCA has already produced regional delistings, and the new Anti-Money Laundering Authority will say which assets count; whether optional-privacy coins fall inside is contested.

The **FATF**'s seventh targeted update, 16 July 2026, found that 83% of jurisdictions have Travel Rule legislation, that stablecoins carry about 84% of illicit virtual-asset volume, and still urged supervision of anonymity-enhancing products.

**Japan**'s exchanges delisted XMR, ZEC and DASH under FSA pressure from 2018. **South Korea** has banned high-risk coins for VASPs since March 2021. **Dubai**'s VARA has prohibited issuance of and VASP activity in anonymity-enhanced cryptocurrencies since 2023.

The **United States** has no ban; ZEC trades on Coinbase and Robinhood. Enforcement has targeted operators rather than coins: the Tornado Cash sanctions were lifted on 21 March 2025, Roman Storm was convicted in August 2025 only of unlicensed money transmission, and the Samourai Wallet founders were sentenced in November 2025. The Blockchain Regulatory Certainty Act passed the Senate Banking Committee in May 2026 and the CLARITY Act passed the House.

## What to watch over the next 12 months

Monero's **FCMP++** stressnet, forked on 5 October 2026, is the first full-scale test of replacing rings with full-chain membership proofs; a mainnet date would be the biggest change to the mandatory model since RingCT.

Zcash's **NU7** activates on mainnet on 5 November 2026 with 25-second blocks, the first upgrade the Orchard-adopting chains must decide whether to follow.

**SWARM's public mining** opens on 1 November 2026, 15:42 UTC. The question for 2 November: how many independent miners found blocks, and how fast Equihash hardware arrived. Both are readable from the explorer.

**AMLA guidance** on what counts as an anonymity-enhancing coin will decide whether the optional-privacy bloc keeps its EU listings after 10 July 2027, and whether optionality was a strategy or a reprieve.

None of this changes the basic choice. A coin that hides everything by default is harder to find on a regulated exchange; a coin that hides on request is easier to list and less private in practice. 2027 will show what each side of that trade cost.

## Sources

Research was collected on 6 October 2026. Figures that depend on a tracker or press report are marked "reported" above.

- Regulation (EU) 2024/1624, Article 79, in the Official Journal of the European Union (EUR-Lex, ELI reg/2024/1624/oj; the site answers automated link checks with a 202, so it is cited by identifier rather than linked)
- FATF, seventh targeted update on virtual assets and virtual asset service providers, 16 July 2026 (fatf-gafi.org, which refuses automated requests, so it is cited by name)
- Monero Qubic incident: https://www.halborn.com/ and https://decrypt.co/
- Zcash shielded share: https://zecstats.org/shielded (read on 6 October 2026); earlier reports: https://defillama.com/; NU6.1: https://leastauthority.com/
- Dash Orchard integration: https://cointelegraph.com/ and https://hackernoon.com/
- Firo roadmap and Spark hard fork: https://firo.org/
- Horizen pivot: https://www.theblock.co/ and https://thedefiant.io/
- Secret Network migration: https://scrt.network/; Aztec rollout: https://aztec.network/
- AMLR application date: https://coingeek.com/ and https://cointelegraph.com/
- VARA prohibition: https://blockworks.co/ and https://www.elliptic.co/
- Tornado Cash sanctions: https://thedefiant.io/; Samourai sentencing: https://www.justice.gov/; Blockchain Regulatory Certainty Act: https://www.govinfo.gov/
- Hong Kong, 2019: Hong Kong Free Press, 22 September 2019, https://hongkongfp.com/2019/09/22/explainer-communist-partys-railway-hong-kongs-respected-mtr-fell-afoul-protesters/ ; BuzzFeed News, https://www.buzzfeednews.com/article/rosalindadams/hong-kong-mtr-protests
- Bitcoin's genesis headline: facsimile of The Times, 3 January 2009, https://www.thetimes03jan2009.com/ ; supply cap and schedule: https://en.wikipedia.org/wiki/Bitcoin
- Bitcoin white paper, section 10: https://bitcoin.org/bitcoin.pdf
- Meiklejohn et al., "A Fistful of Bitcoins", Internet Measurement Conference 2013: https://cseweb.ucsd.edu/~smeiklejohn/files/imc13.pdf
- SWARM protocol and economics: https://swarm.green/network, https://swarm.green/verify, https://github.com/Swarmcoin/swarm-releases
