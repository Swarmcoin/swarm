# Networks

Two SWARM networks run. The rule to remember: **the plain hostnames are the testnet; the mainnet names say so.**

| | Mainnet | Testnet |
| --- | --- | --- |
| Name shown in software | `SwarmMainnet` | `SwarmTestnet` |
| Live since | 2 October 2026, 15:42 UTC | 21 September 2026 |
| Coins | SWM, real | no value, mined in the open |
| Light-wallet server (gRPC over TLS) | `lwd-main.swarm.green:443` | `lwd.swarm.green:443` |
| Explorer | https://mainnet.explore.swarm.green (also https://explore.swarm.green) | https://testnet.explore.swarm.green/ |
| Status feed | https://lwd-main.swarm.green/status.json | — |
| Downloads | https://lwd-main.swarm.green/downloads/ (linked from swarm.green) | — |
| Shielded address prefix | `swm1…` | `swarm1…` |
| Transparent address prefixes | `s1…` (P2PKH), `s3…` (P2SH) | testnet prefixes |
| Messenger | `chat.swarm.green` | — |

## How to tell at a glance

- **Addresses.** `swm1…` is mainnet, `swarm1…` is testnet. A wallet refuses to send to an address of the other network.
- **Explorer.** Every page of the explorer carries the network name in its ribbon, header chip and title.
- **Wallet.** The wallet names the network beside the balance; a fresh install is on mainnet.
- **Status feed.** `status.json` on the mainnet host reports the mainnet genesis hash, `01b76d8a…`.

## Running your own

A full node (`zebrad` from [privacy-zebra](https://github.com/louisinthesubway/privacy-zebra)) joins the network by itself; it needs no account and no key. A light-wallet server (`zainod` from [privacy-zaino](https://github.com/louisinthesubway/privacy-zaino)) sits beside a node and serves wallets; pointing SWARM Wallet at your own server removes the project's server from the picture. Build instructions: [building.md](building.md).

## Operational note

The project-run endpoints above are operated by the project and can be moved or go down. The chain does not depend on them: peers find each other through the node's peer discovery, and any node can serve any indexer.
