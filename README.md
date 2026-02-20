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


## Compliance Levels

- **Core** — baseline auditable controls for decision-capable systems
- **Agent** — Core + autonomous-agent execution and control requirements
- **Enterprise** — Agent + enterprise operational governance controls

## Repository map

- [RATIONALE.md](./RATIONALE.md) — Why this baseline exists
- [Failure_Taxonomy.md](./Failure_Taxonomy.md) — Failure classes and testable indicators
- [v2/](./v2/) — Stable specification track
- [v3/](./v3/) — Draft specification track and modules
- [examples/](./examples/) — Non-normative implementation examples
- [docs/INDEX.md](./docs/INDEX.md) — Authoritative documentation navigation

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

## Public Compliance Toolkit

- Compliance badge policy: [COMPLIANCE_BADGE_POLICY.md](./governance/compliance/COMPLIANCE_BADGE_POLICY.md)
- Badge snippets: [BADGES.md](./governance/compliance/BADGES.md)
- Compliance declaration template: [COMPLIANCE_DECLARATION_TEMPLATE.md](./governance/compliance/COMPLIANCE_DECLARATION_TEMPLATE.md)
- Compliance checklist: [COMPLIANCE_CHECKLIST.md](./governance/compliance/COMPLIANCE_CHECKLIST.md)
- Registry guide: [registry/README.md](./registry/README.md)
- Public registry: [registry/COMPLIANT_SYSTEMS.md](./registry/COMPLIANT_SYSTEMS.md)
- Registry submission issue form: [registry_submission.yml](./.github/ISSUE_TEMPLATE/registry_submission.yml)

## Autonomous Agent Addendum

- [AUTONOMOUS_AGENT_ADDENDUM.md](./AUTONOMOUS_AGENT_ADDENDUM.md)

## Agent Safety Modules

- [AUTONOMY_SCOPE_DECLARATION.md](./agent_safety/AUTONOMY_SCOPE_DECLARATION.md)
- [AUTONOMY_EVIDENCE_REQUIREMENT.md](./agent_safety/AUTONOMY_EVIDENCE_REQUIREMENT.md)
- [ECONOMIC_SAFETY_CONSTRAINT.md](./agent_safety/ECONOMIC_SAFETY_CONSTRAINT.md)
- [SKILL_PLUGIN_TRUST_LEVELS.md](./agent_safety/SKILL_PLUGIN_TRUST_LEVELS.md)
- [EXTERNAL_AGENT_INTERACTION_POLICY.md](./agent_safety/EXTERNAL_AGENT_INTERACTION_POLICY.md)
- [SAFETY_METRICS_OBSERVABILITY.md](./agent_safety/SAFETY_METRICS_OBSERVABILITY.md)


## License

Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
