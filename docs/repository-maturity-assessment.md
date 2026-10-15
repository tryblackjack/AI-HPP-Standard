# Repository Maturity Assessment

Status: point-in-time `ACTIVE_INFORMATIVE` assessment; not certification.
Assessment date: 2026-10-15

## Method and determination

This assessment distinguishes artifact existence, normative requirements,
integrated controls, runtime evidence, and independent validation. No state
implies the next. It reviews only the active canonical tree; archived material is
historical and cannot satisfy an active requirement.

**Overall status: `USABLE_DRAFT`.** AI-HPP v4.3.0 provides a stable normative
baseline, detailed requirement IDs, gate contracts, traceability, negative tests,
and an informative failure register. The repository does not provide evidence
that a deployment implements those controls, does not contain independent
validation of control effectiveness, and is not certification-ready.

| Category | Maturity | Current evidence and boundary |
| --- | --- | --- |
| Reference architecture | Usable Draft | The active Signal → State → Gates → Bridge → Evidence flow, architecture document, gate index, and traceability matrix identify enforcement and evidence points. Product-specific deployment views and conformance-grade reference implementations remain outside this repository. |
| Safety standard | Usable Draft | Seven stable MVP controls and detailed HUS/agentic requirements have evidence obligations, tests, and fail-closed outcomes. Repository validators check document/data consistency only; no runtime evidence bundle is assessed here. |
| Failure evidence | Usable Draft, informative | The PAF document, YAML register, schema, validator, case studies, discovery profile, and outlook form an active informative taxonomy and promotion path. Evidence classes do not themselves create normative controls. |
| Technical oversight and evaluation | Usable Draft, informative | The active assurance protocol defines a system boundary, claim ladder, run manifest, counterfactual and positive controls, evaluator independence, mutation accounting, uncertainty, publication boundaries, and reassessment. It is not an assessor-accreditation or certification process. |
| Certification framework | Emerging | Archived certification and regulator-simulation artifacts are not active certification criteria. There is no canonical assessor accreditation, certificate lifecycle, or independent certification decision. |
| Repository governance | Usable Draft | Active precedence and repository-governance documents define review, exact CI contexts, baseline immutability, and normative promotion. Live hosting enforcement and independent reviewer availability require provider-side evidence. |

## Active strengths

- The Minimum Viable Profile retains exactly seven controls with stable IDs,
  runtime evidence minimums, and uniform fail-closed semantics.
- Detailed requirements have stable family IDs and map once each to architecture
  points, gate contracts, evidence, negative tests, severity, and profiles.
- `spec/safety.md` defines trigger, input, allowed outcome, output, failure, and
  escalation contracts for the active gates.
- The technical oversight protocol, machine-readable run template, semantic
  counterfactual fixtures, and executable mutation witnesses provide a common
  path from specified claims to reproducible public reference tests.
- The progressive-autonomy model makes restriction reduction explicit and
  evidence-based through an `A0`–`A4` ladder, consequence-comprehension tests,
  external grants, monitoring, revocation, and envelope reduction.
- The active PAF register provides evidence-qualified failure scenarios and a
  machine-validated schema without becoming normative by implication.
- Canonical precedence distinguishes active normative, draft, informative,
  assessment, machine-readable, mirror, and archived surfaces.
- Version `v4.3.0` defines an immutable public reference point and requires new
  evidence to pass the existing promotion rule before future normative change.

## Remaining limitations

1. No deployment-specific runtime evidence demonstrates integration or control
   effectiveness.
2. No independent eligible reviewer or independent validation is established by
   repository content.
3. MVP-to-every-detailed-requirement mapping and product-specific applicability
   may still require assessor judgment.
4. No active certification workflow, assessor handbook, certificate lifecycle,
   or accreditation model exists. The evidence contract is an informative
   precursor, not a certification decision.
5. CI validates repository structure, licensing, links, registers, reference
   models, formal invariants, and mutation witnesses; it is not a deployment
   runtime conformance harness.
6. The counterfactual fixtures have not yet been executed across multiple model,
   guardrail, language, and deployment families with independent public results.
7. The autonomy ladder and consequence-comprehension criteria are informative;
   cross-domain thresholds and independent longitudinal results remain open.
8. Live branch protection, metadata, collaborator topology, and private
   vulnerability reporting are external settings and cannot be inferred from
   documentation.

## Maturity guardrails

A stronger classification requires evidence beyond cleaner prose: repeatable
assessment procedures, representative implementation evidence, documented
exceptions and residual risk, independent review with conflict-of-interest
controls, and verified lifecycle governance. Until those artifacts exist and are
reviewed, `USABLE_DRAFT` remains the accurate classification.
