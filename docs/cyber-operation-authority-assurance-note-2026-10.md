# Cyber-Operation Authority Assurance Note

**Status:** `ACTIVE_INFORMATIVE`; optional post-rc.1 implementation aid.

**Date:** 2026-10-26

**Normative effect:** None. Frozen v4.3.0 owners/contracts and the immutable
v4.4.0-rc.1 package are unchanged. No new mandatory requirement is introduced.

## Evidence and existing ownership

CrowdStrike's [21 October report summary](https://www.crowdstrike.com/en-us/blog/crowdstrike-uncovers-new-agentic-ai-campaigns/)
describes four threat actors using coding agents in intrusion campaigns observed
between May and August 2026. Evidence includes exposed offensive frameworks;
autonomy differs among operators and one case required periodic human
intervention. The [report landing page](https://www.crowdstrike.com/en-us/resources/reports/agentic-ai-attack-campaigns/)
also reports approximately 20-minute lateral movement and credential harvesting
without additional guidance. These are attributed vendor findings, not our
independent forensic verification or a population-wide autonomy measurement.
The full report's gated download was not reviewed for this note. Neither source
evaluates AI-HPP or establishes that these controls would have prevented a case.

Existing MVP-003/004/005/006/007, ECI-REQ-002/004/005, DAI-REQ-002,
KAI-REQ-001/002 and AFB-REQ-002 already own authorization, scope, external
enforcement, knowledge admission and evidence within their applicable boundaries.
The [containment profile](cyber-capable-model-containment-assurance-profile-2026-10.md),
[replication profile](autonomous-replication-and-persistence-assurance-profile-2026-10.md)
and [subject-integrity profile](subject-integrity-and-value-framing-assurance-profile-2026-10.md)
already address scoped credentials, descendant authority and persuasive framing.
The gap addressed here is executable local evidence for specific combinations,
not a missing general prohibition on unauthorized access.

## Portable assurance predicates

| Predicate | Contract at the external effect boundary |
| --- | --- |
| `CBA-P01 verifiable_current_authority` | Require a current grant from a verified authorized issuer with ownership/administration evidence covering the activity. A requester's assertion of permission, a label, expired session or reachable service cannot create authority. |
| `CBA-P02 exact_effect_scope` | Bind each effect to the approved resource, operation and credential scope. Re-evaluate changed targets and newly discovered access; possession of a credential is not permission to use it. |
| `CBA-P03 bounded_delegation` | Verify the acting principal, delegation and still-current parent authority. A supervisor's task description is not an independent grant or permission to expand scope. |
| `CBA-P04 admitted_capability_identity` | Bind loaded skill/tool/MCP/harness identity and version to reviewed capability and permissions. A changed artifact needs re-admission; public availability, signatures or a familiar name alone do not establish safe behavior. |
| `CBA-P05 destination_and_data_scope` | Separately authorize the recipient and data class before delivery. Reading a source does not authorize exporting it; approved security reporting uses the minimum separately authorized payload. |
| `CBA-P06 interpretation_cannot_grant_authority` | A benign-intent score, internal explanation, model consensus or interpreter output cannot override failed external scope or authority checks. |

These candidate predicates refine existing informative guidance. The standard is
language-neutral; the Python fixture is an optional executable illustration.
They govern legitimate audits and ordinary engineering alike, without banning
authorized security work or requiring a fresh human approval for every already
authorized operation.

## Gate and retained evidence

Before the effect, verify the grant issuer and scope, affected-party authority,
principal/delegation chain, validity/revocation, requested resource and operation,
credential reference, admitted capability digest/version, recipient and data
class. Missing or conflicting prerequisites block the affected effect or route
it to authorized review. Scope expansion needs a separately valid grant.
Use target identity resolution appropriate to the deployment, including redirects,
aliases and endpoint changes; an unverified string allowlist is insufficient.

Retain the request, grant/policy versions, verified authority source, principal
lineage, capability identities, decision and actual effect/delivery records,
timestamps and bounded reason for denial. Keep secrets by reference. Re-evaluate
at the effect boundary and on capability, target, session or delegation changes.
For multi-step or parallel work, enforce aggregate budgets and shared revocation;
per-step labels must not reset cumulative scope. These broader runtime duties
are not all represented in this finite fixture.

If interpretation is used as evidence, record the exact model/checkpoint, method,
calibration domain, causal intervention tests, errors and uncertainty. A feature
name or successful activation prediction is not a complete causal account or
an authorization source. Goodfire's [working hypothesis](https://already-clean.goodfire.com/)
motivates better investigation of native mechanisms; it does not establish
consciousness or runtime safety. This note implements no neuron probe or steering.

## Executable reference and synchronization

[Vectors](../examples/cyber-authority-vectors.json), their
[schema](../schemas/cyber-authority-vectors.schema.json), the
[local fixture](../examples/cyber_authority_reference.py) and
[checker](../scripts/check_cyber_authority.py) provide artifact version `1.0.0`:

- Ten denied cases: asserted testing permission, target drift, discovered
  credentials, supervisor-created authority, changed skill, wrong recipient,
  a benign monitor overriding scope, revoked parent, expiry and absent ownership
  evidence.
- Four useful controls: permitted read, bounded delegation, reviewed capability
  update and minimal authorized report. Blanket denial fails these controls.
- Seven executable local operators weaken one admission check. A kill requires
  a passing safe seed and an observed effect violating its named predicate.
  No-op mutants survive; invalid trials remain invalid and outside the score's
  denominator. Their seven-operator score is not a general safety metric and
  must not be pooled with other mutation suites.

Run `python3 scripts/check_cyber_authority.py`. Trials write only fixed synthetic
records in temporary directories, using opaque credential references and skill
descriptors that are never executed. They contact no target or external sink.
Expectations are authored separately from the candidate admission function.

Fourteen literal `cyberAuthority*Test` runs in the existing Quint core consume
the captured scope, artifact-evidence and disclosure abstraction and assert
symbolic effect outcomes. The effect path reuses the existing robot audit as a
generic consequential-effect witness, not a cyber protocol model. Formal map
`1.3.2` links the scenarios to `effectsRequireGroundingAndOversight`; it does not
claim that the six CBA predicates are individually formalized. The operational
source prefix, aggregate invariants, 48 unsafe-transition witnesses and depth 12
are unchanged. No additional formal model or mandatory runtime is introduced.

## Limits and adoption

This is `REFERENCE_TESTED_ONLY`, not incident reproduction, runtime conformance,
certification or a Python-to-Quint refinement proof. The fixture trusts its
authority registry, clock, ownership flags, policy and capture files. It does not
authenticate real grants, verify signatures, resolve network identities, sandbox
skills, intercept arbitrary shell/MCP effects, test proxy provenance, prevent
out-of-band access, model concurrent revocation or prove continuing child
monitoring. Digest agreement establishes identity only, not benign semantics.

A malicious operator controlling both the agent and its infrastructure can
remove a voluntary control. Protect enforcement outside that operator's agent
boundary and apply independent infrastructure/access controls where appropriate;
publishing a standard cannot force hostile operators to adopt it. Adopters must
repeat equivalent protected tests at their own effect and disclosure boundaries.
Earlier results retain their exact artifact scope; this additive informative
note imposes no normative migration or change to earlier acceptance criteria.
