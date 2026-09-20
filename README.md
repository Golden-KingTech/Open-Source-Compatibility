# Open Source Compatibility

A lightweight command-line tool for checking whether a project is compatible with the environment it is running in.

Version **0.1.0** checks:

- Operating system
- Python version
- Installed dependency versions
- Overall compatibility score
- Human-readable or JSON output

## Why this project exists

Open-source projects often work on one machine but fail on another because of operating-system differences, unsupported Python versions, or missing dependencies. Open Source Compatibility provides a small, portable checker that maintainers can include in their projects or CI workflows.

## Installation

Clone the repository:

```bash
git clone https://github.com/Golden-KingTech/Open-Source-Compatibility.git
cd Open-Source-Compatibility
```

Install in editable mode:

```bash
python -m pip install -e .
```

For development and testing:

```bash
python -m pip install -e ".[dev]"
```

## Usage

Run a basic environment check:

```bash
osc-check
```

Use a configuration file:

```bash
osc-check --config examples/sample-config.json
```

Return machine-readable output:

```bash
osc-check --config examples/sample-config.json --json
```

Example output:

```text
OS: Windows 11
Architecture: AMD64
Python: 3.13.2

Compatibility checks:
✓ Python: Python 3.13.2 is compatible.
✓ Operating system: Windows is supported.

Compatibility score: 100%
```

## Configuration

Configuration uses JSON:

```json
{
  "min_python": "3.10",
  "max_python": "3.14",
  "supported_os": ["Windows", "Linux", "Darwin"],
  "dependencies": {
    "pytest": "8.4.2"
  }
}
```

Dependency versions are exact matches in v0.1. More flexible version ranges are planned for a future release.

## Testing

Run:

```bash
pytest
```

GitHub Actions automatically tests supported Python versions on Windows, Ubuntu, and macOS.

## Roadmap

- **v0.1** — OS, Python, dependency checks, CLI, JSON output
- **v0.2** — Version ranges and richer configuration validation
- **v0.3** — Project file detection and automated suggestions
- **v0.4** — HTML compatibility reports
- **v1.0** — Stable plugin-friendly compatibility framework

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License. See [LICENSE](LICENSE).
