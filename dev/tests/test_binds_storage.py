import unittest
import unittest.mock

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
        self.assertEqual(storage.get("some/path"), "120 120 120")

    def test_deserialize_should_complement_dictionary(self):
        pass

if __name__ == '__main__':
    unittest.main()
