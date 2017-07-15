import unittest
from unittest import mock

from dev.src.model_corrector import ModelCorrector

class TestModelCorrector(unittest.TestCase):
    def setUp(self):
        self.model_corrector = ModelCorrector()
        self.model_corrector.working_path = "some/path"

    @mock.patch("dev.src.model_corrector.os")
    def test_get_t3d_files_should_call_get_textures_order_from_file(self, mock_os):
        mock_os.listdir.return_value = ["to.t3d"]
        self.model_corrector._get_textures_order_from_file = mock.Mock()
        self.model_corrector._get_t3d_files()
        self.model_corrector._get_textures_order_from_file.assert_called_once()

if __name__ == '__main__':
    unittest.main()
