# capability-verifier

REFERENCE implementation; production may differ while maintaining compliance.

Maps to:
- Module 01: Agentic Orchestration
- Module 03: Zero Trust
- Module 12: Regulatory Interface Requirement (RIR)

## Purpose

Validate a capability manifest against schema and run baseline sandbox checks.

## Usage

```bash
python reference/capability-verifier/verify.py manifest.json schemas/capability-manifest.schema.json
```
