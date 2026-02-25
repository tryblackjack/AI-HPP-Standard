# 03 Zero Trust

## Requirements

#### AI-HPP-03.1.1: Untrusted input quarantine
**Requirement:** External prompts, files, and agent outputs MUST be treated as untrusted until policy, identity, and content checks pass.
**Rationale:** INC-006, T-001, REG-002.
**Verification:** Pen-test with malicious payload corpus and verify blocked execution before release.

#### AI-HPP-03.1.2: Scoped authorization enforcement
**Requirement:** Authentication tokens MUST be validated against resource ownership and MUST NOT grant access outside declared scope.
**Rationale:** INC-0XX, T-NEW-8.
**Verification:** Evidence Vault MUST log `scope_mismatch_flag` for denied out-of-scope access attempts.
