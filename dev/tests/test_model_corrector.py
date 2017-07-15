import unittest
from unittest import mock
import pathlib

from dev.src.model_corrector import ModelCorrector

class TestModelCorrector(unittest.TestCase):
    def setUp(self):
        self.model_corrector = ModelCorrector()

    def test_set_working_file_should_set_working_file(self):
        self.model_corrector.set_working_file(pathlib.Path("models/some/model.t3d"))
        expected = pathlib.Path("models/some/model.t3d")
        self.assertEqual(expected, self.model_corrector.working_file)

    def test_add_to_queue_should_add_texture_path_to_queue(self):
        self.model_corrector.add_to_queue(pathlib.Path("some/texture/path"))
        self.model_corrector.add_to_queue(pathlib.Path("another/texture/path"))
        expected = [
            pathlib.Path("some/texture/path"),
            pathlib.Path("another/texture/path")
            ]
        self.assertEqual(expected, self.model_corrector._textures_queue)

    def test_save_correted_file_should_call_transform_queue_to_iterator(self):
        pass


if __name__ == '__main__':
    unittest.main()
