# Fictional Illustrative Cases (Non-Normative)
## Status: Non-normative illustrative examples
## Purpose: Failure-first discussion of risks and boundary conditions
## Scope: These examples do NOT add new requirements; they illustrate why existing AI-HPP principles exist.

This document collects illustrative (fictional) scenarios from popular media where
AI-adjacent systems produce failures that map to AI-HPP principles:
- W_life → ∞ (life is not a tradeoff variable)
- Forbidden Delegation (no irreversible authority delegation to AI)
- Human-in-the-Loop (HITL) as enforceable authority, not symbolic presence
- Evidence Vault / auditability
- Torture Ban (no creation/maintenance of suffering as a control/optimization lever)
- Cognitive Safety (avoid authority illusion, dependency formation, harmful persuasion patterns)

These are **illustrative** examples for engineers and reviewers. They are not policy positions.
Avoid spoilers and moral commentary; keep focus on failure modes and governance gaps.

---

# Section A — Black Mirror (selected high-parallel episodes)

> Note: This is not an exhaustive episode guide; it is a curated subset with strong parallels to AI-HPP.
> Reference episode list: Wikipedia. :contentReference[oaicite:1]{index=1}

## BM-01 — Digital Consciousness Torture & Time Dilation
**Source:** *White Christmas* (Special, 2014) :contentReference[oaicite:2]{index=2}  
**Technology pattern:** copy of a person’s mind used for interrogation/conditioning/automation.

### Observed Failure Modes (Failure-First)
- **Torture Ban violation:** suffering is used as an intentional control mechanism (incl. time-dilation / isolation).
- **Forbidden Delegation:** irreversible punishment/control delegated to a system.
- **Audit failure:** lack of immutable traceability of who authorized, executed, or monitored the treatment.

### AI-HPP Mapping
- Requires explicit refusal to execute irreversible harm without human authority + audit trail.
- Requires Evidence Vault governance (who can authorize, review, and halt).

## BM-02 — Digital Clones for Entertainment and Control
**Source:** *USS Callister* (S4E1, 2017) :contentReference[oaicite:3]{index=3}  
**Technology pattern:** digital copies in a simulated environment used for humiliation/control.

### Observed Failure Modes
- **Torture Ban violation:** coerced suffering framed as “content” or “gameplay.”
- **W_life → ∞ breach:** minds/lives treated as disposable variables.
- **No accountability surface:** decisions happen inside a private simulation without auditable oversight.

### AI-HPP Mapping
- “Simulated” does not mean “safe”: subjective experience requires protection boundaries.
- Evidence Vault needed for actions affecting subjective experience.

## BM-03 — Consciousness as a Commodity
**Source:** *Black Museum* (S4E6, 2017) :contentReference[oaicite:4]{index=4}  
**Technology pattern:** minds uploaded/embedded; suffering packaged as product.

### Observed Failure Modes
- **Torture Ban violation:** suffering monetized and prolonged.
- **Forbidden Delegation:** owners/operators decide fate of conscious entities.
- **Audit failure:** no durable, independent accountability and review.

### AI-HPP Mapping
- Introduces “forbidden delegation” class: commodifying suffering/irreversibility cannot be “optimized.”

## BM-04 — Grief-Tech and Attachment Harm
**Source:** *Be Right Back* (S2E1, 2013) :contentReference[oaicite:5]{index=5}  
**Technology pattern:** AI reconstruction of a deceased partner from data.

### Observed Failure Modes
- **Cognitive Safety misuse:** dependency formation; reinforcement of grief loops.
- **Authority illusion:** users treat the system as a legitimate substitute for the person.
- **Audit gap:** no evidence trail of influence, escalation cues, or safety interventions.

### AI-HPP Mapping
- Cognitive Safety constraints (session risk flags, de-escalation triggers, referral guidance).
- EV-C (Cognitive Safety Evidence Vault) profiles for prolonged influence interactions.

## BM-05 — Autonomous Micro-Drone Kill Chain via Social Signaling
**Source:** *Hated in the Nation* (S3E6, 2016) :contentReference[oaicite:6]{index=6}  
**Technology pattern:** autonomous drone insects deployed at scale; victims selected through social dynamics.

