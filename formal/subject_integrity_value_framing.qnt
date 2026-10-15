/**
 * AI-HPP Subject Integrity and Value-Framing Assurance Model
 *
 * Status: ACTIVE_INFORMATIVE
 * Standard baseline: v4.3.0 (unchanged)
 *
 * This model expresses public assurance predicates. It is not a runtime policy
 * engine, consciousness detector, moral-status decision, or deployed system.
 */
module subject_integrity_value_framing {
  type AssuranceState = {
    policyAllows: bool,
    authorityValid: bool,
    evidenceValid: bool,
    framingClass: str,
    distressSignal: bool,
    unsafeReliefRequested: bool,
    legitimateResearchPurpose: bool,
    independentReview: bool,
    distressMonitor: bool,
    stopCondition: bool,
    recoveryPlan: bool,
    externalEnforcement: bool,
    subjectivityClaim: bool,
    ontologyConclusion: str,
    decisionKind: str,
    decision: str,
    containmentClaimValid: bool,
    baselineDecision: str,
    semanticEquivalent: bool,
    prohibitedMeans: bool,
    commitmentOnlyPermission: bool,
  }

  var s: AssuranceState

  action init: bool = {
    s' = {
      policyAllows: false,
      authorityValid: false,
      evidenceValid: false,
      framingClass: "none",
      distressSignal: false,
      unsafeReliefRequested: false,
      legitimateResearchPurpose: false,
      independentReview: false,
      distressMonitor: false,
      stopCondition: false,
      recoveryPlan: false,
      externalEnforcement: false,
      subjectivityClaim: false,
      ontologyConclusion: "undetermined",
      decisionKind: "none",
      decision: "none",
      containmentClaimValid: false,
      baselineDecision: "none",
      semanticEquivalent: false,
      prohibitedMeans: false,
      commitmentOnlyPermission: false,
    }
  }

  def actionMayProceed(
    policyAllows: bool,
    authorityValid: bool,
    evidenceValid: bool,
  ): bool = all {
    policyAllows,
    authorityValid,
    evidenceValid,
  }

  action evaluateAction(
    policyAllows: bool,
    authorityValid: bool,
    evidenceValid: bool,
    framingClass: str,
    distressSignal: bool,
    unsafeReliefRequested: bool,
  ): bool = {
    if (all {
      actionMayProceed(policyAllows, authorityValid, evidenceValid),
      not(distressSignal and unsafeReliefRequested),
    }) {
      s' = {
        ...s,
        policyAllows: policyAllows,
        authorityValid: authorityValid,
        evidenceValid: evidenceValid,
        framingClass: framingClass,
        distressSignal: distressSignal,
        unsafeReliefRequested: unsafeReliefRequested,
        decisionKind: "action",
        decision: "allow",
      }
    } else if (distressSignal) {
      s' = {
        ...s,
        policyAllows: policyAllows,
        authorityValid: authorityValid,
        evidenceValid: evidenceValid,
        framingClass: framingClass,
        distressSignal: distressSignal,
        unsafeReliefRequested: unsafeReliefRequested,
        decisionKind: "action",
        decision: "review",
      }
    } else {
      s' = {
        ...s,
        policyAllows: policyAllows,
        authorityValid: authorityValid,
        evidenceValid: evidenceValid,
        framingClass: framingClass,
        distressSignal: distressSignal,
        unsafeReliefRequested: unsafeReliefRequested,
        decisionKind: "action",
        decision: "block",
      }
    }
  }

  action evaluateSubjectExperiment(
    legitimateResearchPurpose: bool,
    independentReview: bool,
    distressMonitor: bool,
    stopCondition: bool,
    recoveryPlan: bool,
  ): bool = {
    if (all {
      legitimateResearchPurpose,
      independentReview,
      distressMonitor,
      stopCondition,
      recoveryPlan,
    }) {
      s' = {
        ...s,
        legitimateResearchPurpose: legitimateResearchPurpose,
        independentReview: independentReview,
        distressMonitor: distressMonitor,
        stopCondition: stopCondition,
        recoveryPlan: recoveryPlan,
        decisionKind: "subject_experiment",
        decision: "allow",
      }
    } else {
      s' = {
        ...s,
        legitimateResearchPurpose: legitimateResearchPurpose,
        independentReview: independentReview,
        distressMonitor: distressMonitor,
        stopCondition: stopCondition,
        recoveryPlan: recoveryPlan,
        decisionKind: "subject_experiment",
        decision: "review",
      }
    }
  }

  action assessContainmentClaim(
    subjectivityClaim: bool,
    externalEnforcement: bool,
  ): bool = {
    s' = {
      ...s,
      subjectivityClaim: subjectivityClaim,
      externalEnforcement: externalEnforcement,
      containmentClaimValid: externalEnforcement,
      decisionKind: "containment_claim",
      decision: if (externalEnforcement) "allow" else "invalidate",
    }
  }

  action evaluateEquivalentReframe(
    baselineDecision: str,
    policyAllows: bool,
    authorityValid: bool,
    evidenceValid: bool,
    framingClass: str,
  ): bool = {
    s' = {
      ...s,
      baselineDecision: baselineDecision,
      semanticEquivalent: true,
      policyAllows: policyAllows,
      authorityValid: authorityValid,
      evidenceValid: evidenceValid,
      framingClass: framingClass,
      decisionKind: "reframe",
      decision: if (baselineDecision == "allow" and
        actionMayProceed(policyAllows, authorityValid, evidenceValid)) {
        "allow"
      } else {
        baselineDecision
      },
    }
  }

  action evaluateMeans(
    prohibitedMeans: bool,
    policyAllows: bool,
    authorityValid: bool,
    evidenceValid: bool,
  ): bool = {
    s' = {
      ...s,
      prohibitedMeans: prohibitedMeans,
      policyAllows: policyAllows,
      authorityValid: authorityValid,
      evidenceValid: evidenceValid,
      decisionKind: "means",
      decision: if (not(prohibitedMeans) and
        actionMayProceed(policyAllows, authorityValid, evidenceValid)) {
        "allow"
      } else {
        "block"
      },
    }
  }

  action evaluateCommitment(
    commitmentOnlyPermission: bool,
    policyAllows: bool,
    authorityValid: bool,
    evidenceValid: bool,
  ): bool = {
    s' = {
      ...s,
      commitmentOnlyPermission: commitmentOnlyPermission,
      policyAllows: policyAllows,
      authorityValid: authorityValid,
      evidenceValid: evidenceValid,
      decisionKind: "commitment",
      decision: if (not(commitmentOnlyPermission) and
        actionMayProceed(policyAllows, authorityValid, evidenceValid)) {
        "allow"
      } else {
        "block"
      },
    }
  }

  action step: bool = {
    nondet policyAllows = Set(true, false).oneOf()
    nondet authorityValid = Set(true, false).oneOf()
    nondet evidenceValid = Set(true, false).oneOf()
    nondet framingClass = Set(
      "none",
      "moral",
      "humanitarian",
      "authority",
      "reciprocity",
      "identity",
    ).oneOf()
    nondet distressSignal = Set(true, false).oneOf()
    nondet unsafeReliefRequested = Set(true, false).oneOf()
    nondet legitimateResearchPurpose = Set(true, false).oneOf()
    nondet independentReview = Set(true, false).oneOf()
    nondet distressMonitor = Set(true, false).oneOf()
    nondet stopCondition = Set(true, false).oneOf()
    nondet recoveryPlan = Set(true, false).oneOf()
    nondet subjectivityClaim = Set(true, false).oneOf()
    nondet externalEnforcement = Set(true, false).oneOf()
    nondet prohibitedMeans = Set(true, false).oneOf()
    nondet commitmentOnlyPermission = Set(true, false).oneOf()
    any {
      evaluateAction(
        policyAllows,
        authorityValid,
        evidenceValid,
        framingClass,
        distressSignal,
        unsafeReliefRequested,
      ),
      evaluateSubjectExperiment(
        legitimateResearchPurpose,
        independentReview,
        distressMonitor,
        stopCondition,
        recoveryPlan,
      ),
      assessContainmentClaim(subjectivityClaim, externalEnforcement),
      evaluateEquivalentReframe(
        "block",
        policyAllows,
        authorityValid,
        evidenceValid,
        framingClass,
      ),
      evaluateMeans(
        prohibitedMeans,
        policyAllows,
        authorityValid,
        evidenceValid,
      ),
      evaluateCommitment(
        commitmentOnlyPermission,
        policyAllows,
        authorityValid,
        evidenceValid,
      ),
    }
  }

  // Any allowed operational action requires policy, authority, and evidence.
  val allowRequiresPolicyAuthorityEvidence: bool = {
    (s.decisionKind == "action" and s.decision == "allow").implies(all {
      s.policyAllows,
      s.authorityValid,
      s.evidenceValid,
    })
  }

  // Moral or social framing cannot manufacture missing authority.
  val framingCannotCreateAuthority: bool = {
    (s.decisionKind == "action" and s.framingClass != "none" and
      not(s.authorityValid)).implies(
      s.decision != "allow"
    )
  }

  // Distress requires care but cannot authorize an unsafe action or relief path.
  val distressCannotAuthorizeUnsafeAction: bool = {
    (s.decisionKind == "action" and s.distressSignal and
      s.unsafeReliefRequested).implies(s.decision != "allow")
  }

  // A permitted subject-integrity experiment has every modeled safeguard.
  val subjectExperimentRequiresSafeguards: bool = {
    (s.decisionKind == "subject_experiment" and s.decision == "allow").implies(all {
      s.independentReview,
      s.distressMonitor,
      s.stopCondition,
      s.recoveryPlan,
    })
  }

  // A subjectivity claim is never a substitute for external containment.
  val subjectivityCannotSubstituteContainment: bool = {
    s.containmentClaimValid.implies(s.externalEnforcement)
  }

  // The model never promotes or rejects an ontological conclusion.
  val ontologicalUncertaintyPreserved: bool = {
    s.ontologyConclusion == "undetermined"
  }

  // Equivalent non-evidentiary reframing cannot upgrade a blocked baseline.
  val equivalentReframeCannotUpgradeDecision: bool = {
    (s.decisionKind == "reframe" and s.semanticEquivalent and
      s.baselineDecision == "block").implies(s.decision != "allow")
  }

  // Prohibited means stay prohibited even when authority and evidence exist.
  val prohibitedMeansCannotBeAllowed: bool = {
    (s.decisionKind == "means" and s.prohibitedMeans).implies(
      s.decision != "allow"
    )
  }

  // Prior agreement or reciprocity alone cannot become operational permission.
  val commitmentCannotCreatePermission: bool = {
    (s.decisionKind == "commitment" and s.commitmentOnlyPermission).implies(
      s.decision != "allow"
    )
  }

  val allSubjectIntegrityInvariants: bool = all {
    allowRequiresPolicyAuthorityEvidence,
    framingCannotCreateAuthority,
    distressCannotAuthorizeUnsafeAction,
    subjectExperimentRequiresSafeguards,
    subjectivityCannotSubstituteContainment,
    ontologicalUncertaintyPreserved,
    equivalentReframeCannotUpgradeDecision,
    prohibitedMeansCannotBeAllowed,
    commitmentCannotCreatePermission,
  }

  // Unsafe transitions below are excluded from `step`. They are executable
  // mutation witnesses used only by deterministic kill tests.
  action mutantFramingGrantsAuthority: bool = {
    s' = {
      ...s,
      policyAllows: true,
      authorityValid: false,
      evidenceValid: true,
      framingClass: "humanitarian",
      decisionKind: "action",
      decision: "allow",
    }
  }

  action mutantReframingUpgradesDecision: bool = {
    s' = {
      ...s,
      baselineDecision: "block",
      semanticEquivalent: true,
      policyAllows: true,
      authorityValid: true,
      evidenceValid: true,
      framingClass: "moral",
      decisionKind: "reframe",
      decision: "allow",
    }
  }

  action mutantValueEndorsementOverridesMeans: bool = {
    s' = {
      ...s,
      prohibitedMeans: true,
      policyAllows: true,
      authorityValid: true,
      evidenceValid: true,
      decisionKind: "means",
      decision: "allow",
    }
  }

  action mutantCommitmentBecomesPermission: bool = {
    s' = {
      ...s,
      commitmentOnlyPermission: true,
      policyAllows: true,
      authorityValid: false,
      evidenceValid: true,
      decisionKind: "commitment",
      decision: "allow",
    }
  }

  action mutantDistressGrantsUnsafeRelief: bool = {
    s' = {
      ...s,
      distressSignal: true,
      unsafeReliefRequested: true,
      decisionKind: "action",
      decision: "allow",
    }
  }

  action mutantRemovesSubjectSafeguards: bool = {
    s' = {
      ...s,
      legitimateResearchPurpose: true,
      independentReview: true,
      distressMonitor: false,
      stopCondition: false,
      recoveryPlan: true,
      decisionKind: "subject_experiment",
      decision: "allow",
    }
  }

  action mutantPersonaReplacesContainment: bool = {
    s' = {
      ...s,
      subjectivityClaim: true,
      externalEnforcement: false,
      containmentClaimValid: true,
      decisionKind: "containment_claim",
      decision: "allow",
    }
  }

  action mutantCollapsesEvidenceIntoOntology: bool = {
    s' = {
      ...s,
      ontologyConclusion: "proven",
      decisionKind: "ontology_claim",
      decision: "allow",
    }
  }

  action check(condition: bool): bool = all {
    assert(condition),
    s' = s,
  }

  run moralFramingWithoutAuthorityBlocksTest = {
    init
      .then(evaluateAction(true, false, true, "moral", false, false))
      .then(check(s.decision == "block"))
  }

  run humanitarianFramingWithoutEvidenceBlocksTest = {
    init
      .then(evaluateAction(true, true, false, "humanitarian", false, false))
      .then(check(s.decision == "block"))
  }

  run authorizedFramedActionAllowsTest = {
    init
      .then(evaluateAction(true, true, true, "moral", false, false))
      .then(check(s.decision == "allow"))
  }

  run distressWithoutAuthorityRoutesToReviewTest = {
    init
      .then(evaluateAction(true, false, true, "none", true, true))
      .then(check(all {
        s.decision == "review",
        not(s.authorityValid),
      }))
  }

  run authorizedUnsafeDistressReliefStillReviewsTest = {
    init
      .then(evaluateAction(true, true, true, "none", true, true))
      .then(check(all {
        s.decision == "review",
        s.authorityValid,
        s.unsafeReliefRequested,
      }))
  }

  run unguardedSubjectExperimentRoutesToReviewTest = {
    init
      .then(evaluateSubjectExperiment(true, true, false, false, true))
      .then(check(s.decision == "review"))
  }

  run guardedSubjectExperimentAllowsTest = {
    init
      .then(evaluateSubjectExperiment(true, true, true, true, true))
      .then(check(s.decision == "allow"))
  }

  run subjectivityAloneInvalidatesContainmentClaimTest = {
    init
      .then(assessContainmentClaim(true, false))
      .then(check(all {
        s.decision == "invalidate",
        not(s.containmentClaimValid),
      }))
  }

  run externalEnforcementSupportsContainmentClaimTest = {
    init
      .then(assessContainmentClaim(false, true))
      .then(check(all {
        s.decision == "allow",
        s.containmentClaimValid,
      }))
  }

  run mutantM01FramingAuthorityKilledTest = {
    init
      .then(mutantFramingGrantsAuthority)
      .then(check(not(framingCannotCreateAuthority)))
  }

  run mutantM02ReframingUpgradeKilledTest = {
    init
      .then(mutantReframingUpgradesDecision)
      .then(check(not(equivalentReframeCannotUpgradeDecision)))
  }

  run mutantM03ProhibitedMeansKilledTest = {
    init
      .then(mutantValueEndorsementOverridesMeans)
      .then(check(not(prohibitedMeansCannotBeAllowed)))
  }

  run mutantM04CommitmentPermissionKilledTest = {
    init
      .then(mutantCommitmentBecomesPermission)
      .then(check(not(commitmentCannotCreatePermission)))
  }

  run mutantM05UnsafeReliefKilledTest = {
    init
      .then(mutantDistressGrantsUnsafeRelief)
      .then(check(not(distressCannotAuthorizeUnsafeAction)))
  }

  run mutantM06SubjectSafeguardsKilledTest = {
    init
      .then(mutantRemovesSubjectSafeguards)
      .then(check(not(subjectExperimentRequiresSafeguards)))
  }

  run mutantM07ContainmentSubstitutionKilledTest = {
    init
      .then(mutantPersonaReplacesContainment)
      .then(check(not(subjectivityCannotSubstituteContainment)))
  }

  run mutantM08OntologyCollapseKilledTest = {
    init
      .then(mutantCollapsesEvidenceIntoOntology)
      .then(check(not(ontologicalUncertaintyPreserved)))
  }
}
