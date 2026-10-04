# Security policy

## Reporting a vulnerability

Please report security problems **privately**. Do not open a public issue for a vulnerability.

- Preferred: GitHub's private vulnerability reporting on the affected repository ("Security" tab → "Report a vulnerability"), or on this repository if you are unsure where it belongs.
- Alternative: email `swarmofficial@atomicmail.io` with "SECURITY" in the subject. Ask for an encryption key in a first message if you need one.

Tell us what you found, how to reproduce it, and what you think the impact is. You will get an acknowledgement within 72 hours and a first assessment within 14 days.

## What is in scope

- The SWARM-specific changes in every repository of this organisation: network definition, address handling, the wallet core, the desktop and mobile wallets, SWARM Node, SWARM Messenger and its server, SWARM Browser, the explorer and the website.
- The project-run services: the light-wallet servers, the explorers, the messenger server and the download host.

Vulnerabilities in the upstream projects (Zebra, Zaino, zingolib, Signal, Chromium) should go to those projects; tell us too if they affect SWARM users.

## What to expect

- We do not run a bug bounty at the moment. We credit reporters in the release notes if they wish.
- Coordinated disclosure: we ask for 90 days from the acknowledgement before public disclosure, less if a fix ships earlier, more only by agreement.
- Fixes for the chain itself follow the upstream practice: a network upgrade is announced with its activation height in advance; node operators and miners must update before that height.

## Honest statement of the current state

SWARM is experimental software. No independent audit of the SWARM-specific changes has been published. Builds for Windows and macOS are not yet signed with a vendor certificate. The light-wallet server learns which encrypted notes a wallet asks for. Treat every claim on the website as a claim, not a proof, until the matching evidence (checksums, source, explorer data) backs it.
