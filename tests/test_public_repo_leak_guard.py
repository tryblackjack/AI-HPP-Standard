from scripts import public_repo_leak_guard as guard


def test_public_github_noreply_is_allowed() -> None:
    assert guard.is_allowed_public_email("38202526+tryblackjack@users.noreply.github.com")


def test_github_actions_bot_email_is_allowed() -> None:
    assert guard.is_allowed_public_email("actions@github.com")


def test_personal_email_is_not_allowed() -> None:
    sample = "person" + "@" + "example.com"\n    assert not guard.is_allowed_public_email(sample)


def test_fine_grained_github_token_pattern_is_covered() -> None:
    sample = "github_pat_" + "A" * 24
    assert any(pattern.search(sample) for _, pattern in guard.SENSITIVE_PATTERNS)


def test_huggingface_token_pattern_is_covered() -> None:
    sample = "hf_" + "A" * 24
    assert any(pattern.search(sample) for _, pattern in guard.SENSITIVE_PATTERNS)
