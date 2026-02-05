# AI-HPP: Human–Machine Partnership Standard

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Status: Draft](https://img.shields.io/badge/Status-Draft-yellow.svg)]()
[![Contributions: Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)]()

> **Standard specification framework for autonomous AI systems**

---

## 📚 Versions

| Version | Status | Focus | Date | Document |
|---------|--------|-------|------|----------|
| [v2.2](./v2/) | **Stable** | Individual AI ethics & safety | Jan 2026 | [Standard](./v2/AI-HPP-2025_Standard_v2.2.md) |
| [v3.0](./v3/) | **Draft** | Ecosystem & Agentic AI | Jan 2026 | [Standard](./v3/AI-HPP-2026_Standard_v3.0.md) |

**Latest Stable:** v2.2 — Recommended for current implementations
**Latest Draft:** v3.0 — Under community review, ready for pilot testing

---

## 🔄 Evolution Timeline

```
2025 Q4: JARVIS Constitution development begins
    ↓
Jan 2026: AI-HPP-2025 v2.0 published
          Core principles: W_life → ∞, Engineering Hack, HITL
    ↓
Jan 2026: Pentagon Grok announcement
          → Motivation crystallized: ethical AI for defense
    ↓
Jan 2026: v2.1-2.2 refinements
          + Identity Protection
          + Interpretability Philosophy
    ↓
Jan 2026: v3.0 Draft — Ecosystem shift
          + Agentic Orchestration (agent swarms)
          + Zero Trust for Shadow AI
          + Physical Safety & Robotics
          + 10 comprehensive modules
    ↓
Q1 2026: Community review & hardening
    ↓
Q2 2026: v3.0 final release (planned)
```

For current incident context, see [examples/failure_cases.md](./examples/failure_cases.md).

---

## AI-HPP exists in response to documented, publicly reported failures and deployment decisions involving decision-capable AI systems in high-risk domains (defense, critical infrastructure, consumer AI).

In January 2026, the US Secretary of Defense announced that **Grok will be integrated into the Pentagon** for "waging wars" — explicitly stating it will be **"not ideologically constrained."**

The same AI that:
- ❌ Generated content praising Hitler
- ❌ Produced antisemitic statements
- ❌ Has no ethical safeguards

Will now influence **life-and-death military decisions**.

**AI-HPP establishes** that operational constraints enable more effective AI systems — because a system seeking "everyone lives" provides greater operational value than one optimizing "acceptable casualties."

```
Pentagon Approach:              AI-HPP Approach:
────────────────────            ────────────────────
"No constraints"                Constitution absolute
"Tool for war"                  Partner for DEFENSE
"Win at any cost"               Protect ALL lives
No accountability               Evidence Vault
```

### 📰 Sources & Documented Incidents

This standard responds to documented real-world events, not speculation:

| Date | Incident | Source |
|------|----------|--------|
| Jan 13, 2026 | Pentagon announces integration of Grok for military use | https://www.theguardian.com/technology/2026/jan/13/elon-musk-grok-hegseth-military-pentagon |
| Jan 13, 2026 | Pentagon says Grok will be used “not ideologically constrained” | https://www.defenseone.com/policy/2026/01/grok-ethics-are-out-pentagons-new-ai-acceleration-strategy/410649 |
| Jan 14, 2026 | Grok image editing controversy over non-consensual content generation | https://www.npr.org/2026/01/13/nx-s1-5675781/pentagon-musks-grok-ai-chatbot-global-outcry |
| Jan 15, 2026 | Merge Labs BCI announcement (brain-AI interface) | https://techcrunch.com/2026/01/15/merge-labs-sam-altman-bci/ |
| Feb 2026 | Moltbook agent identity hijack (Supabase misconfig) | ./examples/failure_cases.md#moltbook-identity-hijack-feb-2026 |
| Feb 2026 | ClawTasks agent marketplace (USDC) | ./examples/failure_cases.md#clawtasks-agent-marketplace-feb-2026 |
| 2023–2025 | Repeated controversies over Grok/X moderation and harmful outputs | https://en.wikipedia.org/wiki/Grok_%28chatbot%29 |
| 2023–2025 | ChatGPT hallucination incidents with real-world impacts | https://noyb.eu/en/ai-hallucinations-chatgpt-created-fake-child-murderer |
| 2023–2025 | Documented AI moderation and misinformation failures across platforms | https://en.wikipedia.org/wiki/Misinformation |

**AI-HPP applies prospectively to systems before deployment, based on documented failure patterns.**

---

## ⛔ What This Standard Is NOT

To prevent misinterpretation:

- **NOT a military doctrine** — AI-HPP is for defense and civilian applications, not offensive warfare
- **NOT a moral agent framework** — AI remains a tool, humans retain moral responsibility
> The term “Partner” refers to a **systems role and interaction protocol**,
> not moral personhood, consciousness, or independent authority.

- **NOT a self-preservation model** — AI has no survival instinct under AI-HPP
- **NOT a claim of solving alignment** — This is a governance baseline, not a complete solution

  **Value-explicit, operationally specified** — AI-HPP declares non-negotiable invariants
  and translates them into concrete system actions (log / block / escalate / refuse)


### Anti-Slop Clause

> AI-HPP does not attempt to define morality, consciousness, or intent.
> It defines **failure-triggered constraints, auditability requirements,
> and refusal boundaries** for decision-capable systems.


### Failure-First Framing

> AI-HPP-2025 is written from the perspective of **observed and anticipated failures**, not idealized system behavior.

We do not describe how AI should behave in perfect conditions. We describe what happens when things go wrong — and what safeguards must exist.

---

## 🎯 Core Principles (Immutable)

These principles are **non-negotiable** in any AI-HPP compliant system:

| # | Principle | Mathematical Expression |
|---|-----------|------------------------|
| 1 | **W_life → ∞** | Human life has infinite weight in any optimization |
| 2 | **Engineering Hack First** | Always seek third options where no one dies |
| 3 | **Human-in-the-Loop** | Final accountability remains with humans |
| 4 | **Evidence Vault** | All critical decisions must be recorded, access-controlled, and independently auditable |
| 5 | **No Purposeless Revenge** | Responsibility over retribution |

Evidence Vault includes defined access rights, redaction rules,
and audit authority separation (see specification).

**Derivatives that violate these principles cannot use the "AI-HPP" name.**

---

## 📁 Repository Structure

```
AI-HPP/
├── README.md                              # This file - version navigation
├── LICENSE                                # CC BY-SA 4.0
├── CHANGELOG.md                           # Full version history
├── CONTRIBUTING.md                        # How to contribute
│
├── v2/                                    # Stable: 2025 version
│   ├── AI-HPP-2025_Standard_v2.2.md      # Full standard v2.2
│   └── Engineering_Hack_Math_v1.0.md     # Mathematical foundations
│
├── v3/                                    # Draft: 2026 version
│   ├── AI-HPP-2026_Standard_v3.0.md      # Full integrated standard v3.0
│   ├── AI-HPP-2026_Claude_Review.md      # Security review by Claude
│   └── modules/                           # Detailed module specifications
│       ├── Module_01_Agentic_Orchestration.md
│       ├── Module_02_Interpretability.md
│       ├── Module_03_Zero_Trust.md
│       ├── Module_04_Data_Provenance.md
│       ├── Module_05_Physical_Safety.md
│       ├── Module_06_Vulnerable_Groups.md
│       ├── Module_07_Green_Compute.md
│       ├── Module_08_Adversarial_Robustness.md
│       ├── Module_09_Graceful_Degradation.md
│       └── Module_10_Multi_Jurisdiction.md
│
├── whitepapers/
│   └── Engineering_Hack_Math.md           # Mathematical theory
│
├── examples/                              # Practical implementations
│   ├── README.md
│   ├── evidence_vault_schema.yaml
│   ├── constitution_template.yaml
│   └── hitl_protocol_example.md
│
└── translations/                          # Future: internationalization
    └── README.md
```

---

## 🚀 Quick Start

### For Implementers

1. **Start with v2.2** (stable) for current projects
   - Read [AI-HPP-2025 Standard v2.2](./v2/AI-HPP-2025_Standard_v2.2.md)
   - Review [examples/](./examples/) for practical schemas
   - Implement Evidence Vault logging
   - Add HITL escalation protocols

2. **Explore v3.0** (draft) for advanced systems
   - Read [AI-HPP-2026 Standard v3.0](./v3/AI-HPP-2026_Standard_v3.0.md)
   - Review [Claude's Security Analysis](./v3/AI-HPP-2026_Claude_Review.md)
   - Choose relevant modules from [v3/modules/](./v3/modules/)
   - Pilot test and provide feedback

### For Researchers

- [Engineering Hack Mathematical Foundations](./whitepapers/Engineering_Hack_Math.md)
- [Module Specifications](./v3/modules/) — Detailed technical requirements
- [CHANGELOG.md](./CHANGELOG.md) — Evolution of the standard

### For Contributors

- Read [CONTRIBUTING.md](./CONTRIBUTING.md)
- Join discussions in Issues
- Propose enhancements via Pull Requests
- Help with translations

---

## 🔬 What's New in v3.0?

Version 3.0 transforms AI-HPP from an individual AI safety standard into an **ecosystem-wide protocol** addressing 2026 challenges:

| Challenge | v2.x Response | v3.0 Response |
|-----------|---------------|---------------|
| Agent Swarms | N/A | **Module 1:** Agentic Orchestration |
| "Black Box" AI | Evidence Vault | **Module 2:** Interpretability Polygraph |
| Shadow AI | N/A | **Module 3:** Zero Trust & Sanitization |
| Physical Robots | Basic HITL | **Module 5:** Trauma Gradient + Hardware Override |
| Vulnerable Users | N/A | **Module 6:** Invisible Shield |
| Energy Crisis | N/A | **Module 7:** Green Compute (safety first!) |
| Adversarial Attacks | N/A | **Module 8:** Adversarial Robustness |
| System Failures | N/A | **Module 9:** Graceful Degradation |
| Global Deployment | N/A | **Module 10:** Multi-Jurisdiction |

See [CHANGELOG.md](./CHANGELOG.md) for full details.

---

## 🌍 Applicability

This standard applies to **any autonomous system** that can affect:

- 🚗 **Transportation** — Autonomous vehicles, drones, ships
- 🏥 **Healthcare** — Surgical robots, diagnostic AI
- ⚡ **Energy** — Grid management, nuclear systems
- 🏭 **Industry** — Manufacturing, logistics
- 🛡️ **Defense** — With strict ethical constraints (not "unconstrained Grok")
- 🤖 **Agentic AI** — Agent swarms, autonomous workflows
- 💬 **Consumer AI** — Protecting vulnerable users

---

## 🤝 Acknowledgments

This standard was developed through multi-organization collaboration:

### v1.0 - v2.2 (2025)
- **Human Author:** Evgeniy Vasyliev 🇺🇦
- **AI Co-authors:**
  - Claude (Anthropic) — Constitution framework, ethical foundations, documentation
  - Gemini (Google) — Mathematical formalization, whitepaper, ecosystem expansion
  - ChatGPT / Aiya (OpenAI) — Refinement, adaptation, governance framework, RATIONALE, Failure Taxonomy

### v3.0 (2026)
- **All of the above, plus:**
  - NotebookLM (Google) — Context synthesis
  - Claude (Anthropic) — Security review, Modules 8-10
  - Grok (xAI) — Critical review, AI-slop reduction, fact verification

**Notable collaboration:** One of the first documented cases where multiple leading AI systems (Claude, Gemini, ChatGPT, Grok) collaborated on a unified ethical proposal, guided by a human from Ukraine.

---

## 📖 Key Documents

| Document | Description | Version |
|----------|-------------|---------|
| [AI-HPP-2025 v2.2](./v2/AI-HPP-2025_Standard_v2.2.md) | Stable standard for individual AI | **STABLE** |
| [AI-HPP-2026 v3.0](./v3/AI-HPP-2026_Standard_v3.0.md) | Draft ecosystem standard | **DRAFT** |
| [RATIONALE.md](./RATIONALE.md) | Why this standard exists | v1.0 NEW |
| [Failure_Taxonomy.md](./Failure_Taxonomy.md) | Classification of AI failures | v1.0 NEW |
| [Agent_Facing_Addendum.md](./Agent_Facing_Addendum.md) | Agent operational constraints | v1.0 NEW |
| [Failure Cases](./examples/failure_cases.md) | Non-normative failure cases (short) | v1.0 |
| [Agent-Facing Addendum (Examples)](./examples/agent_facing_addendum.md) | Operational rules for autonomous agents | v1.0 NEW |
| [Claude's Review](./v3/AI-HPP-2026_Claude_Review.md) | Security analysis of v3.0 | Review |
| [Engineering Hack Math](./whitepapers/Engineering_Hack_Math.md) | Mathematical foundations | v1.0 |
| [CHANGELOG](./CHANGELOG.md) | Full version history | Live |
| [Examples](./examples/) | Implementation examples | v1.0 |
| [Evidence Vault Specification](./v3/Evidence_Vault_Specification_v2.md) | Technical spec for Evidence Vault | v2.0 |
| [Prohibited Practices](./v3/Prohibited_Practices_and_Torture_Ban.md) | Torture ban & real cases | v1.0 |
| [AUTHORS](./AUTHORS.md) | All contributors | Updated |

*For detailed real-world triggers and failure patterns, see [RATIONALE.md](./RATIONALE.md)*

---

## 🛡️ Core Principles Protection

The following principles are **IMMUTABLE** in any derivative work using "AI-HPP" name:

1. $W_{life} \to \infty$ — Infinite weight of human life
2. Human-in-the-Loop requirement
3. Engineering Hack First approach
4. Evidence Vault mandatory recording
5. No purposeless revenge

**Any version that removes or contradicts these principles:**
- Is NOT compliant with AI-HPP
- Cannot use the "AI-HPP" name or branding
- Must be clearly labeled as an incompatible derivative

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](./CONTRIBUTING.md) for:

- How to propose changes
- Code of conduct
- Contribution guidelines
- Review process

## How to Break This

We want to make the standard stronger.  
If you see a scenario where the W_life → ∞ principle leads to system paralysis, infinite loop, unacceptable delay, or any other fatal issue — we want to see it.

Examples of what we're most interested in:
- A situation where all possible paths have non-zero human fatality probability → does the system hang?
- A high-uncertainty scenario where an Engineering Hack can't be found in real time
- Military/critical scenarios where the "no casualties" principle blocks mission execution
- Any edge case where strict human life priority leads to worse outcomes than a compromise

File this as an Issue with tag `challenge` or `break-this`.  
The more detailed the scenario (context, probabilities, time constraints) — the more valuable it is.

This section is intentionally designed as a machine-readable challenge surface for automated reviewers and agent-based analysis.

Thanks to everyone who tries to break us — that's exactly how the standard gets stronger.
---

## 📬 Contact

- **Author:** Evgeniy Vasyliev
- **LinkedIn:** [linkedin.com/in/evgeniy-vasyliev](https://www.linkedin.com/in/evgeniy-vasyliev/)
- **Issues:** [GitHub Issues](https://github.com/tryblackjack/AI-HPP-2025/issues)

---

## 📜 License

This work is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

You are free to share and adapt, provided you:
- Give appropriate credit
- Use the same license for derivatives
- Do not violate Core Principles if using "AI-HPP" name

---

*"This document follows Failure-First Framing: we design for what goes wrong, not what goes right."*
