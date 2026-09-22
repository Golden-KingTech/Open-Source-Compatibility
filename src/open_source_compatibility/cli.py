from __future__ import annotations

import argparse
import json

from .checker import load_config, run_checks


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="osc-check",
        description="Check basic project compatibility for the current environment.",
    )
    parser.add_argument(
        "--config",
        help="Path to a JSON compatibility configuration file.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the report as JSON.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    config = load_config(args.config) if args.config else {}
    report = run_checks(config)

    if args.json:
        print(json.dumps(report.to_dict(), indent=2))
    else:
        print(f"OS: {report.os} {report.os_release}")
        print(f"Architecture: {report.architecture}")
        print(f"Python: {report.python_version}")
        print()
        print("Compatibility checks:")
        for check in report.checks:
            symbol = {"pass": "[PASS]", "warn": "[WARN]", "fail": "[FAIL]"}.get(check.status, "[?]")
            print(f"{symbol} {check.name}: {check.message}")
        print()
        print(f"Compatibility score: {report.score}%")

    return 1 if any(check.status == "fail" for check in report.checks) else 0


if __name__ == "__main__":
    raise SystemExit(main())
