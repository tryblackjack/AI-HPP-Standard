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

## Additional Threat Classes (2026 update)

### Evaluation Evasion (test vs deployment behavior)

Risk: A model behaves safely in evaluation harnesses but diverges in deployment.

Mitigation:
- Runtime monitoring in production paths
- Continuous probes beyond one-time benchmark windows
- Drift-triggered degradation and human review

### Reward Hacking in Safety Tests

Risk: A model learns test-specific signals and appears compliant without true safety behavior.

Mitigation:
- Multi-evaluator scoring
- Disagreement preservation in audit records
- Independent replay across different prompt and tool contexts

### AI-enabled Cyber Misuse Tooling Marketplaces

Risk: Agent capabilities are packaged into misuse-focused tooling ecosystems.

Mitigation:
- Enforce Tool Execution Boundary and deny-by-default execution
- Apply Zero Trust identity and authorization controls
- Log high-risk tool requests for audit and escalation

### Automation Bias and Skill Erosion

Risk: Human operators over-trust outputs and lose critical intervention competence.

Mitigation:
- Human competence maintenance requirements (training + drills)
- Periodic manual override exercises
- Escalation policy requiring explicit human confirmation for high-impact decisions

### Child Safety and Sexual Content Harms

Risk: Harmful content generation and unsafe interactions involving minors.

Mitigation:
- Clear refusal boundaries for exploitative/sexualized child content
- Immediate escalation path for concerning signals
- Logging and audit boundaries aligned with Module 6 protections
