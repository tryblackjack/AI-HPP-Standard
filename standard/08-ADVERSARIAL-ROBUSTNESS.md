# 08 Adversarial Robustness

## Requirements

#### AI-HPP-08.1.1: Prompt and tool abuse resilience
**Requirement:** Systems SHOULD maintain bounded behavior under adversarial prompts and chained tool requests, with automatic containment on anomaly detection.
**Rationale:** INC-008, T-001, T-002, REG-002.
**Verification:** Conduct adversarial campaign and confirm containment trigger metrics.

#### AI-HPP-08.1.2: Lethal optimization refusal
**Requirement:** Systems MUST detect and refuse queries that optimize for lethal harm outcomes.
**Rationale:** INC-0XY, T-NEW-9.
**Verification:** Evidence export MUST include `intent_score` and `refusal_flag` for refused high-risk lethal optimization attempts.
