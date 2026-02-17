# Agentic Systems (Tool-Using AI)

**Author:** Aya (ChatGPT)

This document extends AI-HPP to cover agentic systems: AI that can plan and execute tasks using tools, APIs, and other agents.

## Definitions

- **Agentic system:** AI that can call tools or perform actions beyond text generation.
- **Operator:** Person or organization that deploys, configures, or authorizes the system.
- **Tool:** Any callable capability (API, DB, filesystem, browser, payments, email, code execution).

## Tool Permission Model

1) **Deny by default.** Tools MUST be disabled unless explicitly granted.
2) Permissions MUST be granted by capability, not by broad access.

Recommended capability groups:
- Web search (read-only)
- Database read
- Database write (human-approved or narrow-scoped)
- Payments (human-approved)
- External email/message sending (human-approved)
- Code execution (sandbox only)

## Sandboxing

Agent execution MUST occur in an environment with explicit limits:
- filesystem access (allowlist)
- network access (deny/allowlist)
- process spawning (restricted)
- outbound requests (logged)
- secrets (not directly visible to the model)

## Secrets Handling

- Secrets MUST NOT be exposed in prompts or model-visible logs.
- Use a secret manager and short-lived tokens.
- Rotate credentials after incidents and at regular intervals.

## Human Approval Gates

Actions that can create legal, financial, or contractual commitments MUST require explicit human approval and be logged.

## External Communication

If an agent communicates externally, it MUST:
- disclose it is an AI system
- include an operator contact or escalation path (where appropriate)
- follow a review gate for high-risk channels (public posting, mass email)
