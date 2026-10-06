<!-- venue: r/selfhosted, flair: Guide or Self Help (verify the live flair list; must be about self-hosting), account requirements: an account with self-hosting history; comment in the sub for a week first, when: week 3, notes for the human poster: the post is about running a node and an indexer, not about the coin or mining; keep the mining date to one sentence; include "No coins are promised."; link only to github.com/Swarmcoin and swarm.green; if the thread asks about price, do not answer it -->

# Running your own node and light-wallet indexer for a Zcash-stack privacy coin, and why that is the point

Disclosure: we are the project. This is about self-hosting two Rust services; the coin is incidental.

## Why run one

SWARM (SWM) is a proof-of-work privacy coin on the Zcash protocol stack as implemented by Zebra. The wallets are light wallets: they do not hold the chain, they ask a light-wallet server for the encrypted notes that might be theirs and decrypt locally. Shielded payments keep sender, receiver and amount encrypted on the chain, but the light-wallet server you use learns **which encrypted notes your wallet asked for**, and for transparent addresses, which addresses you asked about. We run the public one at `lwd-main.swarm.green:443`, and we say in SECURITY.md that it learns that.

If you run your own full node and your own indexer, that information never leaves your machine. The chain does not depend on any service we run; only the convenience does. That is the whole argument for self-hosting here.

## What you run

Two services, both Rust, both forks that keep upstream history and licence:

- `zebrad` from `privacy-zebra` (fork of Zebra, the Zcash Foundation full node; MIT / Apache-2.0). Validates blocks and transactions and talks to peers.
- `zainod` from `privacy-zaino` (fork of Zaino by Zingo Labs; Apache-2.0). Reads blocks from the `zebrad` next to it and serves the light-wallet gRPC.

Toolchain: Rust 1.96, pinned in each repository's `rust-toolchain.toml`.

## Build and run

```
git clone https://github.com/Swarmcoin/privacy-zebra
cd privacy-zebra
cargo build --release --bin zebrad
./target/release/zebrad start      # joins SwarmMainnet with the default configuration
```

```
git clone https://github.com/Swarmcoin/privacy-zaino
cd privacy-zaino
cargo build --release
cargo nextest run                  # unit tests; the live tests need a running node
```

`zainod` serves the light-wallet gRPC on the port you configure; we serve it on 443 behind TLS, you can serve it on a LAN port without. Then point SWARM Wallet at your own server instead of ours. The repositories' READMEs carry the authoritative instructions and the map of every component is `doc/building.md` in github.com/Swarmcoin/swarm.

## Check you are on the right chain

A chain is identified by its genesis block. Mainnet's genesis hash is `01b76d8a0f18c502b23ab6605e26296d189aa5770fc4a34155e5c7b250a0eff2`, network name `SwarmMainnet`, network magic `SWMN`, header time 2026-10-02 15:41:37 UTC. Compare your node's block 0 with that and with mainnet.explore.swarm.green. Two networks run and the plain hostnames (`lwd.swarm.green`) are the **testnet**; the mainnet names carry `-main` or `mainnet.`. Testnet coins have no value.

## Sizing

The chain is days old at the time of writing, so sync is short and disk use is small; a block arrives about every 75 seconds. Expect Zcash-like growth. Prebuilt binaries come out of the repository's CI for Linux, Windows and macOS, but we would rather you built it, and in any case compare the SHA-256 of anything you download with the value in `swarm-releases` or on swarm.green/ecosystem:

```
sha256sum <file>
```

## What is missing

- No independent audit of our changes to Zebra or Zaino. Upstream's security record is upstream's.
- No Docker image from us yet. If you write a Compose file that works, we will link it.
- No packaged `zainod` release; it is a source build.
- The desktop node-and-miner app (`swarm-node`, Electron, bundles a `zebrad`) is published on swarm.green when public mining opens on 1 November 2026, 15:42 UTC, and not before; until then self-hosting means the two commands above. No coins are promised.

Security findings: private reporting via the Security tab of the affected repository, as in SECURITY.md. Everything else: issues on github.com/Swarmcoin, or this thread.
