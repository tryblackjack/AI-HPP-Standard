SAFE_FOR_PUBLIC_REPO: YES
NO PRODUCTION DATA. NO SECRETS. NO CUSTOMER INFO.

# AI-HPP Implementation Examples

This directory contains practical implementation examples for AI-HPP-2026 v3.0 standard.

## Contents

| File | Description | Module |
|------|-------------|--------|
| [evidence_vault_schema.yaml](./evidence_vault_schema.yaml) | Evidence Vault data structure specification | Core (v2.x+) |
| [evidence_vault_ref](./evidence_vault_ref/README.md) | Minimal Evidence Vault reference implementation | Core (v3.x) |
| [constitution_template.yaml](./constitution_template.yaml) | Constitution configuration template | Module 1 |
| [hitl_protocol_example.md](./hitl_protocol_example.md) | Human-in-the-Loop protocol implementation | Core (v2.x+) |
| [failure_cases.md](./failure_cases.md) | Short, non-normative failure cases | Cross-cutting |

## Purpose

These examples demonstrate how to implement AI-HPP principles in real systems.
They are starting points, not production-ready code.

## Getting Started

1. **Choose your use case:**
   - Autonomous vehicles → Focus on Physical Safety (Module 5)
   - Agent swarms → Focus on Agentic Orchestration (Module 1)
   - Content generation → Focus on Vulnerable Groups (Module 6)
   - Code generation → Focus on Zero Trust (Module 3)

2. **Review relevant examples:**
   - Start with `evidence_vault_schema.yaml` (required for all)
   - Add `constitution_template.yaml` for agent configuration
   - Implement `hitl_protocol_example.md` for human oversight

3. **Adapt to your system:**
   - These are templates, not prescriptions
   - Modify based on your technical stack
   - Maintain AI-HPP core principles
   - Document your adaptations

## Important Notes

### These Are Examples, Not Official Implementations

The files in this directory demonstrate AI-HPP concepts but are **not** production-ready code. You must:

- Review for your specific security requirements
- Test thoroughly in your environment
- Consult legal counsel for compliance
- Engage safety experts for physical systems
- Validate with interpretability researchers

### Core Principles Are Non-Negotiable

While implementation details are flexible, these principles are **immutable**:

1. $W_{life} \to \infty$ — Human life has infinite weight
2. Human-in-the-Loop — Final accountability with humans
3. Engineering Hack First — Always seek solutions where everyone lives
4. Evidence Vault — All critical decisions must be recorded
5. No Purposeless Revenge — Responsibility over retribution

## Additional Resources

- [AI-HPP-2026 Standard v3.0](../v3/AI-HPP-2026_Standard_v3.0.md) — Full specification
- [Agent-Facing Addendum](../v3/Agent_Facing_Addendum.md) — Identity and auditability notes
- [Module Specifications](../v3/modules/) — Detailed requirements per module
- [Claude's Review](../v3/AI-HPP-2026_Claude_Review.md) — Security analysis and hardening

## Contributing Examples

Have an implementation example to share? We welcome contributions!

1. Ensure it follows AI-HPP principles
2. Document which module(s) it addresses
3. Include comments explaining key decisions
4. Provide context on use case
5. Submit as Pull Request

See [CONTRIBUTING.md](../legacy-top/CONTRIBUTING.md) for details.

## License

Examples in this directory are licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), same as the AI-HPP standard.

---
