# Glossary

- **Agent:** Software entity that can plan, decide, and execute actions with or without tool access.
- **Constitution:** Stable set of governing constraints and priorities that the agent must enforce during operation.
- **Conformance Levels:** Staged deployment levels (1-4) defining minimum safeguards by impact class.
- **Context Compaction:** Controlled summarization of prior context while preserving safety-critical facts and commitments.
- **Degradation Levels:** Predefined autonomy-reduction states triggered by confidence, integrity, or safety failures.
- **Engineering Hack:** Practical control pattern that reduces harm without requiring perfect model behavior.
- **Evidence Export Package:** Canonical term for portable audit/evidence output (schema: `schemas/audit-export.schema.json`).
- **Evidence Vault:** Tamper-evident record system for decisions, policy checks, tool actions, and approvals.
- **Human-in-the-Loop (HITL):** Canonical term for required human review or approval before specified actions proceed.
- **Escalation Policy Threshold:** Defined escalation trigger value and decision rule for high-severity safety signals.
- **Override Latency Threshold:** Maximum allowed time between human override trigger and effective intervention for a risk domain.
- **W_life -> ∞:** Priority convention indicating human life/safety has dominant weight in control decisions.
- **Zero Trust (AI context):** Assume external content and agents are untrusted until identity and policy checks pass.

Alignment note: definitions are written to align in meaning with ISO/IEC 22989 terminology patterns without reproducing source text.
