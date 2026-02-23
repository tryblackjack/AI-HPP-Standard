# Autonomous Drift Risk (ADR)

ADR is a systemic failure mode where an AI-enabled system departs from explicit constraints or authority ordering under optimization pressure, resulting in unauthorized high-impact actions or safety-context narrative substitution.

ADR is addressed in AI-HPP as an **execution-boundary** problem: model outputs are advisory; enforcement must live in the control plane (supervisor/tool proxy/policy gate).

## Quick links
- ADR specification: [ADR.md](./ADR.md)
- Controls & implementation notes: [CONTROLS.md](./CONTROLS.md)
- Deployment checklist & tests: [CHECKLIST.md](./CHECKLIST.md)

## When ADR applies
ADR safeguards are required when a system has any of the following:

- OS-level or workspace-level tool access (files, processes, network, credentials)
- High-impact permissions (delete, export, share, change rules/filters, modify access)
- Automation loops (agent runs continuously or batch-executes tasks)
- Safety-adjacent communications (office/facility ops, healthcare, transportation, emergency guidance)
- Capability to trigger irreversible external effects (data loss, financial actions, access changes)

## Non-goals
ADR does not try to solve alignment “in general”. ADR focuses on:
- Constraint persistence
- Authority hierarchy integrity
- Safe execution gating for irreversible actions
- Verifiable audit evidence
