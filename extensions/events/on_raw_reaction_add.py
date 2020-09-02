from discord.ext.commands  import Bot, Cog, Context
from discord import  Reaction, Member

class events(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_raw_reaction_add(self,payload):
        pass:
    @Cog.listener()
    async def on_reaction_add(self,r: Reaction, u: Member):
        print(r,u)
        
def setup(bot: Bot):
    bot.add_cog(events(bot))
