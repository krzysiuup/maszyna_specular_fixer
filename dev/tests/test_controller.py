import sys
import unittest
from unittest import mock

from PyQt5 import QtWidgets

from dev.src.controller import Controller
from dev.src.ui_manager import UiManager

app = QtWidgets.QApplication(sys.argv)

class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller(UiManager)
        self.controller.ui_manager = mock.Mock()

    @mock.patch("dev.src.controller.os")
    def test_get_working_path(self, os_mock):
        self.controller.ui_manager.get_value_from_file_dialog.return_value = "some/path/to/models/and/deeper"
        self.controller.ui_manager.validate_path.return_value = True
        self.controller.get_working_path()
        os_mock.chdir.assert_called_with("some/path/to")

if __name__ == '__main__':
    unittest.main()
