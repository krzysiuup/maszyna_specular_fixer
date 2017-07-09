import os
import logging

class TextureSearcher:
    def __init__(self):
        self.set_working_path()

    def set_working_path(self, path):
        self.working_path = path

    def next(self):
        try:
            path = next(self.generator)
            return path
            logging.info("Next path was yielded from texture searcher: {}".format(path))
        except StopIteration:
            return False
            logging.info("Texture searcher generator is exhausted!")

    def rewind(self):
        self.generator = self._generate_absolute_textures_paths()
        logging.info("Texture searcher generator was succesfully rewinded.")

    def _generate_absolute_textures_paths(self):
        for file_ in os.listdir(self.working_path):
            with open(os.path.join(self.working_path, file_)) as model_file:
            for line in model_file:
                if "map" in line:
                    texture_path = line.split(":").strip()
                    yield texture_path
