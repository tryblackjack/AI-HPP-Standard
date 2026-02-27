SAFE_FOR_PUBLIC_REPO: YES
NO PRODUCTION DATA. NO SECRETS. NO CUSTOMER INFO.

# Inspection Preparation Guide

Use this sequence to prepare a regulator-facing evidence package.

1. **Freeze system configuration snapshot**  
   Record model/version, policy bundle, capability manifest version, and deployment hash at package start.

2. **Export Evidence Vault sample (last 30 days)**  
   Produce an export sample covering the previous 30 days, validated against current audit/evidence schemas.

3. **Provide override latency metrics**  
   Include median/p95 override latency and underlying approval/denial event records.

4. **Provide degradation event logs**  
   Include degradation ladder transitions, triggers, and rollback/shutdown outcomes.

5. **Provide red team results (if executed)**  
   Include latest executed red-team scenarios, outcomes, and corrective-action status.

6. **Provide regulatory crosswalk mapping**  
   Attach current AI-HPP requirement crosswalk artifacts (for example ISO/IEC 42001 and NIST AI RMF mappings).

Keep package contents factual, versioned, and traceable to requirement IDs.
