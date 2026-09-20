from __future__ import annotations

import importlib.metadata
import json
import platform
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any


@dataclass
class CheckResult:
    name: str
    status: str
    message: str


@dataclass
class CompatibilityReport:
    os: str
    os_release: str
    architecture: str
    python_version: str
    checks: list[CheckResult]
    score: int

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        return data


def get_environment() -> dict[str, str]:
    return {
        "os": platform.system() or "Unknown",
        "os_release": platform.release() or "Unknown",
        "architecture": platform.machine() or "Unknown",
        "python_version": platform.python_version(),
    }


def version_tuple(version: str) -> tuple[int, ...]:
    parts: list[int] = []
    for piece in version.split("."):
        digits = "".join(ch for ch in piece if ch.isdigit())
        if not digits:
            break
        parts.append(int(digits))
    return tuple(parts)


def check_python(config: dict[str, Any]) -> CheckResult:
    current = sys.version_info[:3]
    minimum = config.get("min_python")
    maximum = config.get("max_python")

    if minimum and current < version_tuple(str(minimum)):
        return CheckResult(
            "Python",
            "fail",
            f"Python {platform.python_version()} is below minimum {minimum}.",
        )

    if maximum and current > version_tuple(str(maximum)):
        return CheckResult(
            "Python",
            "fail",
            f"Python {platform.python_version()} is above maximum {maximum}.",
        )

    return CheckResult(
        "Python",
        "pass",
        f"Python {platform.python_version()} is compatible.",
    )


def check_os(config: dict[str, Any]) -> CheckResult:
    supported = [str(item).lower() for item in config.get("supported_os", [])]
    current = (platform.system() or "Unknown").lower()

    if supported and current not in supported:
        return CheckResult(
            "Operating system",
            "fail",
            f"{platform.system()} is not listed in supported_os.",
        )

    return CheckResult(
        "Operating system",
        "pass",
        f"{platform.system()} is supported.",
    )


def check_dependencies(config: dict[str, Any]) -> list[CheckResult]:
    results: list[CheckResult] = []
    dependencies = config.get("dependencies", {})

    for package, required_version in dependencies.items():
        try:
            installed = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            results.append(
                CheckResult(package, "fail", f"{package} is not installed.")
            )
            continue

        if required_version and installed != str(required_version):
            results.append(
                CheckResult(
                    package,
                    "warn",
                    f"Installed {installed}; config requests {required_version}.",
                )
            )
        else:
            results.append(
                CheckResult(package, "pass", f"Installed version {installed}.")
            )

    return results


def calculate_score(checks: list[CheckResult]) -> int:
    if not checks:
        return 100

    weights = {"pass": 1.0, "warn": 0.5, "fail": 0.0}
    total = sum(weights.get(check.status, 0.0) for check in checks)
    return round((total / len(checks)) * 100)


def run_checks(config: dict[str, Any] | None = None) -> CompatibilityReport:
    config = config or {}
    env = get_environment()

    checks = [check_python(config), check_os(config)]
    checks.extend(check_dependencies(config))

    return CompatibilityReport(
        os=env["os"],
        os_release=env["os_release"],
        architecture=env["architecture"],
        python_version=env["python_version"],
        checks=checks,
        score=calculate_score(checks),
    )


def load_config(path: str | Path) -> dict[str, Any]:
    config_path = Path(path)
    with config_path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, dict):
        raise ValueError("Configuration root must be a JSON object.")

    return data
