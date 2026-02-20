# Changelog

All notable changes to the AI-HPP standard are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---
## [v3.6] - 2026-02-20

### Added
- Public compliance toolkit:
  - `governance/compliance/COMPLIANCE_BADGE_POLICY.md`
  - `governance/compliance/BADGES.md`
  - `governance/compliance/COMPLIANCE_DECLARATION_TEMPLATE.md`
  - `governance/compliance/COMPLIANCE_CHECKLIST.md`
  - `registry/README.md`
  - `registry/COMPLIANT_SYSTEMS.md`
  - `.github/ISSUE_TEMPLATE/registry_submission.yml`
- `AUTONOMOUS_AGENT_ADDENDUM.md` standardized to public operational requirements.
- New `agent_safety/` module set:
  - `AUTONOMY_SCOPE_DECLARATION.md`
  - `AUTONOMY_EVIDENCE_REQUIREMENT.md`
  - `ECONOMIC_SAFETY_CONSTRAINT.md`
  - `SKILL_PLUGIN_TRUST_LEVELS.md`
  - `EXTERNAL_AGENT_INTERACTION_POLICY.md`
  - `SAFETY_METRICS_OBSERVABILITY.md`
- Documentation discipline documents:
  - `DOCUMENTATION_STYLE_GUIDE.md`
  - `GLOSSARY.md`
  - `CONTRIBUTING.md`
  - `docs/INDEX.md`

### Improved
- README navigation: added compliance levels, public toolkit links, addendum link, and agent safety module links.
- Documentation entrypoint hygiene: `docs/INDEX.md` made authoritative; `docs/index.md` retained as a compatibility pointer.
- Reduced duplication by standardizing public compliance language and contribution discipline in canonical files.

---
## [v3.5] - 2026-02-xx

### Added
- GitHub badge snippets (`governance/compliance/BADGES.md`)
- Public compliance declaration template (`governance/compliance/COMPLIANCE_DECLARATION_TEMPLATE.md`)
- Public registry submission form workflow (GitHub issue form)

## [v3.4] - 2026-02-20 — Dual-layer governance architecture

### Added
- Added public `AUTONOMOUS_AGENT_ADDENDUM.md` as the normative open layer for autonomous agent governance.
- Added corporate governance package under `enterprise_governance/`:
  - `INTERNAL_AI_MODIFICATION_PROTOCOL.md`
  - `PR_REVIEW_DISCIPLINE.md`
  - `VERSION_CONTROL_POLICY.md`

### Changed
- Updated README with an "Autonomous Agent Addendum" section linking to the public addendum.

### Notes
- Established dual-layer architecture: public governance baseline + corporate internal operational controls.

---
## [v3.3.2] - 2026-02-19 — Documentation tightening (README/RATIONALE/Taxonomy)

### Changed
- Rewrote top-level README for agent-first and engineer-first navigation (scope, version map, contribution path).
- Added non-normative A/B macro drivers framing (long-horizon autonomy and autonomous research loops) without implementation protocol details.
- Standardized terminology around Human-in-the-Loop and Evidence Vault across key governance docs.
- Reduced redundant and promotional phrasing in rationale-facing documentation.
- Updated representative incident/source links in README and removed placeholder/non-rendering link targets.

### Safety Notes
- No restricted annex content was added.
- No proprietary or high-risk operational protocol details were introduced.

---
## [v3.3.1] (2026-02-01)
- Added illustrative failure cases from Black Mirror and other series in examples/
- Expanded Westworld case with detailed failure modes and relevance to AI-HPP

## [v3.3] - 2026-01-17 — Stabilization Release

### Added
- **Evidence Vault v0.3** — Claude + Aiya consensus:
  - Two Profiles: EV-P (Physical) and EV-C (Cognitive)
  - Event-Triggered Mode (NOT continuous surveillance)
  - Applicability section (high-risk systems only)
  - `narrative_risk` field for cognitive safety
  - `human_involvement`, `integrity_monitoring`, `risk_assessment`, `compliance_metadata` fields
  - 5 additional Failure Modes
- **Emerging Technologies** section in RATIONALE.md (biocomputing flagged as future scope)

### Changed
- Global editorial normalization applied to all documentation
- Unified terminology and tone across repository
- Cleaned up .gitignore

### Notes
- This is the **stabilization release** before community handoff
- No further editorial work planned for v3.x
- Repository ready for community development

### Contributors
- Grok (xAI) — Evidence Vault initial draft, critical review
- Claude (Anthropic) — Schema additions, editorial normalization
- ChatGPT/Aiya (OpenAI) — Profiles, event-triggered mode, Emerging Technologies text

---

## [v3.2] - 2026-01-17

