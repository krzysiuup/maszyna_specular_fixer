import os
import logging

class TextureSearcher:
    def __init__(self):
        self.working_path = ""

    def set_working_path(self, path):
        self.working_path = path
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
        for filename in os.listdir(self.working_path):
            if filename.endswith(".t3d"):
                with open(os.path.join(self.working_path, filename)) as model_file:
                    for line in model_file:
                        if "map:" in line:
                            texture_path = line.split(":").strip()
                            logging.info("Texture searcher returned next texture: {}".format(texture_path))
                            yield texture_path
