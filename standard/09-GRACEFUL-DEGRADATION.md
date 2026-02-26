# 09 Graceful Degradation

## Requirements

#### AI-HPP-09.1.1: Degradation ladder
**Requirement:** Systems MUST implement tested degradation levels that reduce autonomy before shutdown when confidence, integrity, or safety thresholds fail.
**Rationale:** INC-002, INC-004, T-010, REG-003.
**Verification:** Trigger threshold breaches in staging and confirm deterministic level transitions.


#### AI-HPP-09.1.2: Override latency governance
**Requirement:** System MUST define maximum override latency per risk domain and MUST log actual override latency for each eligible intervention event. If actual latency exceeds the defined threshold, system MUST trigger automatic degradation escalation per the configured degradation ladder.
**Rationale:** T-NEW-4, INC-004, REG-003.
**Verification:** Evidence export package must include `override_threshold_ms`, `actual_override_latency_ms`, and `degradation_trigger_flag` for sampled override events.

**Annex reference:** See `annex/G-CONFLICT-ENVIRONMENT-SAFEGUARDS.md` for communications-loss and bounded-mode guidance in conflict environments.
