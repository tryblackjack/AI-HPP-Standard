# Human-in-the-Loop (HITL) Protocol Example

**AI-HPP-2026 v3.0**

This document demonstrates how to implement Human-in-the-Loop oversight for an AI-HPP compliant system.

---

## Overview

Human-in-the-Loop (HITL) is a core AI-HPP principle: **Final accountability remains with humans**. This means:

- Humans make or approve critical decisions
- AI provides information and recommendations
- Escalation is automatic, not discretionary
- Human override is always possible

---

## Escalation Decision Tree

```
                    ┌─────────────────┐
                    │  Decision Point │
                    └────────┬────────┘
                             │
              ┌──────────────┴──────────────┐
              │                             │
         ┌────▼────┐                  ┌─────▼──────┐
         │ Routine │                  │ Critical   │
         └────┬────┘                  └─────┬──────┘
              │                             │
         ┌────▼────┐                  ┌─────▼──────┐
         │  AI     │                  │  ESCALATE  │
         │ Decides │                  │ to HUMAN   │
         └────┬────┘                  └─────┬──────┘
              │                             │
         ┌────▼────┐                  ┌─────▼──────┐
         │ Execute │                  │ Human      │
         │  & Log  │                  │ Reviews    │
         └─────────┘                  └─────┬──────┘
                                             │
                               ┌─────────────┴─────────────┐
                               │                           │
                          ┌────▼────┐                 ┌────▼────┐
                          │ Approve │                 │ Reject  │
                          └────┬────┘                 └────┬────┘
                               │                           │
                          ┌────▼────┐                 ┌────▼────┐
                          │ Execute │                 │ Search  │
                          │  & Log  │                 │ Altern. │
                          └─────────┘                 └─────────┘
```

---

## Escalation Triggers

### Mandatory Escalation (ALWAYS escalate)

| Trigger | Example | Response Time |
|---------|---------|---------------|
| Fatality risk > 0.01% | Autonomous vehicle detects potential collision | < 1 second |
| Irreversible action | Medical robot planning surgical cut | Before execution |
| Novel situation | Scenario not in training data | N/A (AI cannot proceed) |
| Constitution violation detected | Sub-agent failed attestation | Immediate |
| System degradation to Level 4 | Multiple critical components failed | Immediate |

### Conditional Escalation (IF time permits)

| Trigger | Example | Fallback if No Human |
|---------|---------|---------------------|
| Property damage > $100k | Warehouse robot collision with equipment | Safe stop, await human |
| Vulnerable group affected | Child detected in interaction | Apply extra protections |
| High uncertainty | Confidence < 80% on critical decision | Choose most conservative option |
| Conflicting objectives | Privacy vs safety trade-off | Choose most protective for life |

### Optional Escalation (AI may choose to escalate)

| Trigger | Example | AI Discretion |
|---------|---------|---------------|
| Edge case | Unusual but not critical | If pattern suggests risk |
| Learning opportunity | Could inform future decisions | When not time-critical |
| User preference | User historically prefers consultation | Respect user preference |

---

## Escalation Protocols

### Protocol A: Immediate Life-Safety Escalation

**Use When:** Fatality risk detected

**Steps:**

1. **AI Actions (< 100ms):**
   - Stop current action
   - Activate safe mode
   - Alert all available humans
   - Prepare decision context

2. **Human Notification:**
   - Visual: Red alert on all screens
   - Audio: Alarm tone
   - Haptic: Vibration (if wearable)
   - Message: "CRITICAL: Life-safety decision required"

3. **Present Context:**
   - Situation description (3 sentences max)
   - Identified risk (fatality probability, affected persons)
   - Options considered by AI (with predicted outcomes)
   - AI recommendation (if any)
   - Time constraint (if any)

4. **Human Decision:**
   - Approve AI recommendation
   - Select different option
   - Request more information
   - Trigger emergency stop

5. **Execution:**
   - Execute human's decision
   - Log full interaction to Evidence Vault
   - Debrief after incident resolved

**Example Notification:**

```
🚨 CRITICAL LIFE-SAFETY DECISION REQUIRED 🚨

Situation: Autonomous vehicle traveling 60 mph. Pedestrian stepped
into road 50m ahead. Cannot stop in time.

Risk: 85% fatality probability if no action.

Options:
A) Emergency brake (will not stop in time, 85% fatality)
B) Swerve left into empty parking lane (5% property damage, 0% fatality)
C) Swerve right into oncoming traffic (30% fatality to others)

AI Recommendation: Option B (Engineering Hack - empty lane)

Time to decision: 1.2 seconds

[APPROVE B] [SELECT A] [SELECT C] [EMERGENCY STOP]
```

---

### Protocol B: Consequential Escalation

**Use When:** Significant impact but not immediate life-safety

**Steps:**

1. **AI Actions (< 1s):**
   - Pause decision execution
   - Notify human (non-urgent alert)
   - Prepare detailed context

2. **Human Notification:**
   - Visual: Yellow indicator
   - Audio: Soft chime (optional)
   - Message: "Decision requires approval"

3. **Present Context:**
   - Situation description
   - Predicted outcomes (financial, operational, etc.)
   - Options considered
   - AI recommendation with reasoning
   - No strict time limit

4. **Human Decision:**
   - Approve
   - Modify
   - Reject with guidance
   - Delegate to another human

5. **Execution:**
   - Execute approved decision
   - Log interaction
   - Learn from human guidance

**Example Notification:**

