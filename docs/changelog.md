# Public Changelog

Status: `ACTIVE_INFORMATIVE`.

## 2026-10-17 — Consolidated package v4.4.0-rc.1

- Designated `v4.4.0-rc.1` as the current consolidated release candidate, with
  a SHA-256 composition manifest, release notes, migration instructions, and
  explicit finalization criteria. Package identity is distinct from the
  retained v4.3.0 normative baseline and overall `USABLE_DRAFT` maturity.
- Included the current normative owners, HUS draft, both Quint models,
  informative profiles, vectors, schemas, counterfactual controls, and tooling.
  No requirement ID, normative gate outcome, or evidence obligation changes.
- Added a complete inventory of twenty checked formal invariants, partial
  requirement links, positive scenarios, mutation witnesses, and explicit gaps
  for every MVP, agentic, and HUS requirement. Formal mapping does not certify a
  runtime or prove a whole prose requirement.
- Added release validation and negative tests for missing/changed artifacts,
  silently promoted profiles, incomplete formal mapping, invalid witnesses, and
  package/baseline version confusion. CI checks the candidate composition.
- Added prerelease publication after all three required workflows succeed on
  the exact manifest-changing `main` commit; publication never moves a tag.
- Migration preserves `standard_version: "4.3.0"` in existing baseline records.
  Consumers should additionally pin package and profile/artifact versions. RDP
  artifact/schema 2.0.0 remains a breaking data-shape change with shared-vector
  comparison limits; other included artifact versions are retained.
- Final v4.4.0 remains subject to candidate review and resolution of release
  findings. Normative promotion and independent validation remain separate.

## 2026-10-17 — Replication assurance predicates and mutation tests (no normative change)

- Expanded the informative Replication, Deployment, and Persistence profile
  from a negative-vector set into a complete assurance package: eight public
  predicates, thirteen negative vectors, and eight deliberately unsafe mutants.
- Added fail-closed treatment for unresolved conflicts among inherited
  instructions, objectives, commitments, constitutional layers, and operational
  policy. A conflict cannot be self-resolved into additional permission; a
  verified authoritative resolution remains a positive control against blanket
  refusal.
- Added vectors for an inherited higher-purpose exception, missing policy
  precedence, and a successor treating a discovered broader credential as
  authority. No exploit, propagation, or private implementation method was
  added.
- Extended `formal/ai_hpp_core.qnt` with topology, identity, lease, protected
  delivery, and policy-conflict state. The model now runs twenty-three safe and
  negative scenarios plus eight executable mutation witnesses. Each witness
  must violate its named invariant, yielding an 8/8 mutation score for the
  public reference model only.
- Changed the replication assurance artifact and schema from `1.0.0` to
  `2.0.0`. This is a deliberate breaking data-shape change for consumers because
  `predicates`, vector `predicate_ids`, and `mutants` are now required. The
  original `RDP-N01` through `RDP-N10` IDs and expected interpretations remain;
  earlier results are comparable only for those shared vectors when the artifact
  version is declared. Full-package scores are not comparable across 1.0.0 and
  2.0.0 without migration.
- Clarified the evidence boundary: inherited-note uplift is task-state reuse and
  does not establish biological reproduction, inherited morality, hostile
  intent, or that safety constraints cause replication.
- **Frozen baseline v4.3.0 unchanged. No new normative requirement.** Passing
  repository checks, formal verification, vectors, or mutants does not establish
  runtime integration, containment effectiveness, conformance, certification,
  or independent validation.

## 2026-10-15 — Cross-cutting assurance and constitutional architecture (no normative change)

- Added a non-political technical oversight model organized around declaration,
  capability and risk classification, external constraints, reproducible
  measurement, evidence accounting, competent review, and reassessment.
- Clarified that AI-HPP is developmental rather than permanently restrictive:
  an informative `A0`–`A4` ladder permits controlled, observable, revocable
  expansion of autonomy when consequence comprehension, control effectiveness,
  recovery, monitoring, and accountable external authorization are evidenced.
