import pytest

from open_source_compatibility.checker import (
    calculate_score,
    check_python,
    run_checks,
    validate_config,
    version_satisfies,
    version_tuple,
)


def test_version_tuple():
    assert version_tuple("3.12.4") == (3, 12, 4)


def test_version_ranges():
    assert version_satisfies("2.5.1", ">=2.0,<3.0")
    assert version_satisfies("8.4.2", "==8.4.2")
    assert not version_satisfies("3.0.0", ">=2.0,<3.0")


def test_python_current_version_is_compatible():
    assert check_python({"min_python": "3.8"}).status == "pass"


def test_python_impossible_minimum_fails():
    assert check_python({"min_python": "99.0"}).status == "fail"


def test_score_calculation():
    report = run_checks({"min_python": "3.8"})
    assert 0 <= report.score <= 100
    assert calculate_score(report.checks) == report.score


def test_unknown_config_key_is_rejected():
    with pytest.raises(ValueError, match="Unknown configuration"):
        validate_config({"mystery": True})


def test_dependencies_must_be_mapping():
    with pytest.raises(ValueError, match="dependencies must be an object"):
        validate_config({"dependencies": []})
