# Contributing

Thanks for your interest in improving the SAFER Protocol.

## Ways to contribute

- Propose clarifications or additions to field definitions
- Add or improve examples
- Report interoperability issues
- Improve the JSON Schema
- Add test vectors and validators

## Ground rules

- Keep the required core small and stable.
- Put vendor-/site-specific extensions inside `OPTIONAL` whenever possible.
- Prefer backwards-compatible changes. If a breaking change is necessary, increment `SAFER_ID.version`
  and include migration notes.

## Pull requests

1. Fork the repository and create a feature branch.
2. Update documentation and/or schema.
3. Add or update examples.
4. Ensure examples validate against `schema/safer-event.schema.json`.
5. Open a pull request describing the change and rationale.

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.
