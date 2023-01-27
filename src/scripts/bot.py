import os
import shutil


class Bot:
    def __init__(self):
        self.path = None
        self.image_extensions = ("png", "jpg", "jpeg")
        self.video_extensions = ("mp4", "mov")

    def __filter_file(self, file_name: str, look_for_images: bool) -> bool:
        extension = file_name.split(".")[-1]
        if look_for_images:
            return extension in self.image_extensions
        return extension in self.video_extensions

    def __filter_image(self, file_name: str) -> bool:
        return self.__filter_file(file_name, True)

    def __filter_video(self, file_name: str) -> bool:
        return self.__filter_file(file_name, False)

    def __validate_directory(self, files: list, target_directory: str) -> None:
        if target_directory in files:
            os.mkdir(target_directory)

    def run(self, path: str):
        self.path = path

        directories = os.listdir(self.path)
        for directory in directories:
            files = os.listdir(directory)
            images = filter(self.__filter_image, files)
            videos = filter(self.__filter_video, files)
            print(f"Organized {directory}!")
