# SAFER Protocol

Version 1.1 - October 2026

**S**ecurity **A**nd **F**ire **E**mergency **R**eports (**SAFER**) defines a JSON event payload for life-safety and security reports. It gives systems a common way to carry reporting context, point identity, device type, location, and reported condition while preserving useful source information.

SAFER v1.1 is a proposed event-payload specification. Questions and improvements are welcome through [GitHub Issues](https://github.com/rescuelogic/SAFER/issues) and [Pull Requests](https://github.com/rescuelogic/SAFER/pulls).

- [Protocol v1.1](SAFER_Protocol_v1_1.pdf): field definitions, STATUS meanings, and conformance requirements.
- [FAQ v1.1](SAFER_Protocol_FAQ_v1_1.pdf): scope, adoption, and implementation questions.
- [What Does Everybody Know?](What_Does_Everybody_Know.pdf): a plain-language introduction to the idea.

## Purpose and scope

SAFER standardizes the event payload. It does not define transport, pathway supervision, reliability, product listing, regulatory compliance, or emergency response policy. Those responsibilities remain with the surrounding system and applicable requirements.

The five conceptual information roles are reporting system, point identity, device type, location, and reported condition. The v1.1 wire format uses **seven required JSON fields**: `CUSTOMER` and `PANEL_ID` represent reporting context, while `SAFER_ID` supplies version and report-record identity.

A received report may describe activation, restoration, repetition, or a status observation. It does not by itself establish a new physical transition or verify the physical condition. Preserve the distinction between source information, customer-maintained records, derived interpretations, and unknown information.

## Implementing SAFER v1.1

Sections 5, 6, and 12 of the [protocol](SAFER_Protocol_v1_1.pdf) govern required fields, STATUS meanings, and baseline conformance. The companion publications explain the model without changing these requirements.

### Minimal payload

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

### STATUS meanings

| Code | Meaning |
|---:|---|
| 1 | Active |
| 2 | Supervisory |
| 3 | Restore |
| 4 | Trouble |
| 5 | Status only |
| 6 | Previously reported |

These six meanings are retained from v1.0. They encompass conditions, classifications, and reporting relationships; they are not interchangeable with Contact ID qualifiers or RescueLogic Base State and Logical State keys. Separating condition from qualifier is a future design question, not an adopted v1.1 change.

### Optional context and legacy reports

`OPTIONAL` can carry `CONDITION`, `EVENT_TIME`, `SOURCE_FORMAT`, `SOURCE_MESSAGE`, `CONTACT_ID`, and other context described in Section 7 of the specification. `CONDITION` adds descriptive detail without overriding `STATUS`. Prefer ISO 8601 for `EVENT_TIME`.

Contact ID can coexist with SAFER through preservation or translation. Interpret its event code, qualifier, and source context together; do not substitute its qualifier directly for SAFER `STATUS`. Keep original source reports and identify lookup or derived enrichment where practical. Do not invent a device type or location to make an incomplete report pass validation.

### Schema validation and compatibility

The [JSON Schema](schema/safer-event.schema.json) implements the minimal structural checks in specification Appendix A using JSON Schema Draft 2020-12. It checks the seven required fields, version `"1.1"`, a nonempty report identifier, and the six STATUS values. It permits additional properties and requires `OPTIONAL` to be an object when present.

Compared with the previous repository schema, this removes UUID-only and closed-object restrictions. The five descriptive fields must be strings, but the minimal schema does not require them to be nonempty. Earlier payloads must declare their actual version; the v1.1 schema rejects other version declarations.

The specification governs field meaning and optional-field structure. Schema validation alone does not check semantic consistency, physical conditions, correct source interpretation, or identifier uniqueness across reports. Document additional application checks separately from baseline conformance.

### Example payloads

All 12 [JSON examples](examples/) declare version `"1.1"`.

| Example | Purpose |
|---|---|
| [minimal-fire-alarm.json](examples/minimal-fire-alarm.json) | Seven required fields only; STATUS 1 |
| [full-fire-alarm.json](examples/full-fire-alarm.json) | Expanded active report with optional context |
| [burglary.json](examples/burglary.json) | Active intrusion report; STATUS 1 |
| [supervisory.json](examples/supervisory.json) | Supervisory report; STATUS 2 |
| [restore.json](examples/restore.json) | Restoration report; STATUS 3 |
| [trouble.json](examples/trouble.json) | Trouble report with descriptive condition; STATUS 4 |
| [status-only.json](examples/status-only.json) | Status observation; STATUS 5 |
| [previously-reported.json](examples/previously-reported.json) | Repeated valve report; STATUS 6, with a distinct report identifier |
| [protocol-minimal.json](examples/protocol-minimal.json) | Specification Section 8.1 |
| [protocol-with-context.json](examples/protocol-with-context.json) | Section 8.2: EVENT_TIME, SOURCE_FORMAT, and SOURCE_MESSAGE |
| [protocol-supervisory.json](examples/protocol-supervisory.json) | Specification Section 8.3 |
| [protocol-trouble.json](examples/protocol-trouble.json) | Section 8.4: Trouble with Open Circuit detail |

Contact ID strings and example.com URLs in the older expanded examples are illustrative data, not verified adapter mappings or live facility references. Schema acceptance does not verify a Contact ID checksum or its interpretation. A repeated report does not establish a new activation, and descriptive condition text does not override STATUS 6.

## Companion publications

### Understanding event information

| Publication | Focus |
|---|---|
| [What Does Everybody Know?](What_Does_Everybody_Know.pdf) | Discovering common information roles in manufacturer-specific reports |
| [What Is an Alarm Event?](What_Is_an_Alarm_Event.pdf) | A one-page introduction for training and orientation |
| [The Grammar of a Fire Alarm System](The_Grammar_of_a_Fire_Alarm_System.pdf) | Understanding identity, type, location, and condition |

### Architecture and research

| Publication | Focus |
|---|---|
| [Information Infrastructure for Life Safety](Information_Infrastructure_for_Life_Safety_v1_1.pdf) | Transport independence and semantic interoperability |
| [A Minimal Event Information Model - Review Version](SAFER_Minimal_Event_Information_Model_review_version.pdf) | Shorter technical treatment, Revision 0.2 |
| [A Minimal Event Information Model - Full Technical Working Paper](SAFER_Minimal_Event_Information_Model_Full_Technical_Working_Paper.pdf) | Detailed research into the model and its limitations, Revision 0.2 |

“Review Version” identifies the shorter edition of the information-model paper.

### Installation practice and engineering history

| Publication | Focus |
|---|---|
| [The Ordered Fire Alarm System](The_Ordered_Fire_Alarm_System.pdf) | Checking and maintaining installation information and RescueLogic workflows |
| [One Architecture. Many Manufacturers. Decades of Continuity.](RescueLogic_One_Architecture_Engineering_History.pdf) | Dan Horon's firsthand engineering history and preservation of installation knowledge |

## Contributing

Use [Issues](https://github.com/rescuelogic/SAFER/issues) for questions, observations, discrepancies, and proposals. Use [Pull Requests](https://github.com/rescuelogic/SAFER/pulls) for specific changes. Include the document and page or section, your observation, the suggested interpretation, and a supporting example where useful. Remove customer-identifying information from examples.

Contributions can clarify field definitions, improve examples or the schema, report interoperability issues, or provide test vectors and validators.

- Keep the required core small and stable, and put vendor- or site-specific extensions inside `OPTIONAL` whenever possible.
- Prefer backward-compatible changes. Breaking changes require a new major version and migration notes.
- Preserve the defined STATUS meanings and distinguish them from source qualifiers and application display states.
- Preserve source information and uncertainty; do not invent missing device details.

To submit a change:

1. Fork the repository and create a feature branch.
2. Update the relevant documentation or schema and any affected examples.
3. Ensure the examples validate against [the schema](schema/safer-event.schema.json) and remain consistent with the specification.
4. Open a pull request explaining the change and rationale.

By contributing, you agree that your contributions will be licensed under the Apache License 2.0. Direct inquiries may also be sent to Dan Horon at dan@rescuelogic.com or Jeff Horon at jeff@rescuelogic.com.

## Licensing and earlier publications

The SAFER Protocol is published under the [Apache License 2.0](LICENSE). Original protocol copyright © 2024 Dan Horon; U.S. Copyright Registration No. TXu 2-426-289, effective March 7, 2024. Companion publications retain their stated attribution and notices. Publication does not imply endorsement, approval, certification, or listing by NFPA, UL, or another organization.

The [v1.0 specification](SAFER%20v1.0.pdf) and [earlier FAQ](SAFER%20FAQ.pdf) remain available for historical reference. Use the v1.1 publications and current schema for v1.1 implementation.
