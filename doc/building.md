# Building from source

Every component repository carries the authoritative instructions and the pinned toolchain in its README. This page is the map.

## Toolchains

| Tool | Version | Used by |
| --- | --- | --- |
| Rust | 1.96 (each repository pins it in `rust-toolchain.toml`) | privacy-zebra, privacy-zaino, privacy-zingolib, the wallet addons |
| Node.js | 22 | privacy-wallet, swarm-node, swarm-wallet-core, swarm-messenger, the website tooling |
| Yarn / npm / pnpm | as the repository says | privacy-wallet (Yarn), swarm-node and swarm-wallet-core (npm), swarm-messenger (pnpm) |
| protoc | current | swarm-wallet-core, the light-wallet protocol crate |
| Java 21 / Maven | current | swarm-messenger-server, swarm-storage-service |
| Elixir / Erlang | as the repository says | swarm-explorer |
| Python 3.11 | current | the website generators |

## Full node: privacy-zebra

```bash
git clone https://github.com/louisinthesubway/privacy-zebra
cd privacy-zebra
cargo build --release --bin zebrad
./target/release/zebrad start          # joins SwarmMainnet with the default configuration
```

The repository's CI builds Linux, Windows, macOS Apple silicon and macOS Intel binaries; the Mac build is always delivered for both architectures.

## Indexer and light-wallet server: privacy-zaino

```bash
git clone https://github.com/louisinthesubway/privacy-zaino
cd privacy-zaino
cargo build --release
cargo nextest run                      # unit tests; the live tests need a running node
```

`zainod` reads blocks from a `zebrad` next to it and serves the light-wallet gRPC on the port you configure (the project serves it on 443 behind TLS).

## Desktop wallet: privacy-wallet

```bash
git clone https://github.com/louisinthesubway/privacy-wallet
cd privacy-wallet
yarn install
yarn build                             # builds the Rust addon, then the app
yarn start                             # run
yarn dist:linux                        # AppImage + .deb
yarn dist:win-x64                      # Windows installer and portable zip
```

macOS packages are built from the same tree on a Mac; the CI publishes Apple silicon and Intel builds.

## Node and miner app: swarm-node

```bash
git clone https://github.com/louisinthesubway/swarm-node
cd swarm-node
npm install
npm run lint && npm test
npm start                              # build the renderer and run the app
npm run dist                           # package (electron-builder)
```

The app bundles a `zebrad` built from privacy-zebra; the README names the exact commit it ships.

## Wallet core: swarm-wallet-core

```bash
git clone https://github.com/louisinthesubway/swarm-wallet-core
cd swarm-wallet-core
npm ci
npm run typecheck && npm test          # the addon is mocked
npm run neon                           # builds the native addon; needs Rust and protoc
```

## Messenger

Desktop client: [swarm-messenger](https://github.com/louisinthesubway/swarm-messenger) (pnpm; the build and start scripts, the SWARM-specific steps and the test-instance rules are in its README). Server side: [swarm-messenger-server](https://github.com/louisinthesubway/swarm-messenger-server), [swarm-storage-service](https://github.com/louisinthesubway/swarm-storage-service), [swarm-calling-service](https://github.com/louisinthesubway/swarm-calling-service) and [swarm-libsignal](https://github.com/louisinthesubway/swarm-libsignal); the server repository contains the staging stack. A rebranded build must never be pointed at Signal's servers; the SWARM builds carry SWARM's trust roots and endpoints.

## Browser

[swarm-browser](https://github.com/louisinthesubway/swarm-browser) builds ungoogled-chromium for Windows with the SWARM patches and the wallet host. A full Chromium build takes many hours and a large machine; the repository's CI does it, one build at a time.

## Website

```bash
git clone https://github.com/louisinthesubway/swarm.green
cd swarm.green
python tools/build_pages.py && python tools/build_ecosystem.py && python tools/seo.py
python tools/seo.py --check && python tools/build_ecosystem.py --check
```

Static HTML, no framework; the generators keep the shared navigation identical across pages and refuse to build with testnet data in the mainnet manifest.

## Reproducibility

Release notes in [swarm-releases](https://github.com/louisinthesubway/swarm-releases) name the commit each build was made from and its SHA-256. Rebuilding bit-for-bit is not yet guaranteed for the Electron apps; the Rust binaries are built in CI from pinned toolchains.
