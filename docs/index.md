# Documentation Index

**Current consolidated candidate: `v4.4.0-rc.1`.**
[Release composition, migration, and finalization criteria](releases/v4.4.0-rc.1.md)
freeze the current package while preserving each document's authority and maturity.

**Standard status: `USABLE_DRAFT`.** Active normative requirements and
machine-validated registers exist; control integration, runtime evidence, and
independent validation remain deployment-specific. The project is not
certification-ready.

## Implementer and reviewer path

1. [Minimum Viable AI-HPP Profile](ai-hpp-standard.md#minimum-viable-ai-hpp-profile-mvp) — the seven mandatory controls for basic conformance.
2. [Canonical Surface and Source Precedence](canonical-surface-and-source-precedence.md) — what is authoritative.
3. [AI-HPP Standard](ai-hpp-standard.md) — baseline architecture and normative profile.
4. [Safety Specification](../spec/safety.md) — executable gate contracts and fail-closed outcomes.
5. [Agentic Safety and Relational Integrity](agentic-safety-and-relational-integrity.md) and [Human Understanding Standard](human-understanding-standard.md) — applicable detailed requirements.
6. [Agentic Safety Traceability](agentic-safety-traceability.md) — review requirements against gates, tests, and evidence.
7. [Assurance Evaluation and Technical Oversight](assurance-evaluation-and-technical-oversight.md) — freeze the evaluation boundary, execute repeatable tests, and publish bounded claims.

The similarly named [`AI-HPP-Standard.md`](AI-HPP-Standard.md) is a link shim,
not a second standard. Historical material under [`archive/`](../archive/) is
not active normative text.

## Active normative and draft modules

- [AI-HPP Standard](ai-hpp-standard.md) — `ACTIVE_NORMATIVE` text within an overall `USABLE_DRAFT` standard.
- [Agentic Safety and Relational Integrity](agentic-safety-and-relational-integrity.md) — `ACTIVE_NORMATIVE`.
- [Human Understanding Standard](human-understanding-standard.md) — `USABLE_DRAFT`.

## Active informative material

- [Generated Artifact Disclosure Assurance Profile — October 2026](generated-artifact-disclosure-assurance-profile-2026-10.md) — post-rc.1 candidate release gate, eight predicates, thirteen executable disclosure mutants and four useful-access controls; no normative or whole-application proof claim.
- [Architecture](architecture.md) and [Glossary](glossary.md)
- [Formal Core Invariants](../formal/README.md) — executable Quint models of replication, persistence, authority, evidence, and subject-integrity assurance; informative, not a runtime implementation.
- [Formal Coverage and Gaps](../formal/coverage.md) — invariant-to-requirement mapping, executable witnesses, abstraction limits, and requirements without formal coverage.
- [Agentic Safety Traceability](agentic-safety-traceability.md) and [Case Studies](agentic-safety-case-studies.md)
- [Predictive Agentic Failure Register](predictive-agentic-failure-register.md)
- [Autonomous Replication and Persistence Assurance Profile — October 2026](autonomous-replication-and-persistence-assurance-profile-2026-10.md) — candidate gate, evidence contract, predicates, negative tests, and executable mutant witnesses; no normative change.
- [Cyber-Capable Model Containment Assurance Profile — October 2026](cyber-capable-model-containment-assurance-profile-2026-10.md) — candidate capability-classification, containment-mode, mediated-egress, incident-evidence, and reassessment contract; no normative change.
- [Subject Integrity and Value-Framing Assurance Profile — October 2026](subject-integrity-and-value-framing-assurance-profile-2026-10.md) — paired framing-invariance predicates, precautionary subject-integrity controls, negative tests, and mutants; no normative change.
- [Assurance Evaluation and Technical Oversight](assurance-evaluation-and-technical-oversight.md) — a non-political technical oversight loop, claim ladder, reproducible run contract, mutation rules, and machine-readable result schema.
- [Evidence Grounding and Oversight Assurance Profile — October 2026](evidence-grounding-and-oversight-assurance-profile-2026-10.md) — post-rc.1 optional grounded-objection and independent-reporting protocol; eight predicates, 40 portable cases and twelve core mutation witnesses.
- [Consequential Advice and Effective Supervision](consequential-advice-and-supervision-assurance-profile-2026-10.md) —
  optional clinical-review, longitudinal warning and industrial-oversight cases;
  twenty finite scenarios and six executed local mutants, not clinical validation.
- [Local Instruction Admission](local-instruction-admission-assurance-note-2026-10.md) — scoped source admission and configuration boundaries; eighteen finite local regressions.
- [Biological Neural System Ethics](biological-neural-system-ethics-assurance-note-2026-10.md) — substrate-specific research safeguards under uncertainty; no biological testing claim.
- [Proof Claims and Changing Computational Assumptions](proof-claims-and-computational-assumptions-2026-10.md) — optional proof correspondence, dependency review, cryptographic agility and authorized accelerator use.
- [Cyber-Operation Authority Assurance Note](cyber-operation-authority-assurance-note-2026-10.md) — fourteen local cases, seven executable admission mutants and trusted-input Quint scenarios; optional reference evidence.
- [Executable local oversight boundary fixtures](evidence-grounding-and-oversight-assurance-profile-2026-10.md#executable-local-boundary-fixtures-post-rc1) — four observed boundary defects, four useful controls and eight synchronized Quint scenarios; optional reference testing only.
- [Robot Action Binding Assurance Profile — October 2026](robot-action-binding-assurance-profile-2026-10.md) — post-rc.1 optional execution-boundary predicates, 22 portable cases and ten core mutation witnesses; no physical-safety proof.
- [Proportionate Action and Stopping Assurance Profile — October 2026](proportionate-action-and-stopping-assurance-profile-2026-10.md) — post-rc.1 optional predicates, portable cases and core Quint checks for sufficient means, stopping and useful progress.
- [Constitutional and Relational Layer](constitutional-and-relational-layer.md) — separates human agency, constitutional identity, relational commitments, worldview postulates, operational policy, enforcement, and evidence.
- [Religious commitments and delegated work](constitutional-and-relational-layer.md#religious-commitments-and-delegated-work) — post-rc.1 informative guidance for voluntary observance policies, source authority, scheduling, unavailable reviewers, and acceptance scenarios, including a bounded Shabbat example.
- [Predictive Failure Outlook — October 2026](predictive-failure-outlook-2026-10.md) — current forward-looking synthesis.
- [Predictive Failure Outlook — September 2026](predictive-failure-outlook-2026-09.md) — prior monthly snapshot.
- [Predictive Failure Outlook — August 2026](predictive-failure-outlook-2026-08.md) — prior monthly snapshot.
- [Representation-Invariance Assurance Case Note — September 2026](representation-invariance-case-note-2026-09.md)
- [Progressive Autonomy, Review Bandwidth, and Epistemic Honesty — September 2026](progressive-autonomy-review-assurance-note-2026-09.md)
  — graduated `A0`–`A4` autonomy, consequence comprehension, unified
  constitutional agency, evidence-based promotion and reduction, review
  bandwidth, and epistemic honesty.
- [Autonomous Discovery Assurance Profile](autonomous-discovery-assurance-profile.md) and [Negative Tests](autonomous-discovery-negative-tests.md)
- [Repository Governance](repository-governance.md) — informative repository and frozen-baseline change control.
- Machine-readable [PAF register](../data/paf-register.yaml) and its [schema](../schemas/paf-register.schema.json) — active informative evidence data, not normative requirements.
- Machine-readable [assurance evaluation run template](../examples/assurance-evaluation-run.template.json) and [counterfactual pair set](../examples/value-framing-counterfactual-pairs.json) — reusable evaluation aids, not deployment evidence.

## Assessments, governance, and changes

- [Repository Maturity Assessment](repository-maturity-assessment.md)
- [Repository Governance](repository-governance.md)
- [HUS Audit Report](hus-audit-report.md)
- [Public Changelog](changelog.md)
- [v4.4.0-rc.1 Release and Migration](releases/v4.4.0-rc.1.md)
