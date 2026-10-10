<!-- venue: r/selfhosted, flair: Guide or Self Help (verify the live flair list; must be about self-hosting), account requirements: an account with self-hosting history; comments in r/selfhosted for at least a week before posting (10 to 21 October 2026 is comments-only), when: Thu 29 Oct 2026 15:00 UTC (not Friday: r/selfhosted moves vibe-coded project posts into a Friday thread), notes for the human poster: the body starts with "I work on SWARM."; the post is about running a node and an indexer, not about the coin; keep the mining date to one sentence; "No coins are promised." and the ASIC sentence stay in; link only to github.com/Swarmcoin and swarm.green; if the thread asks what SWM is worth, answer with the one sentence in the last section and nothing more; the story's source, for a reader who asks: CoinGecko's profile of Hal Finney (coingecko.com/learn/who-is-hal-finney-first-bitcoin-transaction) -->

# "Running bitcoin": a network starts when a second person runs it. A guide to self-hosting a node and light-wallet indexer for SWARM

I work on SWARM. We built it, nothing in this post is for sale, and we will not discuss what SWM is worth; this is about self-hosting two Rust services.

## 11 January 2009

On 11 January 2009 Hal Finney posted two words: "Running bitcoin". Finney was a cypherpunk who had worked on PGP and had built a reusable proof-of-work system in 2004. Bitcoin's software had been released days before, and he was one of the first people other than its author to run it. The next day he received the first Bitcoin transaction, 10 BTC from Satoshi Nakamoto. (Dates from CoinGecko's profile of Finney.)

Finney was diagnosed with ALS later that year and kept writing code while the illness took his movement; he died in 2014. The part that matters for this sub is smaller and quieter than his life: one person started a program on his own machine, and a piece of software became a network.

The lesson: a network begins when a second person runs it, and its independence is counted in independent nodes, not in users, downloads or followers. A chain whose nodes all belong to the people who wrote it is still one party's ledger.

## Why I am telling you this

Our chain has been live since 2 October 2026, 15:42 UTC, and today a wallet that uses our public light-wallet server depends on a machine we run. That is the honest state of a new network. The fix is people running their own, which is what this sub does better than anyone.

## What is unfinished, first

- No independent audit of the SWARM-specific changes to the node and the indexer has been published. Upstream's security record is upstream's.
- No Docker image from us yet. If you write a Compose file that works, we will link it.
- No packaged `zainod` release; it is a source build.
- The desktop node-and-miner app (`swarm-node`, Electron, bundles a `zebrad`) is published on swarm.green when public mining opens on 1 November 2026, 15:42 UTC, and not before. No coins are promised. Please keep ASICs and rented hash power off the network.
- Desktop builds of the apps are unsigned; the browser is a Windows-only pre-release without tracker blocking or phishing lists; the messenger is a first release, one desktop per account, no phone app.
- Shielding hides what is on the chain, not that you use SWARM from your ISP.

## Why run one

SWARM is a proof-of-work privacy coin built on open-source foundations that have secured real value, left unmodified. The wallets are light wallets: they do not hold the chain, they ask a light-wallet server for the encrypted notes that might be theirs and decrypt locally. Shielded payments keep sender, receiver and amount encrypted on the chain, but the light-wallet server you use learns **which encrypted notes your wallet asked for**, and for transparent addresses, which addresses. We run the public one at `lwd-main.swarm.green:443`, and SECURITY.md says plainly that it learns that.

Run your own full node and indexer and that information never leaves your machine. The chain does not depend on any service we run; only the convenience does.

## What you run

Two Rust services, both forks that keep upstream history and licence:

- `zebrad`, from the node repository (its name is in the README of github.com/Swarmcoin/swarm; MIT / Apache-2.0). Validates blocks and transactions and talks to peers.
- `zainod`, from `privacy-zaino` (Apache-2.0). Reads blocks from the `zebrad` next to it and serves the light-wallet gRPC.

Toolchain: Rust 1.96, pinned in each repository's `rust-toolchain.toml`.

## Build and run

```
git clone https://github.com/Swarmcoin/<node repository>
cd <node repository>
cargo build --release --bin zebrad
./target/release/zebrad start      # joins SwarmMainnet with the default configuration
```

```
git clone https://github.com/Swarmcoin/privacy-zaino
cd privacy-zaino
cargo build --release
cargo nextest run                  # unit tests; the live tests need a running node
```

`zainod` serves the light-wallet gRPC on the port you configure; we serve it on 443 behind TLS, you can serve it on a LAN port without. Then point SWARM Wallet at your own server instead of ours. The READMEs carry the authoritative instructions, and the map of every component is `doc/building.md` in github.com/Swarmcoin/swarm.

## Check you are on the right chain

A chain is identified by its genesis block. The genesis hash is `01b76d8a0f18c502b23ab6605e26296d189aa5770fc4a34155e5c7b250a0eff2`, network name `SwarmMainnet`, network magic `SWMN`, header time 2026-10-02 15:41:37 UTC. Compare your node's block 0 with that and with mainnet.explore.swarm.green. Use the hostnames that carry `-main` or `mainnet.`.

## Sizing

The chain is weeks old, so sync is short and disk use is small; a block arrives about every 75 seconds. Expect growth like the upstream chain's over time. If you download any binary instead of building, take it only from swarm.green/ecosystem and compare its SHA-256 with the value on the page before you run it:

```
sha256sum <file>          # Linux
Get-FileHash <file>       # Windows PowerShell
```

## The coin, briefly

The closed start runs until 31 October 2026, 15:42 UTC (project machines only, about 33,408 blocks, about 208,800 SWM, about 0.99 % of the cap); the waiting list gets the next 24 hours; public mining from 1 November 2026, 15:42 UTC. We do not dress this up: 20 % of every block goes to the project for the life of the chain, 8 % Core Development, 4 % Grants & Ecosystem, 8 % Community & Development Reserve, about 4.2 million SWM to 2-of-3 multisig addresses fixed in the genesis rules; 80 % goes to the miner plus fees. Nothing exists before it is mined. What is SWM worth? Whatever people agree it is worth. Nobody promises you a price, and SWM can lose all its value.

Security findings: private reporting via the Security tab of the affected repository, as in SECURITY.md. Everything else: issues on github.com/Swarmcoin, or this thread.
