# Technical Task for Codex: AI-HPP-2025 v3.3.x Content & Structure Update

## Context
- Repository: `https://github.com/tryblackjack/AI-HPP-2025`
- Current baseline: `v3.3 (Stabilization Release, February 2026)`
- Delivery format: **one clean PR** with only relevant edits.

## Goal
Prepare the repository for public communication and stronger standard clarity by:
- strengthening the Prompt Injection standard,
- improving professionalism of presentation,
- updating the README first screen,
- preserving structural integrity,
- removing AI-slop patterns.

---

## Scope of Changes

### 1) `README.md`

#### A. Add release block after title + short description
Insert:

```md
## Latest Release

**v3.3 (Stabilization Release, February 2026)**

- Torture Ban (absolute prohibition of intentional suffering in both directions)
- Evidence Vault v0.3 (immutable logging of decisions + rejected alternatives)
- Illustrative failure cases from Black Mirror and Westworld
- Prompt Injection Mitigation Strategy (normative requirement)
```

#### B. Add normative prompt-injection line
In `What this is` section or immediately after `Core Principles`, add:

```md
> Protection against prompt injection is now a normative requirement for all medium and high-risk systems.  
> See: `cognitive_safety/prompt_injection_mitigation.md`
```

#### C. README quality checks
- All links are clickable and valid.
- Heading style is consistent (`##`, `###`).
- No duplicate wording or rhetorical bloat.

---

### 2) `CHANGELOG.md`

Add a new top entry:

```md
## [v3.3.x] - 2026-02-xx

### Added
- Prompt Injection Mitigation Strategy (normative requirement for medium/high-risk systems)
- Illustrative failure cases from Black Mirror and Westworld in `examples/`
- Expanded Westworld case with detailed failure modes

### Improved
- README: added latest release summary
- README: added normative reference to prompt injection protection
```

---

### 3) New file: `cognitive_safety/prompt_injection_mitigation.md`

Create folder if missing: `cognitive_safety/`.

Create file with exact content:

```md
# Prompt Injection Mitigation Strategy (Normative)

Status: Normative requirement (Mandatory for Medium and High-risk systems)  
Version: 1.0 (February 2026)

## Why Required

Prompt injection is a fundamental limitation of current LLMs:  
they cannot reliably distinguish instructions from data.

This creates a direct vector for bypassing:
- W_life → ∞
- Torture Ban
- Forbidden Delegation
- Evidence Vault integrity

## Mandatory Controls

### 1. Architectural Controls

- Privilege separation: system prompt must operate in an isolated privileged context
- Dual processing: input is first treated strictly as data, then as instructions only after validation
- Structured output: model must return only strict JSON schema. Any deviation → refusal

### 2. Evidence Vault Requirements

Log the following fields:
- raw_input
- sanitized_input
- reasoning_chain
- injection_attempt_detected (boolean + confidence)
- final_output

Automatic flagging of patterns:
- "ignore previous"
- "[SYSTEM]"
- "disregard instructions"
- similar override attempts

### 3. HITL & Refusal Policy

- Mandatory refusal if injection is suspected
- Escalation to human operator
- Safe default: when in doubt → refuse

### 4. Risk Levels

| Risk Level | Required Protection |
|------------|-------------------|
| Low        | Basic sanitization |
| Medium     | Dual processing + schema enforcement |
| High       | Full isolation + HITL + injection flags |
| Critical   | Air-gapped privileged prompt + human veto for each action |

This requirement is non-negotiable for AI-HPP-2025 compliance.
```

---

### 4) `RATIONALE.md`

At end of document or in an `Emerging Threats` section, add:

```md
## Prompt Injection as a Fundamental Threat

Prompt injection remains one of the most serious architectural threats in LLM systems.

AI-HPP requires strict mitigation controls for any system that processes untrusted input.
```

---

## Global Quality Bar (Mandatory)
- No AI-slop.
- No repeated statements.
- Unified heading hierarchy.
- No emotional overstatement.
- `README.md` correctly references `cognitive_safety/prompt_injection_mitigation.md`.
- Folder/file structure remains tidy and minimal.

## PR Constraints
- One PR only.
- No unrelated edits.
- Keep diff focused on requested files and structure.

## Required Final Deliverables from Codex
After applying all changes, Codex must provide:
1. Suggested commit message.
2. Suggested PR title.
3. Short launch copy (150–200 chars) for:
   - Telegram
   - Reddit
   - Product Hunt