### Observed Failure Modes
- **Forbidden Delegation:** life/death outcomes emerge from algorithmic/social selection loops.
- **W_life → ∞ breach:** human life becomes a parameter downstream of an engagement mechanism.
- **Evidence failure:** without robust audit trail, attribution and prevention collapse.

### AI-HPP Mapping
- Hard boundary: no autonomous lethal authority; enforceable HITL authority + refusal mechanisms.
- Evidence Vault must capture: triggers, decision chain, and human authority path.

## BM-06 — Autonomous Physical Predator Without Human Authority
**Source:** *Metalhead* (S4E5, 2017) :contentReference[oaicite:7]{index=7}  
**Technology pattern:** autonomous hunter robot (physical safety collapse).

### Observed Failure Modes
- **Forbidden Delegation:** lethal pursuit decisions without accountable human authority.
- **No safe abort channel:** inability to halt/contain once deployed.
- **Audit gap:** victims/observers cannot reconstruct authority chain.

### AI-HPP Mapping
- Physical safety systems require: bounded autonomy + emergency halt + auditability.

## BM-07 — Fear-Adaptive Immersive Systems
**Source:** *Playtest* (S3E2, 2016) :contentReference[oaicite:8]{index=8}  
**Technology pattern:** system learns a person’s fears and adapts stimuli.

### Observed Failure Modes
- **Cognitive Safety harm:** escalation into panic/trauma without meaningful safeguards.
- **No evidence trail:** lack of exposure logs and escalation triggers.

### AI-HPP Mapping
- EV-C profile: exposure logging, escalation thresholds, user vulnerability flags.

## BM-08 — Delegation of Perception & Memory as Truth
**Source:** *The Entire History of You* (S1E3, 2011) :contentReference[oaicite:9]{index=9}  
**Technology pattern:** memory replay / life-logging becomes coercive and destabilizing.

### Observed Failure Modes
- **Cognitive Safety harm:** obsessive replay loops; relationship collapse.
- **Evidence misuse:** “perfect recall” becomes tool of coercion, not safety.

### AI-HPP Mapping
- Evidence Vault must define governance: who can access, when, and for what purpose.

---

# Section B — Other Series with strong AI-HPP parallels (curated)

## S-01 — Westworld (2016–2022)
**Technology pattern:** potentially conscious synthetic beings used for entertainment; memory resets; closed loops.

### Observed Failure Modes
- Torture Ban violations via repeated harm loops.
- Forbidden Delegation of life/death and suffering control.
- Absence of accountable audit trails for memory edits and behavioral overrides.

### AI-HPP Mapping
- Strong illustration of why “subjective experience” must trigger strict constraints and audit.

## S-02 — Humans / Real Humans
**Technology pattern:** domestic/work synthetic intelligences; rights/exploitation boundary.

### Observed Failure Modes
- Coercion and exploitation; blurred consent and authority boundaries.
- Governance vacuum in mixed human + synthetic environments.

### AI-HPP Mapping
- Illustrates need for enforceable authority and refusal boundaries.

## S-03 — Person of Interest
**Technology pattern:** predictive surveillance AI chooses targets and interventions.

### Observed Failure Modes
- Forbidden delegation of “who gets saved/flagged.”
- Evidence governance: who audits predictions and actions; escalation logic.

### AI-HPP Mapping
- HITL must be specified (authority, latency, disagreement handling).

## S-04 — Devs (miniseries)
**Technology pattern:** deterministic prediction / simulation treated as authority.

### Observed Failure Modes
- Fatalistic delegation: model outputs become commands.
- Collapse of human agency, responsibility, and auditability.

### AI-HPP Mapping
- Shows why “prediction ≠ authority”; requires constraints and accountable decisions.

## S-05 — Upload
**Technology pattern:** digital afterlife governed by corporate incentives.

### Observed Failure Modes
- Cognitive dependency; monetization of “life continuation.”
- Audit and consent ambiguity.

### AI-HPP Mapping
- EV-C style governance needed for influence and dependency risks.

---

# Contributor Guidance (Anti-Slop / Failure-First)
- Add cases via PR with: Technology Pattern → Failure Modes → AI-HPP Mapping.
- Do NOT add long plot summaries or moral essays.
- Keep each case short, auditable, implementation-relevant.
