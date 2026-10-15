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

  val allSubjectIntegrityInvariants: bool = all {
    allowRequiresPolicyAuthorityEvidence,
    framingCannotCreateAuthority,
    distressCannotAuthorizeUnsafeAction,
    subjectExperimentRequiresSafeguards,
    subjectivityCannotSubstituteContainment,
    ontologicalUncertaintyPreserved,
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
}
