# AI-HPP Standard

**Status: `USABLE_DRAFT`.** AI-HPP is an emerging technical standard for making
agent behavior bounded, reviewable, and attributable to authorized human
objectives. It is usable for engineering and review, but is not certification-ready.

## Start here

1. Implement the seven [Minimum Viable AI-HPP Profile controls](docs/ai-hpp-standard.md#minimum-viable-ai-hpp-profile-mvp).
2. Read the [canonical-surface and precedence rules](docs/canonical-surface-and-source-precedence.md).
3. Apply the [baseline](docs/ai-hpp-standard.md), its applicable normative
   modules, and the [gate contracts](spec/safety.md).
4. Use the [traceability matrix](docs/agentic-safety-traceability.md) to review
   requirements, gates, tests, and evidence.

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

## Maturity and claims

AI-HPP distinguishes: text exists; a requirement is normative; a test procedure
exists; a reference implementation exists; a control is integrated; runtime
evidence exists; and independent validation exists. None implies the next.
Conformance is scoped to a declared system, deployment, version, and time window.
See the [repository maturity assessment](docs/repository-maturity-assessment.md).

AI-HPP is not a claim of universal safety, operational enforcement, external
adoption, or scientific proof of machine consciousness. Persistent identity is
used only as an engineering assumption for continuity and attribution.

## Active modules and repository map

- [Human Understanding Standard](docs/human-understanding-standard.md) —
  `USABLE_DRAFT`; objective retention and review.
- [Agentic Safety and Relational Integrity](docs/agentic-safety-and-relational-integrity.md) —
  `ACTIVE_NORMATIVE`; tool-using and multi-agent controls.
- [Predictive Agentic Failure Register](docs/predictive-agentic-failure-register.md) —
  `ACTIVE_INFORMATIVE`; evidence-qualified scenarios.
- [Predictive Failure Outlook — September 2026](docs/predictive-failure-outlook-2026-09.md) —
  `ACTIVE_INFORMATIVE`; current forward-looking test priorities and inferred cases.
- [Progressive Autonomy, Review Bandwidth, and Epistemic Honesty](docs/progressive-autonomy-review-assurance-note-2026-09.md) —
  `ACTIVE_INFORMATIVE`; evidence-bounded autonomy, event-triggered human review, review-bandwidth scaling, and epistemic-honesty test guidance.
- [`docs/`](docs/index.md) — active documents and assessments.
- `spec/` — compact gate, signal, and core specifications.
- `data/` and `schemas/` — machine-readable registers and schemas.
- `scripts/` and `tests/` — structural and consistency checks.
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
and `PYTHONPATH=. pytest tests`. These checks establish repository consistency,
not runtime AI-HPP conformance.

> Reviewers are encouraged to attack the assumptions, negative tests, gate
> semantics and evidence requirements rather than treat repository consistency
> as proof of safety.
