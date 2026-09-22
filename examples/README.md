# Examples

This directory contains small inputs that demonstrate how Open Source Compatibility can be used.

## Example configuration

`compatibility.json` supports Python and operating-system requirements plus dependency constraints.

Example dependency constraint:

```json
"pytest": ">=8,<9"
```

Run the checker from the repository root using the CLI documented in the main README. Use JSON output when integrating the result with scripts or CI.
