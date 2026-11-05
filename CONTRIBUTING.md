# Contributing

Thanks for your interest in improving the SAFER Protocol.

## Ways to contribute

Use [Issues](https://github.com/rescuelogic/SAFER/issues) for questions, observations,
discrepancies, and proposals. Use [Pull Requests](https://github.com/rescuelogic/SAFER/pulls)
for specific changes. Include the document and page or section, your observation,
the suggested interpretation, and a supporting example when useful. Remove
customer-identifying information from examples.

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
- Keep the six v1.1 STATUS meanings distinct from Contact ID qualifiers and application display states.
- Treat condition/qualifier separation as a future design proposal, not a v1.1 requirement.
- Preserve source information and uncertainty; do not invent missing device details.

## Pull requests

1. Fork the repository and create a feature branch.
2. Update documentation and/or schema.
3. Add or update examples.
4. Ensure examples validate against `schema/safer-event.schema.json`.
5. Open a pull request describing the change and rationale.

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.

## Running the checks

With Python 3.10 or newer:

```sh
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
```

The schema follows the minimal structural profile in Protocol v1.1 Appendix A.
Keep the schema, examples, and specification consistent. Document any additional
application validation separately from baseline conformance.
