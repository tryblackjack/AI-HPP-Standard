# AI-HPP Repository Index (TOC)

This is the primary navigation entrypoint for humans and AI agents.

## Read paths

### Implementers (recommended path)
1) Start with **v2.2 (stable)**:
   - Standard: [v2/AI-HPP-2025_Standard_v2.2.md](../v2/AI-HPP-2025_Standard_v2.2.md)
2) Review operational enforcement patterns:
   - [policies/Trusted_Skills_Policy.md](../policies/Trusted_Skills_Policy.md)
   - [policies/Tool_Execution_Boundary.md](../policies/Tool_Execution_Boundary.md)
   - [policies/Session_Isolation_Mandate.md](../policies/Session_Isolation_Mandate.md)
   - [policies/Control_Plane_Exposure_Policy.md](../policies/Control_Plane_Exposure_Policy.md)
   - [policies/Multi_Agent_Consensus_Requirements.md](../policies/Multi_Agent_Consensus_Requirements.md)
   - [policies/Regulatory_Interface_Requirement.md](../policies/Regulatory_Interface_Requirement.md)
3) Add Evidence Vault + HITL:
   - [examples/](../examples/) (schemas + patterns)
4) Reference governance docs:
   - [docs/MATURITY_MODEL.md](./MATURITY_MODEL.md)
   - [docs/THREAT_MODEL.md](./THREAT_MODEL.md)
   - [docs/COMPLIANCE_CHECKLISTS.md](./COMPLIANCE_CHECKLISTS.md)

### Researchers / Auditors
- Rationale (canonical): [docs/RATIONALE.md](./RATIONALE.md)
- Failure taxonomy (canonical): [docs/Failure_Taxonomy.md](./Failure_Taxonomy.md)
- Agent-facing addendum (canonical): [docs/Agent_Facing_Addendum.md](./Agent_Facing_Addendum.md)
- International readiness: [docs/INTERNATIONAL_READINESS.md](./INTERNATIONAL_READINESS.md)
- Changelog: [CHANGELOG.md](../CHANGELOG.md)
- Whitepapers: [whitepapers/](../whitepapers/)

### Contributors
- Contribution guide: [CONTRIBUTING.md](../CONTRIBUTING.md)
- Repo layout rules: [docs/REPO_LAYOUT.md](./REPO_LAYOUT.md)
- Reference implementation: [reference_orchestrator/](../reference_orchestrator/) (reference skeleton)

## Versions
- v2 (stable): [v2/](../v2/)
- v3 (draft): [v3/](../v3/)
- v3 module: [v3/modules/Module_11_Multi_Agent_Governance.md](../v3/modules/Module_11_Multi_Agent_Governance.md)

## Examples & cases
- Failure cases: [examples/failure_cases.md](../examples/failure_cases.md)
- Implementations & schemas: [examples/](../examples/)
- Evidence Bundle schema: [examples/evidence_bundle_schema.json](../examples/evidence_bundle_schema.json)
- Evidence Bundle example: [examples/evidence_bundle_example.json](../examples/evidence_bundle_example.json)

## Quick map (what goes where)
- **Normative rules that must be enforced** → [policies/](../policies/)
- **Standards by version** → [v2/](../v2/), [v3/](../v3/)
- **Non-normative analysis / essays** → [docs/](./) (or legacy root stubs)
- **Schemas / templates / sample configs** → [examples/](../examples/)
- **Long-form technical research** → [whitepapers/](../whitepapers/)
