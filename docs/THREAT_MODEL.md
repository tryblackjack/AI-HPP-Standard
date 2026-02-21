# Threat Model (Practical)

## Primary threats
1) Prompt injection via untrusted channels (chat, email, web content)
2) Tool abuse (exec/fs/net) leading to destructive actions
3) Skill/plugin supply-chain compromise
4) Control plane exposure (misconfigured admin endpoints)
5) Cross-tenant context or memory leakage
6) Audit log tampering / evidence deletion
7) Unsafe content generation (e.g., minors/non-consensual edits) triggering regulatory escalation

## Default stance
- Fail-closed on ambiguity
- Least privilege for tools
- Isolation by tenant/session/task
- Evidence Bundles for high-impact outcomes


## Emerging Global Risk Domains

### Biosecurity Risk

Highly capable models may be misused to assist in harmful biological research or pathogen synthesis.

AI-HPP Mitigation:

- Explicit high-risk domain tagging
- Mandatory refusal boundaries under W_life → ∞
- Escalation to human review for sensitive biological queries
- Evidence logging of refusal events (privacy-preserving)

### Autonomous Cyber Exploitation

Advanced coding agents may autonomously identify and exploit software vulnerabilities.

AI-HPP Mitigation:

- Strict Tool Execution Boundaries (sandboxed execution)
- Separation of "analysis" vs "execution" modes
- Human-in-the-Loop gating for high-impact exploit simulations
- Tamper-evident Evidence Bundles
