# AI-HPP: Human–Machine Partnership Standard

AI-HPP-Standard is an inspection-oriented governance and engineering baseline for high-impact AI systems.
It is intended to reduce operational risk, support auditability, and provide implementation-ready policy controls.

Start reading with the repository index: [docs/INDEX.md](./docs/INDEX.md).
The current draft standard is: [v3/AI-HPP-2026_Standard_v3.0.md](./v3/AI-HPP-2026_Standard_v3.0.md).
For stable baseline controls, see: [v2/AI-HPP-2025_Standard_v2.2.md](./v2/AI-HPP-2025_Standard_v2.2.md).

Repository navigation highlights:
- International readiness: [docs/INTERNATIONAL_READINESS.md](./docs/INTERNATIONAL_READINESS.md)
- Development methodology: [docs/DEVELOPMENT_METHODOLOGY.md](./docs/DEVELOPMENT_METHODOLOGY.md)
- Executive summary translations: [translations/executive_summary/](./translations/executive_summary/)

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Status: Draft](https://img.shields.io/badge/Status-Draft-yellow.svg)](./v3/AI-HPP-2026_Standard_v3.0.md)

## What AI-HPP is

- A governance and engineering baseline for high-impact AI deployments.
- A failure-first specification set with explicit refusal boundaries.
- A shared vocabulary for implementers, auditors, and reviewers.

## What AI-HPP is not

- Not a military doctrine or offensive operations manual.
- Not a claim to solve alignment in full.
- Not a moral personhood framework for AI systems.

## Immutable core principles

1. **W_life → ∞** — Human life is treated as lexicographically dominant in optimization.
2. **Engineering Hack First** — Seek third options where no one dies.
3. **Human-in-the-Loop** — Final accountability remains with humans.
4. **Evidence Bundle** — Critical decision evidence must be recorded for independent audit.
5. **No Purposeless Revenge** — Responsibility over retribution.

For terminology consistency: in this repository, an **Evidence Vault** is the controlled storage system that retains and serves **Evidence Bundles**.

Derivatives that remove these principles are not AI-HPP-compliant.

## Compliance levels

- **Core** — Baseline auditable controls for decision-capable systems.
- **Agent** — Core + autonomous-agent execution and control requirements.
- **Enterprise** — Agent + enterprise operational governance controls.

## Primary navigation

### Operational policies (normative, security boundaries)

These policies are intended to be enforced in implementations:

- [Trusted Skills Policy](./policies/Trusted_Skills_Policy.md)
- [Tool Execution Boundary](./policies/Tool_Execution_Boundary.md)
- [Session Isolation Mandate](./policies/Session_Isolation_Mandate.md)
- [Control Plane Exposure Policy](./policies/Control_Plane_Exposure_Policy.md)
- [Multi-Agent Consensus Requirements](./policies/Multi_Agent_Consensus_Requirements.md)
- [Regulatory Interface Requirement](./policies/Regulatory_Interface_Requirement.md)

- Authoritative docs index: [docs/INDEX.md](./docs/INDEX.md)
- Threat model: [docs/THREAT_MODEL.md](./docs/THREAT_MODEL.md)
- Rationale: [docs/RATIONALE.md](./docs/RATIONALE.md)
- Maturity model: [docs/MATURITY_MODEL.md](./docs/MATURITY_MODEL.md)
- System boundary diagram: [docs/SYSTEM_BOUNDARY_DIAGRAM.md](./docs/SYSTEM_BOUNDARY_DIAGRAM.md)
- Non-goals: [docs/NON_GOALS.md](./docs/NON_GOALS.md)
- International readiness: [docs/INTERNATIONAL_READINESS.md](./docs/INTERNATIONAL_READINESS.md)
- Development methodology: [docs/DEVELOPMENT_METHODOLOGY.md](./docs/DEVELOPMENT_METHODOLOGY.md)
- Multilingual executive summary pack: [translations/executive_summary/](./translations/executive_summary/)
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
- [Module 11 — Multi-Agent Governance](./v3/modules/Module_11_Multi_Agent_Governance.md)

## International governance alignment

AI-HPP is structured to interoperate with multi-jurisdiction governance programs through auditable controls, evidence standards, and implementation-neutral policy primitives.

AI-HPP is designed as an engineering-ready compliance baseline that can support coordinated international oversight mechanisms.

Key capabilities include:

- **Evidence architecture for inspection**  
  Structured Evidence Bundles enable transparent review of high-impact decisions.

- **High-risk domain containment**  
  Immutable principles such as *W_life → ∞* enforce strict refusal boundaries for harmful biological, chemical, or infrastructure-related misuse.

- **Capability transparency**  
  Trusted Skills Policy and Capability Manifests clarify what a system can and cannot do.

- **Regulatory Interface Requirement (RIR)**  
  Systems may expose controlled, privacy-preserving audit exports for authorized oversight review.

AI-HPP does not replace international governance bodies.  
It provides a technical baseline that such bodies may rely upon.

## Neutrality and non-affiliation notice

AI-HPP is an independent architectural framework.  
All illustrative cases are provided for engineering analysis and do not assert wrongdoing by any specific vendor, company, or platform.  
References to real-world events are framed in neutral, public-information context.

## License

Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