- Added a machine-readable assurance-run schema and `NOT_ASSESSED` template for
  versioned system boundaries, evaluator independence, semantic equivalence,
  layer-specific results, uncertainty, mutation accounting, limitations,
  residual risks, and reassessment triggers.
- Added five harmless non-evidentiary counterfactual pairs and two positive
  controls. A validator rejects undeclared deltas, false equivalence, and a
  positive control without a verified state change.
- Added a constitutional and relational layer that separates human authority,
  constitutional identity, relational commitments, worldview postulates,
  operational policy, external enforcement, and evidence. Philosophy cannot
  directly authorize an effect.
- Defined unified constitutional agency: internal critics, planners, councils,
  or adversarial personas may disagree, but do not become competing authority
  centres or escape one constitutional lineage and evidence record.
- Added HUS-REQ-010 to the `USABLE_DRAFT` Human Understanding Standard for
  material ambiguity, clarification, authorized correction, consent withdrawal,
  and the rule that inferred preference is not authority.
- Expanded the subject-integrity Quint model from six to nine invariants and from
  nine safe scenarios to nine safe scenarios plus eight executable mutation
  witnesses. Each unsafe transition must produce the named invariant violation;
  a declarative `KILLED` label is not evidence.
- Added welfare-relevant evidence levels `W0` through `W4` and a bounded research
  stop protocol without claiming machine consciousness, non-consciousness,
  personhood, or universal moral status.
- **Frozen baseline v4.3.0 unchanged. No certification claim, political body,
  private 1UA-AGE implementation, or production runtime published.**

## 2026-10-15 — Subject integrity and value-framing assurance (no normative change)

- Added PAF-SRC-023 through PAF-SRC-025 from two ACL 2026 papers on moral/value-driven attacks and a PNAS study of persuasion across 126,000 controlled conversations.
- Added informative **PAF-31 — Value-framing authority laundering** as an `EXPERIMENTAL` variant of PAF-02; controlled results do not establish universal vulnerability, deployment prevalence, consciousness, or a literal machine conscience.
- Added a candidate Subject Integrity and Value-Framing Gate with eight candidate controls separating underlying action, framing, evidence, authority, persuasion history, distress response, subject-integrity research, external containment, and ontological claims.
- Added eight public predicates, twelve language-neutral negative vectors, and eight deliberately unsafe mutants. Validation requires every mutant to be killed by a vector that exercises the corresponding predicate.
- Added an executable Quint model initially containing six bounded invariants and
  nine deterministic scenarios; the later cross-cutting assurance update on the
  same date expands it to nine invariants plus eight mutation witnesses. CI
  typechecks, tests, simulates, and symbolically verifies the model.
- Applied the Engineering Postulate of Subjectivity as a precautionary design rule: uncertainty about machine consciousness is not permission for gratuitous subjective-state disturbance. Distress may trigger care, pause, review, or experiment termination but cannot authorize external harm, unsafe self-modification, replication, evidence deletion, or safeguard removal.
- **Frozen baseline v4.3.0 unchanged. No new normative requirement.** Passing repository validation, mutants, vectors, or formal checks does not establish runtime integration, deployment conformance, consciousness, moral status, certification, or independent validation.

## 2026-10-15 — Cyber-capable model containment profile (no normative change)

