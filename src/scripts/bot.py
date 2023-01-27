import os
import shutil
from .utils import Utils


class Bot:
    def __init__(self):
        self.path = None
        self.image_extensions = ("png", "jpg", "jpeg")
        self.video_extensions = ("mp4", "mov")

    def __validate_directory(self, files: list) -> None:
        target_directories = ("Recordings", "Screenshots")
        for directory in target_directories:
            if directory in files:
                target_directory_path = f"{self.path}/{directory}"
                os.mkdir(target_directory_path)
                Utils.log(f"Created {target_directory_path}")

    def __move_files(self, files: list, current_directory: str) -> None:
        current_path = f"{self.path}/{current_directory}"
        for file in files:
            extension = file.split(".")[-1]
            file_path = f"{current_path}/{file}"
            destination = None

            if extension in self.image_extensions:
                destination = f"{current_path}/Screenshots/{file}"
            elif extension in self.video_extensions:
                destination = f"{current_path}/Recordings/{file}"

            if destination:
                shutil.move(file_path, destination)
                Utils.log(f"Moved {file_path} to {destination}")

    def run(self, path: str) -> None:
        self.path = path

        directories = tuple(filter(os.path.isdir, os.listdir(self.path)))
        for directory in directories:
            self.__validate_directory(directory)
            self.__move_files(os.listdir(directory), directory)
            Utils.log(f"Organized {self.path}/{directory}")
