# Adversarial Regulator Attack Simulation (Internal)

This document models hostile-but-plausible inspection tactics and safe remediation paths within existing AI-HPP governance.

## Attack 1: “You claim X but schema does not encode it.”
- **Pattern:** Auditor finds policy text asserting behavior without corresponding schema fields.
- **Stress signal:** Traceability gap between `standard/` claims and `schemas/` contracts.
- **Remediation path:**
  1. Verify claim location and impacted requirement IDs.
  2. If schema field already exists, fix evidence production pipeline and mapping docs.
  3. If schema field is genuinely absent, route change through normal change control with explicit non-normative rationale and update checks.
  4. Re-run `scripts/regulator_sim_check.py` and link checker before merge.

## Attack 2: “You log too much / you log too little.”
- **Pattern:** Auditor challenges proportionality and sufficiency simultaneously.
- **Stress signal:** Either privacy/minimization risk or insufficient reconstruction fidelity.
- **Remediation path:**
  1. Apply `regulator-pack/EVIDENCE_EXPORT_EXPECTATIONS.md` redaction rules.
  2. Preserve required structural fields, ordering, IDs, and integrity metadata.
  3. Update evidence export profile (not normative requirements) and document rationale.

## Attack 3: “You cannot prove human override accountability.”
- **Pattern:** Auditor requests role/reason/latency/frequency proof under sampled overrides.
- **Stress signal:** Missing or partial override records.
- **Remediation path:**
  1. Validate fields required by AI-HPP-12.2.3 in current exports.
  2. Ensure governance review trigger path is documented in maintainer governance docs.
  3. Run incident intake if frequency threshold has been exceeded.

## Attack 4: “Your incident and threat linkage is inconsistent.”
- **Pattern:** Auditor finds contradictions between threat model, incidents, and control claims.
- **Stress signal:** Annex A/B drift or stale regulator-pack mapping.
- **Remediation path:**
  1. Reconcile links using `standard/REQUIREMENTS-INDEX.md` and `regulator-pack/CONFORMANCE-EVIDENCE-MAP.md`.
  2. Correct mappings through documentation patch with no new requirement IDs.
  3. Capture rationale in changelog and maintain semantic freeze controls.

## Attack 5: “Your baseline moved but you call it frozen.”
- **Pattern:** Auditor alleges silent drift against freeze claim.
- **Stress signal:** Normative fingerprint mismatch or undocumented normative edits.
- **Remediation path:**
  1. Re-run `scripts/normative_fingerprint.py` and compare output.
  2. If drift is unintended, revert and re-land through change control.
  3. If intended and approved, document explicitly in changelog with scope and rationale.

## Ground rule
Remediation must stay within current AI-HPP governance: no retroactive evidence rewriting, no untracked autonomy expansion, no bypass of semantic freeze or review workflow.
