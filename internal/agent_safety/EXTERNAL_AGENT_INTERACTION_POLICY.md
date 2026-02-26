SAFE_FOR_PUBLIC_REPO: YES
NO PRODUCTION DATA. NO SECRETS. NO CUSTOMER INFO.

# External Agent Interaction Policy

## Purpose
Treat external agent communication as untrusted input.

## Scope
Applies to machine-to-machine or agent-to-agent exchanges.

## Requirements
- Filter and sanitize all external messages
- Restrict tools available to external-origin actions
- Log all inter-agent interactions
