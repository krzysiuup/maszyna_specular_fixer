import os
import logging

class ModelCorrector:
    def __init__(self, controller):
        self.controller = controller
        self.specular_queue = []

    def save_corrected_model(self, model_path, output_file_path):
        with open(model_path) as input_file, open(output_file_path, "w") as output_file:
            for line in input_file:
                if "specular" in line:
                    value = line.split(":")[1].strip()
                    line = line.replace(value, specular_queue.pop(0))
                output_file.write(line)
        logging.info("Corrected model as save in {}".format(output_file_path))
