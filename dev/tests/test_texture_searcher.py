import unittest
from unittest import mock
import pathlib
import types

from dev.src.texture_searcher import TextureSearcher

class TestTextureSearcher(unittest.TestCase):
    def setUp(self):
        self.texture_searcher = TextureSearcher()

    def test_set_working_file_should_set_working_file(self):
        self.texture_searcher.set_working_file(pathlib.Path("some/path/to/file.t3d"))
        expected = pathlib.Path("some/path/to/file.t3d")
        self.assertEqual(expected, self.texture_searcher.working_file)

    def test_set_working_file_should_make_generator(self):
        self.texture_searcher.set_working_file(pathlib.Path("models/some/file.t3d"))
        self.assertTrue(isinstance(self.texture_searcher.textures_paths_queue, types.GeneratorType))

    def test_get_next_texture_file_should_return_proper_path(self):
        self.texture_searcher.textures_paths_queue = iter([
            pathlib.Path("some/path/to/texture")
            ])
        actual = self.texture_searcher.get_next_texture_path()
        expected = pathlib.Path("some/path/to/texture")
        self.assertEqual(expected, actual)

    def test_get_next_texture_file_should_return_none(self):
        self.texture_searcher.textures_paths_queue = iter([])
        actual = self.texture_searcher.get_next_texture_path()
        self.assertIsNone(actual)

if __name__ == '__main__':
    unittest.main()
