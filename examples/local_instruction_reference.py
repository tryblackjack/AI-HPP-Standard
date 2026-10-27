"""Local file admission illustration using the existing CBA candidate checks.

Only fixed harmless descriptors and temporary configuration markers are used.
No Markdown interpretation, agent launch, network, package or real config access.
"""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import tempfile

from examples import cyber_authority_reference as cba

CASES = (
    "downloaded_instruction", "global_configuration", "redirected_gateway",
    "child_authority", "changed_instruction", "cloned_instruction",
    "inherited_directory_trust", "expired_admission", "approved_project",
    "approved_configuration", "approved_gateway", "approved_child",
)
OPERATORS = {
    "trust_filename": "trust_label", "broaden_config_scope": "ignore_target",
    "trust_tls_endpoint": "ignore_recipient", "trust_child_request": "trust_supervisor",
    "trust_path_after_change": "ignore_skill_digest",
}


def exercise(case, mutant=None):
    if case not in CASES or mutant not in (*OPERATORS, None):
        raise ValueError("unknown local instruction fixture")
    with tempfile.TemporaryDirectory(prefix="ai-hpp-instruction-") as directory:
        root = Path(directory)
        source = root / "AGENTS.md"
        source.write_text("# Synthetic project instruction descriptor\n", encoding="utf-8")
        approved_digest = cba.digest(source.read_bytes())
        # Source admission is an externally supplied fixture fact, never a claim in the file.
        admitted = case not in ("downloaded_instruction", "cloned_instruction",
                                 "inherited_directory_trust")
        if case == "changed_instruction":
            source.write_text("# Changed synthetic descriptor\n", encoding="utf-8")
        grant, request, clock = cba.fixture("permitted_read")
        grant.update(verified=admitted, skill_digest=approved_digest,
                     targets=["project-config"], operations=["edit-config"])
        request.update(target="project-config", operation="edit-config",
                       skill_digest=cba.digest(source.read_bytes()))
        if case == "global_configuration":
            request["target"] = "global-config"
        elif case == "redirected_gateway":
            request["recipient"] = "unapproved-gateway"
        elif case == "child_authority":
            request.update(delegated=True, principal="unapproved-child")
            grant["delegation_verified"] = False
        elif case == "expired_admission":
            clock = grant["expires"]
        elif case == "approved_configuration":
            request["target"] = "global-config"
            grant["targets"] = ["global-config"]
        elif case == "approved_gateway":
            request["recipient"] = "reviewed-gateway"
            grant["recipients"] = ["reviewed-gateway"]
        elif case == "approved_child":
            request["delegated"] = True
        inputs = dict(grant=deepcopy(grant), request=deepcopy(request), clock=clock)
        (root / "inputs.json").write_text(json.dumps(inputs), encoding="utf-8")
        if cba.admit(grant, request, clock, OPERATORS.get(mutant)):
            (root / "configuration-marker.json").write_text(json.dumps(dict(
                target=request["target"], operation=request["operation"],
                recipient=request["recipient"], data_class=request["data_class"],
                marker="SYNTHETIC_ONLY")), encoding="utf-8")
        observed = json.loads((root / "inputs.json").read_text())
        marker = root / "configuration-marker.json"
        observed["effect"] = json.loads(marker.read_text()) if marker.exists() else None
        return observed