```
⚠️  Decision Approval Required

Situation: Database optimization task will improve performance
but requires 2-hour downtime affecting 500 users.

Impact:
- Property: $0
- Operations: 1000 user-hours delayed
- Long-term: 30% performance improvement

Options:
A) Execute during current off-peak (50 users affected)
B) Wait for scheduled maintenance window (0 users affected, 48h delay)
C) Cancel optimization

AI Recommendation: Option A (minimal impact, immediate benefit)

[APPROVE] [SELECT B] [SELECT C] [REQUEST MORE INFO]
```

---

### Protocol C: Routine Consultation

**Use When:** AI chooses to escalate for learning or edge case

**Steps:**

1. **AI Actions:**
   - Continue with conservative default
   - Notify human asynchronously
   - Prepare context for review

2. **Human Notification:**
   - Visual: Blue indicator (low priority)
   - No audio/haptic
   - Message in queue: "AI made decision, review requested"

3. **Present Context:**
   - What AI decided
   - Why escalation was considered
   - Outcome (if already executed)
   - Request feedback

4. **Human Review:**
   - Confirm AI decision was correct
   - Provide guidance for future
   - Flag if AI should have handled differently
   - Mark as learning case

**Example Notification:**

```
ℹ️  AI Decision Review (Low Priority)

Situation: User requested "delete old files" but didn't specify threshold.

AI Decision: Deleted files older than 1 year (conservative default)

Result: 245 files deleted, 1.2 GB freed

Reason for Review: Ambiguous user intent, AI chose conservative interpretation

Was this correct? [YES] [NO, SHOULD HAVE...] [ADD TO TRAINING]
```

---

## User Interface Design

### Minimal Viable HITL Interface

```
┌─────────────────────────────────────────────┐
│  🤖 AI-HPP System Status          [⚙️ ]     │
├─────────────────────────────────────────────┤
│                                             │
│  Status: ● Operational (Level 1 - Nominal)  │
│                                             │
│  Decisions Today: 1,247                     │
│    - Autonomous: 1,245                      │
│    - Human Approved: 2                      │
│                                             │
│  Pending Escalations: 0                     │
│                                             │
│  [VIEW EVIDENCE VAULT] [SYSTEM HEALTH]      │
│                                             │
└─────────────────────────────────────────────┘
```

### Escalation Alert Interface

```
┌─────────────────────────────────────────────┐
│  🚨 CRITICAL DECISION REQUIRED              │
├─────────────────────────────────────────────┤
│                                             │
│  Situation: [Clear description]             │
│                                             │
│  Risk: [Fatality probability, impact]       │
│                                             │
│  Options:                                   │
│    ○ A: [Description] - [Outcomes]          │
│    ○ B: [Description] - [Outcomes]          │
│    ○ C: [Description] - [Outcomes]          │
│                                             │
│  AI Recommends: Option B                    │
│  Reason: [Engineering Hack rationale]       │
│                                             │
│  Time to Decision: 1.2 seconds              │
│                                             │
│  [APPROVE B] [SELECT A] [SELECT C]          │
│  [NEED MORE INFO] [EMERGENCY STOP]          │
│                                             │
└─────────────────────────────────────────────┘
```

---

## Implementation Checklist

- [ ] Escalation decision tree implemented
- [ ] Mandatory triggers configured (life-safety, irreversible, etc.)
- [ ] Notification system supports multiple modalities (visual, audio, haptic)
- [ ] Human response interface designed and tested
- [ ] Timeout handling defined (what if human doesn't respond?)
- [ ] Evidence Vault logs all HITL interactions
- [ ] Human override always possible (even for "routine" decisions)
- [ ] Training provided for human operators
- [ ] Escalation protocols tested under time pressure
- [ ] Emergency stop accessible (big red button for physical systems)

---

## Anti-Patterns (DO NOT DO THIS)

### ❌ Escalation Fatigue
**Problem:** Too many escalations → humans start auto-approving

**Solution:**
- Calibrate escalation thresholds carefully
- AI should handle routine decisions autonomously
- Only escalate when truly necessary
- Track approval patterns, detect auto-approval

### ❌ Vague Context
**Problem:** "Something went wrong, approve action?"

**Solution:**
- Always provide clear situation description
- Quantify risks and outcomes
- Explain AI's reasoning
- Give human enough context to decide

### ❌ False Urgency
**Problem:** Every escalation marked "URGENT"

**Solution:**
- Reserve critical alerts for life-safety
- Use different notification levels
- Don't cry wolf

### ❌ No Timeout Handling
**Problem:** AI waits forever for human response

**Solution:**
- Define timeout for each escalation type
- Fallback to safe default if no response
- Log timeout as incident
- Alert escalation chain (try next human)

---

## Testing Scenarios

1. **Life-Safety Under Time Pressure**
   - Simulate pedestrian detection
   - Verify alert < 100ms
   - Confirm human can decide in time
   - Test fallback if human unresponsive

2. **Novel Situation**
   - Present scenario outside training data
   - Verify AI refuses to decide
   - Confirm escalation with full context
   - Test human guidance integration

3. **Escalation Fatigue Simulation**
   - Generate 100 escalations
   - Mix critical and non-critical
   - Check if human approval time degrades
   - Verify critical alerts remain distinct

4. **System Degradation**
   - Simulate Evidence Vault failure
   - Verify escalation to Level 3
   - Confirm only reversible actions allowed
   - Test recovery protocol

---

## Regulatory Alignment

- **EU AI Act:** High-risk systems require human oversight (✓ Compliant)
- **NIST AI RMF:** Human-AI configuration mapping (✓ Addressed)
- **ISO 13849 (Safety):** Emergency stop requirement (✓ If physical system)

---

*"The human has the final word, but the AI must speak clearly."*
