from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any


@dataclass
class DetectedProjectFile:
    path: str
    kind: str
    runtime: str | None
    dependencies: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _requirements(path: Path) -> list[str]:
    names: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith(("-", ".")):
            continue
        name = re.split(r"[<>=!~;\s\[]", line, maxsplit=1)[0].strip()
        if name:
            names.append(name)
    return names


def _package_json(path: Path) -> tuple[str | None, list[str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    runtime = data.get("engines", {}).get("node")
    deps = sorted(set(data.get("dependencies", {})) | set(data.get("devDependencies", {})))
    return runtime, deps


def _pyproject(path: Path) -> tuple[str | None, list[str]]:
    # Keep the core package dependency-free. Extract common PEP 621 fields conservatively.
    text = path.read_text(encoding="utf-8")
    runtime_match = re.search(r'^requires-python\s*=\s*["\']([^"\']+)["\']', text, re.MULTILINE)
    deps_match = re.search(r"^dependencies\s*=\s*\[(.*?)\]", text, re.MULTILINE | re.DOTALL)
    deps: list[str] = []
    if deps_match:
        for value in re.findall(r'["\']([^"\']+)["\']', deps_match.group(1)):
            name = re.split(r"[<>=!~;\s\[]", value, maxsplit=1)[0].strip()
            if name:
                deps.append(name)
    return runtime_match.group(1) if runtime_match else None, deps


def detect_project_files(root: str | Path = ".") -> list[DetectedProjectFile]:
    root_path = Path(root)
    found: list[DetectedProjectFile] = []

    pyproject = root_path / "pyproject.toml"
    if pyproject.is_file():
        runtime, deps = _pyproject(pyproject)
        found.append(DetectedProjectFile("pyproject.toml", "python", runtime, deps))

    requirements = root_path / "requirements.txt"
    if requirements.is_file():
        found.append(DetectedProjectFile("requirements.txt", "python", None, _requirements(requirements)))

    package_json = root_path / "package.json"
    if package_json.is_file():
        runtime, deps = _package_json(package_json)
        found.append(DetectedProjectFile("package.json", "node", runtime, deps))

    lockfiles = {
        "package-lock.json": "npm lockfile",
        "pnpm-lock.yaml": "pnpm lockfile",
        "yarn.lock": "yarn lockfile",
        "uv.lock": "uv lockfile",
        "poetry.lock": "poetry lockfile",
    }
    for filename, kind in lockfiles.items():
        if (root_path / filename).is_file():
            found.append(DetectedProjectFile(filename, kind, None, []))

    return found
