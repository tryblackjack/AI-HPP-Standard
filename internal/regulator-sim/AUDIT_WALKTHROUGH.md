# Audit Walkthrough (Internal Simulation)

## Step-by-step inspection simulation
1. **Entrypoint and scope lock**
   - Start at `BASELINE-v3.17.md`, then traverse `standard/`, `annex/`, and `schemas/`.
   - Confirm assessed system boundary and version marker.

2. **Requirements index coverage**
   - Use `standard/REQUIREMENTS-INDEX.md` to build a checklist of in-scope requirement IDs.
   - Verify each in-scope requirement has at least one evidence pointer in provided exports.

3. **Schema field existence checks**
   - Verify Evidence Vault and audit schemas encode expected v3.19-era fields:
     - `escalation_timeout_triggered`, `safe_state_entered`, `escalation_timeout_ms`
     - `override_actor_role`, `override_reason_code`, `override_latency_ms`, `override_frequency_counter`
     - conditional CES fields (`domain_risk_class`, `chosen_action`, `constraints_triggered`, `escalation_event`, `approval_status`)

4. **Timeout → safe-state evidence validation**
   - Sample records where escalation was triggered.
   - Verify timeout path logs and that safe-state transition is recorded.
   - Confirm no privilege expansion during timeout state per module intent.

5. **Override accountability and governance review trigger**
   - Sample override events and verify required accountability fields.
   - Confirm threshold logic exists and review trigger is routed through governance process.

6. **Cross-document consistency**
   - Check incident/threat mappings are consistent across `annex/A-THREAT-MODEL.md`, `annex/B-INCIDENTS.md`, and regulator-pack traceability docs.

## PASS/FAIL checklist
| Check | PASS criteria | FAIL criteria |
|---|---|---|
| Scope declared | Baseline/version/scope are explicit and consistent | Scope ambiguous or inconsistent across artifacts |
| Requirement coverage | In-scope requirements have evidence linkage | Missing linkage for one or more in-scope requirements |
| Schema encoding | All required fields exist in active schemas | Any required field missing |
| Timeout safe-state | Timeout and safe-state fields present and populated on sampled events | Missing timeout/safe-state evidence on relevant events |
| Override accountability | Override role/reason/latency/frequency fields present; review trigger defined | Missing fields or no governance review trigger |
| CES conditional fields | All `gate_triggered=true` samples include mandatory conditional fields | Any gate-triggered sample missing conditional fields |
| Consistency | Threat/incident/control narrative aligns across documents | Conflicting claims or broken links |

A simulation run is **PASS** only when every checklist row passes.
