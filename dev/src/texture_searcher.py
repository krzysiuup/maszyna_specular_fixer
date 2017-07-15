import os
import logging

class TextureSearcher:
    def __init__(self):
        self.working_path = ""

    def set_working_path(self, path):
        self.working_path = path

    def get_next_texture_path(self, path):
