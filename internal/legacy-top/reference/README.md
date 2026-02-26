SAFE_FOR_PUBLIC_REPO: YES
NO PRODUCTION DATA. NO SECRETS. NO CUSTOMER INFO.

# Reference Implementations

Python 3.10+ reference modules using stdlib + `jsonschema` + `pytest`.

- `capability-verifier/`: schema validation + sandbox requirement checks.
- `risk-calculator/`: file-in/file-out proportional response calculation.
- `degradation-monitor/`: four-level runtime state machine.
- `audit-exporter/`: RIR-style export bundle generation with redaction policy and integrity placeholders.

All modules are local/stateless and are intended for compliance demonstrations.