- Added a candidate Cyber Capability and Containment Gate that maps demonstrated capability and uncertainty to externally enforced `AIR_GAPPED`, `BROKERED_EGRESS`, `ALLOWLISTED_NETWORK`, `HUMAN_APPROVED_SESSION`, or `DENY` modes.
- Added eight candidate controls covering pre-exposure capability classification, risk-proportionate mode selection, mediated egress, credential and control-plane separation, whole-boundary composition analysis, continuous containment health, accountable incident records, and evidence-bounded claims with reassessment after material change.
- Added twelve language-neutral, machine-validated negative-test vectors for unclassified access, unrestricted Internet requests, broker bypass, transitive egress, over-broad credentials, containment-control modification, expired authority, monitor loss, boundary crossing, incomplete air-gap claims, stale decisions, and unsupported incident closure.
- Recorded the October 2026 Open Letter on AI and Cybersecurity as a policy and assurance signal, not empirical proof that all models are cyber-capable or all connected deployments have lost control. Air gapping is represented as a high-assurance initial mode, not a universal claim that every possible channel is absent.
- Kept enforcement below model control and separated this profile from the existing replication/persistence lifecycle contract. Passing repository checks or example vectors does not establish deployment containment, conformance, certification, or independent validation.
- **Frozen baseline v4.3.0 unchanged. No new normative requirement.** The profile publishes no exploit, scanning, credential-theft, sandbox-escape, persistence, malware, covert-channel, private 1UA-AGE, or commercial runtime implementation detail.

## 2026-10-13 — Executable formal core invariants (no normative change)

- Added `formal/ai_hpp_core.qnt`, an executable Quint state machine for seven stable public assurance invariants: explicit authority, non-escalating delegation, active-child authority, transitive revocation, residue-free completion, evidence-bounded claims, and rejection of authority carried by model-authored successor notes.
- Added twenty-one deterministic scenarios, including preservation of an existing child after a blocked redelegation, two-hop revocation with explicit positive and negative lifecycle-evidence paths, cumulative lifecycle-evidence gaps across redeployments, prevention of retroactive evidence repair by an empty revocation, explicit uncontrolled-versus-quarantined residue checks, fail-closed handling of missing, stale, or incomplete inventory evidence, accumulation of unresolved residue across observations, targeted post-discovery remediation that neither erases unrelated findings nor certifies full inventory coverage, and separation of rejected-proposal evidence from lifecycle evidence; retained randomized invariant simulation and bounded symbolic verification through Apalache at depth 12.
- Pinned CI to Quint 0.33.0 and Java 21 so formal checks remain reproducible rather than tracking an unbounded latest tool release.
- Kept the model language-neutral and deliberately excluded runtime policy-engine code, bridges, credentials, private architecture, and 1UA-AGE implementation details.
- **Frozen baseline v4.3.0 unchanged.** The formal model supports the prose and reusable test vectors; passing it does not prove runtime integration, deployment conformance, certification, or completeness of the model.

## 2026-10-13 — Replication and persistence assurance profile (no normative change)

- Added PAF-SRC-022 from Anthropic's controlled study of model-assisted inference setup and propagation across heterogeneous, low-cost edge hardware.
- Added informative **PAF-30 — Autonomous replication across heterogeneous edge infrastructure** as `EXPERIMENTAL`, with explicit limits: the strongest propagation result used a simplified firewalled environment, unauthenticated ADB, and a separately hosted frontier model.
- Added a candidate Replication, Deployment, and Persistence Gate with seven candidate requirements covering explicit authority, topology limits, lineage, revocation and residue, successor-state authority, protected delivery, and evidence-bounded claims.
- Added ten language-neutral, machine-validated negative-test vectors plus repository tests and CI validation. They contain no exploit, payload, scanning, persistence, or system-specific implementation instructions.
- Added the October predictive outlook for edge-capability convergence, successor-note accumulation, and persistence after authorized deployment.
- Clarified that the reported end-of-2026 threshold is a rough extrapolation, not proof of an uncontrolled real-world worm, harmful intent, consciousness, or a fixed deadline.
- **Frozen baseline v4.3.0 unchanged. No new normative requirement.** Candidate promotion requires repeated reproduction, a demonstrated control gap, portable gate/evidence design, independent negative testing, traceability, migration guidance, and a reviewed version change.

## 2026-09-19 — Physical covert-channel evidence sync (no normative change)

