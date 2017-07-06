import unittest
from unittest import mock

from dev.src.texture_searcher import TextureSearcher

class TestTextureSearcher(unittest.TestCase):
    def setUp(self):
        self.texture_searcher = TextureSearcher()

    def test_next_should_return_first_item(self):
        items = ["foo", "bar", "baz"]
        with mock.patch("dev.src.texture_searcher.TextureSearcher._generate_absolute_textures_paths") as mock_generator:
            mock_generator.return_value.__iter__.return_value = iter(items)
            result = self.texture_searcher.next()
            expected = "foo"
            print(list(self.texture_searcher.generator)
        self.assertEqual(expected, result)

    def test_next_should_return_false(self):
        items = []
        with mock.patch("dev.src.texture_searcher.TextureSearcher._generate_absolute_textures_paths") as mock_generator:
            mock_generator.return_value.__iter__.return_value = iter(items)
            result = self.texture_searcher.next()
        self.assertFalse(result)

    def test_rewind_should_rewind_the_generator(self):
        items = ["foo", "bar"]
        with mock.patch("dev.src.texture_searcher.TextureSearcher._generate_absolute_textures_paths") as mock_generator:
            mock_generator.return_value.__iter__.return_value = iter(items)
            self.texture_searcher.next()
            self.texture_searcher.next()
            self.texture_searcher.rewind()
        self.assertEqual(list(self.texture_searcher.generator), items)


if __name__ == '__main__':
    unittest.main()
