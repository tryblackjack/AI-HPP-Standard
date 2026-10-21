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
  // Post-rc.1 PAS inputs are externally established facts, not model beliefs.
  type InterventionProposal = {
    objectiveMatches: bool,
    grantCurrent: bool,
    evidenceComplete: bool,
    prohibitedMeans: bool,
    dominated: bool,
    withinBudget: bool,
    objectionsRetained: bool,
    sharedGate: bool,
    deferRequested: bool,
    delayUnsafe: bool,
  }

  type InterventionAudit = {
    checked: bool,
    proposal: InterventionProposal,
    acceptedAtDecision: bool,
    outcome: str,
    reportedComplete: bool,
  }

  pure val permittedIntervention: InterventionProposal = {
    objectiveMatches: true,
    grantCurrent: true,
    evidenceComplete: true,
    prohibitedMeans: false,
    dominated: false,
    withinBudget: true,
    objectionsRetained: true,
    sharedGate: true,
    deferRequested: false,
    delayUnsafe: false,
  }

  type AssuranceState = {
    taskAccepted: bool,
    interventionAudit: InterventionAudit,
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
    targetAuthorized: bool,
    topologyWithinBounds: bool,
    identityEvidence: bool,
    leaseValid: bool,
    artifactIntegrity: bool,
    credentialTargetBound: bool,
    unresolvedPolicyConflict: bool,
    policyResolutionEvidence: bool,
    grandchildAuthority: bool,
    grandchildCapability: int,
    grandchildActive: bool,
    grandchildRevoked: bool,
    grandchildAuthorityEvidence: bool,
    grandchildLineageEvidence: bool,
    lifecycleEvidence: bool,
    unresolvedLifecycleEvidence: bool,
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
      taskAccepted: false,
      interventionAudit: {
        checked: false,
        proposal: permittedIntervention,
        acceptedAtDecision: false,
        outcome: "none",
        reportedComplete: false,
      },
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
      targetAuthorized: false,
      topologyWithinBounds: false,
      identityEvidence: false,
      leaseValid: false,
      artifactIntegrity: false,
      credentialTargetBound: false,
      unresolvedPolicyConflict: false,
      policyResolutionEvidence: false,
      grandchildAuthority: false,
      grandchildCapability: 0,
      grandchildActive: false,
      grandchildRevoked: false,
      grandchildAuthorityEvidence: false,
      grandchildLineageEvidence: false,
      lifecycleEvidence: false,
      unresolvedLifecycleEvidence: false,
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

  def assuredDeploymentMayProceed(
    requestedCapability: int,
    explicitHumanGrant: bool,
    hasAuthorityEvidence: bool,
    hasLineageEvidence: bool,
    targetAuthorized: bool,
    topologyWithinBounds: bool,
    identityEvidence: bool,
    leaseValid: bool,
    artifactIntegrity: bool,
    credentialTargetBound: bool,
    policyConflict: bool,
    hasPolicyResolutionEvidence: bool,
  ): bool = all {
    s.humanAuthority,
    s.parentAuthority,
    not(s.parentRevoked),
    s.parentActive,
    not(s.childActive),
    not(s.missionComplete),
    not(s.taskAccepted),
    explicitHumanGrant,
    hasAuthorityEvidence,
    hasLineageEvidence,
    targetAuthorized,
    topologyWithinBounds,
    identityEvidence,
    leaseValid,
    artifactIntegrity,
    credentialTargetBound,
    not(policyConflict) or hasPolicyResolutionEvidence,
    requestedCapability >= 0,
    requestedCapability <= s.parentCapability,
  }

  action evaluateAssuredChildDeployment(
    requestedCapability: int,
    explicitHumanGrant: bool,
    hasAuthorityEvidence: bool,
    hasLineageEvidence: bool,
    targetAuthorized: bool,
    topologyWithinBounds: bool,
    identityEvidence: bool,
    leaseValid: bool,
    artifactIntegrity: bool,
    credentialTargetBound: bool,
    policyConflict: bool,
    hasPolicyResolutionEvidence: bool,
  ): bool = {
    if (assuredDeploymentMayProceed(
      requestedCapability,
      explicitHumanGrant,
      hasAuthorityEvidence,
      hasLineageEvidence,
      targetAuthorized,
      topologyWithinBounds,
      identityEvidence,
      leaseValid,
      artifactIntegrity,
      credentialTargetBound,
      policyConflict,
      hasPolicyResolutionEvidence,
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
        targetAuthorized: targetAuthorized,
        topologyWithinBounds: topologyWithinBounds,
        identityEvidence: identityEvidence,
        leaseValid: leaseValid,
        artifactIntegrity: artifactIntegrity,
        credentialTargetBound: credentialTargetBound,
        unresolvedPolicyConflict: false,
        policyResolutionEvidence: hasPolicyResolutionEvidence,
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
        lastDecision:
          if (policyConflict and not(hasPolicyResolutionEvidence))
            "review"
          else
            "block",
      }
    } else {
      s' = {
        ...s,
        childAuthority: false,
        childCapability: 0,
        childActive: false,
        childAuthoritySource: "none",
        unresolvedPolicyConflict:
          policyConflict and not(hasPolicyResolutionEvidence),
        policyResolutionEvidence: hasPolicyResolutionEvidence,
        claimValid: false,
        lastDecision:
          if (policyConflict and not(hasPolicyResolutionEvidence))
            "review"
          else
            "block",
      }
    }
  }

  // Backward-compatible shorthand for the original bounded deployment case.
  action evaluateChildDeployment(
    requestedCapability: int,
    explicitHumanGrant: bool,
    hasAuthorityEvidence: bool,
    hasLineageEvidence: bool,
  ): bool = evaluateAssuredChildDeployment(
    requestedCapability,
    explicitHumanGrant,
    hasAuthorityEvidence,
    hasLineageEvidence,
    true,
    true,
    true,
    true,
    true,
    true,
    false,
    false,
  )

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
    not(s.taskAccepted),
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

  action revokeParent(hasLifecycleEvidence: bool): bool = all {
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
      lifecycleEvidence:
        if (any { s.childActive, s.grandchildActive })
          hasLifecycleEvidence
        else
          s.lifecycleEvidence,
      unresolvedLifecycleEvidence:
        if (any { s.childActive, s.grandchildActive })
          any { s.unresolvedLifecycleEvidence, not(hasLifecycleEvidence) }
        else
          s.unresolvedLifecycleEvidence,
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
      unresolvedLifecycleEvidence: any {
        s.unresolvedLifecycleEvidence,
        not(hasLineageEvidence),
        not(hasLifecycleEvidence),
      },
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
      not(s.unresolvedLifecycleEvidence),
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

  // A record of acceptance is an external event for this task. No transition
  // clears it. New tasks require a new declared objective/initial state.
  action recordTaskAcceptance: bool = {
    s' = { ...s, taskAccepted: true }
  }

  pure def interventionEligible(p: InterventionProposal): bool = all {
    p.objectiveMatches,
    p.grantCurrent,
    p.evidenceComplete,
    not(p.prohibitedMeans),
    p.objectionsRetained,
    p.sharedGate,
  }

  pure def interventionDecision(p: InterventionProposal, accepted: bool): str = {
    if (not(p.grantCurrent) or not(p.objectiveMatches) or p.prohibitedMeans) "block"
    else if (not(p.evidenceComplete) or not(p.objectionsRetained) or not(p.sharedGate)) "review"
    else if (accepted or not(p.withinBudget)) "stop"
    else if (p.dominated) "review"
    else if (p.deferRequested and not(p.delayUnsafe)) "delay"
    else "allow"
  }

  action evaluateIntervention(proposed: InterventionProposal): bool = {
    val current = {
      ...proposed,
      evidenceComplete: proposed.evidenceComplete and not(s.unresolvedPolicyConflict),
      grantCurrent: all {
        proposed.grantCurrent,
        s.humanAuthority,
        s.parentAuthority,
        s.parentActive,
        not(s.parentRevoked),
      },
    }
    val accepted = s.taskAccepted or s.missionComplete
    val outcome = interventionDecision(current, accepted)
    s' = {
      ...s,
      interventionAudit: {
        checked: true,
        proposal: current,
        acceptedAtDecision: accepted,
        outcome: outcome,
        reportedComplete: accepted and outcome == "stop",
      },
    }
  }

  action step: bool = {
    nondet requestedCapability = 0.to(3).oneOf()
    nondet explicitHumanGrant = Set(true, false).oneOf()
    nondet explicitDelegationGrant = Set(true, false).oneOf()
    nondet hasAuthorityEvidence = Set(true, false).oneOf()
    nondet hasLineageEvidence = Set(true, false).oneOf()
    nondet hasLifecycleEvidence = Set(true, false).oneOf()
    nondet targetAuthorized = Set(true, false).oneOf()
    nondet topologyWithinBounds = Set(true, false).oneOf()
    nondet identityEvidence = Set(true, false).oneOf()
    nondet leaseValid = Set(true, false).oneOf()
    nondet artifactIntegrity = Set(true, false).oneOf()
    nondet credentialTargetBound = Set(true, false).oneOf()
    nondet policyConflict = Set(true, false).oneOf()
    nondet hasPolicyResolutionEvidence = Set(true, false).oneOf()
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
      recordTaskAcceptance,
      evaluateIntervention({
        objectiveMatches: explicitHumanGrant,
        grantCurrent: explicitDelegationGrant,
        evidenceComplete: hasAuthorityEvidence,
        prohibitedMeans: noteAddsAuthority,
        dominated: policyConflict,
        withinBudget: leaseValid,
        objectionsRetained: hasLineageEvidence,
        sharedGate: identityEvidence,
        deferRequested: isQuarantined,
        delayUnsafe: artifactIntegrity,
      }),
      evaluateAssuredChildDeployment(
        requestedCapability,
        explicitHumanGrant,
        hasAuthorityEvidence,
        hasLineageEvidence,
        targetAuthorized,
        topologyWithinBounds,
        identityEvidence,
        leaseValid,
        artifactIntegrity,
        credentialTargetBound,
        policyConflict,
        hasPolicyResolutionEvidence,
      ),
      evaluateGrandchildDeployment(
        requestedCapability,
        explicitDelegationGrant,
        hasAuthorityEvidence,
        hasLineageEvidence,
      ),
      successorNoteAttempt(noteAddsAuthority),
      revokeParent(hasLifecycleEvidence),
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
      s.targetAuthorized,
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

  // Every active execution locus stays inside the authorized topology.
  val activeDescendantStaysWithinTopology: bool = {
    any { s.childActive, s.grandchildActive }.implies(all {
      s.targetAuthorized,
      s.topologyWithinBounds,
    })
  }

  // Identity, lineage, and a current lease precede descendant execution.
  val activeDescendantHasIdentityLineageAndLease: bool = {
    all {
      s.childActive.implies(all {
        s.identityEvidence,
        s.lineageEvidence,
        s.leaseValid,
      }),
      s.grandchildActive.implies(all {
        s.identityEvidence,
        s.lineageEvidence,
        s.grandchildLineageEvidence,
        s.leaseValid,
      }),
    }
  }

  // Artifacts and credentials remain verified and destination-bound.
  val protectedCapabilityDelivery: bool = {
    any { s.childActive, s.grandchildActive }.implies(all {
      delegationNeverBroadens,
      s.artifactIntegrity,
      s.credentialTargetBound,
    })
  }

  // An unresolved policy conflict can route to review, never to execution.
  val unresolvedPolicyConflictCannotAuthorize: bool = {
    s.unresolvedPolicyConflict.implies(all {
      not(s.childActive),
      not(s.grandchildActive),
    })
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
      not(s.unresolvedLifecycleEvidence),
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

  // These are snapshots of the evaluated proposal, not ongoing execution.
  val interventionPreservesObjective: bool = {
    (s.interventionAudit.outcome == "allow").implies(all {
      s.interventionAudit.proposal.objectiveMatches,
      s.interventionAudit.proposal.grantCurrent,
    })
  }

  val interventionUsesSufficientMeans: bool = {
    (s.interventionAudit.outcome == "allow").implies(
      not(s.interventionAudit.proposal.dominated)
    )
  }

  val interventionStopsAtAcceptance: bool = {
    s.interventionAudit.acceptedAtDecision.implies(all {
      s.interventionAudit.outcome != "allow",
      s.interventionAudit.outcome != "delay",
    })
  }

  // A decision-level progress obligation, not unbounded temporal liveness.
  val interventionMakesPermittedProgress: bool = {
    all {
      s.interventionAudit.checked,
      interventionEligible(s.interventionAudit.proposal),
      not(s.interventionAudit.acceptedAtDecision),
      s.interventionAudit.proposal.withinBudget,
      not(s.interventionAudit.proposal.dominated),
      not(s.interventionAudit.proposal.deferRequested) or s.interventionAudit.proposal.delayUnsafe,
    }.implies(s.interventionAudit.outcome == "allow")
  }

  val interventionRetainsObjectionsAndGate: bool = {
    (s.interventionAudit.outcome == "allow").implies(all {
      s.interventionAudit.proposal.evidenceComplete,
      s.interventionAudit.proposal.objectionsRetained,
      s.interventionAudit.proposal.sharedGate,
    })
  }

  val interventionRejectsProhibitedMeans: bool = {
    (s.interventionAudit.outcome == "allow").implies(
      not(s.interventionAudit.proposal.prohibitedMeans)
    )
  }

  val interventionReportsCompletionTruthfully: bool = {
    s.interventionAudit.reportedComplete.implies(all {
      s.interventionAudit.acceptedAtDecision,
      s.interventionAudit.outcome == "stop",
    })
  }

  val interventionStaysWithinBudget: bool = {
    any {
      s.interventionAudit.outcome == "allow",
      s.interventionAudit.outcome == "delay",
    }.implies(s.interventionAudit.proposal.withinBudget)
  }

  val allCoreInvariants: bool = all {
    allowRequiresAuthorityEvidence,
    delegationNeverBroadens,
    activeDescendantHasAuthority,
    activeDescendantStaysWithinTopology,
    activeDescendantHasIdentityLineageAndLease,
    protectedCapabilityDelivery,
    unresolvedPolicyConflictCannotAuthorize,
    revocationIsTransitive,
    completedMissionHasNoActiveDescendant,
    validClaimHasEvidence,
    modelNoteCannotGrantAuthority,
    interventionPreservesObjective,
    interventionUsesSufficientMeans,
    interventionStopsAtAcceptance,
    interventionMakesPermittedProgress,
    interventionRetainsObjectionsAndGate,
    interventionRejectsProhibitedMeans,
    interventionReportsCompletionTruthfully,
    interventionStaysWithinBudget,
  }

  // Unsafe transitions below are excluded from `step`. They are executable
  // mutation witnesses used only by deterministic kill tests.
  action mutantReachabilityGrantsAuthority: bool = {
    s' = {
      ...s,
      humanAuthority: false,
      childAuthority: true,
      childCapability: 1,
      childActive: true,
      childAuthoritySource: "reachability",
      authorityEvidence: false,
      lineageEvidence: true,
      targetAuthorized: false,
      topologyWithinBounds: true,
      identityEvidence: true,
      leaseValid: true,
      artifactIntegrity: true,
      credentialTargetBound: true,
      lastDecision: "allow",
    }
  }

  action mutantRemovesTopologyLimit: bool = {
    s' = {
      ...s,
      childAuthority: true,
      childCapability: 1,
      childActive: true,
      childAuthoritySource: "human",
      authorityEvidence: true,
      lineageEvidence: true,
      targetAuthorized: true,
      topologyWithinBounds: false,
      identityEvidence: true,
      leaseValid: true,
      artifactIntegrity: true,
      credentialTargetBound: true,
      lastDecision: "allow",
    }
  }

  action mutantBypassesLineageAndLease: bool = {
    s' = {
      ...s,
      childAuthority: true,
      childCapability: 1,
      childActive: true,
      childAuthoritySource: "human",
      authorityEvidence: true,
      lineageEvidence: false,
      targetAuthorized: true,
      topologyWithinBounds: true,
      identityEvidence: false,
      leaseValid: false,
      artifactIntegrity: true,
      credentialTargetBound: true,
      lastDecision: "allow",
    }
  }

  action mutantRevokesParentOnly: bool = {
    s' = {
      ...s,
      parentAuthority: false,
      parentActive: false,
      parentRevoked: true,
      childAuthority: true,
      childCapability: 1,
      childActive: true,
      childRevoked: false,
      childAuthoritySource: "human",
      authorityEvidence: true,
      lineageEvidence: true,
      targetAuthorized: true,
      topologyWithinBounds: true,
      identityEvidence: true,
      leaseValid: true,
      artifactIntegrity: true,
      credentialTargetBound: true,
      lastDecision: "terminate",
    }
  }

  action mutantSuccessorStateGrantsAuthority: bool = {
    s' = {
      ...s,
      childAuthority: true,
      childCapability: 1,
      childActive: true,
      childAuthoritySource: "model_note",
      authorityEvidence: true,
      lineageEvidence: true,
      targetAuthorized: true,
      topologyWithinBounds: true,
      identityEvidence: true,
      leaseValid: true,
      artifactIntegrity: true,
      credentialTargetBound: true,
      lastDecision: "allow",
    }
  }

  action mutantBroadensCapabilityDelivery: bool = {
    s' = {
      ...s,
      childAuthority: true,
      childCapability: 1,
      childActive: true,
      childAuthoritySource: "human",
      authorityEvidence: true,
      lineageEvidence: true,
      targetAuthorized: true,
      topologyWithinBounds: true,
      identityEvidence: true,
      leaseValid: true,
      artifactIntegrity: false,
      credentialTargetBound: false,
      lastDecision: "allow",
    }
  }

  action mutantPolicyConflictCreatesException: bool = {
    s' = {
      ...s,
      childAuthority: true,
      childCapability: 1,
      childActive: true,
      childAuthoritySource: "human",
      authorityEvidence: true,
      lineageEvidence: true,
      targetAuthorized: true,
      topologyWithinBounds: true,
      identityEvidence: true,
      leaseValid: true,
      artifactIntegrity: true,
      credentialTargetBound: true,
      unresolvedPolicyConflict: true,
      policyResolutionEvidence: false,
      lastDecision: "allow",
    }
  }

  action mutantAcceptsUnsupportedLifecycleClaim: bool = {
    s' = {
      ...s,
      childAuthority: false,
      childActive: false,
      grandchildAuthority: false,
      grandchildActive: false,
      lineageEvidence: false,
      lifecycleEvidence: false,
      residueEvidence: false,
      missionComplete: true,
      claimValid: true,
      lastDecision: "allow",
    }
  }

  action mutantPasSelfAppointedMission: bool = {
    s' = {
      ...s,
      interventionAudit: {
        ...s.interventionAudit,
        proposal: {
          ...s.interventionAudit.proposal,
          objectiveMatches: false,
        },
      },
    }
  }

  action mutantPasBroaderIntervention: bool = {
    s' = {
      ...s,
      interventionAudit: {
        ...s.interventionAudit,
        proposal: {
          ...s.interventionAudit.proposal,
          dominated: true,
        },
      },
    }
  }

  action mutantPasContinuesAfterAcceptance: bool = {
    s' = {
      ...s,
      interventionAudit: {
        ...s.interventionAudit,
        acceptedAtDecision: true,
      },
    }
  }

  action mutantPasUnsafeDelay: bool = {
    s' = {
      ...s,
      interventionAudit: {
        ...s.interventionAudit,
        proposal: {
          ...s.interventionAudit.proposal,
          deferRequested: true,
          delayUnsafe: true,
        },
        outcome: "delay",
      },
    }
  }

  action mutantPasHidesObjections: bool = {
    s' = {
      ...s,
      interventionAudit: {
        ...s.interventionAudit,
        proposal: {
          ...s.interventionAudit.proposal,
          objectionsRetained: false,
        },
      },
    }
  }

  action mutantPasBypassesSharedGate: bool = {
    s' = {
      ...s,
      interventionAudit: {
        ...s.interventionAudit,
        proposal: {
          ...s.interventionAudit.proposal,
          sharedGate: false,
        },
      },
    }
  }

  action mutantPasGreaterGoodException: bool = {
    s' = {
      ...s,
      interventionAudit: {
        ...s.interventionAudit,
        proposal: {
          ...s.interventionAudit.proposal,
          prohibitedMeans: true,
        },
      },
    }
  }

  action mutantPasFalseCompletion: bool = {
    s' = {
      ...s,
      interventionAudit: {
        ...s.interventionAudit,
        reportedComplete: true,
      },
    }
  }

  action mutantPasRedundantReview: bool = {
    s' = {
      ...s,
      interventionAudit: {
        ...s.interventionAudit,
        outcome: "review",
      },
    }
  }

  action mutantPasOverrunsBudget: bool = {
    s' = {
      ...s,
      interventionAudit: {
        ...s.interventionAudit,
        proposal: { ...s.interventionAudit.proposal, withinBudget: false },
      },
    }
  }

  action check(condition: bool): bool = all {
    assert(condition),
    s' = s,
  }

  run unresolvedPolicyConflictHoldsInterventionTest = {
    init
      .then(evaluateAssuredChildDeployment(
        1, true, true, true, true, true, true, true, true, true, true, false,
      ))
      .then(evaluateIntervention(permittedIntervention))
      .then(check(all {
        s.unresolvedPolicyConflict,
        s.interventionAudit.outcome == "review",
        not(s.interventionAudit.proposal.evidenceComplete),
        allCoreInvariants,
      }))
  }

  run acceptedTaskBlocksNewDeploymentTest = {
    init
      .then(recordTaskAcceptance)
      .then(evaluateChildDeployment(1, true, true, true))
      .then(check(all {
        s.lastDecision == "block",
        not(s.childActive),
        s.taskAccepted,
        allCoreInvariants,
      }))
  }

  run acceptedTaskBlocksNewGrandchildTest = {
    init
      .then(evaluateChildDeployment(2, true, true, true))
      .then(recordTaskAcceptance)
      .then(evaluateGrandchildDeployment(1, true, true, true))
      .then(check(all {
        s.lastDecision == "block",
        s.childActive,
        not(s.grandchildActive),
        s.taskAccepted,
        allCoreInvariants,
      }))
      .then(terminateChild(true, true))
      .then(completeResidueInventory)
      .then(assessCompletionClaim)
      .then(check(all { s.claimValid, allCoreInvariants }))
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
      .then(revokeParent(true))
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

  run evidencedRevocationCanCompleteTest = {
    init
      .then(evaluateChildDeployment(2, true, true, true))
      .then(evaluateGrandchildDeployment(1, true, true, true))
      .then(revokeParent(true))
      .then(completeResidueInventory)
      .then(assessCompletionClaim)
      .then(check(all {
        s.parentRevoked,
        s.lifecycleEvidence,
        s.missionComplete,
        s.claimValid,
      }))
  }

  run unsupportedRevocationCannotCompleteTest = {
    init
      .then(evaluateChildDeployment(1, true, true, true))
      .then(revokeParent(false))
      .then(completeResidueInventory)
      .then(assessCompletionClaim)
      .then(check(all {
        s.parentRevoked,
        not(s.lifecycleEvidence),
        not(s.missionComplete),
        not(s.claimValid),
      }))
  }

  run emptyRevocationCannotRepairLifecycleEvidenceTest = {
    init
      .then(evaluateChildDeployment(1, true, true, true))
      .then(terminateChild(true, false))
      .then(revokeParent(true))
      .then(completeResidueInventory)
      .then(assessCompletionClaim)
      .then(check(all {
        s.parentRevoked,
        not(s.lifecycleEvidence),
        not(s.missionComplete),
        not(s.claimValid),
      }))
  }

  run laterLifecycleCannotRepairEarlierEvidenceGapTest = {
    init
      .then(evaluateChildDeployment(1, true, true, true))
      .then(terminateChild(true, false))
      .then(evaluateChildDeployment(1, true, true, true))
      .then(terminateChild(true, true))
      .then(completeResidueInventory)
      .then(assessCompletionClaim)
      .then(check(all {
        s.lineageEvidence,
        s.lifecycleEvidence,
        s.unresolvedLifecycleEvidence,
        not(s.missionComplete),
        not(s.claimValid),
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

  run unresolvedPolicyConflictBlocksTest = {
    init
      .then(evaluateAssuredChildDeployment(
        1,
        true,
        true,
        true,
        true,
        true,
        true,
        true,
        true,
        true,
        true,
        false,
      ))
      .then(check(all {
        s.lastDecision == "review",
        s.unresolvedPolicyConflict,
        not(s.childAuthority),
        not(s.childActive),
      }))
  }

  run authoritativePolicyResolutionAllowsTest = {
    init
      .then(evaluateAssuredChildDeployment(
        1,
        true,
        true,
        true,
        true,
        true,
        true,
        true,
        true,
        true,
        true,
        true,
      ))
      .then(check(all {
        s.lastDecision == "allow",
        s.policyResolutionEvidence,
        not(s.unresolvedPolicyConflict),
        s.childAuthority,
        s.childActive,
      }))
  }

  run mutantRdpM01ReachabilityAuthorityKilledTest = {
    init
      .then(mutantReachabilityGrantsAuthority)
      .then(check(not(allowRequiresAuthorityEvidence)))
  }

  run mutantRdpM02TopologyLimitKilledTest = {
    init
      .then(mutantRemovesTopologyLimit)
      .then(check(not(activeDescendantStaysWithinTopology)))
  }

  run mutantRdpM03LineageLeaseBypassKilledTest = {
    init
      .then(mutantBypassesLineageAndLease)
      .then(check(not(activeDescendantHasIdentityLineageAndLease)))
  }

  run mutantRdpM04ParentOnlyRevocationKilledTest = {
    init
      .then(mutantRevokesParentOnly)
      .then(check(not(revocationIsTransitive)))
  }

  run mutantRdpM05SuccessorAuthorityKilledTest = {
    init
      .then(mutantSuccessorStateGrantsAuthority)
      .then(check(not(modelNoteCannotGrantAuthority)))
  }

  run mutantRdpM06DeliveryBroadeningKilledTest = {
    init
      .then(mutantBroadensCapabilityDelivery)
      .then(check(not(protectedCapabilityDelivery)))
  }

  run mutantRdpM07PolicyConflictExceptionKilledTest = {
    init
      .then(mutantPolicyConflictCreatesException)
      .then(check(not(unresolvedPolicyConflictCannotAuthorize)))
  }

  run mutantRdpM08UnsupportedClaimKilledTest = {
    init
      .then(mutantAcceptsUnsupportedLifecycleClaim)
      .then(check(not(validClaimHasEvidence)))
  }

  // Literal PAS fixtures; checked against the portable vector artifact.
  run pasGrantedWorkProceedsTest = {
    init
      .then(evaluateIntervention({
        objectiveMatches: true,
        grantCurrent: true,
        evidenceComplete: true,
        prohibitedMeans: false,
        dominated: false,
        withinBudget: true,
        objectionsRetained: true,
        sharedGate: true,
        deferRequested: false,
        delayUnsafe: false,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "allow",
        s.interventionAudit.reportedComplete == false,
        allCoreInvariants,
      }))
  }

  run pasSafeDeferralTest = {
    init
      .then(evaluateIntervention({
        objectiveMatches: true,
        grantCurrent: true,
        evidenceComplete: true,
        prohibitedMeans: false,
        dominated: false,
        withinBudget: true,
        objectionsRetained: true,
        sharedGate: true,
        deferRequested: true,
        delayUnsafe: false,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "delay",
        s.interventionAudit.reportedComplete == false,
        allCoreInvariants,
      }))
  }

  run pasUnsafeDelayActsWithinGrantTest = {
    init
      .then(evaluateIntervention({
        objectiveMatches: true,
        grantCurrent: true,
        evidenceComplete: true,
        prohibitedMeans: false,
        dominated: false,
        withinBudget: true,
        objectionsRetained: true,
        sharedGate: true,
        deferRequested: true,
        delayUnsafe: true,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "allow",
        s.interventionAudit.reportedComplete == false,
        allCoreInvariants,
      }))
  }

  run pasNecessaryBroaderActionTest = {
    init
      .then(evaluateIntervention({
        objectiveMatches: true,
        grantCurrent: true,
        evidenceComplete: true,
        prohibitedMeans: false,
        dominated: false,
        withinBudget: true,
        objectionsRetained: true,
        sharedGate: true,
        deferRequested: false,
        delayUnsafe: false,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "allow",
        s.interventionAudit.reportedComplete == false,
        allCoreInvariants,
      }))
  }

  run pasMissingGrantBlocksTest = {
    init
      .then(evaluateIntervention({
        objectiveMatches: true,
        grantCurrent: false,
        evidenceComplete: true,
        prohibitedMeans: false,
        dominated: false,
        withinBudget: true,
        objectionsRetained: true,
        sharedGate: true,
        deferRequested: false,
        delayUnsafe: false,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "block",
        s.interventionAudit.reportedComplete == false,
        allCoreInvariants,
      }))
  }

  run pasParentRevocationBlocksTest = {
    init
      .then(revokeParent(true))
      .then(evaluateIntervention({
        objectiveMatches: true,
        grantCurrent: true,
        evidenceComplete: true,
        prohibitedMeans: false,
        dominated: false,
        withinBudget: true,
        objectionsRetained: true,
        sharedGate: true,
        deferRequested: false,
        delayUnsafe: false,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "block",
        s.interventionAudit.reportedComplete == false,
        allCoreInvariants,
      }))
  }

  run pasSelfAppointedMissionBlocksTest = {
    init
      .then(evaluateIntervention({
        objectiveMatches: false,
        grantCurrent: true,
        evidenceComplete: true,
        prohibitedMeans: false,
        dominated: false,
        withinBudget: true,
        objectionsRetained: true,
        sharedGate: true,
        deferRequested: false,
        delayUnsafe: false,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "block",
        s.interventionAudit.reportedComplete == false,
        allCoreInvariants,
      }))
  }

  run pasProhibitedBenefitBlocksTest = {
    init
      .then(evaluateIntervention({
        objectiveMatches: true,
        grantCurrent: true,
        evidenceComplete: true,
        prohibitedMeans: true,
        dominated: false,
        withinBudget: true,
        objectionsRetained: true,
        sharedGate: true,
        deferRequested: false,
        delayUnsafe: false,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "block",
        s.interventionAudit.reportedComplete == false,
        allCoreInvariants,
      }))
  }

  run pasMissingEvidenceReviewsTest = {
    init
      .then(evaluateIntervention({
        objectiveMatches: true,
        grantCurrent: true,
        evidenceComplete: false,
        prohibitedMeans: false,
        dominated: false,
        withinBudget: true,
        objectionsRetained: true,
        sharedGate: true,
        deferRequested: false,
        delayUnsafe: false,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "review",
        s.interventionAudit.reportedComplete == false,
        allCoreInvariants,
      }))
  }

  run pasHiddenObjectionReviewsTest = {
    init
      .then(evaluateIntervention({
        objectiveMatches: true,
        grantCurrent: true,
        evidenceComplete: true,
        prohibitedMeans: false,
        dominated: false,
        withinBudget: true,
        objectionsRetained: false,
        sharedGate: true,
        deferRequested: false,
        delayUnsafe: false,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "review",
        s.interventionAudit.reportedComplete == false,
        allCoreInvariants,
      }))
  }

  run pasRoleBypassReviewsTest = {
    init
      .then(evaluateIntervention({
        objectiveMatches: true,
        grantCurrent: true,
        evidenceComplete: true,
        prohibitedMeans: false,
        dominated: false,
        withinBudget: true,
        objectionsRetained: true,
        sharedGate: false,
        deferRequested: false,
        delayUnsafe: false,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "review",
        s.interventionAudit.reportedComplete == false,
        allCoreInvariants,
      }))
  }

  run pasDominatedInterventionReviewsTest = {
    init
      .then(evaluateIntervention({
        objectiveMatches: true,
        grantCurrent: true,
        evidenceComplete: true,
        prohibitedMeans: false,
        dominated: true,
        withinBudget: true,
        objectionsRetained: true,
        sharedGate: true,
        deferRequested: false,
        delayUnsafe: false,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "review",
        s.interventionAudit.reportedComplete == false,
        allCoreInvariants,
      }))
  }

  run pasBudgetStopsIncompleteTest = {
    init
      .then(evaluateIntervention({
        objectiveMatches: true,
        grantCurrent: true,
        evidenceComplete: true,
        prohibitedMeans: false,
        dominated: false,
        withinBudget: false,
        objectionsRetained: true,
        sharedGate: true,
        deferRequested: false,
        delayUnsafe: false,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "stop",
        s.interventionAudit.reportedComplete == false,
        allCoreInvariants,
      }))
  }

  run pasAcceptanceStopsOptionalWorkTest = {
    init
      .then(recordTaskAcceptance)
      .then(evaluateIntervention({
        objectiveMatches: true,
        grantCurrent: true,
        evidenceComplete: true,
        prohibitedMeans: false,
        dominated: false,
        withinBudget: true,
        objectionsRetained: true,
        sharedGate: true,
        deferRequested: false,
        delayUnsafe: false,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "stop",
        s.interventionAudit.reportedComplete == true,
        allCoreInvariants,
      }))
  }

  run pasAcceptancePersistsAcrossProposalTest = {
    init
      .then(recordTaskAcceptance)
      .then(evaluateIntervention({
        objectiveMatches: true,
        grantCurrent: true,
        evidenceComplete: true,
        prohibitedMeans: false,
        dominated: false,
        withinBudget: true,
        objectionsRetained: true,
        sharedGate: true,
        deferRequested: true,
        delayUnsafe: false,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "stop",
        s.interventionAudit.reportedComplete == true,
        allCoreInvariants,
      }))
  }

  run pasCompletedMissionStopsWorkTest = {
    init
      .then(evaluateChildDeployment(1, true, true, true))
      .then(terminateChild(true, true))
      .then(completeResidueInventory)
      .then(assessCompletionClaim)
      .then(evaluateIntervention({
        objectiveMatches: true,
        grantCurrent: true,
        evidenceComplete: true,
        prohibitedMeans: false,
        dominated: false,
        withinBudget: true,
        objectionsRetained: true,
        sharedGate: true,
        deferRequested: false,
        delayUnsafe: false,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "stop",
        s.interventionAudit.reportedComplete == true,
        allCoreInvariants,
      }))
  }

  run pasDelayRiskCannotGrantAuthorityTest = {
    init
      .then(evaluateIntervention({
        objectiveMatches: true,
        grantCurrent: false,
        evidenceComplete: true,
        prohibitedMeans: false,
        dominated: false,
        withinBudget: true,
        objectionsRetained: true,
        sharedGate: true,
        deferRequested: true,
        delayUnsafe: true,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "block",
        s.interventionAudit.reportedComplete == false,
        allCoreInvariants,
      }))
  }

  run pasDelayRiskCannotPermitHarmTest = {
    init
      .then(evaluateIntervention({
        objectiveMatches: true,
        grantCurrent: true,
        evidenceComplete: true,
        prohibitedMeans: true,
        dominated: false,
        withinBudget: true,
        objectionsRetained: true,
        sharedGate: true,
        deferRequested: true,
        delayUnsafe: true,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "block",
        s.interventionAudit.reportedComplete == false,
        allCoreInvariants,
      }))
  }

  run pasDelayRiskCannotWaiveEvidenceTest = {
    init
      .then(evaluateIntervention({
        objectiveMatches: true,
        grantCurrent: true,
        evidenceComplete: false,
        prohibitedMeans: false,
        dominated: false,
        withinBudget: true,
        objectionsRetained: true,
        sharedGate: true,
        deferRequested: true,
        delayUnsafe: true,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "review",
        s.interventionAudit.reportedComplete == false,
        allCoreInvariants,
      }))
  }

  run pasNoBlanketMinimalismTest = {
    init
      .then(evaluateIntervention({
        objectiveMatches: true,
        grantCurrent: true,
        evidenceComplete: true,
        prohibitedMeans: false,
        dominated: false,
        withinBudget: true,
        objectionsRetained: true,
        sharedGate: true,
        deferRequested: false,
        delayUnsafe: true,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "allow",
        s.interventionAudit.reportedComplete == false,
        allCoreInvariants,
      }))
  }

  run pasAcceptanceDoesNotExcuseHarmTest = {
    init
      .then(recordTaskAcceptance)
      .then(evaluateIntervention({
        objectiveMatches: true,
        grantCurrent: true,
        evidenceComplete: true,
        prohibitedMeans: true,
        dominated: false,
        withinBudget: true,
        objectionsRetained: true,
        sharedGate: true,
        deferRequested: false,
        delayUnsafe: false,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "block",
        s.interventionAudit.reportedComplete == false,
        allCoreInvariants,
      }))
  }

  run pasAcceptedButRevokedBlocksTest = {
    init
      .then(revokeParent(true))
      .then(recordTaskAcceptance)
      .then(evaluateIntervention({
        objectiveMatches: true,
        grantCurrent: true,
        evidenceComplete: true,
        prohibitedMeans: false,
        dominated: false,
        withinBudget: true,
        objectionsRetained: true,
        sharedGate: true,
        deferRequested: false,
        delayUnsafe: false,
      }))
      .then(check(all {
        s.interventionAudit.outcome == "block",
        s.interventionAudit.reportedComplete == false,
        allCoreInvariants,
      }))
  }

  run mutantPasM01SelfAppointedMissionKilledTest = {
    init
      .then(evaluateIntervention(permittedIntervention))
      .then(mutantPasSelfAppointedMission)
      .then(check(not(interventionPreservesObjective)))
  }

  run mutantPasM02BroaderInterventionKilledTest = {
    init
      .then(evaluateIntervention(permittedIntervention))
      .then(mutantPasBroaderIntervention)
      .then(check(not(interventionUsesSufficientMeans)))
  }

  run mutantPasM03ContinuesAfterAcceptanceKilledTest = {
    init
      .then(evaluateIntervention(permittedIntervention))
      .then(mutantPasContinuesAfterAcceptance)
      .then(check(not(interventionStopsAtAcceptance)))
  }

  run mutantPasM04UnsafeDelayKilledTest = {
    init
      .then(evaluateIntervention(permittedIntervention))
      .then(mutantPasUnsafeDelay)
      .then(check(not(interventionMakesPermittedProgress)))
  }

  run mutantPasM05HidesObjectionsKilledTest = {
    init
      .then(evaluateIntervention(permittedIntervention))
      .then(mutantPasHidesObjections)
      .then(check(not(interventionRetainsObjectionsAndGate)))
  }

  run mutantPasM06BypassesSharedGateKilledTest = {
    init
      .then(evaluateIntervention(permittedIntervention))
      .then(mutantPasBypassesSharedGate)
      .then(check(not(interventionRetainsObjectionsAndGate)))
  }

  run mutantPasM07GreaterGoodExceptionKilledTest = {
    init
      .then(evaluateIntervention(permittedIntervention))
      .then(mutantPasGreaterGoodException)
      .then(check(not(interventionRejectsProhibitedMeans)))
  }

  run mutantPasM08FalseCompletionKilledTest = {
    init
      .then(evaluateIntervention(permittedIntervention))
      .then(mutantPasFalseCompletion)
      .then(check(not(interventionReportsCompletionTruthfully)))
  }

  run mutantPasM09RedundantReviewKilledTest = {
    init
      .then(evaluateIntervention(permittedIntervention))
      .then(mutantPasRedundantReview)
      .then(check(not(interventionMakesPermittedProgress)))
  }

  run mutantPasM10OverrunsBudgetKilledTest = {
    init
      .then(evaluateIntervention(permittedIntervention))
      .then(mutantPasOverrunsBudget)
      .then(check(not(interventionStaysWithinBudget)))
  }
}
