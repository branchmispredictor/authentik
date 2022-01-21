"""Test Converter utils"""

from typing import Optional

from attrs import define, field
from cattr.errors import StructureHandlerNotFoundError
from datetime import datetime
from django.test import TestCase

from authentik.lib.utils.converter import from_dict


class TestConverterUtils(TestCase):
    """Test Converter-utils"""

    @define
    class DataClass:
        str_field: str
        datetime_field: datetime
        opt_int_field: Optional[int] = field(default=None)

    def test_valid(self):
        data = {'str_field': 'a', 'datetime_field': datetime.now()}
        result = from_dict(TestConverterUtils.DataClass, data)
        self.assertEqual(result, TestConverterUtils.DataClass(data['str_field'], data['datetime_field'], None))

    def test_missing_required_field(self):
        data = {'str_field': 'a'}
        with self.assertRaises(KeyError):
            result = from_dict(TestConverterUtils.DataClass, data)

    def test_missing_conversion_handler(self):
        data = {'str_field': 'a', 'datetime_field': 1234}
        with self.assertRaises(StructureHandlerNotFoundError):
            result = from_dict(TestConverterUtils.DataClass, data)