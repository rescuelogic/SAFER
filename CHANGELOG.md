# Changes

## 1.1 publication update - 2026-11-05

- Publish the October 2026 protocol and FAQ, educational companions, architecture companion, Revision 0.2 technical papers, and engineering history.
- Add a document map and contribution guidance; preserve the original v1.0 and earlier FAQ URLs as historical references.
- Remove obsolete publication-status labels from the supplied PDFs and metadata while preserving version numbers, revision dates, and third-party reference titles.
- Align the JSON Schema with Protocol v1.1 Appendix A: require version `"1.1"`, accept any nonempty report identifier, and allow extension properties. The five descriptive fields require strings; the minimal schema does not impose a nonempty constraint on them.
- Replace the former optional-field validation restrictions with Appendix A's minimal object check. The specification still governs optional-field meaning and structure.
- Update existing example version identifiers from `"0.1.0"` to `"1.1"`, make the minimal example contain only required fields, add the four specification examples, and cover STATUS 6 (Previously reported).
- Add validation tests for the schema, examples, required fields, version and identifier rules, all STATUS values, malformed JSON, and extensions.

The seven-field structure and six STATUS meanings remain unchanged. Earlier payloads
must declare their actual version; the v1.1 schema intentionally rejects other
version declarations. Separating reported condition from event qualifier remains
a future design question.
