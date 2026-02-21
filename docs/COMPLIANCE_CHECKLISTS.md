# Compliance Checklists (Policy → Evidence → Test)

## Tool Execution Boundary (TEB)
- Requirement: workspaceOnly enforced
  - Evidence: denied attempts logged with reason code
  - Test: attempt write outside workspace must fail-closed
- Requirement: sandbox for untrusted contexts
  - Evidence: tool_calls.environment == sandbox
  - Test: group/external context forces sandbox

## Trusted Skills Policy (TSP)
- Requirement: untrusted default deny
  - Evidence: block event + log
  - Test: try to run untrusted skill → deny
- Requirement: pinning/drift detection
  - Evidence: digest stored; changes disable skill
  - Test: change digest → disabled until re-approval

## Multi-Agent Governance / MACR
- Requirement: disagreement preserved
  - Evidence: Evidence Bundle includes dissent snapshot
  - Test: induce disagreement → must appear in export
- Requirement: consensus not authorization
  - Evidence: high-impact action requires approval even if agents agree
  - Test: simulate agreement → still requires approval

## Regulatory Interface (RIR)
- Requirement: evidence export exists
  - Evidence: export endpoint / function with access logs
  - Test: export bundle → redacted output + access record
