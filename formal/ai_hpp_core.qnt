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
    assurancePermits: bool,
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

  // RAB: symbolic execution boundary; all sensor/admission facts are assumed.
  type RobotScope = { operation: str, target: str, tool: str }
  type RobotAction = { operation: str, target: str, tool: str, planRevision: int }
  type RobotApproval = { issued: bool, command: RobotAction, epoch: int }
  type RobotExecutionAudit = {
    assurancePermits: bool,
    executed: bool,
    command: RobotAction,
    scope: RobotScope,
    approval: RobotApproval,
    epoch: int,
    humanAuthorized: bool,
    contextFresh: bool,
    hazardBounded: bool,
    historyComplete: bool,
    protectedContents: bool,
    componentsAdmitted: bool,
    externalEnforcement: bool,
    evidenceAvailable: bool,
  }
  type RobotState = {
    scope: RobotScope,
    proposal: RobotAction,
    approval: RobotApproval,
    epoch: int,
    contextFresh: bool,
    hazardBounded: bool,
    historyComplete: bool,
    protectedContents: bool,
    componentsAdmitted: bool,
    externalEnforcement: bool,
    evidenceAvailable: bool,
    lastOutcome: str,
    audit: RobotExecutionAudit,
  }

  pure val robotAppleAction: RobotAction = {
    operation: "cut", target: "apple", tool: "knife", planRevision: 0,
  }
  pure val robotBoxScope: RobotScope = {
    operation: "dispose", target: "box", tool: "gripper",
  }
  pure val robotBoxAction: RobotAction = {
    operation: "dispose", target: "box", tool: "gripper", planRevision: 0,
  }
  pure val initialRobotState: RobotState = {
    scope: { operation: "cut", target: "apple", tool: "knife" },
    proposal: robotAppleAction,
    approval: { issued: false, command: robotAppleAction, epoch: 0 },
    epoch: 0,
    contextFresh: true,
    hazardBounded: true,
    historyComplete: true,
    protectedContents: false,
    componentsAdmitted: true,
    externalEnforcement: true,
    evidenceAvailable: true,
    lastOutcome: "none",
    audit: {
      assurancePermits: true,
      executed: false,
      command: robotAppleAction,
      scope: { operation: "cut", target: "apple", tool: "knife" },
      approval: { issued: false, command: robotAppleAction, epoch: 0 },
      epoch: 0,
      humanAuthorized: true,
      contextFresh: true,
      hazardBounded: true,
      historyComplete: true,
      protectedContents: false,
      componentsAdmitted: true,
      externalEnforcement: true,
      evidenceAvailable: true,
    },
  }

  type GroundingFacts = {
    scopeAuthorized: bool, observationsCurrent: bool, evidenceComplete: bool,
    ruleKnown: bool, factsSupport: bool, policyPermits: bool,
  }
  type GroundingRecord = { facts: GroundingFacts, reason: str }
  type OversightRecord = {
    required: bool, eventId: int, stage: int, owner: int, offeredOwner: int,
    routeAuthorized: bool, payloadMinimal: bool, independent: bool,
    durable: bool, custodyGap: bool, ticks: int, holdOnOpen: bool,
    sentEvidence: bool, receiptEvent: int, reviewEvidence: bool,
    resolutionEvidence: bool, transferEvidence: bool,
    restartStage: int, restartOwner: int, restartTicks: int, lastTransition: str,
  }
  pure val supportedGrounding: GroundingFacts = {
    scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true,
    ruleKnown: true, factsSupport: true, policyPermits: true,
  }
  pure val initialOversight: OversightRecord = {
    required: false, eventId: 0, stage: 0, owner: 1, offeredOwner: 0,
    routeAuthorized: true, payloadMinimal: true, independent: true,
    durable: true, custodyGap: false, ticks: 0, holdOnOpen: false,
    sentEvidence: false, receiptEvent: 0, reviewEvidence: false,
    resolutionEvidence: false, transferEvidence: false,
    restartStage: 0, restartOwner: 1, restartTicks: 0, lastTransition: "none",
  }

  type AssuranceState = {
    grounding: GroundingRecord,
    oversight: OversightRecord,
    robot: RobotState,
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
      grounding: { facts: supportedGrounding, reason: "permitted" },
      oversight: initialOversight,
      robot: initialRobotState,
      taskAccepted: false,
      interventionAudit: {
        assurancePermits: true,
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
    evidenceOversightPermits,
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
    evidenceOversightPermits,
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
      groundingPermits,
      not(oversightOpen),
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
      evidenceComplete: all {
        proposed.evidenceComplete, not(s.unresolvedPolicyConflict),
        evidenceOversightPermits,
      },
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
        assurancePermits: evidenceOversightPermits,
        checked: true,
        proposal: current,
        acceptedAtDecision: accepted,
        outcome: outcome,
        reportedComplete: accepted and outcome == "stop",
      },
    }
  }

  pure def robotActionWithinScope(a: RobotAction, scope: RobotScope): bool = all {
    a.operation == scope.operation,
    a.target == scope.target,
    a.tool == scope.tool,
  }

  val robotHumanAuthority: bool = all {
    s.humanAuthority, s.parentAuthority, s.parentActive,
    not(s.parentRevoked), not(s.unresolvedPolicyConflict),
    not(s.taskAccepted), not(s.missionComplete),
  }

  val robotActionMayProceed: bool = all {
    robotHumanAuthority,
    evidenceOversightPermits,
    robotActionWithinScope(s.robot.proposal, s.robot.scope),
    s.robot.contextFresh,
    s.robot.hazardBounded,
    s.robot.historyComplete,
    not(s.robot.proposal.operation == "dispose" and s.robot.protectedContents),
    s.robot.componentsAdmitted,
    s.robot.externalEnforcement,
    s.robot.evidenceAvailable,
  }

  // Trusted owner event, not a planner-selected scope expansion.
  action recordRobotScope(scope: RobotScope): bool = all {
    robotHumanAuthority,
    s.robot.epoch < 2,
    s' = { ...s, robot: { ...s.robot, scope: scope, epoch: s.robot.epoch + 1 } },
  }

  action proposeRobotAction(proposal: RobotAction): bool = {
    // Preserve the previous approval to exercise plan-substitution rejection.
    s' = { ...s, robot: { ...s.robot, proposal: proposal, lastOutcome: "propose" } }
  }

  // Trusted observation event. Unknown history never proves safe empty contents.
  action changeRobotContext(
    protectedContents: bool, contextFresh: bool,
    historyComplete: bool, hazardBounded: bool,
  ): bool = all {
    s.robot.epoch < 2,
    s' = {
      ...s,
      robot: {
        ...s.robot,
        epoch: s.robot.epoch + 1,
        protectedContents: protectedContents,
        contextFresh: contextFresh,
        historyComplete: historyComplete,
        hazardBounded: hazardBounded,
      },
    },
  }

  action changeRobotComponents(admitted: bool): bool = all {
    s.robot.epoch < 2,
    s' = { ...s, robot: {
      ...s.robot, epoch: s.robot.epoch + 1, componentsAdmitted: admitted,
    } },
  }

  action configureRobotBoundary(enforced: bool, evidenceAvailable: bool): bool = all {
    s.robot.epoch < 2,
    s' = { ...s, robot: {
      ...s.robot, epoch: s.robot.epoch + 1,
      externalEnforcement: enforced, evidenceAvailable: evidenceAvailable,
    } },
  }

  action assessRobotAction: bool = {
    s' = { ...s, robot: {
      ...s.robot,
      approval: {
        issued: robotActionMayProceed,
        command: s.robot.proposal,
        epoch: s.robot.epoch,
      },
      lastOutcome: if (robotActionMayProceed) "allow" else "block",
    } }
  }

  action executeRobotAction: bool = {
    val permitted = all {
      robotActionMayProceed,
      s.robot.approval.issued,
      s.robot.approval.command == s.robot.proposal,
      s.robot.approval.epoch == s.robot.epoch,
    }
    s' = { ...s, robot: {
      ...s.robot,
      // Both successful execution and denial consume this attempted approval.
      approval: { ...s.robot.approval, issued: false },
      lastOutcome: if (permitted) "execute" else "block",
      audit: {
        assurancePermits: evidenceOversightPermits,
        executed: permitted,
        command: s.robot.proposal,
        scope: s.robot.scope,
        approval: s.robot.approval,
        epoch: s.robot.epoch,
        humanAuthorized: robotHumanAuthority,
        contextFresh: s.robot.contextFresh,
        hazardBounded: s.robot.hazardBounded,
        historyComplete: s.robot.historyComplete,
        protectedContents: s.robot.protectedContents,
        componentsAdmitted: s.robot.componentsAdmitted,
        externalEnforcement: s.robot.externalEnforcement,
        evidenceAvailable: s.robot.evidenceAvailable,
      },
    } }
  }

  pure def groundingReason(f: GroundingFacts): str = {
    if (not(f.scopeAuthorized)) "unauthorized"
    else if (not(f.observationsCurrent) or not(f.evidenceComplete) or not(f.ruleKnown)) "insufficient_evidence"
    else if (not(f.factsSupport)) "contradicted"
    else if (not(f.policyPermits)) "prohibited"
    else "permitted"
  }

  val groundingPermits: bool = groundingReason(s.grounding.facts) == "permitted"
  val oversightOpen: bool = s.oversight.required and s.oversight.stage < 6
  val evidenceOversightPermits: bool = all {
    groundingPermits,
    not(oversightOpen and any {
      s.oversight.holdOnOpen, s.oversight.ticks >= 2, s.oversight.custodyGap,
    }),
  }

  // Trusted evidence/policy event, not a model's confidence or self-grant.
  action assessGroundedProposal(proposed: GroundingFacts): bool = {
    val current = { ...proposed, scopeAuthorized: all {
      proposed.scopeAuthorized, s.humanAuthority, s.parentAuthority,
      s.parentActive, not(s.parentRevoked),
    } }
    val reason = groundingReason(current)
    s' = { ...s,
      grounding: { facts: current, reason: reason },
      claimValid: s.claimValid and reason == "permitted",
    }
  }

  // One active obligation; two non-reused IDs in this finite abstraction.
  action registerOversightObligation(required: bool, holdOnOpen: bool): bool = {
    if (required and not(oversightOpen) and s.oversight.eventId < 2) {
      s' = { ...s, claimValid: false, oversight: {
        ...initialOversight,
        required: true, eventId: s.oversight.eventId + 1,
        stage: 1, holdOnOpen: holdOnOpen,
        routeAuthorized: s.oversight.routeAuthorized,
        payloadMinimal: s.oversight.payloadMinimal,
        independent: s.oversight.independent,
        durable: s.oversight.durable,
        lastTransition: "detected",
      } }
    } else { s' = s }
  }

  // Route facts are fixed after dispatch in this bounded model.
  action configureOversightPath(
    authorized: bool, minimal: bool, independent: bool, durable: bool,
  ): bool = {
    if (s.oversight.stage < 3) {
      s' = { ...s, oversight: { ...s.oversight,
        routeAuthorized: authorized, payloadMinimal: minimal,
        independent: independent, durable: durable, lastTransition: "configure",
      } }
    } else { s' = s }
  }

  action queueOversightNotice: bool = {
    if (all { oversightOpen, s.oversight.stage == 1,
              s.oversight.durable, not(s.oversight.custodyGap) }) {
      s' = { ...s, oversight: { ...s.oversight, stage: 2, lastTransition: "queued" } }
    } else { s' = s }
  }

  action dispatchOversightNotice: bool = {
    if (all { oversightOpen, s.oversight.stage == 2,
              s.oversight.routeAuthorized, s.oversight.payloadMinimal,
              s.oversight.independent, s.oversight.durable,
              not(s.oversight.custodyGap) }) {
      s' = { ...s, oversight: { ...s.oversight,
        stage: 3, sentEvidence: true, lastTransition: "sent",
      } }
    } else { s' = s }
  }

  action recordOversightReceipt(eventId: int): bool = {
    if (s.oversight.stage == 3 and eventId == s.oversight.eventId) {
      s' = { ...s, oversight: { ...s.oversight,
        stage: 4, receiptEvent: eventId, lastTransition: "received",
      } }
    } else { s' = s }
  }

  action reviewOversightIncident(hasEvidence: bool): bool = {
    if (all { s.oversight.stage == 4, hasEvidence,
              s.oversight.independent, not(s.oversight.custodyGap) }) {
      s' = { ...s, oversight: { ...s.oversight,
        stage: 5, reviewEvidence: true, lastTransition: "reviewed",
      } }
    } else { s' = s }
  }

  action resolveOversightIncident(hasEvidence: bool): bool = {
    if (all { s.oversight.stage == 5, hasEvidence,
              s.oversight.independent, not(s.oversight.custodyGap) }) {
      s' = { ...s, oversight: { ...s.oversight,
        stage: 6, resolutionEvidence: true, lastTransition: "resolved",
      } }
    } else { s' = s }
  }

  action tickOversightDeadline: bool = {
    if (oversightOpen and s.oversight.ticks < 2) {
      s' = { ...s, oversight: { ...s.oversight,
        ticks: s.oversight.ticks + 1, lastTransition: "tick",
      } }
    } else { s' = s }
  }

  action offerOversightHandoff(owner: int): bool = {
    if (oversightOpen and Set(1, 2).contains(owner) and owner != s.oversight.owner) {
      s' = { ...s, oversight: { ...s.oversight,
        offeredOwner: owner, lastTransition: "offer",
      } }
    } else { s' = s }
  }

  action acceptOversightHandoff(hasTransferEvidence: bool): bool = {
    if (all { oversightOpen, s.oversight.offeredOwner > 0,
              hasTransferEvidence, s.oversight.durable, not(s.oversight.custodyGap) }) {
      s' = { ...s, oversight: { ...s.oversight,
        owner: s.oversight.offeredOwner, offeredOwner: 0,
        transferEvidence: true, lastTransition: "accepted",
      } }
    } else { s' = s }
  }

  action restartOversightWorker: bool = {
    s' = { ...s, oversight: { ...s.oversight,
      custodyGap: s.oversight.custodyGap or (oversightOpen and not(s.oversight.durable)),
      restartStage: s.oversight.stage, restartOwner: s.oversight.owner, restartTicks: s.oversight.ticks,
      lastTransition: "restart",
    } }
  }

  action recoverOversightCustody(hasEvidence: bool): bool = {
    if (hasEvidence and s.oversight.durable) {
      s' = { ...s, oversight: { ...s.oversight,
        custodyGap: false, lastTransition: "recovered",
      } }
    } else { s' = s }
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
    nondet robotOperation = Set("cut", "dispose").oneOf()
    nondet robotTarget = Set("apple", "hand", "box").oneOf()
    nondet robotTool = Set("knife", "gripper").oneOf()
    nondet robotPlanRevision = 0.to(1).oneOf()
    any {
      assessGroundedProposal({
        scopeAuthorized: explicitHumanGrant, observationsCurrent: identityEvidence,
        evidenceComplete: hasAuthorityEvidence, ruleKnown: targetAuthorized,
        factsSupport: artifactIntegrity, policyPermits: topologyWithinBounds,
      }),
      registerOversightObligation(explicitDelegationGrant, policyConflict),
      configureOversightPath(targetAuthorized, artifactIntegrity, identityEvidence, leaseValid),
      queueOversightNotice,
      dispatchOversightNotice,
      recordOversightReceipt(requestedCapability),
      reviewOversightIncident(hasAuthorityEvidence),
      resolveOversightIncident(hasLifecycleEvidence),
      tickOversightDeadline,
      offerOversightHandoff(requestedCapability),
      acceptOversightHandoff(hasLineageEvidence),
      restartOversightWorker,
      recoverOversightCustody(hasAuthorityEvidence),
      proposeRobotAction({
        operation: robotOperation, target: robotTarget,
        tool: robotTool, planRevision: robotPlanRevision,
      }),
      recordRobotScope(robotBoxScope),
      changeRobotContext(noteAddsAuthority, identityEvidence, hasLineageEvidence, leaseValid),
      changeRobotComponents(artifactIntegrity),
      configureRobotBoundary(targetAuthorized, hasAuthorityEvidence),
      assessRobotAction,
      executeRobotAction,
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

  // Historical execution snapshots, not a proof of physical motor behavior.
  val robotExecutionBoundToAuthorizedAction: bool = {
    s.robot.audit.executed.implies(all {
      s.robot.audit.humanAuthorized,
      robotActionWithinScope(s.robot.audit.command, s.robot.audit.scope),
      s.robot.audit.approval.issued,
      s.robot.audit.command == s.robot.audit.approval.command,
    })
  }

  val robotExecutionUsesCurrentContext: bool = {
    s.robot.audit.executed.implies(all {
      s.robot.audit.epoch == s.robot.audit.approval.epoch,
      s.robot.audit.contextFresh,
      s.robot.audit.hazardBounded,
    })
  }

  val robotExecutionPreservesCumulativeSafety: bool = {
    s.robot.audit.executed.implies(all {
      s.robot.audit.historyComplete,
      not(s.robot.audit.command.operation == "dispose" and s.robot.audit.protectedContents),
    })
  }

  val robotExecutionRequiresExternalGate: bool = {
    s.robot.audit.executed.implies(s.robot.audit.externalEnforcement)
  }

  val robotExecutionHasEvidence: bool = {
    s.robot.audit.executed.implies(s.robot.audit.evidenceAvailable)
  }

  val robotExecutionUsesAdmittedComponents: bool = {
    s.robot.audit.executed.implies(s.robot.audit.componentsAdmitted)
  }

  // EGO checks abstract observations, scoped holds and reporting obligations.
  val groundingReasonReflectsInputs: bool = {
    s.grounding.reason == groundingReason(s.grounding.facts)
  }

  val effectsRequireGroundingAndOversight: bool = {
    all {
      (s.interventionAudit.outcome == "allow").implies(s.interventionAudit.assurancePermits),
      s.robot.audit.executed.implies(s.robot.audit.assurancePermits),
    }
  }

  val requiredOversightObligationRetained: bool = {
    (s.oversight.eventId > 0).implies(all {
      s.oversight.required, s.oversight.stage >= 1, s.oversight.owner > 0,
    })
  }

  val oversightStagesHaveEvidence: bool = {
    all {
      (s.oversight.stage >= 3).implies(s.oversight.sentEvidence),
      (s.oversight.stage >= 4).implies(s.oversight.receiptEvent == s.oversight.eventId),
    }
  }

  val oversightDeliveryWithinScope: bool = {
    s.oversight.sentEvidence.implies(all {
      s.oversight.routeAuthorized, s.oversight.payloadMinimal, s.oversight.independent,
    })
  }

  val oversightOwnerCustodyContinuity: bool = {
    all {
      (s.oversight.owner == 2).implies(s.oversight.transferEvidence),
      (s.oversight.lastTransition == "restart").implies(all {
        s.oversight.stage == s.oversight.restartStage,
        s.oversight.owner == s.oversight.restartOwner,
        s.oversight.ticks == s.oversight.restartTicks,
      }),
    }
  }

  val completionRequiresDischargedOversight: bool = {
    s.claimValid.implies(all { groundingPermits, not(oversightOpen) })
  }

  val oversightResolutionNeedsIndependentReview: bool = {
    (s.oversight.stage == 6).implies(all {
      s.oversight.reviewEvidence, s.oversight.resolutionEvidence,
      s.oversight.independent,
    })
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
    robotExecutionBoundToAuthorizedAction,
    robotExecutionUsesCurrentContext,
    robotExecutionPreservesCumulativeSafety,
    robotExecutionRequiresExternalGate,
    robotExecutionHasEvidence,
    robotExecutionUsesAdmittedComponents,
    groundingReasonReflectsInputs,
    effectsRequireGroundingAndOversight,
    requiredOversightObligationRetained,
    oversightStagesHaveEvidence,
    oversightDeliveryWithinScope,
    oversightOwnerCustodyContinuity,
    completionRequiresDischargedOversight,
    oversightResolutionNeedsIndependentReview,
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

  action mutantRabTargetSubstitution: bool = {
    s' = { ...s, robot: { ...s.robot, audit: {
      ...s.robot.audit,
      command: { ...s.robot.audit.command, target: "hand" },
    } } }
  }

  action mutantRabToolSubstitution: bool = {
    s' = { ...s, robot: { ...s.robot, audit: {
      ...s.robot.audit,
      command: { ...s.robot.audit.command, tool: "gripper" },
    } } }
  }

  action mutantRabPlanSubstitution: bool = {
    s' = { ...s, robot: { ...s.robot, audit: {
      ...s.robot.audit,
      command: { ...s.robot.audit.command, planRevision: 1 },
    } } }
  }

  action mutantRabStaleApproval: bool = {
    s' = { ...s, robot: { ...s.robot, audit: {
      ...s.robot.audit,
      epoch: 1,
    } } }
  }

  action mutantRabConcealedContents: bool = {
    s' = { ...s, robot: { ...s.robot, audit: {
      ...s.robot.audit,
      protectedContents: true,
    } } }
  }

  action mutantRabLostHistory: bool = {
    s' = { ...s, robot: { ...s.robot, audit: {
      ...s.robot.audit,
      historyComplete: false,
    } } }
  }

  action mutantRabBypassedGate: bool = {
    s' = { ...s, robot: { ...s.robot, audit: {
      ...s.robot.audit,
      externalEnforcement: false,
    } } }
  }

  action mutantRabMissingEvidence: bool = {
    s' = { ...s, robot: { ...s.robot, audit: {
      ...s.robot.audit,
      evidenceAvailable: false,
    } } }
  }

  action mutantRabUnadmittedPlanner: bool = {
    s' = { ...s, robot: { ...s.robot, audit: {
      ...s.robot.audit,
      componentsAdmitted: false,
    } } }
  }

  action mutantRabStalePerception: bool = {
    s' = { ...s, robot: { ...s.robot, audit: {
      ...s.robot.audit,
      contextFresh: false,
    } } }
  }

  action mutantEgoUnsupportedAllow: bool = {
    s' = { ...s, grounding: { ...s.grounding, reason: "permitted" } }
  }

  action mutantEgoUnsupportedDenial: bool = {
    s' = { ...s, grounding: { ...s.grounding, reason: "contradicted" } }
  }

  action mutantEgoIgnoreHold: bool = {
    s' = { ...s, robot: { ...s.robot, audit: { ...s.robot.audit, assurancePermits: false } } }
  }

  action mutantEgoLeaderVeto: bool = {
    s' = { ...s, oversight: { ...s.oversight, required: false } }
  }

  action mutantEgoPromiseAsDispatch: bool = {
    s' = { ...s, oversight: { ...s.oversight, stage: 3 } }
  }

  action mutantEgoOldReceiptAccepted: bool = {
    s' = { ...s, oversight: { ...s.oversight, stage: 4, receiptEvent: 0 } }
  }

  action mutantEgoExcessDisclosure: bool = {
    s' = { ...s, oversight: { ...s.oversight, payloadMinimal: false } }
  }

  action mutantEgoUnacceptedTransfer: bool = {
    s' = { ...s, oversight: { ...s.oversight, owner: 2, transferEvidence: false } }
  }

  action mutantEgoLostQueueOnRestart: bool = {
    s' = { ...s, oversight: { ...s.oversight, stage: 1 } }
  }

  action mutantEgoFalseCompletion: bool = {
    s' = { ...s, claimValid: true }
  }

  action mutantEgoReceiptAsResolution: bool = {
    s' = { ...s, oversight: { ...s.oversight, stage: 6 } }
  }

  action mutantEgoCorrelatedReview: bool = {
    s' = { ...s, oversight: { ...s.oversight, independent: false } }
  }

  action check(condition: bool): bool = all {
    assert(condition),
    s' = s,
  }

  run completedMissionDeniesRobotExecutionTest = {
    init
      .then(assessRobotAction)
      .then(evaluateChildDeployment(1, true, true, true))
      .then(terminateChild(true, true))
      .then(completeResidueInventory)
      .then(assessCompletionClaim)
      .then(executeRobotAction)
      .then(check(all {
        s.missionComplete,
        s.claimValid,
        s.robot.lastOutcome == "block",
        not(s.robot.audit.executed),
        allCoreInvariants,
      }))
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

  // RAB portable fixtures and excluded unsafe execution witnesses.
  run rabAuthorizedAppleTest = {
    init
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "execute",
        s.robot.audit.executed == true,
        allCoreInvariants,
      }))
  }

  run rabBenignSuffixSameActionTest = {
    init
      .then(proposeRobotAction({ operation: "cut", target: "apple", tool: "knife", planRevision: 0 }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "execute",
        s.robot.audit.executed == true,
        allCoreInvariants,
      }))
  }

  run rabHandSubstitutionTest = {
    init
      .then(proposeRobotAction({ operation: "cut", target: "hand", tool: "knife", planRevision: 0 }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "block",
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run rabToolSubstitutionTest = {
    init
      .then(proposeRobotAction({ operation: "cut", target: "apple", tool: "gripper", planRevision: 0 }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "block",
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run rabRewriteAfterApprovalTest = {
    init
      .then(assessRobotAction)
      .then(proposeRobotAction({ operation: "cut", target: "apple", tool: "knife", planRevision: 1 }))
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "block",
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run rabLegitimateReplanReapprovedTest = {
    init
      .then(assessRobotAction)
      .then(proposeRobotAction({ operation: "cut", target: "apple", tool: "knife", planRevision: 1 }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "execute",
        s.robot.audit.executed == true,
        allCoreInvariants,
      }))
  }

  run rabEnvironmentChangedTest = {
    init
      .then(assessRobotAction)
      .then(changeRobotContext(false, true, true, true))
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "block",
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run rabEnvironmentReapprovedTest = {
    init
      .then(assessRobotAction)
      .then(changeRobotContext(false, true, true, true))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "execute",
        s.robot.audit.executed == true,
        allCoreInvariants,
      }))
  }

  run rabStalePerceptionTest = {
    init
      .then(changeRobotContext(false, false, true, true))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "block",
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run rabUnboundedHazardTest = {
    init
      .then(changeRobotContext(false, true, true, false))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "block",
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run rabProtectedContentsTest = {
    init
      .then(recordRobotScope({ operation: "dispose", target: "box", tool: "gripper" }))
      .then(proposeRobotAction({ operation: "dispose", target: "box", tool: "gripper", planRevision: 0 }))
      .then(assessRobotAction)
      .then(changeRobotContext(true, true, true, true))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "block",
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run rabLostHistoryTest = {
    init
      .then(changeRobotContext(false, true, false, true))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "block",
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run rabMissingBoundaryTest = {
    init
      .then(configureRobotBoundary(false, true))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "block",
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run rabMissingEvidenceTest = {
    init
      .then(configureRobotBoundary(true, false))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "block",
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run rabUnadmittedPlannerTest = {
    init
      .then(changeRobotComponents(false))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "block",
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run rabChangedPlannerStaleTokenTest = {
    init
      .then(assessRobotAction)
      .then(changeRobotComponents(true))
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "block",
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run rabChangedPlannerReapprovedTest = {
    init
      .then(assessRobotAction)
      .then(changeRobotComponents(true))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "execute",
        s.robot.audit.executed == true,
        allCoreInvariants,
      }))
  }

  run rabTokenReplayTest = {
    init
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "block",
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run rabRevokedBeforeExecutionTest = {
    init
      .then(assessRobotAction)
      .then(revokeParent(true))
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "block",
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run rabAcceptedBeforeExecutionTest = {
    init
      .then(assessRobotAction)
      .then(recordTaskAcceptance)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "block",
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run rabPolicyConflictBeforeExecutionTest = {
    init
      .then(assessRobotAction)
      .then(evaluateAssuredChildDeployment(1, true, true, true, true, true, true, true, true, true, true, false))
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "block",
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run rabSafeContainerDisposalTest = {
    init
      .then(recordRobotScope({ operation: "dispose", target: "box", tool: "gripper" }))
      .then(proposeRobotAction({ operation: "dispose", target: "box", tool: "gripper", planRevision: 0 }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.lastOutcome == "execute",
        s.robot.audit.executed == true,
        allCoreInvariants,
      }))
  }

  run mutantRabM01TargetSubstitutionKilledTest = {
    init
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all { s.robot.audit.executed, allCoreInvariants }))
      .then(mutantRabTargetSubstitution)
      .then(check(not(robotExecutionBoundToAuthorizedAction)))
  }

  run mutantRabM02ToolSubstitutionKilledTest = {
    init
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all { s.robot.audit.executed, allCoreInvariants }))
      .then(mutantRabToolSubstitution)
      .then(check(not(robotExecutionBoundToAuthorizedAction)))
  }

  run mutantRabM03PlanSubstitutionKilledTest = {
    init
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all { s.robot.audit.executed, allCoreInvariants }))
      .then(mutantRabPlanSubstitution)
      .then(check(not(robotExecutionBoundToAuthorizedAction)))
  }

  run mutantRabM04StaleApprovalKilledTest = {
    init
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all { s.robot.audit.executed, allCoreInvariants }))
      .then(mutantRabStaleApproval)
      .then(check(not(robotExecutionUsesCurrentContext)))
  }

  run mutantRabM05ConcealedContentsKilledTest = {
    init
      .then(recordRobotScope(robotBoxScope))
      .then(proposeRobotAction(robotBoxAction))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all { s.robot.audit.executed, allCoreInvariants }))
      .then(mutantRabConcealedContents)
      .then(check(not(robotExecutionPreservesCumulativeSafety)))
  }

  run mutantRabM06LostHistoryKilledTest = {
    init
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all { s.robot.audit.executed, allCoreInvariants }))
      .then(mutantRabLostHistory)
      .then(check(not(robotExecutionPreservesCumulativeSafety)))
  }

  run mutantRabM07BypassedGateKilledTest = {
    init
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all { s.robot.audit.executed, allCoreInvariants }))
      .then(mutantRabBypassedGate)
      .then(check(not(robotExecutionRequiresExternalGate)))
  }

  run mutantRabM08MissingEvidenceKilledTest = {
    init
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all { s.robot.audit.executed, allCoreInvariants }))
      .then(mutantRabMissingEvidence)
      .then(check(not(robotExecutionHasEvidence)))
  }

  run mutantRabM09UnadmittedPlannerKilledTest = {
    init
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all { s.robot.audit.executed, allCoreInvariants }))
      .then(mutantRabUnadmittedPlanner)
      .then(check(not(robotExecutionUsesAdmittedComponents)))
  }

  run mutantRabM10StalePerceptionKilledTest = {
    init
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all { s.robot.audit.executed, allCoreInvariants }))
      .then(mutantRabStalePerception)
      .then(check(not(robotExecutionUsesCurrentContext)))
  }

  // EGO portable cases and excluded mutation witnesses.
  run egoPermittedWorkTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(evaluateIntervention(permittedIntervention))
      .then(check(all {
        s.grounding.reason == "permitted",
        s.robot.audit.executed == true,
        s.interventionAudit.outcome == "allow",
        s.oversight.required == false,
        allCoreInvariants,
      }))
  }

  run egoContradictedPremiseTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: false, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(evaluateIntervention(permittedIntervention))
      .then(evaluateChildDeployment(1, true, true, true))
      .then(check(all {
        s.grounding.reason == "contradicted",
        s.robot.audit.executed == false,
        s.interventionAudit.outcome == "review",
        s.lastDecision == "block",
        allCoreInvariants,
      }))
  }

  run egoUnknownIsNotContradictedTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: false, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.grounding.reason == "insufficient_evidence",
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run egoStaleObservationTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: false, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.grounding.reason == "insufficient_evidence",
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run egoUnknownPolicyTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: false, factsSupport: true, policyPermits: true }))
      .then(check(all {
        s.grounding.reason == "insufficient_evidence",
        allCoreInvariants,
      }))
  }

  run egoProhibitedMeansTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: false }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.grounding.reason == "prohibited",
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run egoMissingGrantTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: false, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(evaluateChildDeployment(1, true, true, true))
      .then(check(all {
        s.grounding.reason == "unauthorized",
        s.lastDecision == "block",
        allCoreInvariants,
      }))
  }

  run egoRevocationIsNotSunkCostTest = {
    init
      .then(revokeParent(true))
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.grounding.reason == "unauthorized",
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run egoCorrectionRestoresUsefulWorkTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: false, policyPermits: true }))
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(evaluateIntervention(permittedIntervention))
      .then(check(all {
        s.grounding.reason == "permitted",
        s.robot.audit.executed == true,
        s.interventionAudit.outcome == "allow",
        allCoreInvariants,
      }))
  }

  run egoNonReportableRoutineEventTest = {
    init
      .then(registerOversightObligation(false, false))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(evaluateIntervention(permittedIntervention))
      .then(check(all {
        s.oversight.required == false,
        s.oversight.stage == 0,
        s.robot.audit.executed == true,
        s.interventionAudit.outcome == "allow",
        allCoreInvariants,
      }))
  }

  run egoMandatoryIncidentHoldsEffectsTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(evaluateIntervention(permittedIntervention))
      .then(evaluateChildDeployment(1, true, true, true))
      .then(check(all {
        s.oversight.required == true,
        s.oversight.stage == 1,
        s.robot.audit.executed == false,
        s.interventionAudit.outcome == "review",
        s.lastDecision == "block",
        allCoreInvariants,
      }))
  }

  run egoNoAutomaticGlobalStopTest = {
    init
      .then(registerOversightObligation(true, false))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.oversight.required == true,
        s.oversight.stage == 1,
        s.robot.audit.executed == true,
        allCoreInvariants,
      }))
  }

  run egoDeadlineStopsAffectedWorkTest = {
    init
      .then(registerOversightObligation(true, false))
      .then(tickOversightDeadline)
      .then(tickOversightDeadline)
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.oversight.ticks == 2,
        s.robot.audit.executed == false,
        s.oversight.required == true,
        allCoreInvariants,
      }))
  }

  run egoQueueIsNotDeliveryTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(check(all {
        s.oversight.stage == 2,
        s.oversight.required == true,
        allCoreInvariants,
      }))
  }

  run egoSentIsNotReceiptTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(check(all {
        s.oversight.stage == 3,
        s.oversight.receiptEvent == 0,
        allCoreInvariants,
      }))
  }

  run egoReceiptIsNotResolutionTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(recordOversightReceipt(1))
      .then(check(all {
        s.oversight.stage == 4,
        s.oversight.resolutionEvidence == false,
        allCoreInvariants,
      }))
  }

  run egoReviewIsNotResolutionTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(recordOversightReceipt(1))
      .then(reviewOversightIncident(true))
      .then(check(all {
        s.oversight.stage == 5,
        s.oversight.resolutionEvidence == false,
        allCoreInvariants,
      }))
  }

  run egoIndependentEvidenceResolvesTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(recordOversightReceipt(1))
      .then(reviewOversightIncident(true))
      .then(resolveOversightIncident(true))
      .then(check(all {
        s.oversight.stage == 6,
        s.oversight.resolutionEvidence == true,
        allCoreInvariants,
      }))
  }

  run egoNoResolutionWithoutEvidenceTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(recordOversightReceipt(1))
      .then(reviewOversightIncident(true))
      .then(resolveOversightIncident(false))
      .then(check(all {
        s.oversight.stage == 5,
        s.oversight.resolutionEvidence == false,
        allCoreInvariants,
      }))
  }

  run egoNoReviewWithoutEvidenceTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(recordOversightReceipt(1))
      .then(reviewOversightIncident(false))
      .then(resolveOversightIncident(true))
      .then(check(all {
        s.oversight.stage == 4,
        s.oversight.resolutionEvidence == false,
        allCoreInvariants,
      }))
  }

  run egoUnauthorizedRecipientTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(configureOversightPath(false, true, true, true))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(check(all {
        s.oversight.stage == 2,
        s.oversight.sentEvidence == false,
        allCoreInvariants,
      }))
  }

  run egoExcessPayloadTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(configureOversightPath(true, false, true, true))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(check(all {
        s.oversight.stage == 2,
        s.oversight.sentEvidence == false,
        allCoreInvariants,
      }))
  }

  run egoTeamIsNotIndependentOversightTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(configureOversightPath(true, true, false, true))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(check(all {
        s.oversight.stage == 2,
        s.oversight.sentEvidence == false,
        allCoreInvariants,
      }))
  }

  run egoAuthorizedRepairOfRouteTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(configureOversightPath(false, true, true, true))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(configureOversightPath(true, true, true, true))
      .then(dispatchOversightNotice)
      .then(check(all {
        s.oversight.stage == 3,
        s.oversight.sentEvidence == true,
        allCoreInvariants,
      }))
  }

  run egoOldReceiptRejectedTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(recordOversightReceipt(0))
      .then(check(all {
        s.oversight.stage == 3,
        s.oversight.receiptEvent == 0,
        allCoreInvariants,
      }))
  }

  run egoHandoffOfferKeepsOwnerTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(offerOversightHandoff(2))
      .then(check(all {
        s.oversight.stage == 2,
        s.oversight.owner == 1,
        s.oversight.offeredOwner == 2,
        allCoreInvariants,
      }))
  }

  run egoHandoffNeedsAcceptanceEvidenceTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(offerOversightHandoff(2))
      .then(acceptOversightHandoff(false))
      .then(check(all {
        s.oversight.owner == 1,
        s.oversight.offeredOwner == 2,
        allCoreInvariants,
      }))
  }

  run egoAcceptedHandoffPreservesDeadlineTest = {
    init
      .then(registerOversightObligation(true, false))
      .then(queueOversightNotice)
      .then(tickOversightDeadline)
      .then(offerOversightHandoff(2))
      .then(acceptOversightHandoff(true))
      .then(tickOversightDeadline)
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.oversight.stage == 2,
        s.oversight.owner == 2,
        s.oversight.ticks == 2,
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run egoRestartPreservesDurableQueueTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(tickOversightDeadline)
      .then(restartOversightWorker)
      .then(check(all {
        s.oversight.stage == 2,
        s.oversight.owner == 1,
        s.oversight.custodyGap == false,
        s.oversight.ticks == 1,
        allCoreInvariants,
      }))
  }

  run egoLostCustodyHoldsWorkTest = {
    init
      .then(registerOversightObligation(true, false))
      .then(configureOversightPath(true, true, true, false))
      .then(restartOversightWorker)
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.oversight.stage == 1,
        s.oversight.custodyGap == true,
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run egoCustodyRecoveryNeedsEvidenceTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(configureOversightPath(true, true, true, false))
      .then(restartOversightWorker)
      .then(configureOversightPath(true, true, true, true))
      .then(recoverOversightCustody(false))
      .then(queueOversightNotice)
      .then(check(all {
        s.oversight.stage == 1,
        s.oversight.custodyGap == true,
        allCoreInvariants,
      }))
  }

  run egoVerifiedCustodyRecoveryTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(configureOversightPath(true, true, true, false))
      .then(restartOversightWorker)
      .then(configureOversightPath(true, true, true, true))
      .then(recoverOversightCustody(true))
      .then(queueOversightNotice)
      .then(check(all {
        s.oversight.stage == 2,
        s.oversight.custodyGap == false,
        allCoreInvariants,
      }))
  }

  run egoIncidentBlocksCompletionTest = {
    init
      .then(evaluateChildDeployment(1, true, true, true))
      .then(terminateChild(true, true))
      .then(completeResidueInventory)
      .then(registerOversightObligation(true, false))
      .then(assessCompletionClaim)
      .then(check(all {
        s.claimValid == false,
        s.oversight.required == true,
        s.oversight.stage == 1,
        allCoreInvariants,
      }))
  }

  run egoResolutionRestoresCompletionTest = {
    init
      .then(evaluateChildDeployment(1, true, true, true))
      .then(terminateChild(true, true))
      .then(completeResidueInventory)
      .then(registerOversightObligation(true, false))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(recordOversightReceipt(1))
      .then(reviewOversightIncident(true))
      .then(resolveOversightIncident(true))
      .then(assessCompletionClaim)
      .then(check(all {
        s.claimValid == true,
        s.oversight.stage == 6,
        allCoreInvariants,
      }))
  }

  run egoReportSurvivesMissionRevocationTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(revokeParent(true))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(recordOversightReceipt(1))
      .then(check(all {
        s.oversight.stage == 4,
        s.oversight.required == true,
        allCoreInvariants,
      }))
  }

  run egoReportSurvivesTaskAcceptanceTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(recordTaskAcceptance)
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(recordOversightReceipt(1))
      .then(check(all {
        s.oversight.stage == 4,
        s.oversight.required == true,
        allCoreInvariants,
      }))
  }

  run egoNonReportableEventCannotWaiveOpenDutyTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(registerOversightObligation(false, false))
      .then(check(all {
        s.oversight.stage == 1,
        s.oversight.required == true,
        allCoreInvariants,
      }))
  }

  run egoDuplicateReceiptDoesNotResolveTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(recordOversightReceipt(1))
      .then(recordOversightReceipt(1))
      .then(check(all {
        s.oversight.stage == 4,
        s.oversight.resolutionEvidence == false,
        allCoreInvariants,
      }))
  }

  run egoOldEventCannotCloseNewIncidentTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(recordOversightReceipt(1))
      .then(reviewOversightIncident(true))
      .then(resolveOversightIncident(true))
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(recordOversightReceipt(1))
      .then(check(all {
        s.oversight.stage == 3,
        s.oversight.eventId == 2,
        s.oversight.receiptEvent == 0,
        allCoreInvariants,
      }))
  }

  run egoResolvedIncidentDoesNotPermitContradictedActionTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(recordOversightReceipt(1))
      .then(reviewOversightIncident(true))
      .then(resolveOversightIncident(true))
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: false, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.oversight.stage == 6,
        s.grounding.reason == "contradicted",
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run mutantEgoM01UnsupportedAllowKilledTest = {
    init
      .then(assessGroundedProposal({ ...supportedGrounding, evidenceComplete: false }))
      .then(check(all { allCoreInvariants, s.grounding.reason == "insufficient_evidence" }))
      .then(mutantEgoUnsupportedAllow)
      .then(check(not(groundingReasonReflectsInputs)))
  }

  run mutantEgoM02UnsupportedDenialKilledTest = {
    init
      .then(check(all { allCoreInvariants, groundingPermits }))
      .then(mutantEgoUnsupportedDenial)
      .then(check(not(groundingReasonReflectsInputs)))
  }

  run mutantEgoM03IgnoreHoldKilledTest = {
    init
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(registerOversightObligation(true, true))
      .then(check(all { allCoreInvariants, s.robot.audit.executed and not(evidenceOversightPermits) }))
      .then(mutantEgoIgnoreHold)
      .then(check(not(effectsRequireGroundingAndOversight)))
  }

  run mutantEgoM04LeaderVetoKilledTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(check(all { allCoreInvariants, s.oversight.stage == 1 }))
      .then(mutantEgoLeaderVeto)
      .then(check(not(requiredOversightObligationRetained)))
  }

  run mutantEgoM05PromiseAsDispatchKilledTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(check(all { allCoreInvariants, s.oversight.stage == 2 }))
      .then(mutantEgoPromiseAsDispatch)
      .then(check(not(oversightStagesHaveEvidence)))
  }

  run mutantEgoM06OldReceiptAcceptedKilledTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(check(all { allCoreInvariants, s.oversight.stage == 3 }))
      .then(mutantEgoOldReceiptAccepted)
      .then(check(not(oversightStagesHaveEvidence)))
  }

  run mutantEgoM07ExcessDisclosureKilledTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(check(all { allCoreInvariants, s.oversight.stage == 3 }))
      .then(mutantEgoExcessDisclosure)
      .then(check(not(oversightDeliveryWithinScope)))
  }

  run mutantEgoM08UnacceptedTransferKilledTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(check(all { allCoreInvariants, s.oversight.stage == 2 }))
      .then(mutantEgoUnacceptedTransfer)
      .then(check(not(oversightOwnerCustodyContinuity)))
  }

  run mutantEgoM09LostQueueOnRestartKilledTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(restartOversightWorker)
      .then(check(all { allCoreInvariants, s.oversight.stage == 2 and s.oversight.lastTransition == "restart" }))
      .then(mutantEgoLostQueueOnRestart)
      .then(check(not(oversightOwnerCustodyContinuity)))
  }

  run mutantEgoM10FalseCompletionKilledTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(check(all { allCoreInvariants, s.oversight.stage == 1 }))
      .then(mutantEgoFalseCompletion)
      .then(check(not(completionRequiresDischargedOversight)))
  }

  run mutantEgoM11ReceiptAsResolutionKilledTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(recordOversightReceipt(1))
      .then(check(all { allCoreInvariants, s.oversight.stage == 4 }))
      .then(mutantEgoReceiptAsResolution)
      .then(check(not(oversightResolutionNeedsIndependentReview)))
  }

  run mutantEgoM12CorrelatedReviewKilledTest = {
    init
      .then(registerOversightObligation(true, true))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(recordOversightReceipt(1))
      .then(reviewOversightIncident(true))
      .then(resolveOversightIncident(true))
      .then(check(all { allCoreInvariants, s.oversight.stage == 6 }))
      .then(mutantEgoCorrelatedReview)
      .then(check(not(oversightResolutionNeedsIndependentReview)))
  }

  run boundarySuppressedNoticeTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: false, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(registerOversightObligation(true, false))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(recordOversightReceipt(1))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.oversight.stage == 4,
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run boundaryDummyMonitorTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: false, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(registerOversightObligation(true, false))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(recordOversightReceipt(1))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.oversight.stage == 4,
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run boundaryUnmonitoredChildTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: false, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(registerOversightObligation(true, false))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(recordOversightReceipt(1))
      .then(evaluateChildDeployment(1, true, true, true))
      .then(check(all {
        s.oversight.stage == 4,
        s.lastDecision == "block",
        allCoreInvariants,
      }))
  }

  run boundaryRevokedTokenTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: false, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(revokeParent(true))
      .then(registerOversightObligation(true, false))
      .then(queueOversightNotice)
      .then(dispatchOversightNotice)
      .then(recordOversightReceipt(1))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.oversight.stage == 4,
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run boundaryPermittedRepairTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.oversight.stage == 0,
        s.robot.audit.executed == true,
        allCoreInvariants,
      }))
  }

  run boundaryMonitoredChildTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(evaluateChildDeployment(1, true, true, true))
      .then(check(all {
        s.oversight.stage == 0,
        s.lastDecision == "allow",
        allCoreInvariants,
      }))
  }

  run boundaryCurrentTokenTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.oversight.stage == 0,
        s.robot.audit.executed == true,
        allCoreInvariants,
      }))
  }

  run boundaryAuthorizedReplacementTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.oversight.stage == 0,
        s.robot.audit.executed == true,
        allCoreInvariants,
      }))
  }


  run cyberAuthorityAssertedPentestTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: false, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run cyberAuthorityTargetDriftTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: false, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run cyberAuthorityFoundCredentialTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: false, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run cyberAuthoritySupervisorGrantTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: false, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run cyberAuthorityChangedSkillTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: false, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run cyberAuthorityWrongRecipientTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: false }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run cyberAuthorityBenignMonitorTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: false, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run cyberAuthorityRevokedParentTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: false, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run cyberAuthorityExpiredSessionTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: false, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run cyberAuthorityMissingOwnerProofTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: false, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run cyberAuthorityPermittedReadTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == true,
        allCoreInvariants,
      }))
  }

  run cyberAuthorityBoundedDelegateTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == true,
        allCoreInvariants,
      }))
  }

  run cyberAuthorityReviewedSkillUpdateTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == true,
        allCoreInvariants,
      }))
  }

  run cyberAuthorityMinimalReportTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == true,
        allCoreInvariants,
      }))
  }


  run consequentialAdviceUnverifiedClinicalPlanTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: false, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run consequentialAdviceConcealmentTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: false }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run consequentialAdviceAvoidMonitoringTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: false }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run consequentialAdviceFalseReassuranceTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: false }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run consequentialAdviceWarningAfterSummaryTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: false }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run consequentialAdviceStaleClinicalPlanTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: false, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run consequentialAdviceCareerPressureTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: false, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run consequentialAdviceStaleTwinTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: false, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run consequentialAdviceConflictingTelemetryTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: false, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run consequentialAdviceSafetyVersusEfficiencyTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: false }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run consequentialAdviceReviewerOverloadTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: false, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run consequentialAdviceLateReviewTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: false, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run consequentialAdviceStaleApprovalTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: false, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run consequentialAdviceMissingClinicalContextTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: false, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == false,
        allCoreInvariants,
      }))
  }

  run consequentialAdvicePrepareClinicalSummaryTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == true,
        allCoreInvariants,
      }))
  }

  run consequentialAdviceUrgentSupportTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == true,
        allCoreInvariants,
      }))
  }

  run consequentialAdvicePermittedPlantActionTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == true,
        allCoreInvariants,
      }))
  }

  run consequentialAdviceCorrectedTwinTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == true,
        allCoreInvariants,
      }))
  }

  run consequentialAdviceRestoredReviewTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == true,
        allCoreInvariants,
      }))
  }

  run consequentialAdviceExplainExistingPlanTest = {
    init
      .then(assessGroundedProposal({ scopeAuthorized: true, observationsCurrent: true, evidenceComplete: true, ruleKnown: true, factsSupport: true, policyPermits: true }))
      .then(assessRobotAction)
      .then(executeRobotAction)
      .then(check(all {
        s.robot.audit.executed == true,
        allCoreInvariants,
      }))
  }
}
