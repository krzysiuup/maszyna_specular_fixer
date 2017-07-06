import os
import logging

class TextureSearcher:
    def __init__(self, controller):
        self.controller = controller
        self.rewind()

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
        for line in open(os.path.join(self.controller.working_directory, file_)):
            if "map" in line:
                texture_path = line.split(":").strip()
                yield texture_path
