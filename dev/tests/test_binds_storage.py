import unittest
from unittest import mock
import io

from dev.src.binds_storage import BindsStorage

class TestBindsStorage(unittest.TestCase):
    def setUp(self):
        self.storage = BindsStorage()
        self.storage._binds = {
            "path/foo": "12 34 56",
            "path/bar": "67 89 90"
            }

    def test_add_should_add_value_to_dictionary(self):
        self.storage.add("some/path", "120 120 120")
        expected = {
            "some/path": "120 120 120",
            "path/foo": "12 34 56",
            "path/bar": "67 89 90"
            }
        self.assertEqual(expected, self.storage._binds)

    def test_get_should_return_proper_value_for_given_key(self):
        expected = "12 34 56"
        result = self.storage.get("path/foo")
        self.assertEqual(expected, result)

    def test_get_should_return_none(self):
        self.assertIsNone(self.storage.get("non_existing_key"))

    def test_serialize_should_properly_call_write_method(self):
        mock_open = mock.mock_open()
        with mock.patch("dev.src.binds_storage.open", mock_open, create=True):
            self.storage.serialize()
            handle = mock_open()
            handle.write.assert_any_call("path/foo:12 34 56\n")

    def test_deserialize_should_complement_dictionary(self):
        file_lines = [
            "path/foo:12 34 56",
            "path/bar:78 90 12",
            "path/baz:67 89 19",
        ]
        with mock.patch("dev.src.binds_storage.open") as mocked_open:
            mocked_open.return_value = io.StringIO("\n".join(file_lines))
            self.storage._deserialize()
            expected = {
                "path/foo": "12 34 56",
                "path/bar": "78 90 12",
                "path/baz": "67 89 19",
                }
            self.assertEqual(expected, self.storage._binds)

if __name__ == '__main__':
    unittest.main()
