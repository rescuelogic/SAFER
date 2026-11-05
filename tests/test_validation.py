"""Baseline conformance checks from SAFER v1.1 Section 12 and Appendix A."""

import copy
import json
from pathlib import Path
import re
import unittest

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / 'schema/safer-event.schema.json').read_text(encoding='utf-8'))
VALIDATOR = Draft202012Validator(SCHEMA)
MINIMAL = json.loads((ROOT / 'examples/protocol-minimal.json').read_text(encoding='utf-8'))


class BaselineConformance(unittest.TestCase):
    def test_schema_is_valid(self):
        Draft202012Validator.check_schema(SCHEMA)

    def test_all_examples_and_status_coverage(self):
        statuses = set()
        for path in sorted((ROOT / 'examples').glob('*.json')):
            with self.subTest(example=path.name):
                event = json.loads(path.read_text(encoding='utf-8'))
                VALIDATOR.validate(event)
                statuses.add(event['STATUS'])
        self.assertEqual(statuses, {1, 2, 3, 4, 5, 6})

    def test_readme_example(self):
        text = (ROOT / 'README.md').read_text(encoding='utf-8-sig')
        examples = re.findall(r'```json\s*(.*?)```', text, re.S)
        self.assertTrue(examples)
        for example in examples:
            event = json.loads(example)
            VALIDATOR.validate(event)
            self.assertEqual(event, MINIMAL)

    def test_required_fields(self):
        for field in SCHEMA['required']:
            with self.subTest(field=field):
                event = copy.deepcopy(MINIMAL)
                del event[field]
                self.assertFalse(VALIDATOR.is_valid(event))
        for field in ('version', 'unique_id'):
            with self.subTest(identity_field=field):
                event = copy.deepcopy(MINIMAL)
                del event['SAFER_ID'][field]
                self.assertFalse(VALIDATOR.is_valid(event))

    def test_status_values_and_types(self):
        for status in (1, 2, 3, 4, 5, 6):
            self.assertTrue(VALIDATOR.is_valid(dict(MINIMAL, STATUS=status)))
        for status in (0, 7, 9, -1, 1.5, '1', True, None):
            with self.subTest(status=status):
                self.assertFalse(VALIDATOR.is_valid(dict(MINIMAL, STATUS=status)))

    def test_version(self):
        for version in ('0.0', '0.1.0', '1.0', '1.1.0', '', 1.1, None):
            with self.subTest(version=version):
                event = copy.deepcopy(MINIMAL)
                event['SAFER_ID']['version'] = version
                self.assertFalse(VALIDATOR.is_valid(event))

    def test_report_identifier(self):
        for identifier, valid in [('panel-01-report-00042', True), ('', False), (42, False), (None, False)]:
            with self.subTest(identifier=identifier):
                event = copy.deepcopy(MINIMAL)
                event['SAFER_ID']['unique_id'] = identifier
                self.assertEqual(VALIDATOR.is_valid(event), valid)

    def test_extensions(self):
        event = copy.deepcopy(MINIMAL)
        event['vendor_extension'] = {'context': 'example'}
        event['SAFER_ID']['issuer'] = 'example'
        event['OPTIONAL'] = {
            'UNKNOWN_EXTENSION': {'value': 42},
            'CONTACT_ID': {'version': 'SIA DC-05', 'code': '1234181101010158'},
            'SOURCE_MESSAGE': 'N01-L1:067 ALARM ON PHOTO',
        }
        VALIDATOR.validate(event)
        for optional in (None, [], 'context', 42):
            event['OPTIONAL'] = optional
            self.assertFalse(VALIDATOR.is_valid(event))

    def test_descriptive_field_types(self):
        for field in ('CUSTOMER', 'PANEL_ID', 'DEVICE_ID', 'DEVICE_TYPE', 'DEVICE_LOCATION'):
            with self.subTest(field=field):
                event = copy.deepcopy(MINIMAL)
                event[field] = 123
                self.assertFalse(VALIDATOR.is_valid(event))
                # Appendix A checks type, not whether a description is known or verified.
                event[field] = ''
                self.assertTrue(VALIDATOR.is_valid(event))

    def test_malformed_json(self):
        with self.assertRaises(json.JSONDecodeError):
            json.loads('{"CUSTOMER": "1234",}')


if __name__ == '__main__':
    unittest.main()
