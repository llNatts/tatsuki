from discord.ext.commands import Cog, command, Bot
from discord import Member, Embed

class Teste(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @command(name="bye")
    async def teste_command(self, ctx):
        await ctx.send(f'hello {ctx.author}')
def setup(bot: Bot):
    bot.add_cog(Teste(bot))