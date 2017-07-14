import sys
import logging

from PyQt5 import QtWidgets

from dev.src.ui_manager import UiManager

if __name__ == '__main__':
    logging.basicConfig(filename="specular_fixer.log", filemode="w", level=logging.DEBUG)
    app = QtWidgets.QApplication(sys.argv)
    window = UiManager()
    window.show()
    sys.exit(app.exec_())
