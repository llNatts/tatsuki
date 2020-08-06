from discord.ext.commands import Bot, Cog, command, has_permissions, bot_has_permissions, cooldown, BucketType
from discord import User, Member, Embed
from asyncio import TimeoutError, sleep
from discord.utils import get, find
import asyncio

class Moderation(Cog):
    """
    Suas funcionalidades de moderador.
    """
    def __init__(self, bot: Bot):
        self.bot = bot
    
    @command(name="reload", hidden=True)
    async def reload_command(self, ctx, arg=None):
        if ctx.author.id == 621183220083326996:     
            try:
                self.bot.reload_extension(f'extensions.{arg}')
                await ctx.send(f'O módulo {arg} foi recarregado com sucesso!')
            except Exception as error:
                await ctx.send(f'[ERROR]: {error}')
        else:
            await ctx.send(f'{ctx.author.mention}, você não tem permissão para usar este comando.')
def setup(bot: Bot):
    bot.add_cog(Moderation(bot))