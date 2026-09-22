# Open Source Compatibility — Project Overview

## Purpose
Open Source Compatibility is a lightweight CLI that helps developers check whether their environment matches a project's requirements before they spend time debugging setup failures.

## Problem
Open-source projects run across different operating systems, Python versions, architectures, and dependency versions. A project can fail before it starts simply because a contributor's environment does not match the supported configuration.

## Solution
The tool performs repeatable compatibility checks and returns a clear score and actionable results. It supports human-readable CLI output and machine-readable JSON for CI and automation.

## Current capabilities
- Detect operating system and architecture
- Check supported Python versions
- Check installed dependency versions
- Evaluate simple version constraints
- Validate compatibility configuration
- Produce a compatibility score
- Output results as CLI text or JSON
- Run automated tests across major operating systems

## Roadmap
1. Detect common project files automatically.
2. Generate useful compatibility suggestions.
3. Produce standalone HTML reports.
4. Expand language/ecosystem support.
5. Stabilize a plugin-friendly API.

## Open-source goals
The project is intended to stay small, understandable, testable, and easy for first-time contributors to improve. Features should solve real compatibility problems rather than exist only to increase project size.
