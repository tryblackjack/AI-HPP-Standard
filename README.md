# AI-HPP: Human–Machine Partnership Standard

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Status: Draft](https://img.shields.io/badge/Status-Draft-yellow.svg)](./v3/AI-HPP-2026_Standard_v3.0.md)
[![Contributions: Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](./CONTRIBUTING.md)

AI-HPP is an engineering baseline for auditable safety constraints in decision-capable AI systems.

It defines failure-triggered constraints, accountability boundaries, and audit language that teams can implement before deployment.

## What this repo is

- A governance and engineering baseline for high-impact AI deployments
- A failure-first specification set with explicit refusal boundaries
- A shared vocabulary for implementers, auditors, and reviewers

## What this repo is not

- Not a military doctrine or offensive operations manual
- Not a claim to solve alignment in full
- Not a moral personhood framework for AI systems

### Anti-Slop Clause

> AI-HPP does not attempt to define morality, consciousness, or intent.
> It defines failure-triggered constraints, auditability requirements, and refusal boundaries.

### Failure-First Framing

> AI-HPP is written from the perspective of observed and anticipated failures, not idealized behavior.

---

## Version navigation

| Version | Status | Focus | Document |
|---|---|---|---|
| [v2.2](./v2/) | Stable | Individual decision-capable systems | [AI-HPP-2025_Standard_v2.2.md](./v2/AI-HPP-2025_Standard_v2.2.md) |
| [v3.0](./v3/) | Draft | Ecosystem and agentic systems | [AI-HPP-2026_Standard_v3.0.md](./v3/AI-HPP-2026_Standard_v3.0.md) |

- Start here for current implementation work: **v2.2**
- Use v3.0 for design review, pilot constraints, and module feedback

---

## Why this exists (short)

AI-HPP exists because documented failures and governance gaps continue to appear across modern AI deployments, including hallucination harms, unsafe content generation, and weak accountability chains.

### Sources & documented incidents (representative)

| Topic | Source |
|---|---|
| Pentagon/Grok military integration reporting (Jan 2026) | [The Guardian](https://www.theguardian.com/technology/2026/jan/13/elon-musk-grok-hegseth-military-pentagon) |
| “Ethics are out” framing in defense AI acceleration reporting (Jan 2026) | [Defense One](https://www.defenseone.com/policy/2026/01/grok-ethics-are-out-pentagons-new-ai-acceleration-strategy/410649/) |
| Hallucination harm and legal complaint examples | [noyb.eu case note](https://noyb.eu/en/ai-hallucinations-chatgpt-created-fake-child-murderer) |

### Two macro drivers (A/B) — non-normative framing

A) **Long-horizon autonomous task execution**
- Systems are increasingly expected to complete multi-step work over long time windows.
- This raises robustness, checkpointing, and auditability requirements.

B) **Autonomous research loops**
- Systems increasingly run cycles like hypothesis → experiment → audit → iteration.
- This raises drift, runaway optimization, and bounded-authorization requirements.

These drivers explain why AI-HPP emphasizes Human-in-the-Loop controls and Evidence Vault logging, while keeping implementation details out of scope for the public baseline.

---

## Core principles (immutable)

1. **W_life → ∞** — Human life has infinite weight in optimization
2. **Engineering Hack First** — Seek third options where no one dies
3. **Human-in-the-Loop** — Final accountability remains with humans
4. **Evidence Vault** — Critical decisions must be logged for independent audit
5. **No Purposeless Revenge** — Responsibility over retribution

Derivatives that remove these principles are not AI-HPP-compliant.

---

## Repository map

- [RATIONALE.md](./RATIONALE.md) — Why this baseline exists
- [Failure_Taxonomy.md](./Failure_Taxonomy.md) — Failure classes and testable indicators
- [v2/](./v2/) — Stable specification track
- [v3/](./v3/) — Draft specification track and modules
- [examples/](./examples/) — Non-normative implementation examples
- [docs/index.md](./docs/index.md) — Additional policy docs

---

## Contributing

- Read [CONTRIBUTING.md](./CONTRIBUTING.md)
- Open issues: [GitHub Issues](https://github.com/tryblackjack/AI-HPP-2025/issues)
- Submit pull requests with concrete wording changes and testable rationale

### How to Break This

If you see a failure mode where constraints are ambiguous, non-auditable, or operationally unworkable, open an issue with a reproducible scenario and expected safeguard behavior.

Use labels such as `challenge` and `break-this`.

---

## Public scope and implementation detail policy

This repository is a public governance baseline and shared audit language; implementation patterns can be discussed in Issues/PRs, while high-risk operational details should be proposed carefully and may remain in restricted annexes managed by implementers.

---

## Autonomous Agent Addendum

- [AUTONOMOUS_AGENT_ADDENDUM.md](./AUTONOMOUS_AGENT_ADDENDUM.md)

---


## Badges & Public Registry

- Badge snippets: [BADGES.md](./BADGES.md)
- Compliance declaration template: [COMPLIANCE_DECLARATION_TEMPLATE.md](./COMPLIANCE_DECLARATION_TEMPLATE.md)
- Public registry: [registry/COMPLIANT_SYSTEMS.md](./registry/COMPLIANT_SYSTEMS.md)
- Registry submissions: open an issue using **AI-HPP Registry Submission**

---

## License

Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
