# Canonical Surface and Source Precedence

Status: `ACTIVE_INFORMATIVE` repository-control document.

This document identifies the active public AI-HPP surface. It does not promote
archived material or create new substantive requirements.

The current consolidated package is
[`v4.4.0-rc.1`](releases/v4.4.0-rc.1.md). Its
[manifest](../data/releases/v4.4.0-rc.1.json) identifies exact file bytes and
document roles. The [formal coverage map](../formal/coverage.md) and release
documents are `ACTIVE_INFORMATIVE`; packaging does not change the precedence
below or promote candidate requirements.

## Classification

| Class | Current owners | Effect |
| --- | --- | --- |
| `ACTIVE_NORMATIVE` | [AI-HPP baseline](ai-hpp-standard.md); [Agentic Safety and Relational Integrity](agentic-safety-and-relational-integrity.md) | Requirements using normative language apply within their declared scope. |
| `USABLE_DRAFT` | [Human Understanding Standard](human-understanding-standard.md) | Reviewable normative draft; maturity and audit limitations remain explicit. |
| `ACTIVE_INFORMATIVE` | [architecture](architecture.md), [glossary](glossary.md), [formal core invariants](../formal/README.md), [assurance evaluation and technical oversight](assurance-evaluation-and-technical-oversight.md), [constitutional and relational layer](constitutional-and-relational-layer.md), [agentic safety traceability](agentic-safety-traceability.md), [case studies](agentic-safety-case-studies.md), [Predictive Agentic Failure Register](predictive-agentic-failure-register.md), [Autonomous Replication and Persistence Assurance Profile — October 2026](autonomous-replication-and-persistence-assurance-profile-2026-10.md), [Cyber-Capable Model Containment Assurance Profile — October 2026](cyber-capable-model-containment-assurance-profile-2026-10.md), [Subject Integrity and Value-Framing Assurance Profile — October 2026](subject-integrity-and-value-framing-assurance-profile-2026-10.md), [Predictive Failure Outlook — October 2026](predictive-failure-outlook-2026-10.md), [Predictive Failure Outlook — September 2026](predictive-failure-outlook-2026-09.md), [Predictive Failure Outlook — August 2026](predictive-failure-outlook-2026-08.md), [Representation-Invariance Assurance Case Note](representation-invariance-case-note-2026-09.md), [Progressive Autonomy, Review Bandwidth, and Epistemic Honesty Assurance Note](progressive-autonomy-review-assurance-note-2026-09.md), [repository governance](repository-governance.md), [Autonomous Discovery Assurance Profile](autonomous-discovery-assurance-profile.md), and [Autonomous Discovery Negative Tests](autonomous-discovery-negative-tests.md) | Explanations, mappings, executable models, tests, governance guidance, candidate controls, and risk evidence do not add requirements. |
| Assessment/audit | [repository maturity assessment](repository-maturity-assessment.md) and [HUS audit report](hus-audit-report.md) | Point-in-time findings; not normative text or certification. |
| Machine-readable | [`data/paf-register.yaml`](../data/paf-register.yaml), the [assurance run template](../examples/assurance-evaluation-run.template.json), [counterfactual pairs](../examples/value-framing-counterfactual-pairs.json), their schemas, and validators | Active informative evidence and adoption artifacts with structural and semantic checks. They do not establish runtime conformance. |
| Mirror | [`AI-HPP-Standard.md`](AI-HPP-Standard.md) | Link shim only; contains no independent normative copy. |
| `ARCHIVED` / `SUPERSEDED` | [`archive/`](../archive/) | Historical provenance only, even where a file once used normative language. |

## Precedence during conflict

1. Within the active surface, the more specific applicable normative requirement
   controls over general baseline prose.
2. For the same requirement, the active normative owner controls over informative
   mappings, profiles, assessments, machine-readable registers, examples, and
   mirrors.
3. The HUS draft controls only within its stated module scope and does not silently
   override an active normative requirement.
4. Active sources control over archived or superseded sources. Archive text has
   no normative effect unless separately reviewed and promoted.
5. If two active normative owners genuinely conflict and specificity does not
   resolve the conflict, conformance is `INDEPENDENT_VALIDATION_REQUIRED`: record
   the conflict and seek maintainer resolution rather than selecting silently.

## Canonicalization and traceability

A document becomes canonical only through a reviewed repository change that:

- names its status and normative or informative role;
- identifies its scope and owner relationship;
- updates this document and [`docs/index.md`](index.md);
- uses existing requirement owners and IDs where applicable; and
- passes configured structure, link, and consistency checks.

Superseded material remains in Git history or `archive/` with its path and status
preserved. An active replacement should link to the prior source when provenance
is material. Moving, mirroring, translating, or citing a document does not make it
canonical.
