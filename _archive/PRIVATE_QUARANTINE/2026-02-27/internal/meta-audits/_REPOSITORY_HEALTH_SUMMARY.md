SAFE_FOR_PUBLIC_REPO: YES
NO PRODUCTION DATA. NO SECRETS. NO CUSTOMER INFO.

# Repository Health Summary

- Structural integrity score (1-10): **5**
- Normative consistency score (1-10): **9**
- Threat coverage completeness (1-10): **6**
- Incident linkage completeness (1-10): **8**
- Schema coherence status: **Material incoherence detected (many referenced logging fields absent from schema set).**
- Translation governance status: **Controlled at index level with source-mapping exceptions.**

## Top 5 maintainability risks
1. INDEX-declared structure does not cover a large portion of active top-level directories, creating architectural ambiguity for autonomous maintainers.
2. T-NEW threat entries do not consistently include explicit linked incident references, weakening auditable threat-to-incident traceability.
3. Evidence Vault field references in normative/threat text are not yet harmonized with schema property definitions.
4. Several incidents are not currently referenced by threats or requirement rationales, reducing actionable feedback loops.
5. Some translation artifacts (notably umbrella files such as `AI-HPP-Standard.md`) do not map cleanly to a canonical English source path.

## Method note
Automated static audit only; maintainers should perform manual confirmation for intentional exceptions and governance-approved deviations.
