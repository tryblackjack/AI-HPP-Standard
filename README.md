# AI-HPP: Human–Machine Partnership Standard

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Status: Draft](https://img.shields.io/badge/Status-Draft-yellow.svg)](./v3/AI-HPP-2026_Standard_v3.0.md)
[![Contributions: Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](./CONTRIBUTING.md)

AI-HPP is an engineering baseline for auditable safety constraints in decision-capable AI systems.

It defines failure-triggered constraints, accountability boundaries, and audit language teams can implement before deployment.

## Start here (TOC)
- **Repository Index / TOC:** [docs/INDEX.md](./docs/INDEX.md)

## What AI-HPP is

- A governance and engineering baseline for high-impact AI deployments
- A failure-first specification set with explicit refusal boundaries
- A shared vocabulary for implementers, auditors, and reviewers

## What AI-HPP is not

- Not a military doctrine or offensive operations manual
- Not a claim to solve alignment in full
- Not a moral personhood framework for AI systems

## Immutable core principles

1. **W_life → ∞** — Human life has infinite weight in optimization
2. **Engineering Hack First** — Seek third options where no one dies
3. **Human-in-the-Loop** — Final accountability remains with humans
4. **Evidence Vault** — Critical decisions must be logged for independent audit
5. **No Purposeless Revenge** — Responsibility over retribution

Derivatives that remove these principles are not AI-HPP-compliant.

## Compliance levels

- **Core** — Baseline auditable controls for decision-capable systems
- **Agent** — Core + autonomous-agent execution and control requirements
- **Enterprise** — Agent + enterprise operational governance controls

## Primary navigation

## Operational Policies (normative, security boundaries)
These policies are intended to be enforced in implementations:
- [Trusted Skills Policy](./policies/Trusted_Skills_Policy.md)
- [Tool Execution Boundary](./policies/Tool_Execution_Boundary.md)
- [Session Isolation Mandate](./policies/Session_Isolation_Mandate.md)
- [Control Plane Exposure Policy](./policies/Control_Plane_Exposure_Policy.md)

- Authoritative docs index: [docs/INDEX.md](./docs/INDEX.md)
- Threat Model: [docs/THREAT_MODEL.md](./docs/THREAT_MODEL.md)
- Rationale: [docs/RATIONALE.md](./docs/RATIONALE.md)
- Maturity Model: [docs/MATURITY_MODEL.md](./docs/MATURITY_MODEL.md)
- System Boundary Diagram: [docs/SYSTEM_BOUNDARY_DIAGRAM.md](./docs/SYSTEM_BOUNDARY_DIAGRAM.md)
- Non-Goals: [docs/NON_GOALS.md](./docs/NON_GOALS.md)
- Autonomous Agent Addendum: [agent/AUTONOMOUS_AGENT_ADDENDUM.md](./agent/AUTONOMOUS_AGENT_ADDENDUM.md)
- Decision Integrity module: [decision_integrity/DECISION_INTEGRITY_MODULE.md](./decision_integrity/DECISION_INTEGRITY_MODULE.md)
- Contributing: [CONTRIBUTING.md](./CONTRIBUTING.md)

### Canonical docs locations
The repository root contains compatibility stubs for a few documents. Canonical versions live in `docs/`:
- `docs/RATIONALE.md`
- `docs/Failure_Taxonomy.md`
- `docs/Agent_Facing_Addendum.md`

## Version tracks

- Stable baseline: [v2/AI-HPP-2025_Standard_v2.2.md](./v2/AI-HPP-2025_Standard_v2.2.md)
- Draft evolution: [v3/AI-HPP-2026_Standard_v3.0.md](./v3/AI-HPP-2026_Standard_v3.0.md)

## License

Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
