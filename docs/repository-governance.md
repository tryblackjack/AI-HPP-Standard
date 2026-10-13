# Repository Governance

Status: `ACTIVE_INFORMATIVE`.
Owner: Repository maintainers
Last updated: 2026-10-08

## Purpose

This document records the repository controls expected for changes to AI-HPP. It
does not claim that a hosting provider has enabled those controls; the live
repository settings remain the authoritative evidence for their enforcement.

## Scope

This guidance covers the default branch, repository metadata, and pull-request
lifecycle. It does not define standard conformance or runtime assurance.

## Guidance

## Protected default branch

The `main` branch SHOULD be protected against direct or unreviewed changes. Its
ruleset should:

- require a pull request before merge;
- require independent/CODEOWNER approval when an independent eligible reviewer
  exists, but not create a permanently unmergeable rule in a single-maintainer topology;
- dismiss stale approvals when a reviewable change is pushed;
- require conversation resolution;
- prohibit merge while required checks are pending or failing; and
- apply the rules to administrators unless a documented emergency exception is
  being exercised.

Workflow display names and exact branch-protection contexts are different
identifiers. The configured pre-merge mapping is:

| Workflow display name | Exact job/status-check context |
| --- | --- |
| `Repo Structure Validator` | `validate-structure` |
| `AI-HPP Standard Audit` | `audit` |
| `Spec Consistency Checker` | `spec-check` |

Branch protection should require the exact job contexts, keep the branch strict
or up to date where supported, resolve conversations, prohibit force pushes and
deletion, and dismiss stale approvals where approvals exist. `Auto-Archive
Repository Clutter (AI-HPP v4.3 Rules)` is post-merge hygiene and MUST NOT be a
pre-merge required check.

The verified local environment has no authenticated administrative or
collaborator-topology access. Until live settings establish an independent
eligible reviewer, the limitation is
`OWNER_APPROVAL_NOT_ENFORCEABLE_IN_CURRENT_SINGLE_MAINTAINER_TOPOLOGY`.
Documentation is not evidence that any rule is enabled.

The post-merge `Auto-Archive Repository Clutter` workflow is an additional
repository-hygiene control. It is not a substitute for the pre-merge checks.

## Repository metadata

Hosting metadata MUST describe the project consistently with its declared
maturity. Until runtime effectiveness and certification are supported by
appropriate evidence, the recommended repository description is:

> Evidence-based assurance standard for autonomous AI agents: bounded authority,
> fail-closed runtime gates, provenance, containment, and tamper-evident
> evidence. USABLE_DRAFT.

Metadata is informative and MUST NOT override the canonical surface or maturity
assessment.

## Pull-request lifecycle

Maintainers SHOULD close obsolete pull requests promptly and identify the
change that superseded them. A supersession comment should name the merged pull
request and immutable commit identifier so that reviewers can reconstruct the
decision without treating stale work as an active alternative.

These controls govern repository changes only. Passing them demonstrates
repository consistency and review discipline, not runtime conformance or control
effectiveness.

## Frozen baseline and change control

`v4.3.0` is an immutable published baseline. Future changes to `main` do not
retroactively change `v4.3.0`; a defect requires a new version rather than a
moved tag.

## Implementation compatibility and migration

AI-HPP remains implementation-language neutral. A normative version MUST NOT
make one programming language, framework, or repository validation script an
implementation dependency unless a future reviewed profile explicitly declares
that scope.

Stable requirement IDs MUST NOT be silently repurposed. A future normative
version that changes an existing requirement, gate outcome, evidence obligation,
or conformance condition MUST publish migration notes identifying:

- added, changed, deprecated, and removed requirement IDs;
- changed gate outcomes or evidence fields;
- affected language-neutral test vectors; and
- whether the change is compatible or requires implementation work.

The previous published version remains immutable. Machine-readable examples and
test vectors MAY evolve as informative adoption aids, but they do not alter a
normative requirement and do not establish runtime conformance by themselves.

After freeze, new incidents MAY update informative PAF evidence, case studies,
predictive outlooks, mappings, and explanatory material, but MUST NOT silently
alter the frozen baseline. An incident does not automatically create a new
`MUST`. Normative promotion uses the existing PAF promotion rule and requires:

1. a defined failure mechanism;
2. an evidence classification;
3. a control gap;
4. existing-owner analysis;
5. a gate;
6. required evidence;
7. a negative test;
8. a fail-closed outcome;
9. a traceability update; and
10. a reviewed version change.

This rule resists news-driven normative churn without preventing reviewed future
versions.

## External settings seams

The intended About description is quoted above. Recommended high-signal topics
are `ai-agents`, `agentic-ai`, `autonomous-agents`, `ai-safety`, `ai-security`,
`ai-governance`, `ai-assurance`, `ai-standards`, `runtime-governance`,
`multi-agent-systems`, `responsible-ai`, and `human-in-the-loop`. Without
authenticated admin access, metadata, rulesets, collaborator topology,
Discussions, and private vulnerability reporting remain unverified external
settings. In particular, `SECURE_REPORTING_CHANNEL_OPEN_ITEM` remains open; no
public issue or invented email address is presented as a secure channel.

## Evidence

Reviewers should inspect the hosting provider's live branch rules, check runs,
repository metadata, pull-request history, and merge commits. This document and
`CODEOWNERS` express the intended policy but do not prove that the provider
enforces it.
