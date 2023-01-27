import sys
from scripts.bot import Bot
from scripts.utils import Utils


def main():
    print("Starting automation...")
    bot = Bot()
    bot.run()
    print("Finished automation!")


if __name__ == "__main__":
    main()
