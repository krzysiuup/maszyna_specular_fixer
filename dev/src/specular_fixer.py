import sys
import os
import logging

from PyQt5 import QtWidgets

from dev.ui.main import Ui_MainWindow
from dev.src.texture_searcher import TextureSearcher
from dev.src.binds_storage import BindsStorage
from dev.src.model_corrector import ModelCorrector
from dev.src.model_searcher import ModelSearcher

class SpecularFixer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.get_working_path()
        self.get_root_path()

        self.binds_storage = BindsStorage()
        self.texture_searcher = TextureSearcher(self)
        self.model_corrector = ModelCorrector(self)
        self.model_searcher = ModelSearcher(self)

        self.setup_buttons()

    def setup_buttons(self):
        self.ui.action_listingpath.triggered.connect(self.get_working_path)
        self.ui.button_nexttex.clicked.connect(self.get_next_texture_path)
        self.ui.button_setspecular.clicked.connect()
        self.ui.button_nexttex.setDisabled(True)
        self.ui.button_setspecular.setDisabled(True)

    def get_working_path(self):
        self.working_path = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Wybierz ścieżkę, z której chcesz poprawić modele."))
        logging.info("Working path was set to {}".format(self.working_path))

    def get_root_path(self):
        tail = ""
        expected_tail = ""
        if "dynamic" in self.working_path:
            expected_tail = "dynamic"
        elif "models" in self.working_path:
            expected_tail = "models"
        if expected_tail:
            while tail != expected_tail:
                head, tail = os.path.split(self.working_path)
            self.root_path = head
            logging.info("Root path was set to {}".format(self.root_path))

    def get_next_texture_path(self):
        texture_path = self.texture_searcher.next()
        if texture_path:
            self.ui.label_texturename.setText(os.path.relpath(texture_path, self.root_path))
        else:
            is_work_done = QtWidgets.QMessageBox.question(
                self, "Brak tekstur w kolejce. Czy chcesz poprawiać dalej?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

            if is_work_done == QtWidgets.QMessageBox.Yes:
                self.get_working_path()
            else:
                sys.exit()