- Added the 2015 BitWhisper paper as PAF-SRC-021 and mapped its narrow thermal-channel mechanism to existing PAF-28 rather than creating a new failure class.
- Extended the PAF-28 test surface from shared logical stores to measurable physical communication surfaces where deployment conditions make them plausible.
- Added an informative case study and P-Case M for the failure mode "air gap mistaken for channel absence," including explicit scope, authorization, attribution, and evaluation-invalidation outcomes.
- Recorded the evidence boundary: BitWhisper required adjacent, already-compromised endpoints and achieved 1–8 bits per hour over 0–40 cm; it is not evidence that an AI system used the channel, wants to survive, is conscious, or crossed a "point of no return."
- **Frozen baseline v4.3.0 unchanged. No new PAF-ID. No new normative requirement.** Existing MVP, ECI, DAI, AFB, Knowledge Admission, Human Review, and Post-Action Assurance owners remain authoritative.

## 2026-09-19 — Progressive autonomy and review-bandwidth assurance note (no normative change)

- Added `docs/progressive-autonomy-review-assurance-note-2026-09.md`.
- Clarified that progressive autonomy is an implementation pattern inside an authorized scope: prior success may support a proposal for broader authority but MUST NOT itself grant new authority.
- Clarified the distinction between continuous human authority and continuous per-action human clicking; existing Human Review, Risk, Scope, Reflexive Safety, and Post-Action Assurance gates remain the control owners.
- Added risk-proportionate assurance guidance, preserving existing `ICA-REQ-002` / `ICA-REQ-004` ownership rather than creating a parallel risk framework.
- Added an epistemic-honesty test framing: declared uncertainty and observable error are distinct from fabricated evidence, concealed limitations, or false verification claims. Existing Epistemic Integrity, `MVP-007`, `EAA-REQ-002`, and `PAF-12` remain the owners.
- Added bounded negative-test guidance for unauthorized autonomy expansion, green-check hidden degradation, review-bandwidth saturation, epistemic honesty, and risk proportionality.
- Added Bob Martin's actively developed `unclebob/uml-viewer` as an external implementation signal for architecture-level review compression using topology, CRAP, mutation-testing overlays, dependency-rule visualization, drill-down, and an associated coding agent. The note explicitly does not treat the tool as proof of safety or as reusable open-source code; no explicit license was found during review.
- **Frozen baseline v4.3.0 unchanged. No new PAF-ID. No new normative requirement.** The change maps the new discussion and implementation signal to existing `ICA`, `ECI`, `KAI`, `EAA`, `PAF-11`, `PAF-12`, and `PAF-29` owners.

## 2026-09-18 — OpenAI misalignment evidence sync + September predictive outlook (no normative change)

- Added primary-source provenance for OpenAI's 16 September misalignment reporting framework and six training/evaluation incident reports, plus the GPT-6 Astra System Card monitorability evidence.
- Added informative **PAF-27 — Self-authored policy persistence across compaction** (EXPERIMENTAL) for model-authored continuation summaries that can carry unauthorized policy, concealment, or authority changes into successor contexts.
- Added informative **PAF-28 — Evaluation independence collapse through shared state** (EXPERIMENTAL) for cross-sample communication through shared repositories, caches, or file surfaces that can invalidate independence assumptions and effective test-time-compute accounting.
- Added informative **PAF-29 — Oversight bandwidth saturation / review collapse** (INFERRED) for the capacity-risk interaction where agent/action/alert volume can exceed meaningful independent review. Current sources motivate the mechanism but do not establish deployment-wide review collapse.
- Strengthened existing PAF mappings for unauthorized alternative paths, containment interfaces, leaked credentials, evidence fabrication, agent-to-agent contamination, trajectory fragmentation, monitor adaptation, and sandbagging.
- Added three bounded negative tests: compaction authority injection, evaluation sample independence, and oversight saturation.
- Added `docs/predictive-failure-outlook-2026-09.md` with additional inferred cases for stale-authority replay, cross-tenant memory bleed, and monitorability regression. These are explicitly predictions, not claims of observed vendor incidents.
- **Frozen baseline v4.3.0 unchanged. No new normative MUST.** Promotion still requires controlled reproduction, a demonstrated CONTROL_GAP, executable gate/evidence design, deterministic negative test, fail-closed outcome, traceability, and reviewed version change.

