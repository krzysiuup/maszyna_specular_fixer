import sys
import os
import threading
import logging

from PyQt5 import QtWidgets

from dev.ui.main import Ui_MainWindow
from dev.src.texture_searcher import TextureSearcher
from dev.src.binds_storage import BindsStorage
from dev.src.model_corrector import ModelCorrector

class SpecularFixer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_buttons()

        self.binds_storage = BindsStorage()
        self.texture_searcher = TextureSearcher()
        self.model_corrector = ModelCorrector(self)

    def setup_buttons(self):
        self.ui.menu_set_working_path.triggered.connect(self.get_working_path)
        self.ui.button_nexttex.clicked.connect(self.get_next_texture_path)
        self.ui.button_setspecular.clicked.connect(self.set_specular)

    def get_working_path(self):
        self.working_path = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Wybierz ścieżkę, z której chcesz poprawić modele."))
        self.texture_searcher.set_working_path(self.working_path)
        logging.info("Working path was set to {}".format(self.working_path))
        self.get_root_path()

    def get_root_path(self):
        get_root_thread = threading.Thread(target=self._get_root).start()

    def _get_root(self):
        path = self.working_path
        tail = None
        if "dynamic" in path or "models" in path:
            while tail != "dynamic" or tail != "models":
                path, tail = os.path.split(path)
        else:
            warning = QtWidgets.QMessageBox.information(self, "Błędna ścieżka?", "Ścieżka musi prowadzić do podfolderów dynamic lub models!")

    def get_next_texture_path(self):
        self.current_texture_path = self.texture_searcher.next()
        if self.current_texture_path:
            self.ui.label_texturename.setText(os.path.relpath(self.current_texture_path, self.root_path))
        else:
            is_work_done = QtWidgets.QMessageBox.information(self, "Koniec kolejki", "Brak tekstur w kolejce. Wybierz kolejny folder.")

    def set_specular(self):
        texture_path_head, texture_path_tail = os.path.split(self.current_texture_path)
        final_texture_path = os.path.relpath(self.texture_path_head, os.path.join(self.root_path, "textures"))

        specular = "{} {} {}".format(
            self.ui.spinbox_specular_1.value(),
            self.ui.spinbox_specular_2.value(),
            self.ui.spinbox_specular_3.value()
            )
        self.binds_storage.add(path, specular)
