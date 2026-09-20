# Contributing

Thanks for your interest in Open Source Compatibility.

## Getting started

1. Fork the repository.
2. Create a feature branch.
3. Install the project with development dependencies:

```bash
python -m pip install -e ".[dev]"
```

4. Make your changes.
5. Run the test suite:

```bash
pytest
```

6. Open a pull request explaining what changed and why.

## Good contributions

Useful contributions include:

- New compatibility checks
- Bug fixes
- Tests
- Documentation improvements
- Cross-platform fixes
- Better error messages

## Pull request guidelines

Keep each pull request focused on one change where possible. Add or update tests for behavior changes. Avoid unrelated formatting changes.

## Reporting bugs

When opening an issue, include:

- Operating system
- Python version
- Command you ran
- Expected behavior
- Actual behavior
- Error output if available

## Code style

Prefer clear, small functions with type hints. Keep the core checker dependency-light.
