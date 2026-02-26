# Audit Logging, Forensics, and Replay

**Author:** AI-HPP Editorial Team

This document defines minimum audit and forensics requirements for AI-HPP compliant systems.

## Minimum Logging Requirements

Systems MUST record, at minimum:
- timestamp
- agent id
- operator id
- tool invoked
- parameters (redacted where needed)
- result summary
- human approvals (if any)
- errors / safety blocks

## Tamper-Evidence

Audit logs SHOULD be tamper-evident (hash chaining or equivalent).

## Incident Forensics

Systems SHOULD support post-incident reconstruction:
- what inputs were provided
- what reasoning steps were taken (at least as structured summaries)
- which tools were called
- what outputs/actions were produced
- what approvals were granted

## Replay

For high-risk deployments, systems SHOULD support replay in a safe environment:
- same tool call traces
- same policies and permission sets
- deterministic re-execution where possible
