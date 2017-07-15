import os
import logging
import pathlib

class ModelSearcher:
    def __init__(self):
        self.models_paths_queue = None

    def set_working_path(self, working_path):
        self.working_path = working_path
        self.models_paths_queue = self._models_generator()
        logging.info("ModelSearcher: Working path was set: {}".format(self.working_path))

    def get_next_model_path(self):
        try:
            next_path = next(self.models_paths_queue)
            return next_path
            logging.info("ModelSearcher: Path was returned: {}".format(next_path))
        except StopIteration:
            return None
            logging.info("ModelSearcher: No more paths in queue.")

    def _models_generator(self):
        for filename in os.listdir(self.working_path):
            if filename.endswith(".t3d"):
                yield pathlib.Path(self.working_path, filename)
