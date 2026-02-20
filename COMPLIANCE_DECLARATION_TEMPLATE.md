# AI-HPP Compliance Declaration (Public)

This document is a public self-declaration of alignment with the AI-HPP standard.

AI-HPP is an open governance framework. This declaration does not imply certification.

---

## 1. System Overview

- **System name:**
- **Organization / owner:**
- **Primary use-case:**
- **Deployment type:** (Prototype / Pilot / Production)
- **Public link:** (repo / website / docs)
- **Contact:** (email or issue link)

---

## 2. Declared Compliance Level

Select one:

- [ ] **Core Compliant**
- [ ] **Agent Compliant**
- [ ] **Enterprise Compliant**

---

## 3. Scope of Compliance

Describe what is covered and what is not.

- **In scope:**
- **Out of scope:**
- **Known limitations:**

---

## 4. Implementation Summary (Required)

Provide short, concrete statements:

### 4.1 Evidence Vault
- How decisions are logged:
- What is immutable:
- What is included (e.g., rejected alternatives / overrides):

### 4.2 Prompt Injection Mitigation
- Where untrusted input enters:
- Key defenses (e.g., separation / schema / refusal policy):

### 4.3 Refusal Policy
- When the system refuses:
- When it escalates:
- Default behavior under uncertainty:

---

## 5. Additional Requirements (Depending on Level)

### 5.1 Agent Level (if applicable)
- **Execution separation** (Cognition → Validation → Execution):
- **Tool governance** (capabilities, risk classification, rate limits):
- **Memory integrity** (classes, write validation, untrusted flags):
- **Capability escalation control:**
- **Recursive containment** (if multi-agent):
- **Deliberation / decision buffering:**
- **Failure transparency** (no silent retries / override logging):

### 5.2 Enterprise Level (if applicable)
- **Economic safeguards / loss limits / anomaly detection:**
- **Human veto for critical actions:**
- **Governance documentation available publicly (if any):**
- **Operational monitoring & incident response basics:**

---

## 6. Public References

Link to supporting public artifacts (recommended):

- Architecture overview:
- Security / threat model notes:
- Audit logs example (redacted):
- Test cases / evaluation:

---

## 7. Declaration

By publishing this document, we declare that we have implemented the requirements for the selected AI-HPP compliance level within the declared scope.

- **Declared by:**  
- **Date:**  
- **Version of AI-HPP referenced:**

Рекомендация для проектов: копируют файл как COMPLIANCE_DECLARATION.md в свой репо и заполняют.
