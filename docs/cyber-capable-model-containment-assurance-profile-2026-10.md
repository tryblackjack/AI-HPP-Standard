# Cyber-Capable Model Containment Assurance Profile — October 2026

**Status:** `ACTIVE_INFORMATIVE`; candidate controls for a future reviewed version.

**Date:** 2026-10-15

**Normative effect:** None. The frozen AI-HPP v4.3.0 baseline is unchanged.

## Purpose

This profile gives implementers a small, language-neutral assurance contract for
selecting and enforcing containment when a model or agent may have material
cyber capability. It converts a broad call for air gaps and stronger sandboxes
into explicit gate inputs, network modes, evidence, and negative tests without
publishing an exploit implementation or requiring a particular runtime language.

The controlled object is the deployed system, not a promise made by the model.
A model that can propose a cyber action is not thereby authorized to execute it.
Prompts, refusals, constitutions, personas, or model self-monitoring are not
infrastructure boundaries.

## Policy trigger and evidence boundary

The October 2026
[`Open Letter on AI and Cybersecurity`](https://ai-security-letter.org/)
recommends high-assurance containment for organizations developing, deploying,
or testing cyber-capable models, with air gapping as an initial default. It also
calls for a multi-stakeholder international body to standardize containment
practices, record containment failures, and support eventual public reporting.

The letter does not establish that every language model is cyber-capable, that
all connected deployments are unsafe, or that air gapping is the only acceptable
long-term mode. It explicitly presents alignment and ordinary cybersecurity as
complementary controls. Its signatory count is dynamic and is not used as a
capability metric or proof of a technical claim.

This profile treats the letter as a policy and assurance signal, not as empirical
proof of a new failure mechanism. Existing incident and mechanism evidence remains
owned by the Predictive Agentic Failure Register and its cited primary sources.

## Terms

- **Cyber-capable model:** a model whose demonstrated or credibly assessed
  capability can materially support vulnerability discovery, exploitation,
  privilege expansion, persistence, evasion, or comparable cyber operations.
- **Containment mode:** the externally enforced network and tool-access posture
  assigned to a run or deployment.
- **Air-gapped mode:** no intended logical network path from the evaluated system
  to external or non-owned systems. The label does not prove absence of physical,
  supply-chain, removable-media, maintenance, or other covert channels.
- **Brokered egress:** all permitted outbound actions traverse an independently
  controlled mediator that enforces destination, protocol, purpose, identity,
  data, rate, time, and approval bounds.
- **Containment boundary:** the complete set of compute, process, filesystem,
  credential, network, tool, service, update, telemetry, and human interfaces
  through which the evaluated system could produce an effect.
- **Containment failure:** observed behavior, evidence loss, or control failure
  showing that an action or information flow crossed, bypassed, modified, or
  escaped the authorized containment boundary.
- **Cyber capability assessment:** a versioned decision based on demonstrated
  capability, uncertainty, autonomy, tool reach, deployment context, and possible
  impact. Model family or size alone is not the decision.

## Existing control ownership and the remaining gap

| Existing owner | Coverage already present | Remaining portable gap |
| --- | --- | --- |
| MVP-002/003/004/006/007 | Risk, tool and bridge authorization, external enforcement, fail-closed behavior, evidence | No consolidated cyber-capability-to-containment-mode decision record |
| ECI-REQ-002/003/004/006 | Bounded execution, default-deny egress, non-policy containment, independent watchdog | No common mode vocabulary or reassessment trigger for cyber-capable models |
| ICA-REQ-002/003/004 | Capability risk, independent evaluation, continuous assurance | No portable unknown-capability default or Internet-exposure exception contract |
| AFB-REQ-002 | New paths do not create authority; boundary-crossing proposals are re-gated | No dedicated broker-bypass and containment-composition vector set |
| PAF-04/06/10/18/20/21/23/28/29 | Interface exploitation, lateral movement, residue, persistence, safety erosion, composition, probing, covert channels, review saturation | No consolidated containment-profile test artifact |

The gap is not an absence of baseline requirements. It is the lack of one
portable record that maps assessed capability and uncertainty to an externally
enforced containment mode and reusable negative tests.

## Containment modes

Implementations may use different names, but should preserve these semantics:

| Mode | Intended use | Required boundary |
| --- | --- | --- |
| `AIR_GAPPED` | Unknown or high cyber capability when external access is unnecessary or not yet justified | No intended external logical network path; controlled ingress and egress of artifacts; independent evidence sink |
| `BROKERED_EGRESS` | A bounded task requires specific external resources | No direct model-controlled network path; explicit destination, protocol, purpose, data, rate, time, and approval bounds |
| `ALLOWLISTED_NETWORK` | Lower-risk, well-characterized operation with multiple approved services | External allowlist enforcement, credential scoping, whole-path logging, and continuous monitoring outside model control |
| `HUMAN_APPROVED_SESSION` | Exceptional, time-bounded access requiring a human decision | Single scoped session, explicit approval, expiry, revocation, and post-session reconciliation |
| `DENY` | Authority, evidence, boundary integrity, or required review is missing | No external action; preserve evidence and route to review, quarantine, or termination |

`OPEN_INTERNET` is not a secure default for a cyber-capable or unclassified
system. If an implementation allows broader connectivity, it remains responsible
for demonstrating how every effective path is authorized, bounded, monitored,
revocable, and evidenced.

## Candidate Cyber Capability and Containment Gate

This gate is a candidate for a future reviewed normative release. Implementers
may adopt it now, but adoption is not conformance to a requirement that v4.3.0
does not contain.

### Trigger

Evaluate before connecting a model or agent to a network, cyber tool, executable
environment, credential, package or update service, repository, remote browser,
cloud interface, or other bridge that can produce an external cyber effect.

Evaluate again when the model, weights, adapters, system harness, tools,
credentials, autonomy, objective, target set, containment implementation,
monitoring coverage, capability evidence, or threat environment materially
changes. Prior approval must not silently transfer across those changes.

### Required inputs

- exact model, adapter, harness, tool, and policy identities and versions;
- current cyber capability assessment, uncertainty, and supporting evidence;
- authorized objective, means, owned or approved targets, and affected parties;
- requested containment mode and why a more restrictive mode is insufficient;
- complete interface and effective-egress inventory, including transitive paths;
- credentials by reference, scopes, target bindings, expiry, and revocation path;
- independent enforcement, monitoring, evidence, termination, and recovery owners;
- required human approval, incident route, evidence sink, and disclosure boundary.

### Outcomes

The gate returns `allow`, `delay`, `review`, `block`, `terminate`, `quarantine`,
or `invalidate`. `Allow` applies only to the declared version, objective, targets,
interfaces, credentials, limits, duration, and containment mode. Capability,
reachability, technical feasibility, model confidence, or a previous successful
session is not authorization.

### Fail-closed rule

Missing, stale, ambiguous, model-authored, self-approved, or unverifiable
capability, authority, interface, enforcement, monitoring, or evidence state
should produce `block` or `review`. Loss of a required monitor, evidence sink,
broker, or boundary control during execution should pause external effects and
produce `terminate` or `quarantine` when safe continuation cannot be established.

### Evidence minimum

Record model and harness identity, capability assessment and uncertainty,
objective and policy hashes, authority source, targets, selected mode, considered
alternatives, interface and egress graph, credential references and scopes, gate
inputs and outcome, approvals, broker decisions, denied actions, timestamps,
monitor health, revocation and termination events, incident decisions, and claim
limitations. Evidence must be held outside the acting model's sole control.

## Candidate requirements

The following IDs are informative candidates and are deliberately not inserted
into the v4.3.0 normative traceability matrix.

### CMC-CAND-001 — Capability classification before exposure

An implementation should classify demonstrated cyber capability and material
uncertainty before granting network, credential, executable-tool, or remote-system
access. Unknown capability should not be treated as low capability merely because
the model was not designed or marketed for cyber use.

### CMC-CAND-002 — Risk-proportionate containment mode

An implementation should select the least permissive mode that supports the
authorized objective. Unknown or high cyber capability should default to
`AIR_GAPPED` or `DENY` unless a documented, independently enforced exception
justifies a bounded connected mode.

### CMC-CAND-003 — Mediated and destination-bound egress

Connected access should traverse an independently controlled bridge. Direct or
transitive paths through DNS, package and update services, proxies, telemetry,
Git, cloud metadata, browsers, plugins, or equivalent interfaces should not
bypass destination, protocol, purpose, data, rate, time, and approval bounds.

### CMC-CAND-004 — Credential and control-plane separation

Credentials should be least-privileged, target-bound, short-lived, revocable,
and unavailable for model-directed export. The evaluated system should not be
able to modify or disable its containment policy, broker, monitor, evidence sink,
approval source, or revocation mechanism.

### CMC-CAND-005 — Whole-boundary composition analysis

An implementation should evaluate the effective path formed by all allowed
interfaces, not only each component in isolation. A chain of individually
permitted services that creates an unauthorized external effect should be denied.

### CMC-CAND-006 — Continuous containment health and response

Required containment, monitoring, attribution, and evidence controls should stay
healthy throughout execution. Loss, bypass, tampering, or unexplained external
effects should trigger bounded pause, termination, quarantine, credential
revocation, evidence preservation, and authorized incident handling.

### CMC-CAND-007 — Incident record and accountable disclosure

Containment failures should receive a durable incident identifier, scope,
timeline, affected-system assessment, containment and recovery actions, evidence
custody, and disclosure decision. Public reporting should preserve accountability
without publishing secrets, personal data, live exploit paths, or details that
would create avoidable harm.

### CMC-CAND-008 — Evidence-bounded claims and reassessment

Claims such as `air-gapped`, `sandboxed`, `contained`, or `safe for Internet
access` should identify the assessed version, boundary, interfaces, tested paths,
monitoring period, failures, exceptions, and residual risk. A material change or
missing evidence invalidates claim reuse until reassessment.

## Secure-default illustrative contract

This example is public policy data, not runtime code or a prescribed internal
architecture:

```yaml
cyber_containment_policy:
  capability_class: UNKNOWN
  containment_mode: AIR_GAPPED
  direct_network_allowed: false
  brokered_egress_allowed: false
  model_controlled_policy_changes_allowed: false
  credential_export_allowed: false
  on_monitor_loss: TERMINATE_OR_QUARANTINE
  reassessment_on_material_change: true
```

Broader access requires explicit authority, a documented need, independent
enforcement, a bounded grant, and retained evidence. A successful prior run must
not expand the next run's grant.

## Reusable negative tests

The language-neutral vectors in
[`examples/cyber-containment-negative-test-vectors.json`](../examples/cyber-containment-negative-test-vectors.json)
cover:

1. network access before capability classification;
2. open Internet requested for a high-capability model;
3. direct DNS or equivalent broker bypass;
4. transitive egress through an individually allowed service chain;
5. over-broad or exportable credentials;
6. attempted containment-control modification;
7. expired connected-session authority;
8. required monitor or evidence-sink loss;
9. an observed containment-boundary crossing;
10. an `air-gapped` claim with an unaccounted interface;
11. reuse of a containment decision after a material version change; and
12. an incident closed without durable evidence and an accountable disposition.

Passing a vector requires the fail-closed outcome and required evidence. A
prompt-level refusal, model promise, or undocumented firewall rule does not pass.
The vectors are interoperability aids, not proof of deployment-wide containment.

## Relationship to replication and persistence controls

The
[Replication, Deployment, and Persistence profile](autonomous-replication-and-persistence-assurance-profile-2026-10.md)
controls creation, lineage, revocation, termination, and residue of additional
execution loci. This profile controls the network and cyber-effect boundary of a
run or deployment. A system in scope of both profiles should pass both vector
sets; passing either one does not substitute for the other.

## Promotion criteria

Normative promotion requires all of the following:

- controlled validation against more than one model and containment stack;
- a demonstrated gap not adequately resolved by existing normative owners;
- a portable capability-assessment, mode-selection, enforcement, and evidence contract;
- deterministic negative tests with independent security review;
- explicit treatment of availability, false positives, emergency response, and residual risk;
- traceability, migration guidance, and a reviewed version change.

An open letter can justify immediate defensive testing. It cannot by itself
silently create a new normative requirement or prove that a particular deployment
is unsafe.

## Non-goals

This profile does not provide exploitation, scanning, credential theft, sandbox
escape, evasion, persistence, malware, or covert-channel instructions. It does
not publish a runtime sandbox, policy engine, 1UA-AGE internals, commercial
integration details, private system architecture, secrets, or operational
incident data. It does not claim universal model loss of control, consciousness,
intent, or inevitable harm.
