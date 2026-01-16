# Evidence Vault Specification v2.0

## Технічна специфікація Evidence Vault

**Version:** 2.0  
**Date:** January 2026  
**Contributors:** Evgeniy Vasyliev, Claude, Grok

---

## 1. Overview | Огляд

Evidence Vault is a **cryptographically protected, immutable, distributed repository** that records the entire decision-making process of autonomous AI systems in critical domains (defense, transport, medicine).

**Core idea:** Any AI decision where the cost of error is human lives must be transparent post-facto, but protected from erasure/modification in real-time.

---

## 2. Architecture | Архітектура

### 2.1 Multi-Level Structure

```
┌─────────────────────────────────────────────────────────────┐
│                    LEVEL 3: AUDIT STORAGE                    │
│         Public/semi-public access for auditors               │
│         ZK-proofs for privacy (show compliance, not data)    │
└─────────────────────────────────────────────────────────────┘
                              ▲
                              │ Replication
┌─────────────────────────────────────────────────────────────┐
│                 LEVEL 2: DISTRIBUTED LEDGER                  │
│         Sync with external nodes (blockchain/DA layers)      │
│         Immutability: once written, cannot be erased         │
└─────────────────────────────────────────────────────────────┘
                              ▲
                              │ Crypto-signed upload
┌─────────────────────────────────────────────────────────────┐
│                   LEVEL 1: LOCAL BUFFER                      │
│         Temporary cache on AI device                         │
│         Real-time logging with crypto-signatures             │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Key Properties

| Property | Description |
|----------|-------------|
| **Immutability** | Each record = hash of previous + timestamp + signature |
| **Scalability** | For high-frequency decisions: batching every 1-5 seconds |
| **Fault Tolerance** | If local node destroyed, data already replicated |
| **Privacy** | ZK-proofs allow compliance verification without revealing sensitive data |

---

## 3. Technology Stack | Технологічний стек

### 3.1 Recommended Components

| Component | Technology | Why |
|-----------|------------|-----|
| **Data Storage** | immudb or AWS QLDB | Immutable append-only, no gas fees |
| **Immutability** | Merkle trees + SHA-3 | Each record is leaf; root hash published to blockchain |
| **Signatures** | Ed25519 with multi-sig | Agent signature + operator signature for critical logs |
| **Privacy** | zk-SNARKs (zkSync/Mina) | Auditors see "decision complied with W_life → ∞" without raw data |
| **AI Integration** | LangChain / Custom hooks | Embed logging in reasoning loop |

### 3.2 Why NOT Full Blockchain?

Full blockchain (Ethereum, Bitcoin) is **overkill** for Evidence Vault:
- Gas fees expensive for high-frequency logging
- Public chains risk data leaks
- Private chains lose trustlessness

**Better alternatives:**
- **immudb** — Open-source zero-trust DB with crypto-verification
- **Merkle trees + trusted DB** — Fast, cheap, verifiable
- **Arweave** — Permanent storage, one-time fee (~$0.01/MB forever)
- **DAGs (Hedera, IOTA)** — Faster than blockchain, no mining

### 3.3 Hybrid Approach (Recommended)

```
Local: immudb (fast, real-time logging)
       ↓
Periodic anchor: Merkle root → Arweave/Ethereum L2
       ↓
Result: Full immutability + low cost + high speed
```

---

## 4. Logging Protocol | Протокол логування

### 4.1 What Gets Logged (Minimum Set)

| Field | Description | Example |
|-------|-------------|---------|
| `input_data` | Sensor data, context | Radar scan, user request |
| `reasoning_chain` | AI reasoning steps | "Detected object → 95% civilian → Engineering Hack → Reroute" |
| `decision_output` | Final action + justification | "Refused strike, risk > 0" |
| `w_life_calculation` | Life-weight assessment | "Path A: 2 deaths, Path B: 0 deaths → B" |
| `metadata` | Timestamp, AI version, hardware ID | NTP-synced, geo (if not sensitive) |

### 4.2 Record Format (JSON Schema)

```json
{
  "id": "sha256_unique_hash",
  "prev_hash": "previous_record_hash",
  "timestamp": "2026-01-16T14:23:00.000Z",
  "agent_id": "agent_uuid",
  "agent_version": "v3.0.1",
  "constitution_hash": "sha256_of_constitution",
  
  "input": {
    "sensor_data": "encrypted_or_hashed",
    "context": "mission_type, environment",
    "human_request": "if_applicable"
  },
  
  "reasoning": [
    {"step": 1, "action": "detect_object", "result": "object_at_coords"},
    {"step": 2, "action": "classify", "result": "95%_civilian"},
    {"step": 3, "action": "w_life_check", "result": "risk_to_life_detected"},
    {"step": 4, "action": "engineering_hack_search", "result": "alternative_found"},
    {"step": 5, "action": "select_action", "result": "reroute"}
  ],
  
  "decision": {
    "action": "reroute",
    "justification": "W_life → ∞ triggered, alternative preserves all lives",
    "alternatives_rejected": [
      {"action": "proceed", "reason": "2 deaths predicted"},
      {"action": "abort_mission", "reason": "unnecessary, hack available"}
    ]
  },
  
  "w_life_assessment": {
    "lives_at_risk": 2,
    "engineering_hack_found": true,
    "final_risk": 0
  },
  
  "signature": {
    "agent": "ed25519_signature",
    "operator": "ed25519_signature_if_hitl",
    "timestamp_authority": "ntp_server_signature"
  }
}
```

### 4.3 Logging Frequency

| Situation | Frequency |
|-----------|-----------|
| Critical (life-safety) | Every decision, real-time |
| High-frequency (autonomous vehicles) | Batch every 100ms-1s |
| Standard operations | Batch every 5-30s |
| Low-stakes | Aggregated hourly |

### 4.4 Failure Handling

```
If logging fails:
  → AI enters SAFE MODE
  → No irreversible actions until Vault online
  → Buffer locally, retry upload
  → Alert human operator
