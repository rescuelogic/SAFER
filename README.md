# SAFER Protocol

Version 1.1 - October 2026

**S**ecurity **A**nd **F**ire **E**mergency **R**eports (**SAFER**) defines a JSON event payload for life-safety and security reports. It gives systems a common way to carry reporting context, point identity, device type, location, and reported condition while preserving useful source information.

SAFER v1.1 is a proposed event-payload specification. Technical discussion and suggested improvements are welcome through [GitHub Issues](https://github.com/rescuelogic/SAFER/issues) and [Pull Requests](https://github.com/rescuelogic/SAFER/pulls).

## Start here

- [What Does Everybody Know?](What_Does_Everybody_Know.pdf) explains how common information roles emerge from different manufacturers' reports.
- [SAFER Protocol v1.1](SAFER_Protocol_v1_1.pdf) defines the fields, STATUS meanings, and baseline conformance rules.
- [SAFER Protocol FAQ v1.1](SAFER_Protocol_FAQ_v1_1.pdf) answers scope, adoption, and implementation questions.
- [Document map](DOCUMENT_MAP.md) guides readers through the complete publication collection.
- Developers can start with the [schema](schema/safer-event.schema.json) and [example payloads](examples/README.md).

## Scope and information model

SAFER standardizes the event payload. It does not define transport, pathway supervision, reliability, product listing, regulatory compliance, or emergency response policy. Those responsibilities remain with the surrounding system and applicable requirements.

The five conceptual information roles are reporting system, point identity, device type, location, and reported condition. The v1.1 wire format uses **seven required JSON fields**: reporting context is represented by `CUSTOMER` and `PANEL_ID`, and `SAFER_ID` supplies version and report-record identity.

A received report may describe activation, restoration, repetition, or a status observation. It does not by itself establish a new physical transition or verify the physical condition. Preserve the distinction between source information, customer-maintained records, derived interpretations, and unknown information.

## Minimal event

```json
{
  "CUSTOMER": "1234",
  "PANEL_ID": "Node 01",
  "DEVICE_ID": "L1S067",
  "DEVICE_TYPE": "Smoke Detector",
  "DEVICE_LOCATION": "Classroom 4 West",
  "STATUS": 1,
  "SAFER_ID": {
    "version": "1.1",
    "unique_id": "123e4567-e89b-12d3-a456-426614174000"
  }
}
```

The five descriptive fields are strings, `STATUS` is an integer, and `SAFER_ID` is an object containing `version` and `unique_id`. For baseline v1.1, the version is exactly `"1.1"` and the identifier is a nonempty string. UUIDs are useful but are not required; the issuer is responsible for identifier uniqueness.

## STATUS meanings

| Code | Meaning |
|---:|---|
| 1 | Active |
| 2 | Supervisory |
| 3 | Restore |
| 4 | Trouble |
| 5 | Status only |
| 6 | Previously reported |

These six meanings are retained from v1.0. They encompass conditions, classifications, and reporting relationships; they are not interchangeable with Contact ID qualifiers or RescueLogic Base State and Logical State keys. Separating condition from qualifier is a future design question, not an adopted v1.1 change.

## Optional context and legacy reports

`OPTIONAL` can carry `CONDITION`, `EVENT_TIME`, `SOURCE_FORMAT`, `SOURCE_MESSAGE`, `CONTACT_ID`, and other context described in Section 7 of the specification. `CONDITION` adds descriptive detail without overriding `STATUS`. Prefer ISO 8601 for `EVENT_TIME`.

Contact ID can coexist with SAFER through preservation or translation. Interpret its event code, qualifier, and source context together; do not substitute its qualifier directly for SAFER `STATUS`. Keep original source reports and identify lookup or derived enrichment where practical. Do not invent a device type or location to make an incomplete report pass validation.

## Validation

The [JSON Schema](schema/safer-event.schema.json) implements the minimal structural checks in specification Appendix A using JSON Schema Draft 2020-12. It permits additional properties, requires `OPTIONAL` to be an object when present, and checks the seven required fields, v1.1 version, nonempty identifier, and six STATUS values.

The specification governs field meaning and optional-field structure. Schema validation alone does not check semantic consistency, physical conditions, correct source interpretation, or identifier uniqueness across reports. Applications may apply documented additional checks.

See [CHANGELOG.md](CHANGELOG.md) for the changes from the previous repository schema, including removal of UUID-only and closed-object restrictions.

## How to contribute

Use [Issues](https://github.com/rescuelogic/SAFER/issues) for questions, observations, discrepancies, and proposals. Use [Pull Requests](https://github.com/rescuelogic/SAFER/pulls) for specific suggested changes. Include the document and page or section, your observation, the suggested interpretation, and a supporting example where useful. Remove customer-identifying information from examples.

See [CONTRIBUTING.md](CONTRIBUTING.md) for validation and compatibility guidance. Direct inquiries may also be sent to Dan Horon at dan@rescuelogic.com or Jeff Horon at jeff@rescuelogic.com.

## Licensing and earlier publications

The SAFER Protocol is published under the [Apache License 2.0](LICENSE). Original protocol copyright © 2024 Dan Horon; U.S. Copyright Registration No. TXu 2-426-289, effective March 7, 2024. Companion publications retain their stated attribution and notices. Publication does not imply endorsement, approval, certification, or listing by NFPA, UL, or another organization.

The [v1.0 specification](SAFER%20v1.0.pdf) and [earlier FAQ](SAFER%20FAQ.pdf) remain available for historical reference. Use the v1.1 publications and current schema for v1.1 implementation.
