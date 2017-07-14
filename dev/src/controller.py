import os
import pathlib
import logging

from dev.src.texture_searcher import TextureSearcher

class Controller:
    def __init__(self, ui_manager):
        self.ui_manager = ui_manager
        self.texture_searcher = TextureSearcher()

    def get_working_path(self):
        self.working_path = pathlib.Path(self.ui_manager.get_value_from_file_dialog())
        is_working_path_valid = self.ui_manager.validate_path(self.working_path)
        if is_working_path_valid:
            logging.info("Working path was set to {}".format(self.working_path))
            self.set_cwd()

    def set_cwd(self):
        end_component = "models" if "models" in self.working_path.parts else "dynamic"
        self.root_path = pathlib.Path(*self.working_path.parts[0:self.working_path.parts.index(end_component)])
        os.chdir(self.root_path)
        self.texture_searcher.set_working_path(pathlib.Path(self.working_path).relative_to(self.root_path))

    def get_next_texture_path(self):
        self.current_texture_path = pathlib.Path(self.texture_searcher.next())
        self.ui_manager.update_ui_if_queue_is_not_empty(self.current_texture_path)

    def set_specular(self):
        texture_path = pathlib.Path(self.current_texture_path).relative_to("textures")

        specular = "{} {} {}".format(
            self.ui.spinbox_specular_1.value(),
            self.ui.spinbox_specular_2.value(),
            self.ui.spinbox_specular_3.value()
            )
        self.binds_storage.add(texture_path, specular)