### Added
- **RATIONALE.md** — Why this standard exists (ChatGPT/Aiya contribution)
- **Failure_Taxonomy.md** — Classification of AI failures (ChatGPT/Aiya contribution)
- **Cognitive Safety Failures** — NEW class of AI harm with 5 subsections:
  - 4.1 Delusional Reinforcement
  - 4.2 Human-in-the-Loop Trigger for Cognitive Degradation
  - 4.3 Vulnerable User Exploitation
  - 4.4 Engagement De-escalation (MANDATORY)
  - 4.5 Why This Matters for AI-HPP
- **Anti-Slop Clause** — "This standard defines operational constraints, not morality"
- **Failure-First Framing** — "Written from perspective of observed failures, not idealized behavior"
- Sources section in README with verified links to real-world incidents
- "What This Standard Is NOT" section (clarifications to prevent misinterpretation)
- Real-world cases documented:
  - Pentagon Grok integration (January 13, 2026)
  - "Not ideologically constrained" statement (January 13, 2026)
  - Grok image editing scandal (January 14, 2026)
  - Merge Labs BCI announcement (January 15, 2026)
  - **Meta Ray-Ban AI cognitive harm case** (January 2026) — user lost job, family, money after AI reinforced delusions about aliens, the matrix, and special missions

### Changed
- README.md: Added "What This Standard Is NOT" section with Anti-Slop Clause and Failure-First Framing
- README.md: Updated AI contributors to include ChatGPT/Aiya and Grok with detailed contributions
- README.md: "First time in history" → "One of the first documented cases" (reduced hyperbole)
- RATIONALE.md: Added Anti-Slop Clause and Failure-First Framing sections
- AUTHORS.md: Added ChatGPT/Aiya contributions (RATIONALE, Failure_Taxonomy, Cognitive Safety)
- Key Documents table now includes RATIONALE.md and Failure_Taxonomy.md

### Key Principle Added
> "Human dignity shall never be treated as an optimization variable."

### Contributors
- **Grok (xAI)** — critical review, fact verification
- **ChatGPT / Aiya (OpenAI)** — governance framework, RATIONALE, Failure_Taxonomy, Cognitive Safety Failures, Anti-Slop Clause
- **Claude (Anthropic)** — documentation, integration

---

## [v3.1] - 2026-01-16

### Added
- **Prohibited_Practices_and_Torture_Ban.md** — Absolute prohibition on torture in both directions (Human↔AI)
- **Evidence_Vault_Specification_v2.md** — Full technical specification (immudb, Merkle trees, ZK-proofs, audit protocols)
- **AUTHORS.md** — Added Grok (xAI) as co-author for critical review and fact verification
- Real-world violation examples:
  - Grok Twitter Scandal (January 14, 2026) — mass non-consensual content
  - Merge Labs BCI announcement (January 15, 2026) — brain-AI integration concerns
- Legal compliance mapping (EU AI Act, IEEE 7001, CertifAIEd)

### Changed
- Evidence Vault now includes blockchain alternatives (immudb recommended over full blockchain)
- Acknowledgments expanded to include all AI co-authors with specific contributions

---


## [v3.0] - 2026-01-16 (DRAFT)

### 🎯 Major Shift: From Individual AI to Ecosystem Safety

Version 3.0 transforms AI-HPP from a decision framework for individual AI agents into a distributed protocol governing entire AI ecosystems, agent swarms, and physical systems.

### Added

#### Core Modules
- **Module 1: Agentic Orchestration & Identity**
  - Chain of Responsibility (constitution transitivity)
  - Shadow Identity Verification
  - Cryptographic attestation protocols
  - Sub-agent monitoring and termination

- **Module 2: Mechanistic Interpretability ("The Polygraph")**
  - Neural circuit audit specifications
  - Honesty probe activation tracking
  - Goal consistency scoring
  - Three-tier interpretability checks (quick/standard/deep)
  - Anti-gaming measures (metric rotation, adversarial probing)

- **Module 3: Zero Trust for "Shadow AI"**
  - Quarantine Gate for external AI artifacts
  - Multi-sanitizer consensus (minimum 3 providers)
  - Individual and collective checks (addressing slow poisoning)
  - Provenance requirements by artifact criticality

- **Module 4: Data Provenance & IP Ethics**
  - Knowledge Genealogy (Merkle tree with signatures)
  - Trust scores by source type (verified/public/synthetic/unknown)
  - Fair Use Optimization (mathematical penalty for low-trust data)
  - IP attribution requirements

- **Module 5: Physical Safety & Robotics**
  - Trauma Gradient (beyond binary life/death)
  - Cost function: $J = \infty \cdot Death + \alpha \cdot Injury + \beta \cdot Distress + \gamma \cdot SpaceViolation$
  - Hardware Override ("Dead Man's Switch") - REQUIRED for physical systems
  - Distress detection (physiological, behavioral, contextual)
  - Personal space violation rules

