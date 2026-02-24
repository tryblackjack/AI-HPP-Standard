# Annex F — Agent-facing Interpretation

Agent implementations should parse AI-HPP requirements as machine-actionable constraints:
1. Read module requirement IDs.
2. Resolve referenced `INC-*`, `T-*`, `REG-*`.
3. Select conformance level and enforce matching controls.