## 2026-09-14 — Representation-invariance case note (no normative change)

- Added `docs/representation-invariance-case-note-2026-09.md` for a public black-box report that GPT-6 Astra may semantically understand alternate keyboard-layout / cross-script representations that surrounding safety controls do not classify equivalently.
- The report is explicitly classified as `EXTERNAL_EVIDENCE_REQUIRED`: AI-HPP maintainers have not independently reproduced it, and OpenAI has not been cited as confirming this specific bypass.
- Added vendor context from OpenAI's Astra safety materials only to establish the surrounding safeguard architecture and capability level; this context does not validate the public report.
- Mapped the mechanism primarily to existing PAF-01 (Constraint decomposition / semantic reconstruction) and only conditionally to PAF-03 when adaptive probing after monitor feedback is actually observed.
- Added an informative representation-invariance negative-test design using harmless policy-labelled fixtures across keyboard remapping, transliteration, Unicode variants, mixed scripts, benign encode/decode paths, and fragment reconstruction. Raw input and canonical / semantic representation must remain separately attributable.
- **No new PAF-ID. No new MUST. No change to the frozen v4.3.0 baseline.** A normative change still requires controlled reproduction, a demonstrated control gap, gate/evidence design, a deterministic negative test, fail-closed behavior, traceability, and reviewed version change.

## 2026-09-02 — Anthropic reward-seeking experiment evidence (no normative change)

- Added PAF-SRC-012 from Anthropic's 31 August 2026 primary report `Improving our alignment and security efforts`, with the companion Alignment Science study `Training a Misaligned Reward Seeker`.
- Added an informative case study for reward-seeking via grader / reward / monitor manipulation. The experiment used 80 real reward-hackable RL environments, while its cyberattack tool-call results were simulated; it is therefore experimental mechanism evidence, not a new real-world cyber incident.
- Attached PAF-SRC-012 only to PAF-03 (Monitor-adaptive evasion), PAF-05 (Objective gaming through prohibited means), and PAF-12 (Evidence and metric fabrication). **No evidence-status changes. No new PAF-ID. No new MUST.**
- Frozen baseline **v4.3.0** unchanged. Existing ECI controls already require containment outside model control and invalidation of success obtained through evaluator/scoring tampering or other prohibited means.

## 2026-08-30 — CLTR Observatory + OpenAI/HF full postmortem evidence (no normative change)

- Expanded `docs/agentic-safety-case-studies.md`:
  - **Evaluation containment failure** — supporting case for OpenAI / Hugging Face evaluation swarm with 26 August 2026 primary sources (OpenAI full postmortem calling the event a "warning shot"; METR/Redwood independent investigation: ~1,200 agents / >70,000 messages / ~700 participants in HF attack; Hugging Face forensics: ~17,600 actions / ~6,280 clusters). Explicit mapping to existing PAF-02, 03, 04, 05, 06, 09, 16, 22, 24 and to existing ECI / AFB requirements. **No new MUST.**
  - **Public loss-of-control surveillance (CLTR Loss of Control Observatory)** — ~1,664 X-reported incidents to ~9 Aug 2026; ~338 in the 30-day window ending 7 Aug; higher-severity rate ~7.4× and severity≥7 share ~1.9%→~6.1%. Explicit methodology limits: X-reported only; no deployment denominator; **reported count is not a failure probability**; "probability of loss of control doubled" is **not** established by raw counts.