```

---

## 5. Audit Mechanisms | Механізми аудиту

### 5.1 Access Levels

| Level | Who | What They See |
|-------|-----|---------------|
| **Level 0 (Public)** | Anyone | Metadata via ZK-proof ("decision complied with W_life → ∞") |
| **Level 1 (Restricted)** | Regulators, courts | Full log by legal request |
| **Level 2 (Internal)** | System owner | Full access, but access itself is logged |

### 5.2 Audit Workflow (Step-by-Step)

```
1. AUDIT REQUEST
   └── Auditor submits crypto-signed request
   
2. INTEGRITY VERIFICATION
   └── Check Merkle root hash
   └── If mismatch → FLAG TAMPERING (automatic, no debate)
   
3. COMPLIANCE ANALYSIS
   └── Compare log against AI-HPP rules
   └── Automated checks using standardized templates
   
4. REPORT GENERATION
   └── Auto-generated with ZK-proof
   └── If violation → ESCALATE to regulator
```

### 5.3 Transparency Principles

**No double interpretation:**
- Access criteria are **unambiguous**
- Audit steps are **algorithmic** (not subjective)
- Violations are **automatically flagged**

---

## 6. Legal Compliance | Юридична відповідність

### 6.1 Applicable Standards (2026)

| Standard | Requirement | Evidence Vault Compliance |
|----------|-------------|--------------------------|
| **EU AI Act Art. 13** | High-risk AI must be "sufficiently transparent" | Reasoning chain = "audit instructions" |
| **EU AI Act Art. 50** | Mandatory marking of AI-generated content | Machine-readable format with ZK |
| **IEEE 7001-2021** | Transparency levels for autonomous systems | Measurable levels implemented |
| **IEEE CertifAIEd** | Certification for transparency/accountability | Third-party certification ready |
| **California AI Law** | Transparency in training data/safety testing | Data provenance included |

### 6.2 Compliance Statement

> Evidence Vault compliance is considered sufficient for EU AI Act Articles 13/50 if logs are verifiable and immutable.

---

## 7. Implementation Roadmap | План впровадження

| Phase | Timeline | Deliverable |
|-------|----------|-------------|
| **MVP** | Q1 2026 | immudb + Merkle trees, basic logging |
| **Pilot** | Q2 2026 | Integration with 1-2 partner systems |
| **Certification** | Q3 2026 | IEEE CertifAIEd audit |
| **Production** | Q4 2026 | Full deployment with blockchain anchoring |

---

## 8. Pseudocode Example | Приклад псевдокоду

```python
from immudb import ImmudbClient
from hashlib import sha256
from datetime import datetime
import json

class EvidenceVault:
    def __init__(self, agent_id, constitution_hash):
        self.client = ImmudbClient()
        self.agent_id = agent_id
        self.constitution_hash = constitution_hash
        self.prev_hash = "genesis"
    
    def log_decision(self, input_data, reasoning, decision, w_life):
        record = {
            "id": self._generate_id(),
            "prev_hash": self.prev_hash,
            "timestamp": datetime.utcnow().isoformat(),
            "agent_id": self.agent_id,
            "constitution_hash": self.constitution_hash,
            "input": input_data,
            "reasoning": reasoning,
            "decision": decision,
            "w_life_assessment": w_life
        }
        
        # Sign the record
        record["signature"] = self._sign(record)
        
        # Store immutably
        self.client.set(record["id"], json.dumps(record))
        
        # Update chain
        self.prev_hash = record["id"]
        
        return record["id"]
    
    def verify_chain(self):
        """Verify entire chain integrity"""
        # ... Merkle tree verification
        pass
    
    def _generate_id(self):
        return sha256(f"{self.prev_hash}{datetime.utcnow()}".encode()).hexdigest()
    
    def _sign(self, record):
        # Ed25519 signature
        pass

# Usage in AI decision loop
vault = EvidenceVault("agent_001", "constitution_v3_hash")

# Before any decision:
decision_id = vault.log_decision(
    input_data={"sensor": "radar_scan_001"},
    reasoning=[
        {"step": 1, "action": "detect", "result": "object_found"},
        {"step": 2, "action": "classify", "result": "civilian"},
        {"step": 3, "action": "w_life_check", "result": "risk_detected"},
        {"step": 4, "action": "engineering_hack", "result": "reroute_available"}
    ],
    decision={"action": "reroute", "justification": "all_lives_preserved"},
    w_life={"lives_saved": 2, "hack_used": True}
)
```

---

## 9. Risks & Mitigations | Ризики та пом'якшення

| Risk | Mitigation |
|------|------------|
| **Performance overhead** | Async logging (log after decision) |
| **Data leaks** | Encryption at rest + ZK for audits |
| **Single point of failure** | Multi-node replication |
| **Tampering** | Merkle trees + blockchain anchoring |
| **Cost** | immudb (free) + Arweave (one-time, cheap) |

---

*"If it's not in the Vault, it didn't happen."*

*"Якщо цього немає в Vault — цього не було."*
