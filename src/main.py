import sys
import os
from scripts.bot import Bot
from scripts.utils import Utils


def main():
    if len(sys.argv) < 2:
        raise Exception("Please provide an argument!")
    if not os.path.exists(sys.argv[1]):
        raise Exception("Path provided does not exist!")
    if not os.path.isdir(sys.argv[1]):
        raise Exception("Path provided must be a directory!")
    print()
    Utils.log(f"Path specified: {sys.argv[1]}")

    Utils.log("Starting automation...")
    bot = Bot()
    bot.run(sys.argv[1])
    Utils.log("Finished automation!\n")


if __name__ == "__main__":
    main()
