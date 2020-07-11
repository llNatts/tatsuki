from discord.ext.commands import Bot, Cog, Context
from discord import Message, Member, Game, Reaction, Embed
from discord.utils import get, find

class Events(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_member_join(self, member: Member):
        message = f"{member.mention} está no servidor"

        channel = get(member.guild.text_channels, name='spam')
        await channel.send(message)

def setup(bot: Bot):
    bot.add_cog(Events(bot))