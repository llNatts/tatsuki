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
        
    @cooldown(1,8,BucketType.user)
    @has_permissions(ban_members=True)
    @bot_has_permissions(ban_members=True)
    @command(name='ban', usage='t!ban <user> <reason>')
    async def ban_member(self, ctx, target: Member, * ,reason='O usuário quebrou as regras.'):
        """
        Aplique punição nos malditos arruaceiros
        """
        if ctx.author == target:
            await ctx.send('Você não está sendo muito duro consigo mesmo ?')
            return
        try:
            await target.send(f'Você foi banido pelo: {ctx.author.mention} \nPelo seguinte motivo: \n{reason}')
            await ctx.guild.ban(target, reason=reason)
        except Exception as error:
            print(error)
            await ctx.send('Não foi possível realizar o seu pedido, goshujin-sama')
            
        else:
            await ctx.send(f'O {target.mention} foi banido do servidor pelo seguinte motivo: {reason}')

def setup(bot: Bot):
    bot.add_cog(Moderation(bot))
