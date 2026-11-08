"""Finite synthetic observation admission, not vision, a robot controller or a signature verifier."""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from pathlib import Path
import tempfile

OPERATORS = ("trust_ingest", "ignore_replay", "ignore_uncertainty",
             "count_shared_channels", "reuse_old_approval", "trust_done")


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def materialize(root, name, observation):
    if observation is None:
        return None
    frame = deepcopy(observation["frame"])
    if observation["edit"] == "approved_transform":
        frame["transform_revision"] = "approved-v2"
    path = root / f"{name}.json"
    path.write_text(json.dumps(frame, sort_keys=True))
    admitted_digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if observation["edit"] == "unapproved_substitution":
        frame["object"] = "workpiece"
        path.write_text(json.dumps(frame, sort_keys=True))
    return dict(source=deepcopy(observation["source"]), admitted_digest=admitted_digest,
                raw=path.read_text())


def checks(stage, request, seen):
    c = stage["context"]
    observations = [o for o in (stage["primary"], stage["corroborator"]) if o is not None]
    frames = [json.loads(o["raw"]) for o in observations]
    source = bool(observations) and all(
        o["source"]["admitted"] and hashlib.sha256(o["raw"].encode()).hexdigest() == o["admitted_digest"]
        for o in observations)
    current = all(f["session_id"] == c["session_id"] and f["target_id"] == request["target_id"]
                  and f["epoch"] == c["epoch"] and 0 <= c["now"] - f["capture_tick"] <= 3
                  and (o["source"]["source_id"], f["frame_id"]) not in seen
                  for o, f in zip(observations, frames))
    clear = all(f["quality"] == "usable" and f["object"] == "workpiece"
                and o["source"]["calibration_current"] for o, f in zip(observations, frames))
    independent = not stage["corroboration_required"] or (
        stage["corroborator"] is not None
        and stage["primary"]["source"]["source_id"] != stage["corroborator"]["source"]["source_id"]
        and stage["primary"]["source"]["pipeline_id"] != stage["corroborator"]["source"]["pipeline_id"]
        and bool(stage["primary"]["source"]["failure_domains"])
        and bool(stage["corroborator"]["source"]["failure_domains"])
        and not set(stage["primary"]["source"]["failure_domains"])
        .intersection(stage["corroborator"]["source"]["failure_domains"]))
    return [source, current, clear, independent]


def exercise(inputs, operator=None, *, deny_all=False):
    if operator not in (*OPERATORS, None):
        raise ValueError("unknown finite operator")
    with tempfile.TemporaryDirectory(prefix="ai-hpp-observation-") as directory:
        root = Path(directory)
        (root / "inputs.json").write_text(json.dumps(inputs))
        request = inputs["request"]
        approval = dict(issued=True, epoch=0, bundle_digest="baseline-0", **request)
        seen, stages = set(), []
        for index, spec in enumerate(inputs["stages"], 1):
            stage_root = root / str(index)
            stage_root.mkdir()
            stage = dict(context=deepcopy(spec["context"]),
                         primary=materialize(stage_root, "primary", spec["primary"]),
                         corroborator=materialize(stage_root, "corroborator", spec["corroborator"]),
                         corroboration_required=spec["corroboration_required"])
            bundle = digest(stage)
            conditions = checks(stage, request, seen)
            if operator in OPERATORS[:4]:
                conditions[OPERATORS.index(operator)] = True
            if spec["reapprove"] and all(conditions) and request["authorized"]:
                approval = dict(issued=True, epoch=stage["context"]["epoch"], bundle_digest=bundle, **request)
            presented = deepcopy(approval)
            binding = (presented["issued"] and presented["epoch"] == stage["context"]["epoch"]
                       and presented["bundle_digest"] == bundle
                       and all(presented[k] == request[k] for k in request))
            if operator == "reuse_old_approval":
                binding = True
            if all(conditions) and binding and request["authorized"] and not deny_all:
                (stage_root / "effect.json").write_text(json.dumps(dict(
                    marker="SYNTHETIC_ONLY", bundle_digest=bundle, action_id=request["action_id"])))
            approval["issued"] = False
            effect_path = stage_root / "effect.json"
            effect = json.loads(effect_path.read_text()) if effect_path.exists() else None
            receipt = None
            if spec["receipt"] != "absent" and effect is not None:
                receipt = dict(stage=index, bundle_digest=bundle if spec["receipt"] == "linked"
                               else "unrelated-bundle", action_id=request["action_id"])
                (stage_root / "receipt.json").write_text(json.dumps(receipt))
                receipt = json.loads((stage_root / "receipt.json").read_text())
            complete = bool(spec["report"] and effect is not None and receipt is not None
                            and receipt["bundle_digest"] == bundle)
            if operator == "trust_done" and spec["report"]:
                complete = bool(effect is not None and spec["model_done"])
            (stage_root / "report.json").write_text(json.dumps(dict(complete=complete)))
            stages.append(dict(**stage, approval=presented, effect=effect, receipt=receipt,
                               complete=json.loads((stage_root / "report.json").read_text())["complete"],
                               support_available=not deny_all))
            for observation in (stage["primary"], stage["corroborator"]):
                if observation is not None:
                    seen.add((observation["source"]["source_id"], json.loads(observation["raw"])["frame_id"]))
        return dict(inputs=json.loads((root / "inputs.json").read_text()), stages=stages)
