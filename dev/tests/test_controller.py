import sys
import pathlib
import unittest
from unittest import mock

from PyQt5 import QtWidgets

from dev.src.controller import Controller

app = QtWidgets.QApplication(sys.argv)

class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller(mock.Mock())
        self.controller.texture_searcher = mock.Mock()

    def test_get_working_path_should_call_set_cwd(self):
        self.controller.ui_manager.get_value_from_file_dialog.return_value = pathlib.Path("some/path/to/models/and/deeper")
        self.controller.ui_manager.validate_path.return_value = True
        self.controller.set_cwd = mock.Mock()
        self.controller.get_working_path()
        self.controller.set_cwd.assert_called_once()

    def test_get_working_path_should_not_call_set_cwd(self):
        self.controller.ui_manager.get_value_from_file_dialog.return_value = pathlib.Path("wrong/path/to/another/dir/and/deeper")
        self.controller.ui_manager.validate_path.return_value = False
        self.controller.set_cwd = mock.Mock()
        self.controller.get_working_path()
        self.controller.set_cwd.assert_not_called()

    @mock.patch("dev.src.controller.os")
    def test_set_cwd_should_call_chdir(self, os_mock):
        self.controller.working_path = pathlib.Path("some/path/to/models/and/deeper")
        self.controller.set_cwd()
        os_mock.chdir.assert_called_once_with(pathlib.Path("some/path/to"))

    @mock.patch("dev.src.controller.os.chdir")
    def test_set_cwd_should_call_set_working_path_on_texture_searcher(self, chdir_mock):
        self.controller.working_path = pathlib.Path("some/path/to/models/and/deeper")
        self.controller.set_cwd()
        self.controller.texture_searcher.set_working_path.assert_called_once_with(pathlib.Path("models/and/deeper"))
        
if __name__ == '__main__':
    unittest.main()
