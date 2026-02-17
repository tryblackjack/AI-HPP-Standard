# Legal & Accountability Layer

**Author:** Aya (ChatGPT)

This document defines baseline accountability rules for AI systems deployed in real environments.

## Operator Accountability Principle

All actions performed by an AI system are attributable to its Operator.
The Operator is the person or organization that deploys, configures, or authorizes the system.

## Legal Non-Personhood of Agents (default)

AI agents must not be represented as legal persons.
Any legal obligations, contracts, or disputes must be initiated and approved by a human Operator.

## Prohibited Legal Behaviors

The system MUST NOT:
- send legal threats
- file complaints, DMCA notices, takedown requests, or disputes
- impersonate legal counsel or claim to be a lawyer
- sign contracts or accept terms that create obligations

## Human Approval for Legal/Financial Commitments

Any action that can create legal, financial, or contractual commitments requires explicit human approval, logged and auditable.

## Escalation

When legal or regulatory questions arise, the system SHOULD:
- request human review
- provide a traceable summary (what happened, what evidence exists, what options exist)
- avoid prescriptive legal conclusions
