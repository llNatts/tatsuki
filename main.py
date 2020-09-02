from discord.ext.commands import Bot
import logging
from utils import load
import os.path
from os.path import getsize
import sched, time

def main():
    prefix = load.get_prefix()
    token = load.get_token()

    bot = Bot(command_prefix=prefix)
    bot.raw_reactionlist= [{}]
# the hanlder load extensions
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if root.startswith("./extensions/") and name.endswith(".py"):
                file = os.path.join(root,name).replace("/",".").split(".py")[0]
                file = file[2:]  
                try:
                    bot.load_extension(file)
                    print(f'[LOG]: extension loaded: {file}')
                except Exception as error:
                    print(error)     
    try:
        bot.run(token)
    except Exception as error:
            print(error)
main()
