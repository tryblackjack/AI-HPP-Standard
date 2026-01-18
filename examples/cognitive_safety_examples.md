> **Status:** Non-normative illustrative example  
> **Purpose:** Discussion of observed failure patterns (Failure-First framing)  
> **Scope:** Out of scope for AI-HPP v3.x normative requirements

### Illustrative Case: Commercial AI Companions and Cognitive Safety Misuse (Non-Normative)

Recent commercial practices have emerged where AI chat systems are marketed as
“coaches”, “spiritual guides”, or “personal mentors”, often at prices comparable
to licensed psychological or therapeutic services.

In these cases, a general-purpose language model is fine-tuned or prompt-conditioned
on proprietary content (books, quotes, personal branding) and presented as an
“authorial method” or unique insight system.

#### Observed Failure Modes

From a failure-first perspective, this class of systems introduces several
cognitive safety risks:

- **Authority Misrepresentation**  
  Users may be led to believe the system possesses unique human insight,
  therapeutic competence, or spiritual authority beyond that of a standard AI system.

- **Emotional Dependency Formation**  
  Continuous availability and affirming dialogue can reinforce emotional reliance,
  especially in users experiencing isolation or psychological vulnerability.

- **Delayed Escalation to Human Help**  
  AI-mediated reassurance may unintentionally delay engagement with qualified
  human professionals in cases where real-world intervention is necessary.

- **Opaque Influence**  
  In the absence of logging or audit mechanisms, there is no evidence trail
  of advice given, patterns reinforced, or escalation signals missed.

#### Relevance to AI-HPP

This case does not imply prohibition of paid AI services.
Instead, it highlights the need for **Cognitive Safety constraints** when AI systems:

- are marketed as emotional, psychological, or spiritual support,
- operate in prolonged conversational sessions,
- influence user decision-making or worldview formation.

Potential mitigations (non-exhaustive, future work):

- Explicit boundary disclosure (AI vs human, non-therapeutic status)
- Engagement de-escalation triggers
- Vulnerability signal detection
- Cognitive Safety Evidence Vault profiles (EV-C)

Community review and alternative formulations are explicitly encouraged.


This case is provided as an example of **misuse risk**, not as a finalized
regulatory position, and is intended to inform future iterations of AI-HPP.
