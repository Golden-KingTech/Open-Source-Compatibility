from pathlib import Path

from open_source_compatibility.checker import CheckResult, CompatibilityReport
from open_source_compatibility.reporting import render_html_report, write_html_report


def sample_report() -> CompatibilityReport:
    return CompatibilityReport(
        os="Linux",
        os_release="6.8",
        architecture="x86_64",
        python_version="3.12.3",
        checks=[
            CheckResult("Python", "pass", "Python is compatible."),
            CheckResult("example<package>", "warn", "Installed 1.0; requirement is >=2.0."),
        ],
        score=75,
    )


def test_render_html_report_contains_environment_and_checks():
    html = render_html_report(sample_report())

    assert "<!doctype html>" in html
    assert "Compatibility score: 75%" in html
    assert "Linux 6.8" in html
    assert "x86_64" in html
    assert "3.12.3" in html
    assert "Python is compatible." in html


def test_render_html_report_escapes_dynamic_content():
    html = render_html_report(sample_report())

    assert "example&lt;package&gt;" in html
    assert "example<package>" not in html


def test_write_html_report_creates_parent_directories(tmp_path: Path):
    output = tmp_path / "artifacts" / "compatibility.html"

    result = write_html_report(sample_report(), output)

    assert result == output
    assert output.exists()
    assert "Compatibility score: 75%" in output.read_text(encoding="utf-8")
