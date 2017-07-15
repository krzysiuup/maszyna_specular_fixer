import os
import pathlib
import logging

from PyQt5 import QtWidgets

from dev.ui.main import Ui_MainWindow
from dev.src.texture_searcher import TextureSearcher
from dev.src.binds_storage import BindsStorage

class Controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_buttons()

        self.texture_searcher = TextureSearcher()
        self.binds_storage = BindsStorage()

    def setup_buttons(self):
        self.ui.menu_set_working_path.triggered.connect(self.get_working_path)
        self.ui.button_nexttex.clicked.connect(self.get_next_texture_path)
        self.ui.button_setspecular.clicked.connect(self.set_specular)

    def get_working_path(self):
        self.working_path = pathlib.Path(QtWidgets.QFileDialog.getExistingDirectory(self, "Wybierz ścieżkę, z której chcesz poprawić modele."))
        if "dynamic" in self.working_path.parts or "models" in self.working_path.parts:
            logging.info("Working path was set to {}".format(self.working_path))
            self.set_cwd()
        else:
            QtWidgets.QMessageBox.warning(self, "Zła ścieżka?", "Ścieżka powinna prowadzić przez katalogi 'models' lub 'dynamic'")

    def set_cwd(self):
        end_component = "models" if "models" in self.working_path.parts else "dynamic"
        self.root_path = pathlib.Path(*self.working_path.parts[0:self.working_path.parts.index(end_component)])
        os.chdir(self.root_path)
        logging.info("Current working directory is now in {}".format(self.root_path))
        self.texture_searcher.set_working_path(pathlib.Path(self.working_path).relative_to(self.root_path))

    def get_next_texture_path(self):
        self.current_texture_path = self.texture_searcher.next()
        if self.current_texture_path:
            self.ui.label_texturename.setText(str(self.current_texture_path))
        else:
            QtWidgets.QMessageBox.information(self, "Koniec kolejki.", "Brak tekstur w kolejce. Wybierz kolejny folder.")

    def set_specular(self):
        texture_path = self.current_texture_path.relative_to("textures")

        specular = "{} {} {}".format(
            self.ui.spinbox_specular_1.value(),
            self.ui.spinbox_specular_2.value(),
            self.ui.spinbox_specular_3.value()
            )
        self.binds_storage.add(str(texture_path), specular)
