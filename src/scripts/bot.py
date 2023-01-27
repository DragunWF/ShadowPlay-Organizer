import os
import shutil


class Bot:
    def __init__(self):
        self.path = None

    def run(self, path):  # recordings path
        self.path = path

        directories = os.listdir(self.path)
        for directory in directories:
            files = os.listdir(directory)
            for file in files:
                pass
