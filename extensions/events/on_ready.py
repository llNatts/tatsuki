from discord.ext.commands import Bot, Cog
from discord import  Reaction, ActivityType, Activity

class events(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print("="*20)
        print('Logged in as:')
        print('Username: ' + self.bot.user.name)
        await self.bot.change_presence(activity=Activity(type=ActivityType.watching, name="Animes em: animeshouse.netㅤㅤㅤㅤㅤㅤㅤㅤㅤPrecisa de ajuda ? Me mencione"))

def setup(bot: Bot):
    bot.add_cog(events(bot))