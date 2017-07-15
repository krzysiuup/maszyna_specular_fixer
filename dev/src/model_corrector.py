import os
import logging
import pathlib

class ModelCorrector:
    def __init__(self):
        self.OUTPUT_DIR_ROOT = "SPECULARS_FIXED"
        self.textures_queue = []
        self.working_path = None
        self.current_file_path = None

    def set_working_path(self, path):
        self.working_path = path

    def fix_models(self, binds_storage):
        self.binds_storage = binds_storage
        self._get_t3d_files()

    def _get_t3d_files(self):
        for filename in os.listdir(self.working_path):
            if filename.endswith(".t3d"):
                self.current_file_path = pathlib.Path(self.working_path, filename)
                self._get_textures_order_from_file()

    def _get_textures_order_from_file(self):
        with open(self.current_file_path) as model_file:
            for line in model_file:
                if "map:" in line.lower():
                    texture_path = line.split(":")[1].strip()
                    self.textures_queue.append(texture_path)
            self.textures_queue = iter(self.textures_queue)
            self._save_fixed_file()

    def _save_fixed_file(self):
        with open( "w") as output_file, open(self.controller.current_file_path) as old_file:
            for line in old_file:
                if "specular:" in line.lower():
                    old_specular = line.split(":")[1].strip()
                    new_specular = self.binds_storage[next(self.textures_queue)]
                    line = line.replace(old_specular, new_specular)
                output_file.write(line)
            logging.info("Corrected model: {} was saved in {}".format(input_path, output_path))