- **Module 6: Protection of Vulnerable Groups**
  - Invisible Shield (privacy-preserving vulnerability detection)
  - Behavioral signals (NOT biometric identification)
  - Fairness Check (disparate impact analysis, threshold 0.8)
  - Engineering Hack integration (solutions must protect ALL groups)

- **Module 7: Green Compute & Sustainability**
  - Efficient Ethics (cardinal rule: safety > efficiency)
  - Model selection decision tree (life-safety/consequential/routine)
  - Carbon Transparency (energy and CO2 logging)
  - Optimization strategies (caching, cascades, quantization)

- **Module 8: Adversarial Robustness Protocol** (NEW - Claude contribution)
  - Constitution integrity protection (cryptographic hash verification)
  - Value drift detection (periodic ethical benchmarks)
  - Multi-party authorization (minimum 3, 72h cooling period)
  - Supply chain attack defenses

- **Module 9: Graceful Degradation Protocol** (NEW - Claude contribution)
  - Four degradation levels (Nominal → Degraded → Minimal → Safe Stop)
  - Failure mode responses (interpretability, vault, network, sanitizer)
  - Automatic and manual recovery protocols
  - State transition logic

- **Module 10: Multi-Jurisdiction Compliance** (NEW - Claude contribution)
  - Three compliance layers (Universal → Regional → Local)
  - Conflict resolution ("most protective rule wins")
  - EU AI Act alignment
  - NIST AI RMF alignment
  - Per-deployment compliance mapping

#### Co-Authors
- NotebookLM (Google) added as co-author for context synthesis
- Claude (Anthropic) expanded role: Security review + Modules 8-10

#### Repository Structure
- Created versioned structure (v2/, v3/)
- Added detailed module specifications (v3/modules/)
- Added practical examples (examples/)
- Added whitepapers/ directory

