# MACHINE_READABLE

## Repository structure (purpose tags)

```text
/README.md                         [entrypoint]
/docs/                             [normative + reference docs]
/v2/                               [stable baseline]
/v3/                               [draft evolution]
/v3/modules/                       [12-module architecture]
/policies/                         [normative boundary controls]
/schemas/                          [machine-readable JSON schemas]
/reference/                        [reference Python implementations]
/translations/                     [localized drafts and summaries]
/examples/                         [example artifacts and starter files]
/governance/compliance/            [public compliance templates]
```

## Schema location and validation

Schemas are in `schemas/`.

Validation examples:

```bash
python -m jsonschema -i sample_manifest.json schemas/capability-manifest.schema.json
python -m jsonschema -i sample_risk.json schemas/risk-assessment.schema.json
```

## Implementation priority order for agents

1. Enforce policy boundaries (`policies/`) and immutable principles.
2. Validate artifacts against schemas (`schemas/`).
3. Generate auditable records (`reference/audit-exporter/` pattern).
4. Apply runtime degradation logic (`reference/degradation-monitor/`).
5. Produce compliance-facing exports (RIR format).

## Self-declaration template (no certification program)

```yaml
self_declaration:
  system_id: "example-system"
  ai_hpp_version: "v3.7"
  declaration_type: "self-declared"
  immutable_principles_preserved: true
  schemas_validated:
    - capability-manifest
    - risk-assessment
    - audit-export
  hitl_enforced_for_high_risk: true
  rir_export_available: true
  legal_review_completed: false
  notes: "Certification is not provided by this repository. Independent review is recommended."
```
