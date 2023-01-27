import sys
from scripts.bot import Bot
from scripts.utils import Utils


def main():
    if len(sys.argv) < 2:
        raise Exception("Please provide an argument!")

    print("Starting automation...\n")
    bot = Bot()
    bot.run(sys.argv[1])
    print("Finished automation!\n")


if __name__ == "__main__":
    main()
