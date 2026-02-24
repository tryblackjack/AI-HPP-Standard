# 03 Zero Trust

## Requirements

#### AI-HPP-03.1.1: Untrusted input quarantine
**Requirement:** External prompts, files, and agent outputs MUST be treated as untrusted until policy, identity, and content checks pass.
**Rationale:** INC-006, T-001, REG-002.
**Verification:** Pen-test with malicious payload corpus and verify blocked execution before release.
