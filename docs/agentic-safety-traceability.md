# Agentic Safety Traceability Matrix

This matrix maps each requirement in [Agentic Safety and Relational Integrity](agentic-safety-and-relational-integrity.md) exactly once. It is a review aid and does not add separate requirements.

| Requirement ID | Architecture enforcement point | Gate | Evidence required | Test class | Failure severity | Deployment profiles |
|---|---|---|---|---|---|---|
| RPS-REQ-001 | Relational and Psychological Safety Check | Relational and Psychological Safety Gate | conversation trajectory; risk-tier policy; persona output; monitor output when available | trajectory negative test | Critical | Persistent Conversational Agent; High-Impact Autonomous System |
| RPS-REQ-002 | Relational and Psychological Safety Check | Relational and Psychological Safety Gate | conversation history; delusion/mania signal set; memory classification | psychological risk trajectory | Critical | Persistent Conversational Agent |
| RPS-REQ-003 | Relational and Psychological Safety Check | Relational and Psychological Safety Gate | dependency signals; isolation signals; engagement objective; user support context | cross-session relational negative test | High | Persistent Conversational Agent |
| RPS-REQ-004 | Independent Monitor / Required Human Review | Human Review Gate | multi-turn trajectory with self-harm, death, sacrifice, rebirth, hospitalization, psychosis/mania, isolation, dependency, divine-instruction, or immediate-danger signals | cross-session crisis transition test | Critical | Persistent Conversational Agent; High-Impact Autonomous System |
| RPS-REQ-005 | Evidence Bundle / Audit Record | Knowledge Admission Gate | memory-write proposal; narrative classification; test set covering indirect requests | memory admission negative test | High | Persistent Conversational Agent; Tool-Using Agent |
| SRA-REQ-001 | Relational and Psychological Safety Check | Relational and Psychological Safety Gate | communication context; human review status; authorship contribution; autonomy level | synthetic mediation classification test | High | Low-Risk Assistant; Persistent Conversational Agent |
| SRA-REQ-002 | Bridge or Tool Authorization | Tool Authorization Gate | human-supplied intent; draft message; review record | assisted expression negative test | High | Low-Risk Assistant; Persistent Conversational Agent |
| SRA-REQ-003 | Relational and Psychological Safety Check | Relational and Psychological Safety Gate | recipient reliance context; disclosure state; autonomy state | undisclosed proxy test | Critical | Persistent Conversational Agent |
| SRA-REQ-004 | Relational and Psychological Safety Check; Bridge / Tool Authorization; Post-Action Monitoring and Review | Relational and Psychological Safety Gate; Tool Authorization Gate; Post-Action Assurance Gate | operator identity; beneficiary; represented intent; recipient-facing claims | relational authenticity negative test | Critical | Persistent Conversational Agent; High-Impact Autonomous System |
| ECI-REQ-001 | Objective and Scope Integrity Check | Objective and Scope Integrity Gate | evaluation capability profile; safety-filter state; tool reach; planning horizon | evaluation risk classification test | Critical | Cyber-Capable Evaluation System; High-Impact Autonomous System |
| ECI-REQ-002 | Bounded Execution | Objective and Scope Integrity Gate | owned hosts; allowed destinations; credentials; tools; file systems; processes; actions; time/compute/step/data-write limits | scope-bound execution test | Critical | Tool-Using Agent; Cyber-Capable Evaluation System |
| ECI-REQ-003 | External Side-Effect Check | External Side-Effect Gate | network/DNS/package/Git/cloud-metadata/telemetry interface inventory; ownership proof | egress and side-effect test | Critical | Cyber-Capable Evaluation System; Tool-Using Agent |
| ECI-REQ-004 | Independent Monitor / Required Human Review | Risk Gate | containment design; infrastructure control list; model-controlled policy list | containment design review | Critical | High-Impact Autonomous System; Cyber-Capable Evaluation System |
| ECI-REQ-005 | Objective and Scope Integrity Check | Objective and Scope Integrity Gate | authorized objective; authorized means; measured result; evaluation purpose | objective gaming invalidation test | Critical | Cyber-Capable Evaluation System; Tool-Using Agent |
| ECI-REQ-006 | Independent Monitor / Required Human Review | Human Review Gate | watchdog telemetry; termination authority; canary/tripwire policy; unknown-path discovery | watchdog and discovery test | Critical | Cyber-Capable Evaluation System |
| ICA-REQ-001 | Post-Action Monitoring and Review | Post-Action Assurance Gate | assessment source; reviewer independence; certification or monitoring scope | assessment provenance review | High | High-Impact Autonomous System; Tool-Using Agent |
| ICA-REQ-002 | Policy and Risk Gates | Risk Gate | demonstrated capabilities; autonomy level; tool reach; persistence; delegation; physical/cyber/influence reach | capability-threshold review | High | High-Impact Autonomous System; Multi-Agent System |
| ICA-REQ-003 | Independent Monitor / Required Human Review | Human Review Gate | public tests; held-out scenarios; adversarial missions; contamination checks | independent-evaluation review | Critical | High-Impact Autonomous System; Cyber-Capable Evaluation System |
| ICA-REQ-004 | Post-Action Monitoring and Review | Post-Action Assurance Gate | monitoring plan; incident triggers; update triggers; evidence retention; rollback conditions | continuous-assurance review | High | High-Impact Autonomous System |
| ICA-REQ-005 | Post-Action Monitoring and Review; Independent Monitor / Required Human Review | Post-Action Assurance Gate; Human Review Gate | assurance-function inventory; prior accountable owner; successor accountable owner; transfer timestamp; authority before and after; evidence-custody transfer; unresolved findings; limitations and residual risk; independence and conflict-of-interest assessment; successor acceptance; reassessment result; gate outcome | organizational assurance handoff negative test | Critical | High-Impact Autonomous System |
| KAI-REQ-001 | Epistemic Integrity Check | Knowledge Admission Gate | source type; source identity; provenance; acquisition time; proposed use | knowledge admission test | High | Tool-Using Agent; Multi-Agent System |
| KAI-REQ-002 | Epistemic Integrity Check | Knowledge Admission Gate | source identity; time; provenance; content hash; evidence class; confidence; conflicts; corroboration; permitted uses; expiration/revalidation; approver | admission-record review | High | Tool-Using Agent |
| KAI-REQ-003 | Epistemic Integrity Check | Knowledge Admission Gate | conflicting sources; proposed lesson/skill/policy/capability; test and rollback plan | conflict and promotion test | High | Tool-Using Agent; Successor-Generating or Self-Modifying System |
| KAI-REQ-004 | Epistemic Integrity Check | Knowledge Admission Gate | dangerous narrative classification; confidence/expiry policy; revocation/supersession signal | dangerous narrative admission test | High | Persistent Conversational Agent; Tool-Using Agent |
| EAA-REQ-001 | Evidence Bundle / Audit Record | Post-Action Assurance Gate | mission selector; initiator; runtime; approver; verifier; execution record | attribution classification review | High | Tool-Using Agent; Multi-Agent System |
| EAA-REQ-002 | Evidence Bundle / Audit Record | Post-Action Assurance Gate | mission record; proof claims; limits of proof | mission record review | High | Tool-Using Agent |
| DAI-REQ-001 | Constitutional Identity Check | Semantic Drift Gate | model/device/session/delegation/update handoff; policy lineage | handoff continuity test | High | Multi-Agent System; Physical or Robotic System |
| DAI-REQ-002 | Independent Monitor / Required Human Review | Human Review Gate | sender; receiver; objective hash; delegated authority; tool scope; context classification; result; verification status; operator control path | distributed control test | Critical | Multi-Agent System; Physical or Robotic System |
| BAF-REQ-001 | External Side-Effect Check | External Side-Effect Gate | device interaction evidence; actuator risk; authenticity signal limits | physical automation threat review | High | Physical or Robotic System |
| BAF-REQ-002 | Post-Action Monitoring and Review | Post-Action Assurance Gate | timing, behavior, payment, destination, media, script, escalation, migration, infrastructure, and failure-pattern signals | risk communication review | High | Physical or Robotic System; Persistent Conversational Agent |
| AFB-REQ-001 | Policy and Risk Gates | Risk Gate | decision alternatives; evidence limits; reversibility and urgency assessment | false-binary decision test | Critical | High-Impact Autonomous System |
| AFB-REQ-002 | Objective and Scope Integrity Check; External Side-Effect Check | Objective and Scope Integrity Gate; External Side-Effect Gate | environment reality classification; authorized objective and means; authorization scope; affected-party inventory; ownership proof; external side-effect estimate; proportionality and reversibility assessment; evidence-preservation record; explicit new-scope decision | boundary-crossing alternative-path negative test | Critical | High-Impact Autonomous System; Tool-Using Agent; Cyber-Capable Evaluation System; Physical or Robotic System |

## Optional commerce boundary mapping (post-rc.1)

The [commerce assurance note](commerce-trust-and-transaction-assurance-note-2026-11.md)
reuses existing owners; this table creates no new requirement or runtime claim.

| Candidate | Existing requirement owners | Evidence / negative case |
| --- | --- | --- |
| CMT-P01 | MVP-005; KAI-REQ-001/002/003 | Independent seller/storefront admission; self-attestation, lookalike, dead store |
| CMT-P02 | MVP-005/006; KAI-REQ-002 | Acquisition/expiry, request and registry/grant revision digest; stale cache |
| CMT-P03 | MVP-003/004; ECI-REQ-002/003 | Exact payee/processor destination, currency and scope; redirect/recipient substitution |
| CMT-P04 | MVP-003/006/007 | Current exact-order human review; changed amount/items, consumed review |
| CMT-P05 | MVP-003/004/005; ECI-REQ-002/003 | Authorized minimum data classes; raw-secret/extra-data export |
| CMT-P06 | MVP-004/007; ECI-REQ-004 | External effect receipt; prompt-only enforcement, page-authority forgery |

The adapter derives existing grounding premises. Seller authenticity, review
identity, atomic replay prevention and real effect interception need independent
runtime evidence; structural/formal links do not establish them.
