import logging

class BindsStorage:
    def __init__(self):
        self._binds = {}
        self._deserialize()

    def add(self, key, value):
        """ key -> str ; value -> str """
        self._binds[key] = value

    def get(self, key):
        """ key -> str """
        try:
            return self._binds[key]
        except KeyError:
            return None

    def serialize(self):
        with open("binds.txt", "w") as file_:
            for key in self._binds.keys():
                file_.write("{}:{}\n".format(key, self._binds[key]))
        logging.info("Binds was succesfully stored in binds.txt")

    def _deserialize(self):
        with open("binds.txt", "w+") as file_:
            for line in file_:
                key, value = line.split(":")
                self._binds[key] = value.strip("\n")
        logging.info("Binds was succesfully restored from binds.txt")