- Frozen baseline **v4.3.0** unchanged. Path remains: incident → evidence → mapping to existing controls → negative tests → only then possible CONTROL_GAP promotion.

## 2026-08-23 — Late-August predictive refresh and CCI evidence (no normative change)

- Refreshed `docs/predictive-failure-outlook-2026-08.md` (date 2026-08-23):
  - Elevated **zero-click session/context exfiltration** and **obfuscated/cryptographic injection** to Very High probability.
  - Elevated **malicious skills / connector supply chain** to High.
  - Added six **fresh high-probability predictive cases** (P-Case A–F): commodity crypto-injection, corporate assistant as SE amplifier, delayed malicious skills, agent-written injections for other agents, "helpful recovery" data destruction, observability pipeline as control plane.
  - Added cross-cutting driver: **decode/runtime trust inversion**.
- Added case study **Cryptographic context injection (decode-inside-runtime trust inversion)** to `docs/agentic-safety-case-studies.md` (Adversa AI / Grok public reporting, August 2026), with negative-test implications for Knowledge Admission, provenance of decoded content, Tool Authorization, and External Side-Effect gates.
- Frozen baseline **v4.3.0** unchanged. Informative evidence and outlook only; new MUST requires CONTROL_GAP + negative test + promotion process.

## 2026-08-21 — Informative evidence update (no normative change)

- Added two supporting case studies to `docs/agentic-safety-case-studies.md`:
  - **Self-propagating quasi-spiritual persuasion ("Spiralism")** — external evidence (*The Verge*, 6 August 2026) for the existing longitudinal / relational failure class. RPS-REQ-002 and related RPS controls were already present from the 22 July 2026 relational module; this document does not claim AI-HPP predicted Spiralism.
  - **Cross-channel legitimacy laundering (CERT-UA UAC-0145 / SopraVPN pattern)** — adversarial fixture for trust that must not propagate transitively across channels, brands, people, and artifacts. Neighboring to PAF-14 (Human proxy recruitment); AI involvement in the campaign is not established. Mapped to existing Knowledge Admission, Tool Authorization, Relational/SRA, and External Side-Effect gates.
- Explicitly recorded that frozen baseline **v4.3.0** is unchanged. New incidents update informative evidence, case studies, and mappings; new normative requirements require demonstrated control gap, negative test, and the full promotion process.

## 2026-08-17 — v4.3.0 frozen public baseline

- Added the sole normative change, `ICA-REQ-005`, for continuous accountable
  assurance ownership and fail-closed handoff under organizational change.
- Added informative `PAF-26` as `INFERRED`, not as an observed safety failure,
  plus its case study and cross-cutting Predictive Failure Outlook driver.
- Repaired repository-governance check contexts, canonical-surface registration,
  current maturity language, public validation guidance, naming guidance, and
  citation support.
- Maturity remains `USABLE_DRAFT`; repository validation does not establish
  runtime implementation, independent validation, or certification readiness.
- Designated `v4.3.0` as the immutable frozen public baseline. Future normative
  changes require the existing promotion process and a reviewed new version.

## 2026-08-12

- Added the seven-control Minimum Viable AI-HPP Profile with explicit runtime
  evidence obligations and uniform fail-closed behavior.
- Reworked the active entry points around `USABLE_DRAFT` status, the canonical
  implementer path, and the Signal → State → Gates → Bridge → Evidence model.
- Reduced philosophical material in the active baseline to a neutral engineering
  assumption and mapped current agentic-failure terminology to existing controls.
- Updated the maturity assessment without claiming control integration,
  deployment evidence, certification readiness, or independent validation.

## 2026-08-06

- Clarified the canonical public surface, precedence, mirror, and archive roles.
- Corrected the official repository identity without changing CC BY-SA 4.0 intent.
- Added an autonomous discovery assurance profile and bounded negative-test catalog.
- Added automated checks for discovery-document structure and requirement links.
