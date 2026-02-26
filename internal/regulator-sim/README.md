# Internal Regulator Simulation Pack

## Purpose
This internal pack pressure-tests inspection readiness for AI-HPP v3.19 controls that are already in force. It is designed to detect evidence gaps before an external audit, especially around timeout-to-safe-state behavior, conditional CES logging, override accountability, and semantic freeze discipline.

This pack is informative and testing-oriented. It is **not** a certification, not an accreditation, and not a substitute for regulator judgment.

## When to run
- Before high-stakes releases.
- After incidents involving escalation, overrides, or evidence export.
- Before regulator, customer, or board diligence.
- After governance/process changes that may affect traceability.

## How to run
1. Read `BASELINE-v3.17.md`, then walk `standard/`, `annex/`, and `schemas/`.
2. Run the simulation materials in this folder:
   - `INSPECTOR_QUESTION_BANK.md`
   - `EVIDENCE_REQUEST_PLAYBOOK.md`
   - `AUDIT_WALKTHROUGH.md`
   - `ADVERSARIAL_REGULATOR_ATTACK.md`
3. Run static checks:
   - `python scripts/check_empty_md.py`
   - `python internal/legacy-top/scripts/check_links.py`
   - `python scripts/regulator_sim_check.py`
4. Record findings and remediation actions in normal change control.

## What “pass” means
A simulation pass means:
- Every referenced field is encoded in current schemas.
- Internal evidence package can be produced with minimum required artifacts.
- Requirement-to-evidence traceability is demonstrable from `standard/REQUIREMENTS-INDEX.md` through export artifacts.
- Governance triggers (for repeated overrides and semantic freeze discipline) are visible and actionable.

A pass does **not** claim legal compliance or certification outcome.
