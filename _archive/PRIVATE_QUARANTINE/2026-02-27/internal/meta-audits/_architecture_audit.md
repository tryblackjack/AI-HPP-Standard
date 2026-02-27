SAFE_FOR_PUBLIC_REPO: YES
NO PRODUCTION DATA. NO SECRETS. NO CUSTOMER INFO.

# Architecture Audit

## 1) Missing declared directories
- None.

## 2) Extra top-level directories not declared in INDEX.md
- `.github`
- `adr`
- `agent`
- `agent_safety`
- `conformance`
- `decision_integrity`
- `docs`
- `enterprise_governance`
- `examples`
- `internal`
- `policies`
- `reference_orchestrator`
- `registry`
- `scripts`
- `v2`
- `v3`

## 3) Files located outside declared INDEX structure
- Total: 88 files.
  - `AUTHORS.md`
  - `INDEX.md`
  - `LICENSE`
  - `adr/ADR.md`
  - `adr/CHECKLIST.md`
  - `adr/CONTROLS.md`
  - `adr/README.md`
  - `agent/AUTONOMOUS_AGENT_ADDENDUM.md`
  - `agent/Agent_Facing_Addendum.md`
  - `agent_safety/AUTONOMY_EVIDENCE_REQUIREMENT.md`
  - `agent_safety/AUTONOMY_SCOPE_DECLARATION.md`
  - `agent_safety/ECONOMIC_SAFETY_CONSTRAINT.md`
  - `agent_safety/EXTERNAL_AGENT_INTERACTION_POLICY.md`
  - `agent_safety/SAFETY_METRICS_OBSERVABILITY.md`
  - `agent_safety/SKILL_PLUGIN_TRUST_LEVELS.md`
  - `conformance/AGENT_SYSTEM.md`
  - `conformance/BASELINE.md`
  - `decision_integrity/DECISION_INTEGRITY_MODULE.md`
  - `docs/Agent_Facing_Addendum.md`
  - `docs/COMPLIANCE_CHECKLISTS.md`
  - `docs/DEVELOPMENT_METHODOLOGY.md`
  - `docs/DOCUMENTATION_STYLE_GUIDE.md`
  - `docs/Failure_Taxonomy.md`
  - `docs/INDEX.md`
  - `docs/INTERNATIONAL_READINESS.md`
  - `docs/MATURITY_MODEL.md`
  - `docs/NON_GOALS.md`
  - `docs/RATIONALE.md`
  - `docs/REPO_LAYOUT.md`
  - `docs/SYSTEM_BOUNDARY_DIAGRAM.md`
  - `docs/THREAT_MODEL.md`
  - `docs/agentic-systems.md`
  - `docs/archive/README.md`
  - `docs/archive/superseded/certification-levels.md`
  - `docs/audit-logging.md`
  - `docs/certification-levels.md`
  - `docs/index.md`
  - `docs/legal-accountability.md`
  - `docs/multi-agent-risk.md`
  - `docs/templates/case-study-template.md`
  - `docs/templates/doc-template.md`
  - `enterprise_governance/INTERNAL_AI_MODIFICATION_PROTOCOL.md`
  - `enterprise_governance/PR_REVIEW_DISCIPLINE.md`
  - `enterprise_governance/VERSION_CONTROL_POLICY.md`
  - `examples/README.md`
  - `examples/agent_facing_addendum.md`
  - `examples/agent_social_platform_failure_cases.md`
  - `examples/cognitive_safety_examples.md`
  - `examples/constitution_template.yaml`
  - `examples/evidence_bundle_example.json`
  - `examples/evidence_bundle_schema.json`
  - `examples/evidence_vault_ref/README.md`
  - `examples/evidence_vault_ref/__init__.py`
  - `examples/evidence_vault_ref/cli.py`
  - `examples/evidence_vault_ref/requirements.txt`
  - `examples/evidence_vault_ref/tests/test_vault.py`
  - `examples/evidence_vault_ref/vault.py`
  - `examples/evidence_vault_schema.yaml`
  - `examples/failure_cases.md`
  - `examples/hitl_protocol_example.md`
  - `internal/TECHNICAL_TASK_CODEX_v3.3x.md`
  - `policies/Control_Plane_Exposure_Policy.md`
  - `policies/Multi_Agent_Consensus_Requirements.md`
  - `policies/Regulatory_Interface_Requirement.md`
  - `policies/Session_Isolation_Mandate.md`
  - `policies/Tool_Execution_Boundary.md`
  - `policies/Trusted_Skills_Policy.md`
  - `reference_orchestrator/ARCHITECTURE.md`
  - `reference_orchestrator/README.md`
  - `reference_orchestrator/interfaces/Approvals.md`
  - `reference_orchestrator/interfaces/EvidenceVault.md`
  - `reference_orchestrator/interfaces/PolicyEngine.md`
  - `reference_orchestrator/interfaces/SessionIsolation.md`
  - `reference_orchestrator/interfaces/ToolRegistry.md`
  - `reference_orchestrator/nterfaces/ToolRegistry.md`
  - `registry/COMPLIANT_SYSTEMS.md`
  - `registry/README.md`
  - `scripts/check_links.py`
  - `scripts/check_placeholder_requirement_ids.sh`
  - `scripts/check_slop_words.py`
  - `v2/AI-HPP-2025_Standard_v2.2.md`
  - `v3/AI-HPP-2026_Claude_Review.md`
  - `v3/AI-HPP-2026_Standard_v3.0.md`
  - `v3/Agent_Facing_Addendum.md`
  - `v3/Evidence Vault Specification v0.3 (Draft)`
  - `v3/Prohibited_Practices_and_Torture_Ban.md`
  - `v3/modules/Module_11_Regulated_Cognitive_Intervention.md`
  - `v3/modules/README.md`

## 4) Potential wrong-layer content (heuristic)
- No obvious wrong-layer violations detected by heuristic scan.
