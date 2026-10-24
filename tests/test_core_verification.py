"""Keep the bounded verifier's operational projection tied to the full model."""
import pytest

from scripts.verify_core import MARKER, MODEL, operational_source


def test_verification_preserves_exact_operational_prefix():
    source = MODEL.read_text(encoding="utf-8")
    projection = operational_source(source)
    assert projection == source.split(MARKER)[0] + "}\n"
    assert "action mutant" not in projection
    assert "  run " not in projection


@pytest.mark.parametrize("change", ["missing_boundary", "duplicate_boundary",
                                   "operational_suffix", "missing_aggregate"])
def test_projection_refuses_ambiguous_or_incomplete_partition(change):
    source = MODEL.read_text(encoding="utf-8")
    if change == "missing_boundary":
        source = source.replace(MARKER, "")
    elif change == "duplicate_boundary":
        source += MARKER
    elif change == "operational_suffix":
        source += "  action hiddenOperationalGate: bool = false\n"
    else:
        source = source.replace("  val allCoreInvariants:", "  val missingAggregate:")
    with pytest.raises(ValueError):
        operational_source(source)
