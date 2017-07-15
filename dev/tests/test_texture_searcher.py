import unittest
from unittest import mock

from dev.src.texture_searcher import TextureSearcher

class TestTextureSearcher(unittest.TestCase):
    def setUp(self):
        self.texture_searcher = TextureSearcher()

if __name__ == '__main__':
    unittest.main()
