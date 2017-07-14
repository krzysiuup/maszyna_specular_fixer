import sys
import os
import threading
import logging

from PyQt5 import QtWidgets

from dev.ui.main import Ui_MainWindow
from dev.src.controller import Controller

class UiManager(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_buttons()

        self.controller = Controller(self)

    def setup_buttons(self):
        self.ui.menu_set_working_path.triggered.connect(self.get_working_path)
        self.ui.button_nexttex.clicked.connect(self.get_next_texture_path)
        self.ui.button_setspecular.clicked.connect(self.set_specular)

    def get_value_from_file_dialog(self):
        return str(QtWidgets.QFileDialog.getExistingDirectory(self, "Wybierz ścieżkę, z której chcesz poprawić modele."))

    def validate_path(self, path):
        if "dynamic" not in path or "models" not in path:
            return False
            QtWidgets.QMessageBox.warning(self, "Zła ścieżka?", "Ścieżka powinna prowadzić przez katalogi 'models' lub 'dynamic'")
        return True

    def update_ui_if_queue_is_not_empty(self, path):
        if path:
            self.ui.label_texturename.setText(texture_name)
        else:
            QtWidgets.QMessageBox.information(self, "Koniec kolejki", "Brak tekstur w kolejce. Wybierz kolejny folder.")
