import sys
import pathlib
import unittest
from unittest import mock

from PyQt5 import QtWidgets

from dev.src.controller import Controller

app = QtWidgets.QApplication(sys.argv)

class TestController(unittest.TestCase):
    def setUp(self):
        self.qt_patcher = mock.patch("dev.src.controller.QtWidgets")
        self.qt_mock = self.qt_patcher.start()
        self.controller = Controller()
        self.controller.ui = mock.Mock()
        self.controller.texture_searcher = mock.Mock()
        self.controller.binds_storage = mock.Mock()

    def test_get_working_path_should_call_set_cwd(self):
        self.qt_mock.QFileDialog.getExistingDirectory.return_value = "some/path/to/models/and/deeper"
        self.controller.set_cwd = mock.Mock()
        self.controller.get_working_path()
        self.controller.set_cwd.assert_called_once()

    def test_get_working_path_should_not_call_set_cwd(self):
        self.qt_mock.QFileDialog.getExistingDirectory.return_value = "wrong/path/to/another/dir/and/deeper"
        self.controller.set_cwd = mock.Mock()
        self.controller.get_working_path()
        self.controller.set_cwd.assert_not_called()

    def test_get_working_path_should_call_QMessageBox_warning(self):
        self.qt_mock.QFileDialog.getExistingDirectory.return_value = "wrong/path/to/another/dir/and/deeper"
        self.controller.set_cwd = mock.Mock()
        self.controller.get_working_path()
        self.qt_mock.QMessageBox.warning.assert_called_once()

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

    def test_get_next_texture_path_should_call_QLabel_setText(self):
        self.controller.texture_searcher.next.return_value = pathlib.Path("some/path/to/texture")
        self.controller.get_next_texture_path()
        self.controller.ui.label_texturename.setText.assert_called_once_with(str(pathlib.Path("some/path/to/texture")))

    def test_get_next_texture_path_should_call_QMessageBox_information(self):
        self.controller.texture_searcher.next.return_value = None
        self.controller.get_next_texture_path()
        self.qt_mock.QMessageBox.information.assert_called_once()

    def test_set_specular_should_call_add(self):
        self.controller.current_texture_path = pathlib.Path("textures/and/deeper")
        self.controller.ui.spinbox_specular_1.value.return_value = 255
        self.controller.ui.spinbox_specular_2.value.return_value = 123
        self.controller.ui.spinbox_specular_3.value.return_value = 69
        self.controller.set_specular()
        self.controller.binds_storage.add.assert_called_with(str(pathlib.Path("and/deeper")), "255 123 69")

    def tearDown(self):
        self.qt_patcher.stop()

if __name__ == '__main__':
    unittest.main()
