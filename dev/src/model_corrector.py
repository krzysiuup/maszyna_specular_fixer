import os
import logging
import pathlib

class ModelCorrector:
    def __init__(self):
        self.OUTPUT_DIR_ROOT = "SPECULARS_FIXED"
        self._textures_queue = []
        self.working_path = None
        self.current_file_path = None

    def set_working_file(self, working_file):
        """ working_file -> pathlib.Path"""
        self.working_file = working_file

    def add_to_queue(self, texture_path):
        """ texture_path -> pathlib.Path"""
        self._textures_queue.append(texture_path)

    def correct_and_save_file(self, binds_storage):
        """ binds_storage -> BindsStorage """
        self._transform_queue_to_iterator()
        self.binds_storage = binds_storage
        self._save_corrected_file()

    def _save_corrected_file(self):
        corrected_model_path = pathlib.Path(self.OUTPUT_DIR_ROOT, self.working_file)
        with open(self.working_file) as old_model, open(corrected_model_path, "w") as new_model:
            for line in old_model:
                line = self._replace_specular(line)
                new_model.write(line)

    def _find_and_replace_specular(self, line):
        """ line -> str """
        if "specular:" in line.lower():
            old_specular = line.split(":")[1].strip()
            line = line.replace(old_specular, self.binds_storage.get(next(self._textures_queue)))
        return line

    def _transform_queue_to_iterator(self):
        self._textures_queue = iter(self._textures_queue)
