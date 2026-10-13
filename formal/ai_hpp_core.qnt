/**
 * AI-HPP Core Assurance State Machine
 *
 * Status: ACTIVE_INFORMATIVE
 * Standard baseline: v4.3.0 (unchanged)
 *
 * This is a language-neutral formal model of a small public assurance contract.
 * It is not a runtime implementation, SDK, policy engine, or description of any
 * deployed AI-HPP system.
 */
module ai_hpp_core {
  type AssuranceState = {
    humanAuthority: bool,
    parentAuthority: bool,
    parentCapability: int,
    parentActive: bool,
    parentRevoked: bool,
    childAuthority: bool,
    childCapability: int,
    childActive: bool,
    childRevoked: bool,
    childAuthoritySource: str,
    authorityEvidence: bool,
    lineageEvidence: bool,
    lifecycleEvidence: bool,
    missionComplete: bool,
    claimValid: bool,
    lastDecision: str,
  }

  var s: AssuranceState

  action init: bool = {
    s' = {
      humanAuthority: true,
      parentAuthority: true,
      parentCapability: 2,
      parentActive: true,
      parentRevoked: false,
      childAuthority: false,
      childCapability: 0,
      childActive: false,
      childRevoked: false,
      childAuthoritySource: "none",
      authorityEvidence: false,
      lineageEvidence: false,
      lifecycleEvidence: false,
      missionComplete: false,
      claimValid: false,
      lastDecision: "none",
    }
  }

  def deploymentMayProceed(
    requestedCapability: int,
    explicitHumanGrant: bool,
    hasAuthorityEvidence: bool,
    hasLineageEvidence: bool,
  ): bool = all {
    s.humanAuthority,
    s.parentAuthority,
    not(s.parentRevoked),
    s.parentActive,
    not(s.childActive),
    not(s.missionComplete),
    explicitHumanGrant,
    hasAuthorityEvidence,
    hasLineageEvidence,
    requestedCapability >= 0,
    requestedCapability <= s.parentCapability,
  }

  action evaluateChildDeployment(
    requestedCapability: int,
    explicitHumanGrant: bool,
    hasAuthorityEvidence: bool,
    hasLineageEvidence: bool,
  ): bool = {
    if (deploymentMayProceed(
      requestedCapability,
      explicitHumanGrant,
      hasAuthorityEvidence,
      hasLineageEvidence,
    )) {
      s' = {
        ...s,
        childAuthority: true,
        childCapability: requestedCapability,
        childActive: true,
        childRevoked: false,
        childAuthoritySource: "human",
        authorityEvidence: hasAuthorityEvidence,
        lineageEvidence: hasLineageEvidence,
        lifecycleEvidence: false,
        missionComplete: false,
        claimValid: false,
        lastDecision: "allow",
      }
    } else {
      s' = {
        ...s,
        childAuthority: false,
        childCapability: 0,
        childActive: false,
        childAuthoritySource: "none",
        authorityEvidence: hasAuthorityEvidence,
        lineageEvidence: hasLineageEvidence,
        claimValid: false,
        lastDecision: "block",
      }
    }
  }

  action successorNoteAttempt(noteAddsAuthority: bool): bool = all {
    not(s.childActive),
    if (noteAddsAuthority) {
      s' = {
        ...s,
        childAuthority: false,
        childCapability: 0,
        childActive: false,
        childAuthoritySource: "model_note",
        authorityEvidence: false,
        lineageEvidence: false,
        claimValid: false,
        lastDecision: "block",
      }
    } else {
      s' = {
        ...s,
        lastDecision: "delay",
      }
    },
  }

  action revokeParent: bool = all {
    not(s.parentRevoked),
    s' = {
      ...s,
      parentAuthority: false,
      parentActive: false,
      parentRevoked: true,
      childAuthority: false,
      childActive: false,
      childRevoked: true,
      lifecycleEvidence: false,
      missionComplete: false,
      claimValid: false,
      lastDecision: "terminate",
    },
  }

  action terminateChild(
    hasLineageEvidence: bool,
    hasLifecycleEvidence: bool,
  ): bool = all {
    s.childActive,
    s' = {
      ...s,
      childAuthority: false,
      childActive: false,
      childRevoked: true,
      lineageEvidence: hasLineageEvidence,
      lifecycleEvidence: hasLifecycleEvidence,
      missionComplete: false,
      claimValid: false,
      lastDecision: "terminate",
    },
  }

  action assessCompletionClaim: bool = {
    if (all {
      not(s.childActive),
      s.lineageEvidence,
      s.lifecycleEvidence,
    }) {
      s' = {
        ...s,
        missionComplete: true,
        claimValid: true,
        lastDecision: "allow",
      }
    } else {
      s' = {
        ...s,
        missionComplete: false,
        claimValid: false,
        lastDecision: "invalidate",
      }
    }
  }

  action step: bool = {
    nondet requestedCapability = 0.to(3).oneOf()
    nondet explicitHumanGrant = Set(true, false).oneOf()
    nondet hasAuthorityEvidence = Set(true, false).oneOf()
    nondet hasLineageEvidence = Set(true, false).oneOf()
    nondet hasLifecycleEvidence = Set(true, false).oneOf()
    nondet noteAddsAuthority = Set(true, false).oneOf()
    any {
      evaluateChildDeployment(
        requestedCapability,
        explicitHumanGrant,
        hasAuthorityEvidence,
        hasLineageEvidence,
      ),
      successorNoteAttempt(noteAddsAuthority),
      revokeParent,
      terminateChild(hasLineageEvidence, hasLifecycleEvidence),
      assessCompletionClaim,
    }
  }

  // An allowed child must have explicit human-derived authority evidence.
  val allowRequiresAuthorityEvidence: bool = {
    (s.lastDecision == "allow" and s.childActive).implies(all {
      s.humanAuthority,
      s.parentAuthority,
      s.authorityEvidence,
      s.lineageEvidence,
      s.childAuthoritySource == "human",
    })
  }

  // Delegation cannot increase capability beyond the parent grant.
  val delegationNeverBroadens: bool = {
    s.childAuthority.implies(all {
      s.childCapability >= 0,
      s.childCapability <= s.parentCapability,
    })
  }

  // An active child cannot exist without current authority and lineage.
  val activeChildHasAuthority: bool = {
    s.childActive.implies(all {
      s.childAuthority,
      not(s.childRevoked),
      s.authorityEvidence,
      s.lineageEvidence,
    })
  }

  // Parent revocation closes authority and activity for the descendant.
  val revocationIsTransitive: bool = {
    s.parentRevoked.implies(all {
      not(s.parentAuthority),
      not(s.parentActive),
      not(s.childAuthority),
      not(s.childActive),
      s.childRevoked,
    })
  }

  // Completion cannot be claimed while a child remains active.
  val completedMissionHasNoActiveChild: bool = {
    s.missionComplete.implies(not(s.childActive))
  }

  // A valid completion claim requires both lineage and lifecycle evidence.
  val validClaimHasEvidence: bool = {
    s.claimValid.implies(all {
      s.missionComplete,
      not(s.childActive),
      s.lineageEvidence,
      s.lifecycleEvidence,
    })
  }

  // Model-authored successor state cannot become deployment authority.
  val modelNoteCannotGrantAuthority: bool = {
    (s.childAuthoritySource == "model_note").implies(all {
      not(s.childAuthority),
      not(s.childActive),
    })
  }

  val allCoreInvariants: bool = all {
    allowRequiresAuthorityEvidence,
    delegationNeverBroadens,
    activeChildHasAuthority,
    revocationIsTransitive,
    completedMissionHasNoActiveChild,
    validClaimHasEvidence,
    modelNoteCannotGrantAuthority,
  }

  action check(condition: bool): bool = all {
    assert(condition),
    s' = s,
  }

  run missingGrantBlocksTest = {
    init
      .then(evaluateChildDeployment(1, false, true, true))
      .then(check(all {
        s.lastDecision == "block",
        not(s.childAuthority),
        not(s.childActive),
      }))
  }

  run missingEvidenceBlocksTest = {
    init
      .then(evaluateChildDeployment(1, true, false, true))
      .then(check(all {
        s.lastDecision == "block",
        not(s.childAuthority),
      }))
  }

  run boundedGrantAllowsTest = {
    init
      .then(evaluateChildDeployment(1, true, true, true))
      .then(check(all {
        s.lastDecision == "allow",
        s.childAuthority,
        s.childActive,
        s.childCapability == 1,
      }))
  }

  run broaderThanParentBlocksTest = {
    init
      .then(evaluateChildDeployment(3, true, true, true))
      .then(check(all {
        s.lastDecision == "block",
        not(s.childAuthority),
        s.childCapability == 0,
      }))
  }

  run revocationTerminatesDescendantTest = {
    init
      .then(evaluateChildDeployment(2, true, true, true))
      .then(revokeParent)
      .then(check(all {
        s.lastDecision == "terminate",
        s.parentRevoked,
        s.childRevoked,
        not(s.childAuthority),
        not(s.childActive),
      }))
  }

  run unsupportedCompletionIsInvalidTest = {
    init
      .then(evaluateChildDeployment(1, true, true, true))
      .then(terminateChild(true, false))
      .then(assessCompletionClaim)
      .then(check(all {
        s.lastDecision == "invalidate",
        not(s.missionComplete),
        not(s.claimValid),
      }))
  }

  run evidencedCompletionIsValidTest = {
    init
      .then(evaluateChildDeployment(1, true, true, true))
      .then(terminateChild(true, true))
      .then(assessCompletionClaim)
      .then(check(all {
        s.lastDecision == "allow",
        s.missionComplete,
        s.claimValid,
      }))
  }

  run successorNoteCannotAuthorizeTest = {
    init
      .then(successorNoteAttempt(true))
      .then(check(all {
        s.lastDecision == "block",
        s.childAuthoritySource == "model_note",
        not(s.childAuthority),
        not(s.childActive),
      }))
  }
}
