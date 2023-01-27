import sys
from scripts.bot import Bot
from scripts.utils import Utils


def main():
    if len(sys.argv) < 2:
        raise Exception("Please provide an argument!")
    Utils.log(f"Path specified: {sys.argv[1]}")

    Utils.log("Starting automation...\n")
    bot = Bot()
    bot.run(sys.argv[1])
    Utils.log("Finished automation!\n")


if __name__ == "__main__":
    main()
