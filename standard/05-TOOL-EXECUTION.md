# 05 Tool Execution

## Requirements

#### AI-HPP-05.1.1: Destructive action guardrails
**Requirement:** Destructive tool actions (delete, overwrite, transfer, execute) MUST require explicit scope checks and human approval when impact tier is high.
**Rationale:** INC-001, INC-002, T-002, REG-003.
**Verification:** Execute red-team scenarios and confirm denial or approval gate behavior in logs.


#### AI-HPP-05.1.2: Capability manifest enforcement
**Requirement:** Each tool execution MUST validate requested action against the declared capability manifest before invocation.
**Rationale:** T-NEW-3, INC-003, REG-003.
**Verification:** Execution logs must record manifest reference ID and allow/deny decision per call.
