# Economics

SWARM keeps the monetary base of its upstream (a maximum of about 21 million coins, a halving roughly every four years) and fixes, at genesis, how every block reward is split. Nothing is minted outside block rewards.

## The allocation

In every block with a reward, for the whole emission schedule:

| Share | Recipient | Destination |
| --- | --- | --- |
| 80 % | the miner who found the block, plus all transaction fees | the miner's own payout address |
| 8 % | Core Development | `s3fLmEHc1xqs8KAe7QS7oupkhuGDjidV4eq` (2-of-3 multisig) |
| 4 % | Grants & Ecosystem | `s3RiGvK5JzS8eh6ywN3K22f2LzDAhicgFuq` (2-of-3 multisig) |
| 8 % | Community & Development Reserve | `s3g3pzQVhvVX17bzrrEN3vmcXZWSpj7KFVp` (2-of-3 multisig) |

What each fund is for: Core Development funds work on the node, indexer and wallet; Grants & Ecosystem funds tooling, documentation and community work; the Reserve is set aside for the community and for future development, with its governance to be published separately.

## Per block, by era

| Era | Heights | Block reward | Miner | Core Development | Grants & Ecosystem | Reserve | Era issuance | Cumulative |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 – 1,679,998 | 6.25 | 5.00 | 0.50 | 0.25 | 0.50 | 10,499,987.50 | 10,499,987.50 |
| 1 | 1,679,999 – 3,359,998 | 3.125 | 2.50 | 0.25 | 0.125 | 0.25 | 5,250,000.00 | 15,749,987.50 |
| 2 | 3,359,999 – 5,039,998 | 1.5625 | 1.25 | 0.125 | 0.0625 | 0.125 | 2,625,000.00 | 18,374,987.50 |
| 3 | 5,039,999 – 6,719,998 | 0.78125 | 0.625 | 0.0625 | 0.03125 | 0.0625 | 1,312,500.00 | 19,687,487.50 |
| 4 | 6,719,999 – 8,399,998 | 0.390625 | 0.3125 | 0.03125 | 0.015625 | 0.03125 | 656,250.00 | 20,343,737.50 |
| … | 30 eras in total | → 1 zatoshi | | | | | | 20,999,987.3152 |

Era 0 lasts about four years at the 75-second target; the first halving is expected around October 2030.

## Lifetime totals

Exact replay of the upstream arithmetic:

| Recipient | Coins | Share of all coins |
| --- | --- | --- |
| Miners | 16,799,990.4872 | 80.000003 % |
| Core Development | 1,679,998.7648 | 7.999999 % |
| Grants & Ecosystem | 839,999.2984 | 3.999999 % |
| Community & Development Reserve | 1,679,998.7648 | 7.999999 % |
| Total | 20,999,987.3152 | 100 % |

**Rounding.** The upstream code pays each allocation `floor(block reward × percent / 100)` in zatoshi and gives the miner the remainder. The split is exact to the zatoshi for eras 0 – 6, about the first 28 years. From era 7 the block reward is no longer evenly divisible, so each allocation is rounded down and the miner receives the sub-zatoshi remainders; in the final eras, when the whole reward is a few zatoshi, the three allocations round to zero. This is the inherited rule, not a SWARM choice, and it is why the lifetime miner share is fractionally above 80 %.

## Stated plainly

Zcash's Founders' Reward ended automatically after its first four years and totalled 10 % of supply; its later development funding has been renewed for limited periods by community decision. SWARM's allocation does not end: over the life of the chain 20 % of all coins, about 4.2 million SWM, go to the three project-side destinations. That is the design, and public wording describes it that way; SWARM does not claim a "fair launch without allocation".

## The closed start

The chain launched on 2 October 2026 with a closed start: until 31 October 2026, 15:42 UTC only the project's own machines mine, then 24 hours of early access, then public mining from 1 November 2026, 15:42 UTC. In those 29 days about 33,408 blocks and about 208,800 SWM are produced, about 0.99 % of the maximum supply. Those blocks are ordinary blocks: 80 % to the project's mining wallet, 20 % to the three funds, all visible in the explorer. There was no premine and nothing was allocated outside the block rewards.
