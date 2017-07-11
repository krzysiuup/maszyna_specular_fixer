import unittest

from PyQt5.QtWidgets import QApplication

_instance = None

class QtTestHelper(unittest.TestCase):
    qapplication = True

    def setUp(self):
        super().setUp()
        global _instance
        if _instance is None:
            _instance = QApplication([])
        self.app = _instance

    def tearDown(self):
        del self.app
        super().tearDown()
