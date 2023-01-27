import os
import shutil


class Bot:
    def __init__(self):
        self.path = None
        self.image_extensions = ("png", "jpg", "jpeg")
        self.video_extensions = ("mp4", "mov")

    def __filter_file(self, filename: str, look_for_images: bool) -> bool:
        extension = filename.split(".")[-1]
        if look_for_images:
            return extension in self.image_extensions
        return extension in self.video_extensions

    def __filter_image(self, filename: str) -> bool:
        return self.__filter_file(filename, True)

    def __filter_video(self, filename: str) -> bool:
        return self.__filter_file(filename, False)

    def run(self, path: str):  # recordings path
        self.path = path

        directories = os.listdir(self.path)
        for directory in directories:
            files = os.listdir(directory)
            images = filter(self.__filter_image, os.listdir(directory))
            videos = filter(self.__filter_video, os.listdir(directory))
