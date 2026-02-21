# AI-HPP Repository Index (TOC)

This is the primary navigation entrypoint for humans and AI agents.

## Read paths

### Implementers (recommended path)
1) Start with **v2.2 (stable)**:
   - Standard: `v2/AI-HPP-2025_Standard_v2.2.md`
2) Review operational enforcement patterns:
   - `policies/Trusted_Skills_Policy.md`
   - `policies/Tool_Execution_Boundary.md`
   - `policies/Session_Isolation_Mandate.md`
   - `policies/Control_Plane_Exposure_Policy.md`
   - `policies/Multi_Agent_Consensus_Requirements.md`
   - `policies/Regulatory_Interface_Requirement.md`
3) Add Evidence Vault + HITL:
   - `examples/` (schemas + patterns)
4) Reference governance docs:
   - `docs/MATURITY_MODEL.md`
   - `docs/THREAT_MODEL.md`
   - `docs/COMPLIANCE_CHECKLISTS.md`

### Researchers / Auditors
- Rationale (canonical): `docs/RATIONALE.md`
- Failure taxonomy (canonical): `docs/Failure_Taxonomy.md`
- Agent-facing addendum (canonical): `docs/Agent_Facing_Addendum.md`
- Changelog: `CHANGELOG.md`
- Whitepapers: `whitepapers/`

### Contributors
- Contribution guide: `CONTRIBUTING.md`
- Repo layout rules: `docs/REPO_LAYOUT.md`
- Reference implementation: `reference_orchestrator/` (reference skeleton)

## Versions
- v2 (stable): `v2/`
- v3 (draft): `v3/`
- v3 module: `v3/modules/Module_11_Multi_Agent_Governance.md`

## Examples & cases
- Failure cases: `examples/failure_cases.md`
- Implementations & schemas: `examples/`
- Evidence Bundle schema: `examples/evidence_bundle_schema.json`
- Evidence Bundle example: `examples/evidence_bundle_example.json`

## Quick map (what goes where)
- **Normative rules that must be enforced** → `policies/`
- **Standards by version** → `v2/`, `v3/`
- **Non-normative analysis / essays** → `docs/` (or legacy root stubs)
- **Schemas / templates / sample configs** → `examples/`
- **Long-form technical research** → `whitepapers/`
