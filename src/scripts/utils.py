import os


class Utils:
    @staticmethod
    def get_path() -> str:
        dirname = __file__
        root = os.path.abspath(os.path.join(os.path.dirname(dirname), ".."))
        while "\\" in root:
            root = root.replace("\\", "/")
        root = "".join([i if i != ":" else f"{i}/" for i in root])
        return f"{root[0].upper()}{root[1:]}"
