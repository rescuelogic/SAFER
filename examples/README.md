# SAFER v1.1 examples

All JSON files here use version `"1.1"` and validate against the [baseline schema](../schema/safer-event.schema.json).

| Example | Purpose |
|---|---|
| [minimal-fire-alarm.json](minimal-fire-alarm.json) | Seven required fields only; STATUS 1 |
| [full-fire-alarm.json](full-fire-alarm.json) | Expanded active report with optional context |
| [burglary.json](burglary.json) | Active intrusion report; STATUS 1 |
| [supervisory.json](supervisory.json) | Supervisory report; STATUS 2 |
| [restore.json](restore.json) | Restoration report; STATUS 3 |
| [trouble.json](trouble.json) | Trouble report with descriptive condition; STATUS 4 |
| [status-only.json](status-only.json) | Status observation; STATUS 5 |
| [previously-reported.json](previously-reported.json) | Repeated valve report; STATUS 6, with a distinct report identifier |
| [protocol-minimal.json](protocol-minimal.json) | Specification Section 8.1 |
| [protocol-with-context.json](protocol-with-context.json) | Section 8.2: EVENT_TIME, SOURCE_FORMAT, and SOURCE_MESSAGE |
| [protocol-supervisory.json](protocol-supervisory.json) | Specification Section 8.3 |
| [protocol-trouble.json](protocol-trouble.json) | Section 8.4: Trouble with Open Circuit detail |

The Contact ID strings and example.com URLs in the older expanded examples are
illustrative data, not verified adapter mappings or live facility references.
Schema acceptance does not verify a Contact ID checksum or its interpretation.
Interpret source event codes, qualifiers, and configuration together when building
an adapter. A repeated report does not establish a new activation, and its
descriptive condition does not override STATUS 6.