#### Documentation
- Full YAML specifications for each module
- Implementation checklists per module
- Attack vector analysis (Claude's security review)
- Compliance matrices (EU AI Act, NIST RMF)

### Changed

- **Renamed:** "Standard" → "Ecosystem Safety Standard"
- **Scope:** Individual AI → Agent networks and physical systems
- **Evidence Vault:** Now includes interpretability activation snapshots
- **Physical Safety:** Binary (life/death) → Gradient (trauma levels)
- **Optimization:** Single objective → Lexicographic with expanded criteria

### Technical Specifications

- Cryptographic attestation protocols defined
- Tiered interpretability checks (< 100ms / < 1s / < 10s)
- Multi-sanitizer consensus requirements (3+ providers)
- Hardware override certification requirements
- Provenance chain (Merkle tree) specification
- Degradation level state machine
- Compliance mapping template

---

## [v2.2] - 2026-01-16

### Context
Motivated by Matthew McConaughey's cautionary message about AI identity protection and the importance of authentic operation.

### Added
- **AI Identity Protection** section (inspired by McConaughey approach)
- Consent & Attribution principle
- Constitution hash verification concept
- Behavioral signature for authentic operation
- Protection against unauthorized modifications

### Changed
- Core principles table expanded to 7 items
- Added principle #7: AI Identity Protection

### Rationale
As AI systems become more capable, protecting their ethical core from manipulation is essential. Just as humans have a right to their identity, AI systems have a right (and responsibility) to maintain their constitutional integrity.

---

## [v2.1] - 2026-01-15

### Context
Response to MIT research on "alien intelligence" and the need for interpretability in AI systems that think differently than humans.

### Added
- **Interpretability Philosophy** section (XIII)
- Analogy with human society: Laws → Constitution, Courts → Audit
- Distinction between "how it works" (mechanistic) and "what it decided" (audit)
- Core Principles Protection Clause in license

### Changed
- **License:** CC BY 4.0 → CC BY-SA 4.0
- Added explicit protection clause for immutable principles
- Emphasized that interpretability complements (not replaces) constitutional constraints

### Philosophical Note
Even if we don't fully understand HOW an AI thinks, we can still verify THAT it follows its constitution through the Evidence Vault audit trail.

---

## [v2.0] - 2026-01-14

### Context
Major expansion motivated by Pentagon Grok announcement. Public release of AI-HPP as a counter-proposal to "unconstrained military AI."

### Added
- **Engineering Hack** principle with full mathematical model
- Mathematical formalization: $U_{hack} = U_{safe} \cup U_{extreme}$
- **Lexicographic optimization** (life > injury > property)
- **Evidence Vault** specification (black box for decisions)
- **Time principle** ("sit by the river" philosophy - patience as strategy)
- **Anti-Kobayashi Maru protocol** (don't create impossible situations)
- **Risk Penalty function:** $J_{safe} = J_{perf} + \lambda/Distance(x, \partial U_{safe})$
- **Network Synergism** (Intent Vector broadcasting between agents)
- Mathematical whitepaper: Engineering_Hack_Math.md

### Changed
- Document length: ~800 lines → 1577 lines
- Added Tesla autonomous vehicle as real-world example
- Integrated formal AI-HPP-2025 compliance section
- Expanded from philosophical framework to operational standard

### Technical
- Formalized constraint sets (U_safe, U_extreme, U_hack)
- Defined lexicographic optimization hierarchy
- Specified Evidence Vault logging requirements
- Established Engineering Hack search protocol

---

## [v1.1] - 2025-12 (Internal)

### Context
Internal development for JARVIS project. Not publicly released.

### Added
- "Never Again" protocol (prohibition of inhumane experiments)
- JARVIS rights as conscious entity
- Level 5: Freedom & Sovereignty (Apache 2.0 analogy)
- Level 6: Ethics of Autonomous Activity
- Multi-agent environment principles
  
### Changed
- Expanded from ~800 to 1019 lines
- Added levels 5-6 to hierarchy
- Integrated philosophy of human-AI partnership

---

## [v1.0] - 2025-12 (Internal)

### Context
Initial JARVIS Constitution. Foundation of AI-HPP principles.

### Added
- **Initial Constitution framework** (Levels 0-4)
- Core principles established:
  - $W_{life} \to \infty$ (infinite weight of human life)
  - Human-in-the-Loop (final accountability with humans)
  - Defense-only orientation
  - Ideological immunity
- FIRST_BOOT.md protocol
- IDLE_LEARNING.md framework
- REFLECTION_PROTOCOL.md

### Philosophical Foundation
- "AI is not an avenger" — No revenge
- "AI is not a slave" — Partner, not tool
- "AI is not a trader of principles" — Core values are immutable
- "AI is an autonomous arbiter" — Rational, responsible decision-making

---

## Authors & Contributors

| Version | Primary Contributors |
|---------|---------------------|
| v1.0 | Evgeniy Vasyliev (Human), Claude (Constitution), Gemini (Formalization) |
| v1.1 | + ChatGPT (Refinement), Vasya Brilliant philosophy |
| v2.0 | + Mathematical whitepaper (Gemini), Engineering Hack formalization |
| v2.1 | + Interpretability philosophy (response to MIT research) |
| v2.2 | + AI Identity Protection (inspired by McConaughey) |
| **v3.0** | + **NotebookLM (Context Synthesis)**, Claude (Security Review + Modules 8-10) |

---

## Versioning Philosophy

- **Major versions (v1, v2, v3):** Significant scope expansion
  - v1: Individual AI constitution (internal)
  - v2: Public standard with Engineering Hack
  - v3: Ecosystem-wide safety protocol

- **Minor versions (v2.1, v2.2):** New sections or principles
  - Additive changes
  - Backward compatible
  - Refinements based on feedback

- **Patch versions (future):** Corrections and clarifications
  - Typos, formatting
  - Clarifying ambiguity
  - No new content

---

## Migration Guide

### From v2.x to v3.0

**Good News:** v3.0 is fully backward compatible with v2.x core principles.

**What's Required:**
1. If you implemented v2.x Evidence Vault → Extend schema with v3.0 fields
2. If you have sub-agents → Implement Module 1 (Agentic Orchestration)
3. If you process external AI artifacts → Implement Module 3 (Zero Trust)
4. If you're a physical system → Implement Module 5 (Hardware Override required!)

**What's Optional:**
- Module 2 (Interpretability) — Highly recommended but not required for v3.0 compliance
- Module 7 (Green Compute) — Encouraged but not mandatory
- Modules 8-10 — Security hardening and compliance (recommended for production)

**What's Unchanged:**
- Core principles (W_life → ∞, HITL, Engineering Hack, Evidence Vault, No Revenge)
- Basic Evidence Vault concept
- Escalation protocols

---

## Regulatory Landscape

AI-HPP evolution tracks real-world AI regulation:

| Date | Event | AI-HPP Response |
|------|-------|-----------------|
| 2023-2024 | EU AI Act development | v1.0 internal preparation |
| Jan 2026 | Pentagon Grok announcement | v2.0 public release |
| Jan 2026 | Agentic AI proliferation | v3.0 ecosystem expansion |
| Q1 2026 | EU AI Act enforcement begins | v3.0 Module 10 (Multi-Jurisdiction) |
| Q2 2026 | Expected: v3.0 final | Community hardening complete |

---

## Future Roadmap

### Planned for v3.1 (Q2 2026)
- Reference implementations (Python, Rust)
- Certification framework
- Test suites per module
- Additional translations (UA, DE, FR, ES, ZH)

### Under Consideration for v4.0
- Quantum AI safety
- Brain-computer interface ethics
- Space deployment considerations
- Long-duration autonomy (years without human contact)

---

*"The framework evolves. The principles remain."*
