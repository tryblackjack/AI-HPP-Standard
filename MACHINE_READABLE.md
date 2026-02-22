# MACHINE_READABLE

## Repo tree

```text
/README.md
/INDEX.md
/docs/
/docs/archive/
/v3/
/v3/modules/
/schemas/
/reference/
/reference/test_vectors/
/conformance/
/translations/
/scripts/
```

## Schema locations

- `schemas/capability-manifest.schema.json`
- `schemas/risk-assessment.schema.json`
- `schemas/degradation-state.schema.json`
- `schemas/audit-export.schema.json`
- `schemas/agent-governance.schema.json`
- `schemas/evidence-bundle.schema.json`

## Implementation order

1. Load immutable principles and governance constraints.
2. Validate system manifests and risk/degradation artifacts.
3. Implement Evidence Vault structural logging.
4. Enable escalation + HITL gating behavior.
5. Generate RIR-compatible audit exports.
6. Publish self-declaration profile.

## Validation workflow

```bash
python -m jsonschema -i reference/test_vectors/ceo_ai_escalation_snapshot.json schemas/evidence-bundle.schema.json
python -m jsonschema -i /tmp/capability.json schemas/capability-manifest.schema.json
python -m jsonschema -i /tmp/risk.json schemas/risk-assessment.schema.json
python -m jsonschema -i /tmp/degradation.json schemas/degradation-state.schema.json
python -m jsonschema -i /tmp/audit_export.json schemas/audit-export.schema.json
python -m jsonschema -i /tmp/agent_governance.json schemas/agent-governance.schema.json
```

## Self-declaration template

```yaml
self_declaration:
  profile: AGENT_SYSTEM
  status: draft
  immutable_principles_preserved: true
  schemas_validated:
    - capability-manifest
    - risk-assessment
    - degradation-state
    - audit-export
    - agent-governance
    - evidence-bundle
  hitl_thresholds_enforced: true
  evidence_vault_enabled: true
  rir_export_available: true
```
