from discord.ext.commands import Bot, Cog, Context
from discord import Message, Member, Game, Reaction, Embed
from discord.utils import get, find

class Events(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
       print('Logged in as:')
       print('Username: ' + self.bot.user.name)
def setup(bot: Bot):
    bot.add_cog(Events(bot))