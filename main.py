from discord.ext.commands import Bot
import logging
import load
import os.path

def main():
    prefix = load.prefix
    token = load.token

    bot = Bot(command_prefix=prefix, guild_subscriptions=True)

    for filename in os.listdir('./events'):
        if filename.endswith('.py'):
            file = filename.split('.')[0]
            path = f"events.{file}"
            try:
                bot.load_extension(path)
            except Exception as error:
                print("{0.__class__.__name__}: {0}".format(error))

    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            file = filename.split('.')[0]
            path = f"commands.{file}"
            try:
                bot.load_extension(path)
            except Exception as error:
                print("{0.__class__.__name__}: {0}".format(error))
    bot.run(token)
main()