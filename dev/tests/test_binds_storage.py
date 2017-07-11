import unittest
from unittest import mock
import io

from dev.src.binds_storage import BindsStorage

class TestBindsStorage(unittest.TestCase):
    def test_add_should_add_value_to_dictionary(self):
        storage = BindsStorage()
        storage.add("some/path", "120 120 120")
        expected = {
            "some/path": "120 120 120",
            }
        self.assertEqual(expected, storage._binds)

    def test_get_should_return_proper_value_for_given_key(self):
        storage = BindsStorage()
        storage._binds = {
            "some/path": "120 120 120",
            }
        self.assertEqual("120 120 120", storage.get("some/path"))

    def test_get_should_return_none(self):
        storage = BindsStorage()
        self.assertIsNone(storage.get("non_existing_key"))

    def test_serialize_should_properly_call_write_method(self):
        storage = BindsStorage()
        storage._binds = {
            "path/foo": "12 34 56",
            "path/bar": "67 89 90"
            }
        m = mock.mock_open()
        with mock.patch("dev.src.binds_storage.open", m, create=True):
            storage.serialize()
            handle = m()
            handle.write.assert_any_call("path/foo:12 34 56\n")

    def test_deserialize_should_complement_dictionary(self):
        storage = BindsStorage()
        file_lines = [
            "some/path/foo:12 34 56",
            "some/path/bar:78 90 12",
            "path/baz:67 89 19",
        ]

        with mock.patch("dev.src.binds_storage.open") as mocked_open:
            mocked_open.return_value = io.StringIO("\n".join(file_lines))
            storage._deserialize()
            expected = {
                "some/path/foo": "12 34 56\n",
                "some/path/bar": "78 90 12\n",
                "path/baz": "67 89 19",
                }
            self.assertEqual(expected, storage._binds)

if __name__ == '__main__':
    unittest.main()
