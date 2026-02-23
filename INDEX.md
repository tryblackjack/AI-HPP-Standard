# AI-HPP Repository Index

## Purpose (10 lines)
1. AI-HPP is a vendor-neutral engineering standard for decision-capable AI safety.
2. The repository preserves Draft status while improving audit readiness.
3. Core principles remain immutable and normative.
4. Evidence Vault and HITL are required accountability boundaries.
5. Schemas provide machine-readable interoperability for implementation.
6. Threat modeling and failure taxonomy support risk-first design.
7. Conformance is self-declared; no certification program is defined.
8. Historical artifacts are preserved in structured archives.
9. Translations are retained with freshness tracking metadata.
10. The goal is practical, court-compatible traceability at scale.

## Repository tree (annotated)
- `README.md` — entrypoint and version/status badges.
- `docs/` — normative and operational guidance.
- `docs/archive/` — archived superseded/experimental/historical docs.
- `v3/` — current draft standard and modules.
- `v2/` — stable historical baseline.
- `schemas/` — JSON Schema Draft 2020-12 artifacts.
- `adr/` — Autonomous Drift Risk (ADR) specification and controls.
- `reference/` — reference code and test vectors.
- `conformance/` — self-declaration conformance profiles.
- `translations/` — multilingual copies with freshness metadata.
- `scripts/` — local hygiene tooling (links + language checks).

## Start paths by role
- Engineer: `MACHINE_READABLE.md`
- Auditor: `schemas/README.md`
- Policymaker: `docs/INDEX.md`
- Autonomous AI Agent: `conformance/AGENT_SYSTEM.md`

## ADR safeguards
- Overview: `adr/README.md`
- Core specification: `adr/ADR.md`
- Controls and implementation notes: `adr/CONTROLS.md`
- Deployment checklist: `adr/CHECKLIST.md`
