import unittest
import unittest.mock

from PyQt5 import QtWidgets

from dev.tests.qt_test_helper import QtTestHelper
from dev.src.specular_fixer import SpecularFixer


class TestSpecuarFixer(QtTestHelper):
    def test_get_root_path_should_set_root_path(self):
        fixer = SpecularFixer()
        fixer.working_path = "Some/path/to/folder/in/textures/and/deeper"
        fixer.get_root_path(fixer.working_path)
        self.assertEqual("Some/path/to/folder/in", fixer.root_path)

if __name__ == '__main__':
    unittest.main()
