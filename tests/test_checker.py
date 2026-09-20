from open_source_compatibility.checker import (
    calculate_score,
    check_python,
    run_checks,
    version_tuple,
)


def test_version_tuple():
    assert version_tuple("3.12.4") == (3, 12, 4)


def test_python_current_version_is_compatible():
    result = check_python({"min_python": "3.8"})
    assert result.status == "pass"


def test_python_impossible_minimum_fails():
    result = check_python({"min_python": "99.0"})
    assert result.status == "fail"


def test_score_calculation():
    report = run_checks({"min_python": "3.8"})
    assert 0 <= report.score <= 100
    assert calculate_score(report.checks) == report.score
