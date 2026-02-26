# BASELINE v3.17 — Inspection Entry Point

## Architecture summary
AI-HPP v3.17 preserves the canonical normative surface and introduces enforceable CES safeguards through existing modules. Normative requirements remain in `standard/`, supporting rationale in `annex/`, and machine-readable evidence contracts in `schemas/`.

## Canonical module list
- `standard/00-FOREWORD.md`
- `standard/01-PRINCIPLES.md`
- `standard/02-INTERPRETABILITY.md`
- `standard/03-ZERO-TRUST.md`
- `standard/04-DATA-PROVENANCE.md`
- `standard/05-TOOL-EXECUTION.md`
- `standard/06-VULNERABLE-GROUPS.md`
- `standard/07-PROPORTIONAL-RESPONSE.md`
- `standard/08-ADVERSARIAL-ROBUSTNESS.md`
- `standard/09-GRACEFUL-DEGRADATION.md`
- `standard/10-MULTI-JURISDICTION.md`
- `standard/11-MULTI-AGENT.md`
- `standard/12-EVIDENCE-VAULT.md`

## v3.17 CES baseline change marker
- CES safeguards are enforced normatively through `AI-HPP-07.2.1` to `AI-HPP-07.2.3` and `AI-HPP-12.2.1`.
- Evidence schemas include CES fields for domain gating, escalation metadata, safe-hold, and aggregated top-K alternatives.
- Annex G remains informative guidance for conflict-adjacent operation and does not add a new module.
- Annex H adds informative adaptive governance and high-speed deployment guidance without changing core normative semantics.

## Threat and incident coverage summary
- Threat model includes `T-CES-1` and `T-CES-2`.
- Incident corpus remains `INC-001` through `INC-013` with `INC-010` normalized for source status and evidence confidence.

## Evidence Vault schema version
- Baseline schema set: Draft 2020-12 JSON Schemas under `schemas/`.
- Evidence bundle schema: `schemas/evidence-bundle.schema.json`.
- Evidence export package schema: `schemas/audit-export.schema.json`.
- Baseline marker version: v3.17.

## Governance status
- v3.19 hardening adds escalation-timeout safe-state requirement, conditional CES mandatory Evidence Vault fields, override-accountability logging, and governance boundary clarifications without changing core safety semantics.
- No new modules were added.
- Governance integration includes informative Annex H (AGL + HSDF) with no normative requirement deltas.
- New requirements retain Requirement/Rationale/Verification structure with threat, incident, and regulatory references.
- Prior baseline markers are retained under `archive/baselines/` where applicable.
