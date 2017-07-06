import os
import logging

class ModelSearcher:
    def __init__(self, controller):
        self.controller = controller
        self.rewind()

    def next(self):
        try:
            path = next(self.generator)
            return path
            logging.info("Next path was yielded from model searcher: {}".format(path))
        except StopIteration:
            return False
            logging.info("Model searcher generator is exhausted!")

    def rewind(self):
        self.generator = self._generate_absolute_models_paths()
        logging.info("Model searcher generator was succesfully rewinded.")

    def _generate_absolute_models_paths(self):
        for model in os.listdir(self.controller.working_directory):
            if model.endswith(".t3d"):
                model_path = os.path.join(self.controller.working_directory, model)
                yield model_path
