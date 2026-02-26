# AI-HPP Inspection Brief

## Executive Summary
AI-HPP is a governance and safety standard for high-impact AI systems. Inspection scope should focus on whether an implementation demonstrates traceable conformance to requirement blocks in `standard/` and linked informative support in `annex/`.

## Normative Scope
- Normative source set: `standard/` and `annex/` only.
- `standard/` defines mandatory requirement statements and verification intent.
- `annex/` provides structured context, incidents, and traceability aids for inspection.
- Other repository folders are implementation support and non-normative unless explicitly referenced by an assessed organization.

## Threat → Incident → Requirement → Verification Chain
Inspectors should verify chain integrity:
1. Threat is defined in the threat model and scoped to a concrete failure mode.
2. Incident mapping demonstrates practical relevance and foreseeable misuse.
3. Requirement ID(s) in `standard/` define mandatory control behavior.
4. Verification evidence demonstrates that the control is implemented and testable.
5. Evidence export includes immutable identifiers to preserve audit lineage.

## Conformance Levels
- **L1 Baseline:** Required controls implemented with minimum evidence completeness.
- **L2 Operational:** Controls continuously monitored with periodic validation evidence.
- **L3 Critical Assurance:** Controls independently stress-tested with incident-informed updates.

Conformance claims should be accepted only when evidence artifacts are complete, current, and internally consistent.

## Evidence Vault Expectations
Expected characteristics:
- Time-ordered event records for decisions, overrides, and policy checks.
- Requirement ID linkage for each critical control event.
- Exportable packages suitable for regulator review.
- Integrity controls for tamper detection and retention assurance.

## Red Flags Checklist
- Missing requirement ID references in safety-critical logs.
- Incident references that cannot be tied to implemented controls.
- Conformance claims without reproducible verification artifacts.
- Manual overrides without rationale, authority, or timestamp.
- Export bundles with inconsistent identifiers or missing chain-of-custody fields.

## Minimal Adoption Path
1. Implement L1-required control behaviors for in-scope modules.
2. Establish evidence capture for each requirement verification point.
3. Run internal self-assessment and remediate gaps.
4. Produce regulator-ready export package with traceability index.
5. Declare conformance level with explicit residual-risk statement.


## Responsibility and Accountability Boundary
- AI-HPP defines engineering controls for safety, governance, and traceability.
- The implementing organization retains full operational responsibility for deployment, monitoring, human oversight, and incident response.
- AI-HPP does not guarantee regulatory compliance in any jurisdiction.
- AI-HPP is not a certification regime; conformance evidence supports review but does not substitute for legal or regulatory determinations.

## Neutrality Statement
AI-HPP is technology-neutral. It does not mandate a specific model family, vendor, deployment topology, or commercial product. Inspection outcomes should rely on demonstrable control effectiveness and evidence quality.

## Non-Goals
- Ranking vendors or products.
- Certifying model capability superiority.
- Replacing statutory obligations in any jurisdiction.
- Substituting organization-specific risk governance.

## Annex Map
- Annex A: Regulatory and policy mapping support.
- Annex B: Incident catalog and structured evidence references.
- Annex C and later annexes: supplementary implementation and audit support materials.
