import unittest
from unittest import mock
import pathlib
import types

from dev.src.model_searcher import ModelSearcher

class TestModelSearcher(unittest.TestCase):
    def setUp(self):
        self.model_searcher = ModelSearcher()

    def test_set_working_path_should_set_working_path(self):
        self.model_searcher.set_working_path(pathlib.Path("models/some/path"))
        expected = pathlib.Path("models/some/path")
        self.assertEqual(expected, self.model_searcher.working_path)

    def test_set_working_path_should_make_generator(self):
        self.model_searcher.set_working_path(pathlib.Path("models/some/path"))
        self.assertTrue(isinstance(self.model_searcher.models_paths_queue, types.GeneratorType))

    @mock.patch("dev.src.model_searcher.os")
    def test_get_next_model_path_should_return_proper_path(self, mock_os):
        mock_os.listdir.return_value = iter(["foo.e3d", "bar.t3d"])
        self.model_searcher.set_working_path(pathlib.Path("some/path"))
        actual = self.model_searcher.get_next_model_path()
        expected = pathlib.Path("some/path/bar.t3d")
        self.assertEqual(expected, actual)

    def test_get_next_model_path_should_return_none(self):
        self.model_searcher.models_paths_queue = iter([])
        actual = self.model_searcher.get_next_model_path()
        self.assertIsNone(actual)

if __name__ == '__main__':
    unittest.main()
