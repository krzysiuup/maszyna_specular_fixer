import sys
import logging

from PyQt5 import QtWidgets

from dev.src.controller import Controller

if __name__ == '__main__':
    logging.basicConfig(filename="specular_fixer.log", filemode="w", level=logging.DEBUG)
    app = QtWidgets.QApplication(sys.argv)
    window = Controller()
    window.show()
    sys.exit(app.exec_())
