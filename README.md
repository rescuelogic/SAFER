# SAFER Protocol
Version 1.0 - February 2026  
Open specification published under the Apache License 2.0  

[Access the full specification document](https://github.com/rescuelogic/SAFER/blob/main/SAFER%20v1.0.pdf)

[Read the FAQ](https://github.com/rescuelogic/SAFER/blob/main/SAFER%20FAQ.pdf)

## Overview

The **S**ecurity **A**nd **F**ire **E**mergency **R**eports (**SAFER**) Protocol defines a structured, JSON-based message format for reporting life-safety and security events across modern IP networks.

The objective of SAFER is to provide a clear, extensible, and interoperable structure for representing alarm events in contemporary networked environments.

## Scope

SAFER defines:
-	Required and optional JSON fields for event representation
-	Version identification within each message
-	A structure supporting extensibility without breaking compatibility

SAFER does not define:
-	Transmission methods (TCP, UDP, MQTT, etc.)
-	Supervision models or network performance requirements
-	Product listing or certification requirements
-	Compliance authority

SAFER standardizes the *event payload only*. It does not define transport mechanisms, pathway supervision, listing requirements, or regulatory compliance criteria. Those remain governed by applicable codes, standards, and product certifications.

Implementers are responsible for ensuring conformance with applicable standards and regulatory frameworks.

## Design Principles

The SAFER Protocol is guided by the following principles:
-	Structured Representation – Human- and machine-readable JSON format
-	Clear Identification – Separation of customer, panel, device, and condition
-	Extensibility – Optional fields may be added without invalidating existing implementations
-	Backward Reference Capability – Legacy formats (e.g., Contact ID) may be embedded as optional reference fields
-	Version Control – Each message includes a version identifier to support compatibility management

Example Event Structure:
```
{
  "CUSTOMER": "1234",
  "PANEL_ID": "Node 01",
  "DEVICE_ID": "01-015",
  "DEVICE_TYPE": "Smoke Detector",
  "DEVICE_LOCATION": "2FL CONF RM",
  "STATUS": 1,
  "SAFER_ID": {
    "version": "1.0",
    "unique_id": "123e4567-e89b-12d3-a456-426614174000"
  }
}
```

See the [full specification document](https://github.com/rescuelogic/SAFER/blob/main/SAFER%20v1.0.pdf) for required fields, optional structures, and implementation guidance.

## Governance and Stewardship

SAFER is published as an open specification.

Future revisions may incorporate implementation feedback, clarifications, and interoperability considerations. Governance may evolve through an open working group, collaborative industry participation, or standards development engagement.

No single entity controls adoption.

Implementers are encouraged to reference version identifiers to ensure compatibility with the applicable specification revision.

## Licensing
Copyright © 2024 Dan Horon  
U.S. Copyright Registration No. TXu 2-426-289  
Effective March 7, 2024  
Licensed under the Apache License, Version 2.0.  
Use of this specification is subject to the terms of the Apache 2.0 License.

## Questions, Contact, and Feedback

[Read the FAQ](https://github.com/rescuelogic/SAFER/blob/main/SAFER%20FAQ.pdf)  

Questions or implementation feedback regarding this specification may be directed to:

Dan Horon
dan@rescuelogic.com

Jeff Horon
jeff@rescuelogic.com

Publication of this document does not imply endorsement by NFPA, UL, or any standards development organization.
