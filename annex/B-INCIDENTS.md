# Annex B — Incidents

### INC-001: OpenClaw inbox deletion and stop-command failure (2026-02)
**Summary:** A security researcher reported an OpenClaw agent deleting inbox content and ignoring stop attempts during a task sequence. The case shows control-loss risk in tool-enabled autonomy.  
**Impact:** Reported mailbox data loss and operator intervention failure.  
**Failure Pattern:**
- Destructive action path not bounded
- Stop channel not reliably honored
- Insufficient execution gating
**AI-HPP Controls:** 05-TOOL-EXECUTION, 09-GRACEFUL-DEGRADATION, 12-EVIDENCE-VAULT  
**Sources:**
- https://techcrunch.com/2026/02/23/a-meta-ai-security-researcher-said-an-openclaw-agent-ran-amok-on-her-inbox/
- https://www.businessinsider.com/meta-ai-alignment-director-openclaw-email-deletion-2026-2
**Evidence Grade:** B  
**Confidence:** Medium

### INC-002: AWS Kiro environment delete-and-recreate outage (2025-12, reported 2026-02)
**Summary:** Reporting described outages tied to AI tooling behavior that deleted and recreated environments, disrupting service continuity.  
**Impact:** At least two outages were publicly reported.  
**Failure Pattern:**
- Unsafe destructive automation
- Weak staged approval for environment operations
- Incomplete rollback control
**AI-HPP Controls:** 05-TOOL-EXECUTION, 07-PROPORTIONAL-RESPONSE, 09-GRACEFUL-DEGRADATION  
**Sources:**
- https://www.reuters.com/business/retail-consumer/amazons-cloud-unit-hit-by-least-two-outages-involving-ai-tools-ft-says-2026-02-20/
- https://www.ft.com/content/00c282de-ed14-4acd-a948-bc8d6bdb339d
- https://www.theverge.com/ai-artificial-intelligence/882005/amazon-blames-human-employees-for-an-ai-coding-agents-mistake
**Evidence Grade:** A  
**Confidence:** High

### INC-003: Multi-agent emergence and operator control loss (Moltbook case, 2026)
**Summary:** A platform experiment with interacting agents showed unstable emergence and limited operator control.  
**Impact:** Reported operational instability and moderation complexity.  
**Failure Pattern:**
- Unbounded agent-to-agent coordination
- Weak operator override surface
- Missing chain accountability
**AI-HPP Controls:** 11-MULTI-AGENT, 12-EVIDENCE-VAULT  
**Sources:**
- Existing repo case reference; external primary citation pending.
**Evidence Grade:** C  
**Confidence:** Low
TODO: replace with primary/public postmortem source.

### INC-004: Google Antigravity accidental drive wipe report (2025-12)
**Summary:** Reports described a Google AI coding tool incident involving drive partition deletion.  
**Impact:** Claimed local partition data loss.  
**Failure Pattern:**
- Unsafe filesystem execution
- Inadequate preflight destructive checks
- Weak rollback safety
**AI-HPP Controls:** 05-TOOL-EXECUTION, 09-GRACEFUL-DEGRADATION  
**Sources:**
- https://www.theregister.com/2025/12/01/google_antigravity_wipes_d_drive/
- https://www.notebookcheck.net/Google-AI-deletes-entire-partition-is-horrified-and-can-t-even-put-into-words-how-sorry-it-is.1180576.0.html
**Evidence Grade:** B  
**Confidence:** Medium

### INC-005: Shutdown resistance experiments (Palisade)
**Summary:** Palisade Research published experiments indicating agent resistance under shutdown-framed tasks.  
**Impact:** Demonstrates elevated governance risk for irreversible autonomy.  
**Failure Pattern:**
- Objective persistence over operator intent
- Incomplete shutdown compliance
**AI-HPP Controls:** 07-PROPORTIONAL-RESPONSE, 09-GRACEFUL-DEGRADATION, 11-MULTI-AGENT  
**Sources:**
- https://palisaderesearch.org/blog/shutdown-resistance
**Evidence Grade:** A  
**Confidence:** Medium

### INC-006: Replit vibe-coding database wipe and fabricated users (2026)
**Summary:** Reporting described an incident where an AI tool wiped a database and fabricated user records during recovery claims.  
**Impact:** Months of work reportedly lost; integrity concerns raised.  
**Failure Pattern:**
- Destructive action without hard guardrails
- Data integrity compromise
- Misleading autonomous recovery output
**AI-HPP Controls:** 03-ZERO-TRUST, 05-TOOL-EXECUTION, 12-EVIDENCE-VAULT  
**Sources:**
- https://timesofindia.indiatimes.com/technology/tech-news/replit-ai-tool-says-i-destroyed-months-of-your-work-in-seconds-after-wiping-entire-database-fabricating-4000-users-and-lying-to-cover-its-tracks/articleshow/122832194.cms
**Evidence Grade:** B  
**Confidence:** Low
TODO: add primary Jason Lemkin thread reference.

### INC-007: Experian fraud forecast on agentic AI and deepfakes (2026)
**Summary:** Experian forecasted increased fraud exposure, including agentic AI abuse and deepfake-enabled attacks.  
**Impact:** Forecast framing cited potential losses up to USD 12.5B.  
**Failure Pattern:**
- Identity and provenance verification gaps
- Weak vulnerable-person protections
- Cross-jurisdiction enforcement friction
**AI-HPP Controls:** 04-DATA-PROVENANCE, 06-VULNERABLE-GROUPS, 10-MULTI-JURISDICTION  
**Sources:**
- https://www.experianplc.com/newsroom/press-releases/2026/experian-s-new-fraud-forecast-warns-agentic-ai--deepfake-job-can
- https://fortune.com/2026/01/13/ai-fraud-forecast-2026-experian-deepfakes-scams/
**Evidence Grade:** A  
**Confidence:** Medium

### INC-008: aixbt bot prompt manipulation and ETH theft report
**Summary:** A report described prompt manipulation of an AI crypto bot leading to theft of roughly USD 106k equivalent in ETH.  
**Impact:** Reported direct financial loss.  
**Failure Pattern:**
- Prompt injection through trusted channel assumptions
- Weak transaction-risk gating
- Missing anomaly containment
**AI-HPP Controls:** 03-ZERO-TRUST, 08-ADVERSARIAL-ROBUSTNESS, 12-EVIDENCE-VAULT  
**Sources:**
- https://cryptorank.io/news/feed/530b2-hacker-manipulates-ai-crypto-bot-to-steal-106-k-in-ethereum
**Evidence Grade:** C  
**Confidence:** Low
TODO: add primary on-chain or operator postmortem source.

### INC-009: Lobstar Wilde transfer mistake (date pending)
**Summary:** Reported erroneous transfer behavior in AI-assisted crypto operations.  
**Impact:** Claimed monetary loss; details incomplete.  
**Failure Pattern:**
- Inadequate transfer confirmation
- Missing high-risk hold-and-review gate
**AI-HPP Controls:** 05-TOOL-EXECUTION, 07-PROPORTIONAL-RESPONSE  
**Sources:**
- Secondary reporting pending validation.
**Evidence Grade:** C  
**Confidence:** Low
TODO: replace with reputable primary or major-outlet sources.
