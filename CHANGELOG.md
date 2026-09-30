# Changelog

All notable changes to this project will be documented here.

## [0.4.0] - 2026-09-30

### Added

- Self-contained HTML compatibility reports
- `--html-report PATH` CLI option
- Environment, check-result, and score sections in generated reports
- HTML escaping for dynamic content
- Automatic creation of report output directories
- Focused tests for report generation and CLI integration

## [0.3.0] - 2026-09-26

### Added

- Automatic project metadata detection
- Detection for `pyproject.toml`, `requirements.txt`, `package.json`, and common lockfiles
- CLI support for project detection
- Tests and documentation for project-file discovery

## [0.2.0] - 2026-09-22

### Added

- Dependency version ranges with comma-separated constraints
- Configuration validation for unknown keys and invalid dependency shapes
- Tests for version ranges and validation

## [0.1.0] - 2026-09-20

### Added

- Cross-platform environment detection
- Python minimum and maximum version checks
- Supported operating-system checks
- Installed dependency checks
- Compatibility scoring
- JSON configuration support
- Human-readable CLI output
- JSON report output
- Automated test suite
- GitHub Actions compatibility matrix
- Contribution guidelines
