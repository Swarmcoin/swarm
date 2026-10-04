# Contributing to SWARM

Thank you for looking at the code. This page is about how to work with us; the licences and the security policy are in [LICENSE](LICENSE) and [SECURITY.md](SECURITY.md).

## Where things go

| You want to | Go to |
| --- | --- |
| Report a bug or ask for a feature in a specific app | the issues of that repository (see the table in the [README](README.md#the-software)) |
| Report a security problem | [SECURITY.md](SECURITY.md), privately |
| Ask about the project, the economics or the protocol | the issues of this repository |
| Propose a change to the chain rules | an issue here first, with the reasoning; chain changes ship only as announced network upgrades |

## Pull requests

1. Open an issue first for anything larger than a typo, so nobody does the same work twice.
2. Fork, branch from the default branch, keep the change focused.
3. Say what the change does and how you verified it. Paste the exact commands and results; a claim without evidence is a question, not a fact.
4. Keep the upstream relationship clean: SWARM repositories are forks, and changes to consensus rules or cryptography are **not** accepted in a fork; they belong upstream.
5. Do not add telemetry, analytics or any call to a third-party service to a wallet, node, messenger or browser build.
6. Name the network beside every number and link: a height, an address or a URL without "mainnet" or "testnet" next to it is a bug.

## Code style

Follow the upstream project's style in each fork (`cargo fmt` and `cargo clippy` for Rust, the repository's lint for TypeScript). Commit messages say what the change does in one line, in plain words, and why in the body.

## Licence of contributions

By contributing you agree that your contribution is licensed under the licence of the repository you contribute to (MIT, Apache-2.0, AGPL-3.0 or BSD-3-Clause, as stated there).
