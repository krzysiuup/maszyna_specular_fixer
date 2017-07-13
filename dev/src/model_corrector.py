import os
import logging

class ModelCorrector:
    def __init__(self, controller):
        self.OUTPUT_DIR_ROOT = "SPECULARS_FIXED"
        self.controller = controller
        self.textures_queue = []
        correcting = False

    def _iterate_files(self):
        for filename in os.listdir(self.controller.working_path):
            if filename.endswith(".t3d"):
                self.current_file_path = os.path.join(self.controller.working_path, filename)
                self._handle_line_from_file()

    def _fill_textures_queue(self):
        with open(self.controller.current_file_path) as model_file:
            for line in model_file:
                if "map:" in line.lower():
                    texture_path = line.split(":")[1].strip()
                    self.textures_queue.append(texture_path)
            self.textures_queue = iter(self.textures_queue)
            self._save_fixed_file()

    def _save_fixed_file(self):
        output_path = os.path.join(OUTPUT_DIR_ROOT, self.controller.current_file_path)
        with open(output_path, "w") as output_file, open(self.controller.current_file_path) as old_file:
            for line in old_file:
                if "specular:" in line.lower():
                    old_specular = line.split(":")[1].strip()
                    new_specular = self.controller.binds_storage[next(self.textures_queue)]
                    line = line.replace(old_specular, new_specular)
                output_file.write(line)
