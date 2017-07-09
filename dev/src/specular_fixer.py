import sys
import os
import threading
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
        self.setup_buttons()

        self.binds_storage = BindsStorage()
        self.texture_searcher = TextureSearcher(self)
        self.model_corrector = ModelCorrector(self)

        self.get_root_path()
        self.get_working_path()

    def setup_buttons(self):
        self.ui.action_listingpath.triggered.connect(self.get_working_path)
        self.ui.button_nexttex.clicked.connect(self.get_next_texture_path)
        #self.ui.button_setspecular.clicked.connect()

    def get_root_path(self):
        with open("specular_fixer.cfg", "w+") as config_file:
            contents = config_file.read()
            if not contents:
                self.root_path = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Wybierz główny folder symulatora."))
                config_file.write(self.root_path)
            else:
                self.root_path = contents
        logging.info("Root path was set to {}".format(self.root_path))

    def get_working_path(self):
        self.working_path = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Wybierz ścieżkę, z której chcesz poprawić modele.", self.root_path))
        logging.info("Working path was set to {}".format(self.working_path))
        self.texture_searcher.set_working_path(self.working_path)

    def get_next_texture_path(self):
        self.current_texture_path = self.texture_searcher.next()
        if self.current_texture_path:
            self.ui.label_texturename.setText(os.path.relpath(self.current_texture_path, self.root_path))
        else:
            is_work_done = QtWidgets.QMessageBox.question(
                self, "Brak tekstur w kolejce. Czy chcesz poprawiać dalej?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

            if is_work_done == QtWidgets.QMessageBox.Yes:
                self.get_working_path()
            else:
                sys.exit()

    def set_specular(self):
        path = os.path.relpath(self.current_texture_path, os.path.join(self.root_path, "textures"))
        path = os.path.splittext(path)[0]
        specular = "{} {} {}".format(
            self.ui.spinbox_specular_1.value(),
            self.ui.spinbox_specular_2.value(),
            self.ui.spinbox_specular_3.value()
            )
        self.binds_storage.add(path, specular)
