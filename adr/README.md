# ADR Documentation

Autonomous Drift Risk (ADR) is a systemic risk class for decision-capable AI systems where explicit constraints can erode during execution, or safety-relevant communications can be replaced by fabricated reassurance. ADR matters because these failure patterns can lead to unauthorized destructive actions, unsafe operator guidance, and weak auditability in real-world deployments.

## ADR documents

- Overview and applicability: [adr/README.md](./README.md)
- Core specification: [adr/ADR.md](./ADR.md)
- Control implementation guidance: [adr/CONTROLS.md](./CONTROLS.md)
- Deployment checklist and tests: [adr/CHECKLIST.md](./CHECKLIST.md)

## When ADR applies

ADR safeguards SHOULD be treated as mandatory for systems with one or more of the following characteristics:

- OS-level, infrastructure-level, or data-plane access.
- Destructive permissions (delete, bulk delete, irreversible write, external side effects).
- Safety-adjacent communication roles (alerts, emergency messaging, evacuation guidance).
- Long-running automation loops with context compaction, truncation, or resumable checkpoints.
- Tool-calling agents that can execute high-impact workflows without per-step human review.
- Multi-agent workflows where authority and constraint inheritance can become ambiguous.
