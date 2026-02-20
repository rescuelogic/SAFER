# SAFER Protocol (Open Standard)

**S**ecurity **A**nd **F**ire **E**mergency **R**eports (**SAFER**) is a lightweight, JSON-based message format for reporting life-safety and security events (fire alarm, supervisory, trouble, intrusion, medical/personal emergency, etc.) over modern IP networks.

This repository packages the **SAFER message format** as an open specification, plus **JSON examples** and a **JSON Schema** for validation.

> **Scope note:** SAFER standardizes the *event payload* (the JSON object). Transport (TCP, HTTP, MQTT, syslog, file/print port, etc.), local code compliance, and UL/NFPA listing requirements are out of scope. Implementers are responsible for meeting all applicable safety and regulatory requirements.

## Design goals

- **Human- and machine-readable** (JSON key/value pairs).
- **Extensible**: a small required core with an optional section for richer context.
- **Precise identification** of customer/site, panel/node, and device/point.
- **Backward compatibility** with legacy formats via optional Contact ID fields.
- **Interoperable** across vendors and software stacks.

## Repository layout

- `README.md` – this specification overview
- `schema/safer-event.schema.json` – JSON Schema (Draft 2020-12)
- `examples/` – sample events (minimal + expanded)

## Quick start (minimal event)

A valid SAFER event MUST include the required fields shown below:

```json
{
  "CUSTOMER": "5547785214556987452",
  "PANEL_ID": "Node 01",
  "DEVICE_ID": "22-011",
  "DEVICE_TYPE": "Smoke Detector",
  "DEVICE_LOCATION": "2FL CONF. RM",
  "STATUS": 1,
  "SAFER_ID": {
    "version": "0.1.0",
    "unique_id": "223e4567-e89b-12d3-a456-426614174000"
  }
}
```

## Message envelope

A SAFER event is a single JSON object with these **required** top-level fields:

| Field | Type | Required | Description |
|---|---:|:---:|---|
| `CUSTOMER` | string | ✅ | Customer/site identifier. Use a string (may exceed integer ranges). |
| `PANEL_ID` | string | ✅ | Panel or node identifier (e.g., `Node 01`). |
| `DEVICE_ID` | string | ✅ | Electrical/logical point address (e.g., `N54L32D001`, `01-015`, `22-011`). |
| `DEVICE_TYPE` | string | ✅ | Human-readable device type (e.g., `Smoke Detector`). |
| `DEVICE_LOCATION` | string | ✅ | Installer/programmed location text as shown on-site/panel. |
| `STATUS` | integer | ✅ | Event status code (see below). |
| `SAFER_ID` | object | ✅ | Message identity + versioning (`version`, `unique_id`). |
| `OPTIONAL` | object | ⛔ | Optional extended context (recommended when available). |

### `STATUS` codes

`STATUS` is an integer with the following meanings:

| Code | Meaning |
|---:|---|
| `1` | Active / alarm condition present |
| `2` | Supervisory |
| `3` | Restore (return to normal) |
| `4` | Trouble / fault |
| `5` | Status only (informational) |
| `6` | Previously reported |

### `SAFER_ID`

`SAFER_ID` MUST contain:

- `version` (string): the SAFER message format version, recommended **SemVer** (e.g., `0.1.0`).
- `unique_id` (string): a globally unique identifier for the message, recommended UUID (RFC 4122).

Example:

```json
"SAFER_ID": {
  "version": "0.1.0",
  "unique_id": "223e4567-e89b-12d3-a456-426614174000"
}
```

## OPTIONAL section

`OPTIONAL` is a JSON object for richer context. It MAY contain any of the following keys, and it MAY contain additional vendor-/site-specific keys.

Recommended common keys:

| Field | Type | Description |
|---|---|---|
| `OWNER_LOCATION` | string | More human-friendly location (e.g., “Independent Living Unit 7”). |
| `LOCATION` | string | Coarse location (floor/area). |
| `CONDITION` | string | Condition text (e.g., “Smoke Detected”, “Unauthorized Entry”). |
| `SYSTEM_CATEGORY` | string | Category (Fire Alarm, Burglary, Medical, Personal Emergency, etc.). |
| `DATE` | string (YYYY-MM-DD) | Local date of event. |
| `TIME` | string (HH:MM[:SS]) | Local time of event (24-hour recommended). |
| `PANEL_GPS` | object | GPS at panel (see “Coordinates”). |
| `GPS_COORDINATES` | object | GPS at device/incident location (see “Coordinates”). |
| `ZONE` | object | `{ name, description?, url? }` |
| `GROUP` | object | `{ name, description?, url? }` |
| `CONTACT_ID` | object | Legacy mapping `{ version, code }` |

### Coordinates objects

When used, `PANEL_GPS` and `GPS_COORDINATES` SHOULD be objects shaped like:

```json
{
  "latitude": 37.7749,
  "longitude": -122.4194,
  "altitude": "15m"
}
```

- `latitude` / `longitude` SHOULD be numbers when possible.
- `altitude` MAY be a number (meters) or a string with a unit (e.g., `"15m"`).

## Transport framing recommendations (non-normative)

Because SAFER standardizes payload only, implementations need a framing rule. Common options:

- **NDJSON** (newline-delimited JSON): one JSON object per line.
- HTTP webhook: POST a single JSON object in the request body.
- MQTT: publish the JSON object as message payload.
- TCP stream: prefix with length or delimit with `\n` (avoid ambiguity).

## Validation

Use `schema/safer-event.schema.json` to validate events. The schema enforces the required core and allows additional/unknown keys for forward compatibility.

## Examples

See `examples/`:

- `minimal-fire-alarm.json`
- `full-fire-alarm.json`
- `burglary.json`
- `trouble.json`
- `supervisory.json`
- `restore.json`
- `status-only.json`

## Security considerations

Life-safety and security signals are sensitive. Implementers SHOULD consider:

- encryption in transit (e.g., TLS),
- authentication/authorization for publishers and subscribers,
- network segmentation for life-safety systems,
- input validation and schema checks,
- careful handling of personally identifying information (PII).

## Governance and versioning

- The SAFER payload format uses `SAFER_ID.version`.
- Backward-compatible changes: increment **MINOR** or **PATCH**.
- Backward-incompatible changes: increment **MAJOR** and provide migration notes.

## License

This repository is licensed under the Apache License 2.0. See `LICENSE`.
