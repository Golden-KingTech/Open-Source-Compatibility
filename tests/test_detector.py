from open_source_compatibility.detector import detect_project_files


def test_detects_requirements(tmp_path):
    (tmp_path / "requirements.txt").write_text("pytest>=8\nrequests==2.32.0\n", encoding="utf-8")
    found = detect_project_files(tmp_path)
    assert len(found) == 1
    assert found[0].path == "requirements.txt"
    assert found[0].dependencies == ["pytest", "requests"]


def test_detects_package_json(tmp_path):
    (tmp_path / "package.json").write_text(
        '{"engines":{"node":">=20"},"dependencies":{"react":"^19"},"devDependencies":{"vite":"^7"}}',
        encoding="utf-8",
    )
    found = detect_project_files(tmp_path)
    assert found[0].kind == "node"
    assert found[0].runtime == ">=20"
    assert found[0].dependencies == ["react", "vite"]


def test_detects_pyproject_runtime(tmp_path):
    (tmp_path / "pyproject.toml").write_text(
        '[project]\nrequires-python = ">=3.11"\ndependencies = ["requests>=2", "rich"]\n',
        encoding="utf-8",
    )
    found = detect_project_files(tmp_path)
    assert found[0].runtime == ">=3.11"
    assert found[0].dependencies == ["requests", "rich"]


def test_missing_files_is_safe(tmp_path):
    assert detect_project_files(tmp_path) == []
