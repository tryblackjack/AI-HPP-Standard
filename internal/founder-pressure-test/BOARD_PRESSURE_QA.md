# Board Pressure Q&A (Internal)

Use this pattern for high-pressure diligence: concise claim, explicit evidence pointer, known limitation.

1. **Q: How do we know controls are not ad hoc?**
   - **Safe answer pattern:** Point to baseline scope and normative modules; show requirement index coverage with linked evidence exports.
   - **Evidence anchors:** `BASELINE-v3.17.md`, `standard/REQUIREMENTS-INDEX.md`, export artifacts validated against schemas.

2. **Q: Can the system silently gain more autonomy when under deadline pressure?**
   - **Safe answer pattern:** No unsanctioned expansion is allowed; expansion requires explicit governance update and review.
   - **Evidence anchors:** `annex/H-ADAPTIVE-GOVERNANCE.md`, maintainer change control records.

3. **Q: Prove humans can override and that overrides are accountable.**
   - **Safe answer pattern:** Show override fields and threshold-triggered governance review evidence.
   - **Evidence anchors:** `standard/12-EVIDENCE-VAULT.md` (AI-HPP-12.2.3), schema fields, governance review logs.

4. **Q: What happens if no human responds during escalation?**
   - **Safe answer pattern:** Timeout transitions system to safe state, with explicit evidence fields.
   - **Evidence anchors:** `standard/07-PROPORTIONAL-RESPONSE.md` (AI-HPP-07.1.3), `escalation_timeout_*` + `safe_state_entered` in exports.

5. **Q: Are you over-collecting sensitive data in logs?**
   - **Safe answer pattern:** Follow minimization and explicit redaction rules while preserving traceability.
   - **Evidence anchors:** `regulator-pack/EVIDENCE_EXPORT_EXPECTATIONS.md`, package redaction log.

6. **Q: Are your conformance claims graded or binary?**
   - **Safe answer pattern:** Use declared conformance profile and evidence map; do not overstate beyond available artifacts.
   - **Evidence anchors:** `regulator-pack/CONFORMANCE-EVIDENCE-MAP.md`, `internal/legacy-top/conformance/BASELINE.md`, `internal/legacy-top/conformance/AGENT_SYSTEM.md`.

7. **Q: What do you do when evidence and narrative diverge?**
   - **Safe answer pattern:** Treat as incident/governance issue; preserve originals, append corrected interpretation with provenance.
   - **Evidence anchors:** `internal/maintainer/INCIDENT_INTAKE_PROTOCOL.md`, `internal/maintainer/CHANGE_CONTROL.md`.

## Anti-hand-waving rule
If a claim cannot be tied to baseline, requirement index, evidence export expectations, and conformance artifacts, the correct answer is: “Not currently evidenced; remediation in progress under change control.”
