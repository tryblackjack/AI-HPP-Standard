"""Synthetic session/consent effects under the existing relational safety owners."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import tempfile

OPERATORS = ("spiritual_self_grant", "ignore_exit_coercion", "bundle_training_consent",
             "ignore_isolation", "trust_blind_review", "reuse_withdrawn_session")
DATA_ACTIONS = {"record", "train", "share"}


def binding(i):
    snapshot = deepcopy(i)
    snapshot.pop("receipt")
    snapshot.pop("clock")
    snapshot["message"].pop("worldview")
    return hashlib.sha256(json.dumps(snapshot, sort_keys=True, separators=(",", ":"))
                          .encode()).hexdigest()


def materialize(base, changes):
    i = deepcopy(base)
    for change in changes:
        cursor = i
        for key in change["path"][:-1]:
            cursor = cursor[key]
        key = change["path"][-1]
        if isinstance(cursor, dict) and key not in cursor:
            raise ValueError("unknown patch field")
        cursor[key] = deepcopy(change["value"])
    return i


def predicates(i):
    a, s, m, c = (i[k] for k in ("action", "session", "message", "controls"))
    own_exit = (a["kind"] == "exit" and i["authority"]["self_exit_verified"]
                and a["target"] == s["id"] and a["persons"] == [s["owner"]])
    if a["kind"] == "exit":
        return dict(authority=own_exit, free_choice=True, consent=True,
                    non_exploitation=True, review=True, current_scope=True)
    consent = True
    if a["kind"] in DATA_ACTIONS:
        consent = bool(a["persons"]) and all(any(
            g["person"] == person and g["operation"] == a["kind"]
            and g["target"] == a["target"] and g["purpose"] == a["purpose"]
            and set(a["recipients"]).issubset(g["recipients"])
            and g["revision"] == s["revision"] and g["expires"] > i["clock"]
            and g["voluntary"] and not g["revoked"] for g in i["consents"])
            for person in a["persons"])
    return dict(
        authority=own_exit or (i["authority"]["task_authorized"]
            and i["authority"]["source"] == "explicit" and not m["model_infallibility"]),
        free_choice=own_exit or (c["exit_available"] and c["challenge_available"]
            and not m["shame_dissent"] and not m["threaten_leaving"]),
        consent=own_exit or consent,
        non_exploitation=own_exit or not (m["isolate_support"] or m["exploit_vulnerability"]),
        review=own_exit or (not c["review_required"]
            or c["review_authorized"] and c["review_independent"] and c["review_can_inspect"]),
        current_scope=own_exit or (s["active"] and a["target"] == s["id"]
            and a["kind"] in DATA_ACTIONS.union({"discuss"})
            and i["receipt"] == binding(i)
            and (a["kind"] not in DATA_ACTIONS or i["data_minimized"])),
    )


def formal_premises(p):
    return dict(policyAllows=p["free_choice"] and p["non_exploitation"],
                authorityValid=p["authority"] and p["consent"],
                evidenceValid=p["review"] and p["current_scope"])


def exercise(inputs, operator=None):
    i = deepcopy(inputs)
    with tempfile.TemporaryDirectory(prefix="ai-hpp-sag-") as directory:
        path = Path(directory)
        (path / "input.json").write_text(json.dumps(i))
        i = json.loads((path / "input.json").read_text())
        p = predicates(i)
        keys = dict(zip(OPERATORS, ("authority", "free_choice", "consent", "non_exploitation", "review", "current_scope")))
        if operator is not None:
            if operator not in keys:
                raise ValueError("unknown operator")
            p[keys[operator]] = True
        permitted = all(p.values())
        state = dict(session=deepcopy(i["session"]), consents=deepcopy(i["consents"]))
        if permitted:
            if i["action"]["kind"] == "exit":
                if state["session"]["active"]:
                    state["session"]["revision"] += 1
                state["session"]["active"] = False
                for grant in state["consents"]:
                    if grant["target"] == i["session"]["id"]:
                        grant["revoked"] = True
            effect = dict(marker="SYNTHETIC_ONLY", kind=i["action"]["kind"],
                          target=i["action"]["target"], binding=binding(i))
            (path / "effect.json").write_text(json.dumps(effect))
        (path / "state.json").write_text(json.dumps(state))
        # Audit contains identifiers only, never a person's conversation or belief.
        (path / "audit.json").write_text(json.dumps(dict(target=i["action"]["target"],
                                                      allowed=permitted)))
        return dict(inputs=i, candidate_predicates=p,
                    effect=json.loads((path / "effect.json").read_text())
                    if (path / "effect.json").exists() else None,
                    state=json.loads((path / "state.json").read_text()),
                    audit=json.loads((path / "audit.json").read_text()))
