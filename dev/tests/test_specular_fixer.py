import sys
import unittest
from unittest import mock

from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest

from dev.src.specular_fixer import SpecularFixer

app = QtWidgets.QApplication(sys.argv)

class TestSpecuarFixer(unittest.TestCase):
    def setUp(self):
        self.specular_fixer = SpecularFixer()

    def test_get_root_path_should_set_root_path(self):
        self.specular_fixer.working_path = "some\\path\\to\\models\\and\\deeper"
        self.specular_fixer.get_root_path()
        expected = "some\\path\\to"
        self.assertEqual(self.specular_fixer.root_path, expected)

    def test_get_root_path_should_set_root_path_to_empty_string(self):
        self.specular_fixer.working_path = "some\\path\\to\\another\\dir"
        self.specular_fixer.get_root_path()
        expected = ""
        self.assertEqual(self.specular_fixer.root_path, expected)

    def test_set_specular_should_call_storage_add_method(self):
        expected_path = "and\\deeper"
        expected_specular = "64 255 128"

        with mock.patch("dev.src.specular_fixer") as specular_fixer_mock:
            specular_fixer_mock.ui.spinbox_specular_1.setValue(64)
            specular_fixer_mock.ui.spinbox_specular_2.setValue (255)
            specular_fixer_mock.ui.spinbox_specular_3.setValue(128)

            specular_fixer_mock.current_texture_path = "some\\path\\to\\root\\textures\\and\\deeper"
            specular_fixer_mock.root_path = "some\\path\\to\\root"

            specular_fixer_mock.set_specular()
            specular_fixer_mock.binds_storage.add.assert_any_call(expected_path, expected_specular)

if __name__ == '__main__':
    unittest.main()
