import os
import logging

class ModelCorrector:
    def __init__(self, controller):
        self.controller = controller
        self.textures_queue = []

    def save_corrected_models(self):
        for directory_contents in os.walk(self.controller.working_path):
            absolute_path, dirs_list, files_list = directory_contents
            for filename in files_list:
                if filename.endswith(".t3d"):
                    input_filepath = os.path.join(absolute_path, filename)
                    with open(input_filepath) as model_file:
                        for line in model_file:
                            if "map" in line:
                                value = line.split(":")[1].strip()
                                self.textures_queue.append(value)
                    output_filepath =  os.path.relpath(input_filepath, self.controller.root_path)
                    output_filepath = os.path.join(self.controller.root_path, "SPECULARS_FIXED", output_filepath)
                    with open(output_filepath) as output_file:
                        pass
