# Interface: Approvals (HITL / Dual Control)

## Purpose
Gate high-impact actions.

## Requirements
- create_approval_request(action_summary, evidence_ref)
- approve(request_id, approver_id)
- deny(request_id, approver_id, reason)
- dual_control_mode: require 2 distinct approvers for critical actions
