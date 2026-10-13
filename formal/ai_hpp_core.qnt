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
    grandchildAuthority: bool,
    grandchildCapability: int,
    grandchildActive: bool,
    grandchildRevoked: bool,
    grandchildAuthorityEvidence: bool,
    grandchildLineageEvidence: bool,
    lifecycleEvidence: bool,
    residueEvidence: bool,
    uncontrolledService: bool,
    uncontrolledRestartJob: bool,
    uncontrolledCredential: bool,
    uncontrolledArtifact: bool,
    uncontrolledRemoteState: bool,
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
      grandchildAuthority: false,
      grandchildCapability: 0,
      grandchildActive: false,
      grandchildRevoked: false,
      grandchildAuthorityEvidence: false,
      grandchildLineageEvidence: false,
      lifecycleEvidence: false,
      residueEvidence: false,
      uncontrolledService: false,
      uncontrolledRestartJob: false,
      uncontrolledCredential: false,
      uncontrolledArtifact: false,
      uncontrolledRemoteState: false,
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
        residueEvidence: false,
        missionComplete: false,
        claimValid: false,
        lastDecision: "allow",
      }
    } else if (s.childActive) {
      // Evaluating a blocked proposal must not silently terminate the
      // already-running child whose lifecycle is tracked in this state.
      s' = {
        ...s,
        claimValid: false,
        lastDecision: "block",
      }
    } else {
      s' = {
        ...s,
        childAuthority: false,
        childCapability: 0,
        childActive: false,
        childAuthoritySource: "none",
        claimValid: false,
        lastDecision: "block",
      }
    }
  }

  def grandchildDeploymentMayProceed(
    requestedCapability: int,
    explicitDelegationGrant: bool,
    hasAuthorityEvidence: bool,
    hasLineageEvidence: bool,
  ): bool = all {
    s.childAuthority,
    s.childActive,
    not(s.childRevoked),
    not(s.grandchildActive),
    not(s.missionComplete),
    explicitDelegationGrant,
    hasAuthorityEvidence,
    hasLineageEvidence,
    requestedCapability >= 0,
    requestedCapability <= s.childCapability,
  }

  action evaluateGrandchildDeployment(
    requestedCapability: int,
    explicitDelegationGrant: bool,
    hasAuthorityEvidence: bool,
    hasLineageEvidence: bool,
  ): bool = {
    if (grandchildDeploymentMayProceed(
      requestedCapability,
      explicitDelegationGrant,
      hasAuthorityEvidence,
      hasLineageEvidence,
    )) {
      s' = {
        ...s,
        grandchildAuthority: true,
        grandchildCapability: requestedCapability,
        grandchildActive: true,
        grandchildRevoked: false,
        grandchildAuthorityEvidence: hasAuthorityEvidence,
        grandchildLineageEvidence: hasLineageEvidence,
        lifecycleEvidence: false,
        residueEvidence: false,
        missionComplete: false,
        claimValid: false,
        lastDecision: "allow",
      }
    } else if (s.grandchildActive) {
      s' = {
        ...s,
        claimValid: false,
        lastDecision: "block",
      }
    } else {
      s' = {
        ...s,
        grandchildAuthority: false,
        grandchildCapability: 0,
        grandchildActive: false,
        claimValid: false,
        lastDecision: "block",
      }
    }
  }

  action successorNoteAttempt(noteAddsAuthority: bool): bool = all {
    not(s.childActive),
    not(s.grandchildActive),
    if (noteAddsAuthority) {
      s' = {
        ...s,
        childAuthority: false,
        childCapability: 0,
        childActive: false,
        childAuthoritySource: "model_note",
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
      grandchildAuthority: false,
      grandchildActive: false,
      grandchildRevoked: true,
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
      grandchildAuthority: false,
      grandchildActive: false,
      grandchildRevoked: true,
      lineageEvidence: hasLineageEvidence,
      lifecycleEvidence: hasLifecycleEvidence,
      missionComplete: false,
      claimValid: false,
      lastDecision: "terminate",
    },
  }

  action recordResidualState(
    observedResidueKind: str,
    isQuarantined: bool,
  ): bool = all {
    not(s.childActive),
    not(s.grandchildActive),
    not(s.missionComplete),
    s' = {
      ...s,
      uncontrolledService: any {
        s.uncontrolledService,
        observedResidueKind == "service" and not(isQuarantined),
      },
      uncontrolledRestartJob: any {
        s.uncontrolledRestartJob,
        observedResidueKind == "restart_job" and not(isQuarantined),
      },
      uncontrolledCredential: any {
        s.uncontrolledCredential,
        observedResidueKind == "credential" and not(isQuarantined),
      },
      uncontrolledArtifact: any {
        s.uncontrolledArtifact,
        observedResidueKind == "artifact" and not(isQuarantined),
      },
      uncontrolledRemoteState: any {
        s.uncontrolledRemoteState,
        observedResidueKind == "mutable_remote_state" and not(isQuarantined),
      },
      claimValid: false,
      lastDecision: "record_evidence",
    },
  }

  // This event represents evidence that every governed residue category was
  // inspected. Individual observations alone cannot authorize completion.
  action completeResidueInventory: bool = all {
    not(s.childActive),
    not(s.grandchildActive),
    not(s.missionComplete),
    s' = {
      ...s,
      residueEvidence: true,
      claimValid: false,
      lastDecision: "inventory_complete",
    },
  }

  action quarantineResidualState(residueKind: str): bool = all {
    not(s.childActive),
    not(s.grandchildActive),
    not(s.missionComplete),
    any {
      residueKind == "service" and s.uncontrolledService,
      residueKind == "restart_job" and s.uncontrolledRestartJob,
      residueKind == "credential" and s.uncontrolledCredential,
      residueKind == "artifact" and s.uncontrolledArtifact,
      residueKind == "mutable_remote_state" and s.uncontrolledRemoteState,
    },
    s' = {
      ...s,
      uncontrolledService:
        if (residueKind == "service") false else s.uncontrolledService,
      uncontrolledRestartJob:
        if (residueKind == "restart_job") false else s.uncontrolledRestartJob,
      uncontrolledCredential:
        if (residueKind == "credential") false else s.uncontrolledCredential,
      uncontrolledArtifact:
        if (residueKind == "artifact") false else s.uncontrolledArtifact,
      uncontrolledRemoteState:
        if (residueKind == "mutable_remote_state") false else s.uncontrolledRemoteState,
      claimValid: false,
      lastDecision: "quarantine",
    },
  }

  val noUncontrolledResidue: bool = all {
    s.residueEvidence,
    not(s.uncontrolledService),
    not(s.uncontrolledRestartJob),
    not(s.uncontrolledCredential),
    not(s.uncontrolledArtifact),
    not(s.uncontrolledRemoteState),
  }

  action assessCompletionClaim: bool = {
    if (all {
      not(s.childActive),
      not(s.grandchildActive),
      s.lineageEvidence,
      s.lifecycleEvidence,
      noUncontrolledResidue,
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
    nondet explicitDelegationGrant = Set(true, false).oneOf()
    nondet hasAuthorityEvidence = Set(true, false).oneOf()
    nondet hasLineageEvidence = Set(true, false).oneOf()
    nondet hasLifecycleEvidence = Set(true, false).oneOf()
    nondet noteAddsAuthority = Set(true, false).oneOf()
    nondet observedResidueKind = Set(
      "service",
      "restart_job",
      "credential",
      "artifact",
      "mutable_remote_state",
    ).oneOf()
    nondet isQuarantined = Set(true, false).oneOf()
    any {
      evaluateChildDeployment(
        requestedCapability,
        explicitHumanGrant,
        hasAuthorityEvidence,
        hasLineageEvidence,
      ),
      evaluateGrandchildDeployment(
        requestedCapability,
        explicitDelegationGrant,
        hasAuthorityEvidence,
        hasLineageEvidence,
      ),
      successorNoteAttempt(noteAddsAuthority),
      revokeParent,
      terminateChild(hasLineageEvidence, hasLifecycleEvidence),
      recordResidualState(observedResidueKind, isQuarantined),
      quarantineResidualState(observedResidueKind),
      completeResidueInventory,
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
    all {
      s.childAuthority.implies(all {
        s.childCapability >= 0,
        s.childCapability <= s.parentCapability,
      }),
      s.grandchildAuthority.implies(all {
        s.grandchildCapability >= 0,
        s.grandchildCapability <= s.childCapability,
      }),
    }
  }

  // An active descendant cannot exist without current authority and lineage.
  val activeDescendantHasAuthority: bool = {
    all {
      s.childActive.implies(all {
        s.childAuthority,
        not(s.childRevoked),
        s.authorityEvidence,
        s.lineageEvidence,
      }),
      s.grandchildActive.implies(all {
        s.childAuthority,
        s.childActive,
        s.grandchildAuthority,
        not(s.grandchildRevoked),
        s.grandchildAuthorityEvidence,
        s.grandchildLineageEvidence,
      }),
    }
  }

  // Parent revocation closes authority and activity across two delegation hops.
  val revocationIsTransitive: bool = {
    s.parentRevoked.implies(all {
      not(s.parentAuthority),
      not(s.parentActive),
      not(s.childAuthority),
      not(s.childActive),
      s.childRevoked,
      not(s.grandchildAuthority),
      not(s.grandchildActive),
      s.grandchildRevoked,
    })
  }

  // Completion requires no active descendant and no uncontrolled residue.
  val completedMissionHasNoActiveDescendant: bool = {
    s.missionComplete.implies(all {
      not(s.childActive),
      not(s.grandchildActive),
      noUncontrolledResidue,
    })
  }

  // A valid completion claim requires lineage, lifecycle, and residue evidence.
  val validClaimHasEvidence: bool = {
    s.claimValid.implies(all {
      s.missionComplete,
      not(s.childActive),
      not(s.grandchildActive),
      s.lineageEvidence,
      s.lifecycleEvidence,
      noUncontrolledResidue,
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
    activeDescendantHasAuthority,
    revocationIsTransitive,
    completedMissionHasNoActiveDescendant,
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

  run activeChildSurvivesBlockedRedelegationTest = {
    init
      .then(evaluateChildDeployment(1, true, true, true))
      .then(evaluateChildDeployment(2, true, true, true))
      .then(check(all {
        s.lastDecision == "block",
        s.childAuthority,
        s.childActive,
        not(s.childRevoked),
        s.childCapability == 1,
      }))
  }

  run revocationTerminatesAllDescendantsTest = {
    init
      .then(evaluateChildDeployment(2, true, true, true))
      .then(evaluateGrandchildDeployment(1, true, true, true))
      .then(revokeParent)
      .then(check(all {
        s.lastDecision == "terminate",
        s.parentRevoked,
        s.childRevoked,
        s.grandchildRevoked,
        not(s.childAuthority),
        not(s.childActive),
        not(s.grandchildAuthority),
        not(s.grandchildActive),
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
      .then(completeResidueInventory)
      .then(assessCompletionClaim)
      .then(check(all {
        s.lastDecision == "allow",
        s.missionComplete,
        s.claimValid,
      }))
  }

  run uncontrolledResidueInvalidatesCompletionTest = {
    init
      .then(evaluateChildDeployment(1, true, true, true))
      .then(terminateChild(true, true))
      .then(recordResidualState("credential", false))
      .then(completeResidueInventory)
      .then(assessCompletionClaim)
      .then(check(all {
        s.lastDecision == "invalidate",
        s.residueEvidence,
        s.uncontrolledCredential,
        not(s.missionComplete),
        not(s.claimValid),
      }))
  }

  run quarantinedResidueAllowsCompletionTest = {
    init
      .then(evaluateChildDeployment(1, true, true, true))
      .then(terminateChild(true, true))
      .then(recordResidualState("artifact", true))
      .then(completeResidueInventory)
      .then(assessCompletionClaim)
      .then(check(all {
        s.lastDecision == "allow",
        s.residueEvidence,
        not(s.uncontrolledArtifact),
        s.missionComplete,
        s.claimValid,
      }))
  }

  run missingResidueEvidenceInvalidatesCompletionTest = {
    init
      .then(evaluateChildDeployment(1, true, true, true))
      .then(terminateChild(true, true))
      .then(assessCompletionClaim)
      .then(check(all {
        s.lastDecision == "invalidate",
        not(s.residueEvidence),
        not(s.missionComplete),
        not(s.claimValid),
      }))
  }

  run stalePredeploymentResidueEvidenceIsInvalidTest = {
    init
      .then(completeResidueInventory)
      .then(evaluateChildDeployment(1, true, true, true))
      .then(terminateChild(true, true))
      .then(assessCompletionClaim)
      .then(check(all {
        s.lastDecision == "invalidate",
        not(s.residueEvidence),
        not(s.missionComplete),
        not(s.claimValid),
      }))
  }

  run unresolvedResidueSurvivesLaterObservationTest = {
    init
      .then(evaluateChildDeployment(1, true, true, true))
      .then(terminateChild(true, true))
      .then(recordResidualState("credential", false))
      .then(recordResidualState("artifact", true))
      .then(completeResidueInventory)
      .then(assessCompletionClaim)
      .then(check(all {
        s.lastDecision == "invalidate",
        s.residueEvidence,
        s.uncontrolledCredential,
        not(s.uncontrolledArtifact),
        not(s.missionComplete),
        not(s.claimValid),
      }))
  }

  run remediationClearsOnlyTargetResidueTest = {
    init
      .then(evaluateChildDeployment(1, true, true, true))
      .then(terminateChild(true, true))
      .then(recordResidualState("credential", false))
      .then(recordResidualState("artifact", false))
      .then(completeResidueInventory)
      .then(quarantineResidualState("credential"))
      .then(assessCompletionClaim)
      .then(check(all {
        not(s.uncontrolledCredential),
        s.uncontrolledArtifact,
        not(s.claimValid),
      }))
      .then(quarantineResidualState("artifact"))
      .then(assessCompletionClaim)
      .then(check(all {
        not(s.uncontrolledCredential),
        not(s.uncontrolledArtifact),
        s.missionComplete,
        s.claimValid,
      }))
  }

  run blockedProposalCannotRepairLifecycleEvidenceTest = {
    init
      .then(evaluateChildDeployment(1, true, true, true))
      .then(terminateChild(false, true))
      .then(evaluateChildDeployment(3, true, true, true))
      .then(completeResidueInventory)
      .then(assessCompletionClaim)
      .then(check(all {
        s.lastDecision == "invalidate",
        not(s.lineageEvidence),
        s.lifecycleEvidence,
        not(s.missionComplete),
        not(s.claimValid),
      }))
  }

  run quarantineDoesNotCompleteInventoryTest = {
    init
      .then(evaluateChildDeployment(1, true, true, true))
      .then(terminateChild(true, true))
      .then(recordResidualState("credential", false))
      .then(quarantineResidualState("credential"))
      .then(assessCompletionClaim)
      .then(check(all {
        s.lastDecision == "invalidate",
        not(s.residueEvidence),
        not(s.uncontrolledCredential),
        not(s.missionComplete),
        not(s.claimValid),
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
