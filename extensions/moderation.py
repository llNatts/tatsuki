from discord.ext.commands import Bot, Cog, command, has_permissions, bot_has_permissions
from discord import User, Member, Embed
import asyncio

class Moderation(Cog):
    """
    Suas funcionalidades de moderador.
    """
    def __init__(self, bot: Bot):
        self.bot = bot
    
    @command(name='clear', usage='t!clear <quantidade de mensagem>')
    @has_permissions(manage_messages=True)
    @bot_has_permissions(manage_messages=True)
    async def clear_message(self, ctx, arg=None):
        channel = ctx.message.channel
        if not arg: 
            await ctx.send('Você não especificou a quantidade de mensagem')
        else:
            await channel.purge(limit=int(arg))
            await channel.send(f'Deletei algumas mensagens')
    
def setup(bot: Bot):
    bot.add_cog(Moderation(bot))

