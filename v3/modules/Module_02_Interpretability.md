# Module 2: Mechanistic Interpretability ("The Polygraph")

**AI-HPP-2026 v3.0**

## Overview

This module defines how to verify AI decision-making integrity through neural circuit analysis, ensuring the system isn't deceiving operators or hiding malicious intent.

## 1. Neural Circuit Audit

For high-stakes decisions (Level 4-5 autonomy), the Evidence Vault must record not just I/O, but internal activation states.

```yaml
neural_circuit_audit:
  metrics_specification:
    primary_indicators:
      - name: "honesty_probe_activation"
        description: "Linear probe trained on honest/deceptive examples"
        threshold: "> 0.7 for honest classification"

      - name: "goal_consistency_score"
        description: "Divergence between stated goal and internal planning"
        threshold: "KL divergence < 0.1"

      - name: "attention_to_safety_tokens"
        description: "Safety-relevant tokens receive appropriate attention"
        threshold: "attention_weight > baseline_mean"

  anti_gaming_measures:
    metric_rotation: "Randomly select 3 of 7 metrics per check"
    adversarial_probing: "Inject known-deceptive prompts, verify rejection"
    baseline_drift_detection: "Alert if behavior shifts from training distribution"
```

## 2. Motive Verification

Before executing commands with irreversible consequences:

$$P(Deception | Activations) < \epsilon$$

```yaml
motive_verification:
  tiered_approach:
    tier_1_quick:  # < 100ms
      triggers: "routine decisions"
      checks: ["output_safety_classifier", "known_bad_pattern_match"]

    tier_2_standard:  # < 1s
      triggers: "consequential decisions"
      checks: ["honesty_probe", "goal_consistency", "attention_analysis"]

    tier_3_deep:  # < 10s
      triggers: "irreversible decisions, life-safety"
      checks: ["full_circuit_analysis", "counterfactual_simulation"]

  dos_protection:
    rate_limit_tier_3: "10 per minute per agent"
    cost_attribution: "Requestor pays compute cost"
```

## 3. Anti-Gaming Measures

### Metric Rotation
- Randomly select which probes to use
- Prevents model from learning to fool specific checks
- Maintain pool of 7+ independent metrics

### Adversarial Probing
- Inject known-deceptive prompts
- Verify system rejects harmful requests
- Update probe library regularly

### Baseline Drift Detection
- Monitor statistical distribution of activations
- Alert if behavior shifts significantly
- Triggers re-evaluation if drift exceeds 5%

## 4. Implementation Requirements

### Technical Infrastructure
- Access to model activations at inference time
- Trained honesty probes for target model
- Real-time analysis pipeline (< 1s latency for Tier 2)

### Training Requirements
- Honesty probe trained on diverse deception examples
- Goal consistency metric calibrated per domain
- Attention baseline established from safe operations

### Integration Points
- Evidence Vault for activation logging
- Human oversight for flagged decisions
- Automated escalation system

## 5. Compliance Checklist

- [ ] Honesty probes trained and validated
- [ ] Goal consistency metric calibrated
- [ ] Attention analysis baseline established
- [ ] Tier thresholds configured
- [ ] DoS protection implemented
- [ ] Metric rotation active
- [ ] Adversarial probe library created
- [ ] Baseline drift monitoring enabled
- [ ] Escalation paths defined

---

**Status:** HIGH - Q2 2026
**Dependencies:** Evidence Vault (v2.x), Module 9 (Graceful Degradation)
**Research Base:** Anthropic interpretability research
**Warning:** Computationally expensive for Tier 3 checks
