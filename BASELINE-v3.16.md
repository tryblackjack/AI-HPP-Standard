# BASELINE v3.16 — Inspection Entry Point

## Architecture summary
AI-HPP v3.16 preserves the frozen core normative layer and applies a public-surface simplification for inspection readiness. Normative requirements live in `standard/`, supporting threat/incident rationale in `annex/`, and machine-readable evidence contracts in `schemas/`.

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

## Threat model summary
- Core threat set: T-001, T-002, T-006 through T-011.
- Expanded threat set: T-NEW-1 through T-NEW-5 and T-NEW-8 through T-NEW-10.
- All T-NEW threats are incident-linked or explicitly marked as forward-looking risk classes.

## Incident coverage summary
- Incident corpus: INC-001 through INC-013.
- All incidents include linked threats and AI-HPP control anchors.
- No placeholder incident IDs remain.

## Conformance levels
Conformance is defined in `standard/CONFORMANCE-LEVELS.md` and supported by `regulator-pack/SELF-ASSESSMENT-CHECKLIST.md` and `regulator-pack/CONFORMANCE-EVIDENCE-MAP.md`.

## Evidence Vault schema version
- Baseline schema set: Draft 2020-12 JSON Schemas under `schemas/`.
- Evidence bundle schema: `schemas/evidence-bundle.schema.json`.
- Evidence export package schema: `schemas/audit-export.schema.json`.
- Baseline marker version: v3.16.

## Public Surface Policy
- Root is intentionally minimal; maintainer materials live in `internal/`.
- Canonical normative text lives in `standard/` with supporting normative context in `annex/`.

## Governance status
- Core Normative Layer remains frozen at v3.16 (`standard/`, `annex/`, `schemas/`).
- New baseline-affecting content requires threat reference, incident reference, and measurable verification logic.
- Prior baseline markers are retained under `archive/baselines/`.
