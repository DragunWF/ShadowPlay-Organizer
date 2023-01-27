import os
import shutil
from .utils import Utils


class Bot:
    def __init__(self):
        self.path = None
        self.image_extensions = ("png", "jpg", "jpeg")
        self.video_extensions = ("mp4", "mov")
        Utils.log("Bot initialized!")

    def __validate_directory(self, files: list[str], current_directory: str) -> None:
        target_directories = ("Recordings", "Screenshots")
        for directory in target_directories:
            if not directory in files:
                target_directory_path = f"{self.path}\{current_directory}\{directory}"
                os.mkdir(target_directory_path)
                Utils.log(f"Created {target_directory_path}")

    def __move_files(self, files: list[str], current_directory: str) -> None:
        current_path = f"{self.path}\{current_directory}"
        for file in files:
            extension = file.split(".")[-1]
            file_path = f"{current_path}\{file}"
            destination = None

            if extension in self.image_extensions:
                destination = f"{current_path}\Screenshots\{file}"
            elif extension in self.video_extensions:
                destination = f"{current_path}\Recordings\{file}"

            if destination:
                shutil.move(file_path, destination)
                Utils.log(f"Moved {file_path} to {destination}")

    def __is_dir(self, file_name: str) -> bool:
        return os.path.isdir(f"{self.path}\{file_name}")

    def run(self, path: str) -> None:
        Utils.log("Running bot!")
        self.path = path

        directories = list(filter(self.__is_dir, os.listdir(self.path)))
        for directory in directories:
            full_path = f"{self.path}\{directory}"
            self.__validate_directory(os.listdir(full_path), directory)
            self.__move_files(os.listdir(full_path), directory)
            Utils.log(f"Organized {full_path}")
