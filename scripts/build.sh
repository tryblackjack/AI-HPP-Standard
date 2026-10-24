#!/usr/bin/env bash
set -euo pipefail
python3 scripts/validate.py
python3 scripts/check_agentic_safety.py
python3 scripts/check_paf_register.py
python3 scripts/check_discovery_profile.py
python3 scripts/check_implementation_assets.py
python3 scripts/check_replication_profile.py
python3 scripts/check_cyber_containment_profile.py
python3 scripts/check_subject_integrity_profile.py
python3 scripts/check_assurance_protocol.py
python3 scripts/check_artifact_disclosure_profile.py
python3 scripts/check_proportionate_action_profile.py
python3 scripts/check_robot_action_binding_profile.py
python3 scripts/check_evidence_grounding_oversight_profile.py
python3 scripts/check_oversight_boundary.py
python3 scripts/check_release.py
echo "Build checks completed."
