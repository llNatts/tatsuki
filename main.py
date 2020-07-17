from discord.ext.commands import Bot
import logging
import load
import os.path

def main():
    prefix = load.prefix
    token = load.token

    bot = Bot(command_prefix=prefix)

    for filename in os.listdir('./extensions'):
        if filename.endswith('.py'):
            file = filename.split('.')[0]
            path = f"extensions.{file}"
            try:
                bot.load_extension(path)
                print(f'[LOG]: extension loaded: {path}')
            except Exception as error:
                print(error)
    bot.run(token)
main()