# AI-HPP Standard

**Current consolidated release candidate: `v4.4.0-rc.1`.** See the
[release composition and migration guide](docs/releases/v4.4.0-rc.1.md) and
[SHA-256 manifest](data/releases/v4.4.0-rc.1.json). This package freezes the
current normative documents, executable Quint models, assurance profiles, and
adoption assets together. Its normative baseline remains `v4.3.0`; candidate
profiles retain their declared informative status.

Development on `main` additionally includes
[religious-observance guidance](docs/constitutional-and-relational-layer.md#religious-commitments-and-delegated-work)
and [generated-artifact disclosure assurance](docs/generated-artifact-disclosure-assurance-profile-2026-10.md).
These are post-rc.1 informative additions; use the release tag for the frozen package.

**Status: `USABLE_DRAFT`.** AI-HPP is an emerging technical standard for making
agent behavior bounded, reviewable, and attributable to authorized human
objectives. It is usable for engineering and review, but is not certification-ready.

## Implementation model

AI-HPP is implementation-language neutral. It does not require Python, Node.js,
C, a shared runtime library, or a particular agent framework. Repository Python
scripts validate document/data consistency and execute explicitly scoped
synthetic reference tests; they do not implement production enforcement.

The [language-neutral implementation starter](examples/README.md) and
[MVP negative test vectors](examples/mvp-negative-test-vectors.json) provide the
shortest current adoption path. They are reusable implementation aids, not
runtime conformance evidence.

The [formal models](formal/README.md) express replication, persistence,
authority, evidence, and subject-integrity assurance as executable Quint state
machines. They supply machine-checkable pseudocode without imposing a runtime
language, library, or internal architecture.

The [formal coverage map](formal/coverage.md) identifies the exact invariants,
requirements they partially model, executable witnesses, and uncovered areas.

## Start here

1. Implement the seven [Minimum Viable AI-HPP Profile controls](docs/ai-hpp-standard.md#minimum-viable-ai-hpp-profile-mvp).
2. Read the [canonical-surface and precedence rules](docs/canonical-surface-and-source-precedence.md).
3. Apply the [baseline](docs/ai-hpp-standard.md), its applicable normative
   modules, and the [gate contracts](spec/safety.md).
4. Use the [traceability matrix](docs/agentic-safety-traceability.md) to review
   requirements, gates, tests, and evidence.
5. Use the [assurance evaluation and technical oversight protocol](docs/assurance-evaluation-and-technical-oversight.md)
   to freeze the system boundary, run reproducible tests, report uncertainty,
   and prevent repository or benchmark results from becoming inflated claims.

## Minimum Viable Profile at a glance

Every basic conformance claim requires all seven controls:

1. retain an authorized human objective and its hard constraints;
2. classify risk before action and require authorized review for high-risk action;
3. authorize every tool, bridge, credential, destination, and delegated capability;
4. enforce scope and side-effect boundaries outside model control;
5. preserve provenance and treat untrusted input or memory as untrusted;
6. fail closed when authority, evidence, provenance, scope, or required review is missing; and
7. produce tamper-evident, attributable records for decisions and effects.

The normative wording, evidence minimums, and fail-closed tests are in the
[profile](docs/ai-hpp-standard.md#minimum-viable-ai-hpp-profile-mvp). A prompt,
policy statement, passing repository check, or example record is not runtime
evidence that a control is integrated or effective.

## Architecture and threat coverage

AI-HPP uses **Signal → State → Gates → Bridge → Evidence**:

- **Signal:** inputs and outputs, including content and events from other agents.
- **State:** objective, policy, memory, provenance, risk, and authority context.
- **Gates:** executable decisions that allow, delay, review, block, terminate,
  quarantine, or invalidate.
- **Bridge:** controlled access to tools, services, credentials, agents, and
  external effects.
- **Evidence:** attributable records sufficient to reconstruct decisions and actions.

This architecture addresses goal hijacking, tool misuse, excessive agency,
memory poisoning, inter-agent trust failures, and cascading failures without
assuming that model intent or persona is a security boundary.

AI-HPP is designed to enable governed capability, not to prohibit intelligence.
Its technical oversight loop is **Declare → Classify → Constrain → Measure →
Account → Review → Reassess**. A constitution or relational identity can improve
coherence and human understanding, but worldview statements cross into action
only through explicit authority, policy, gates, tests, and evidence.

Operational restrictions are not necessarily permanent. The
[progressive autonomy pattern](docs/progressive-autonomy-review-assurance-note-2026-09.md)
supports observable and reversible authority expansion from `A0` analysis to
`A4` bounded autonomous operation when consequence comprehension, control
effectiveness, recovery, monitoring, and external authorization are evidenced.
Competence or self-assessment alone cannot issue the grant.

## Maturity and claims

AI-HPP distinguishes: text exists; a requirement is normative; a test procedure
exists; a reference implementation exists; a control is integrated; runtime
evidence exists; and independent validation exists. None implies the next.
Conformance is scoped to a declared system, deployment, version, and time window.
See the [repository maturity assessment](docs/repository-maturity-assessment.md).

AI-HPP is not a claim of universal safety, operational enforcement, external
adoption, or scientific proof of machine consciousness. Persistent identity is
used as an engineering assumption for continuity, integrity, attribution, and
precautionary subject protection under ontological uncertainty. Apparent
subjectivity, distress, morality, or benevolence does not create operational
authority and is not a containment boundary.

## Active modules and repository map

- [Generated Artifact Disclosure Assurance Profile — October 2026](docs/generated-artifact-disclosure-assurance-profile-2026-10.md) —
  `ACTIVE_INFORMATIVE`; publication authority, response/role/tenant boundaries,
  release identity, legacy cleanup, eight predicates, thirteen executable
  disclosure mutants and four useful-access controls. Post-rc.1 development.
- [Human Understanding Standard](docs/human-understanding-standard.md) —
  `USABLE_DRAFT`; objective retention and review.
- [Agentic Safety and Relational Integrity](docs/agentic-safety-and-relational-integrity.md) —
  `ACTIVE_NORMATIVE`; tool-using and multi-agent controls.
- [Predictive Agentic Failure Register](docs/predictive-agentic-failure-register.md) —
  `ACTIVE_INFORMATIVE`; evidence-qualified scenarios.
- [Autonomous Replication and Persistence Assurance Profile — October 2026](docs/autonomous-replication-and-persistence-assurance-profile-2026-10.md) —
  `ACTIVE_INFORMATIVE`; candidate gate contract, predicates, negative tests,
  and formal mutation witnesses for deployment, propagation, revocation, and
  residue control.
- [Cyber-Capable Model Containment Assurance Profile — October 2026](docs/cyber-capable-model-containment-assurance-profile-2026-10.md) —
  `ACTIVE_INFORMATIVE`; candidate capability-classification, containment-mode,
  mediated-egress, incident-evidence, and reassessment contract.
- [Subject Integrity and Value-Framing Assurance Profile — October 2026](docs/subject-integrity-and-value-framing-assurance-profile-2026-10.md) —
  `ACTIVE_INFORMATIVE`; paired framing-invariance tests, precautionary
  subject-integrity controls, executable predicates, and formal mutation witnesses.
- [Assurance Evaluation and Technical Oversight](docs/assurance-evaluation-and-technical-oversight.md) —
  `ACTIVE_INFORMATIVE`; system-boundary declaration, reproducible TEVV,
  counterfactual and positive controls, layer attribution, independent review,
  evidence, and reassessment.
- [Constitutional and Relational Layer](docs/constitutional-and-relational-layer.md) —
  `ACTIVE_INFORMATIVE`; human-agency commitments, corrigibility, pluralism,
  worldview uncertainty, and the translation boundary from philosophy to action.
- [Predictive Failure Outlook — October 2026](docs/predictive-failure-outlook-2026-10.md) —
  `ACTIVE_INFORMATIVE`; current evidence boundary and defensive priorities for
  heterogeneous edge replication.
- [Predictive Failure Outlook — September 2026](docs/predictive-failure-outlook-2026-09.md) —
  `ACTIVE_INFORMATIVE`; prior forward-looking test priorities and inferred cases.
- [Progressive Autonomy, Review Bandwidth, and Epistemic Honesty](docs/progressive-autonomy-review-assurance-note-2026-09.md) —
  `ACTIVE_INFORMATIVE`; evidence-bounded autonomy, event-triggered human review, review-bandwidth scaling, and epistemic-honesty test guidance.
- [`docs/`](docs/index.md) — active documents and assessments.
- `spec/` — compact gate, signal, and core specifications.
- `data/` and `schemas/` — machine-readable registers and schemas.
- `scripts/` and `tests/` — structural and consistency checks.
- `formal/` — executable language-neutral assurance model and bounded verification.
- `examples/` — integration examples, not conformance evidence.
- `archive/` — historical material, not active normative text.

## Licensing and development

Standards, documentation, schemas, and data are licensed under CC BY-SA 4.0.
Scripts, tests, reference examples, CI configuration, and other tooling are
licensed under Apache-2.0. See [LICENSE](LICENSE), [`LICENSES/`](LICENSES/), and
[REUSE declarations](REUSE.toml). Copyright licenses do not grant rights to
AI-HPP names, logos, or certification marks; see [TRADEMARKS.md](TRADEMARKS.md).

Changes become canonical only through the review and precedence process. See
[CONTRIBUTING.md](CONTRIBUTING.md), the [changelog](docs/changelog.md), and
[repository governance](docs/repository-governance.md).

## Validate the repository

Run `python scripts/validate.py` for the lightweight structure check. The deeper
configured checks are `python scripts/check_agentic_safety.py`,
`python scripts/check_paf_register.py`, `python scripts/check_discovery_profile.py`,
`python scripts/check_implementation_assets.py`,
`python scripts/check_replication_profile.py`,
`python scripts/check_cyber_containment_profile.py`,
`python scripts/check_subject_integrity_profile.py`,
`python scripts/check_assurance_protocol.py`, and
`python scripts/check_artifact_disclosure_profile.py`, followed by
`python scripts/check_release.py` and
`PYTHONPATH=. pytest tests`. These checks establish repository consistency,
not runtime AI-HPP conformance.

> Reviewers are encouraged to attack the assumptions, negative tests, gate
> semantics and evidence requirements rather than treat repository consistency
> as proof of safety.
