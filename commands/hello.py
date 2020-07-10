from discord.ext.commands import Cog, command, Bot
from discord import Member

class Teste(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @command(name="teste")
    async def teste_command(self, ctx):
        await ctx.send("""Bem...
        de alguma forma estou viva :) """)

def setup(bot: Bot):
    bot.add_cog(Teste(bot))