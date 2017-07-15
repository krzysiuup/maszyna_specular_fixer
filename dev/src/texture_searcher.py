import os
import logging
import pathlib

class TextureSearcher:
    def __init__(self):
        self.working_path = ""

    def set_working_file(self, working_file):
        """ working_file -> pathlib.Path """
        self.working_file = working_file
        self.textures_paths_queue = self._textures_generator()
        logging.info("TextureSearcher: Working file was set: {}".format(self.working_file))

    def get_next_texture_path(self):
        try:
            next_path = next(self.textures_paths_queue)
            return next_path
            logging.info("TextureSearcher: Texture path was returned: {}".format(next_path))
        except StopIteration:
            return None
            logging.info("TextureSearcher: No more paths in queue.")

    def _textures_generator(self):
        with open(self.working_file) as model_file:
            for line in model_file:
                if "map:" in line.lower():
                    texture_path = line.split()[1].strip()
                    yield pathlib.Path(texture_path)
