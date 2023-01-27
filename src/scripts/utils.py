import os
from datetime import datetime
from colored import fg


class Utils:
    __log_count = 0

    @staticmethod
    def get_path() -> str:
        dirname = __file__
        root = os.path.abspath(os.path.join(os.path.dirname(dirname), ".."))
        while "\\" in root:
            root = root.replace("\\", "/")
        root = "".join([i if i != ":" else f"{i}/" for i in root])
        return f"{root[0].upper()}{root[1:]}"

    @staticmethod
    def format_hour(hour: str) -> str:
        hour_value = int(hour.split(":")[0])
        if hour_value >= 13 or hour_value == 0:
            hour_of_day = hour_value - 12 if hour_value != 0 else 12
        else:
            hour_of_day = hour_value
        formatted_hour = f'{hour_of_day}:{hour.split(":")[1]}'
        mid_day = "PM" if hour_value >= 12 else "AM"
        return f"{formatted_hour} {mid_day}"

    @staticmethod
    def log(message: str) -> None:
        hour = Utils.format_hour(str(datetime.now()).split(" ")[1])
        Utils.__log_count += 1
        print(f"(Log #{Utils.__log_count})[{hour}]: {message}")
