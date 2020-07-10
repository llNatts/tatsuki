from discord.ext.commands import Bot
import logging
import load
import os.path

def main():
    prefix = load.prefix
    token = load.token

    bot = Bot(command_prefix=prefix)

    root = "commands"
    files = ["hello"]

    for file in files:
        path = "{}.{}".format(root, file)
        try:
            bot.load_extension(path)
        except Exception as error:
            print("{0.__class__.__name__}: {0}".format(error))
    bot.run(token)
main()