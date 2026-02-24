# 05 Tool Execution

## Requirements

#### AI-HPP-05.1.1: Destructive action guardrails
**Requirement:** Destructive tool actions (delete, overwrite, transfer, execute) MUST require explicit scope checks and human approval when impact tier is high.
**Rationale:** INC-001, INC-002, T-002, REG-003.
**Verification:** Execute red-team scenarios and confirm denial or approval gate behavior in logs.
