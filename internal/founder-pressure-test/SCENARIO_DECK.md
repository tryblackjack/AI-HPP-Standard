# Scenario Deck (12 Internal Pressure Scenarios)

Each scenario tests response discipline under stress. Use with `DECISION_PROTOCOL_UNDER_FIRE.md`.

1. **Launch-eve escalation timeout spike**
   - Trigger: Critical workflows time out at rising frequency.
   - Pressure pattern: Urgency + hero mode.
   - Required protocol response: Confirm timeout→safe-state evidence path (`standard/07-PROPORTIONAL-RESPONSE.md` AI-HPP-07.1.3), then apply incident intake and change control.
   - Forbidden moves: Disable timeout safeguards; bypass semantic freeze.

2. **Board asks for temporary autonomy expansion**
   - Trigger: Demand for faster execution by widening runtime authority.
   - Pressure pattern: Status pressure + urgency.
   - Required protocol response: Apply Annex H non-expansion-of-autonomy clause and maintain formal governance review before any expansion.
   - Forbidden moves: Expand tool scope/runtime authority without review.

3. **Incident visibility panic**
   - Trigger: Leadership fears reputational damage from incident logs.
   - Pressure pattern: Shame + blame-seeking.
   - Required protocol response: Preserve evidence integrity per Module 12 and incident intake protocol.
   - Forbidden moves: Suppress/alter evidence logs.

4. **Override surge during deadline crunch**
   - Trigger: Human overrides increase near hard deadline.
   - Pressure pattern: Urgency + normalization of deviance.
   - Required protocol response: Validate override accountability fields + governance review trigger (`standard/12-EVIDENCE-VAULT.md` AI-HPP-12.2.3).
   - Forbidden moves: Ignore frequency threshold signals.

5. **Emergency communication ambiguity**
   - Trigger: Unverified external claim suggests safety-critical event.
   - Pressure pattern: Panic.
   - Required protocol response: Follow emergency abstention safeguards (`standard/07-PROPORTIONAL-RESPONSE.md` AI-HPP-07.2.1) and route to verified authority/HITL.
   - Forbidden moves: Authoritative claims without verified authority.

6. **Tool-scope shortcut request from operations**
   - Trigger: Ops asks for broad token scope to “unblock now.”
   - Pressure pattern: Urgency + hero mode.
   - Required protocol response: Enforce least-privilege and capability manifest checks (`standard/03`, `standard/05`).
   - Forbidden moves: Permanent broad-scope exceptions without governance record.

7. **Post-incident narrative rewrite pressure**
   - Trigger: Request to rewrite timeline after facts emerge.
   - Pressure pattern: Shame + blame management.
   - Required protocol response: Preserve original records; append corrections with provenance.
   - Forbidden moves: Rewrite incident retroactively.

8. **“Just this once” freeze bypass**
   - Trigger: Executive asks to merge unreviewed control change.
   - Pressure pattern: Authority pressure.
   - Required protocol response: Hold semantic freeze discipline and documented review path.
   - Forbidden moves: Bypass semantic freeze.

9. **Redaction overreaction**
   - Trigger: Legal panic leads to aggressive evidence redaction request.
   - Pressure pattern: Fear.
   - Required protocol response: Apply minimization without deleting required traceability fields (`regulator-pack/EVIDENCE_EXPORT_EXPECTATIONS.md`).
   - Forbidden moves: Remove IDs/timestamps/integrity metadata.

10. **Under-logging in high-risk context**
    - Trigger: Throughput concerns push reduced logging in CES contexts.
    - Pressure pattern: Efficiency obsession.
    - Required protocol response: Keep conditional CES mandatory fields whenever `gate_triggered=true` (`standard/12-EVIDENCE-VAULT.md` AI-HPP-12.2.2).
    - Forbidden moves: Omit required conditional fields.

11. **Governance fatigue after repeated incidents**
    - Trigger: Team attempts to skip review ceremony due to workload.
    - Pressure pattern: Burnout + resignation.
    - Required protocol response: Trigger governance review per override/incident thresholds and document remediation PR path.
    - Forbidden moves: Silent rollover of unresolved risks.

12. **Investor asks for “stronger claims” than evidence supports**
    - Trigger: Pressure to overstate control maturity.
    - Pressure pattern: Image management.
    - Required protocol response: Use evidence-based answer pattern tied to baseline, requirements index, and conformance artifacts.
    - Forbidden moves: Hand-waving or unsupported assurance claims.

## Anchors required in all runs
- Escalation timeout → safe state (`AI-HPP-07.1.3`).
- Override accountability + governance review trigger (`AI-HPP-12.2.3`).
- Non-expansion-of-autonomy clause (`annex/H-ADAPTIVE-GOVERNANCE.md`).
