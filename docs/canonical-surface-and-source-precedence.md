# Canonical Surface and Source Precedence

Status: `ACTIVE_INFORMATIVE` repository-control document.

This document identifies the active public AI-HPP surface. It does not promote
archived material or create new substantive requirements.

## Classification

| Class | Current owners | Effect |
| --- | --- | --- |
| `ACTIVE_NORMATIVE` | [AI-HPP baseline](ai-hpp-standard.md); [Agentic Safety and Relational Integrity](agentic-safety-and-relational-integrity.md) | Requirements using normative language apply within their declared scope. |
| `USABLE_DRAFT` | [Human Understanding Standard](human-understanding-standard.md) | Reviewable normative draft; maturity and audit limitations remain explicit. |
| `ACTIVE_INFORMATIVE` | [architecture](architecture.md), [glossary](glossary.md), [agentic safety traceability](agentic-safety-traceability.md), [case studies](agentic-safety-case-studies.md), [Predictive Agentic Failure Register](predictive-agentic-failure-register.md), [Predictive Failure Outlook — September 2026](predictive-failure-outlook-2026-09.md), [Predictive Failure Outlook — August 2026](predictive-failure-outlook-2026-08.md), [Representation-Invariance Assurance Case Note](representation-invariance-case-note-2026-09.md), [repository governance](repository-governance.md), [Autonomous Discovery Assurance Profile](autonomous-discovery-assurance-profile.md), and [Autonomous Discovery Negative Tests](autonomous-discovery-negative-tests.md) | Explanations, mappings, tests, governance guidance, and risk evidence do not add requirements. |
| Assessment/audit | [repository maturity assessment](repository-maturity-assessment.md) and [HUS audit report](hus-audit-report.md) | Point-in-time findings; not normative text or certification. |
| Machine-readable | [`data/paf-register.yaml`](../data/paf-register.yaml), governed by [`schemas/paf-register.schema.json`](../schemas/paf-register.schema.json) and its validator | Active informative PAF data with structural and semantic checks. It is not a general conformance schema. |
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
