# Schemas

Machine-readable schemas for AI-HPP artifacts.

- `capability-manifest.schema.json`: Declared capabilities and sandbox controls.
- `risk-assessment.schema.json`: Threat entries, aggregate score, proportional response level.
- `degradation-state.schema.json`: Runtime degradation state event format.
- `audit-export.schema.json`: Evidence Export Package schema with redaction and integrity metadata.
- `agent-governance.schema.json`: Governance policy object covering Human-in-the-Loop (HITL), refusal boundaries, and tool boundaries.
- `evidence-bundle.schema.json`: Canonical Evidence Bundle format for auditable decisions.

Core status: `schemas/` is part of the Core Normative Layer frozen at baseline v3.15.

## Validation

Example validation command:

```bash
python -m jsonschema -i sample.json schemas/capability-manifest.schema.json
```

Any validator supporting JSON Schema Draft 2020-12 is compatible.
