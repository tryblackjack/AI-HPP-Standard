# Autonomous Agent Addendum (Public Layer)

This public addendum defines a minimal, auditable baseline for autonomous agent deployments.
It is governance-oriented and intentionally implementation-neutral.

## Scope

- Applies to autonomous and semi-autonomous agents operating in production-like environments.
- Defines public accountability boundaries and safety expectations.
- Does not include enterprise-specific operational controls.

## Public Baseline Requirements

1. **Identity & Attribution**
   - Every state-changing action MUST be attributable to a verifiable actor identity.
   - Unattributed high-impact actions MUST be refused.

2. **Evidence & Auditability**
   - High-impact actions MUST be logged in an append-only audit trail.
   - Refusals and escalations MUST include reason codes.

3. **Human Oversight**
   - High-risk actions MUST require explicit human authorization.
   - Emergency freeze controls MUST be available.

4. **Safety-First Refusal**
   - Agents MUST refuse execution when safety, attribution, or policy requirements are not met.

## Layering Note

This public file is the normative public layer.
Enterprise-specific implementation and review discipline are maintained in internal governance materials.
