from discord.ext.commands import Bot, Cog, command, has_permissions, bot_has_permissions, cooldown, BucketType
from discord import User, Member, Embed
from asyncio import TimeoutError, sleep
from discord.utils import get, find
import asyncio


class Moderation(Cog):

    def __init__(self, bot: Bot):
        self.bot = bot

    @cooldown(1,8,BucketType.user)
    @has_permissions(ban_members=True)
    @bot_has_permissions(ban_members=True)
    @command(name='unban', usage='t!unban <userID>')
    async def unban_command(self, ctx, arg, reason='Sem motivo aparente'):
        """
        Todos merecem uma segunda chance, não é ?
        """
        banned_users = await ctx.guild.bans()
        arg = int(arg)
        for BanEntry in banned_users:
            if BanEntry.user.id == arg:
                await ctx.guild.unban(BanEntry.user)
                await ctx.send(f'Usuario desbanido pelo seguinte motivo: \n {reason}')
                await BanEntry.user.send(f'Você foi desbanido pelo: \n{ctx.author.mention} \nPelo seguinte motivo: \n{reason}')
            else:
                await ctx.send('Usuario não encontrado.')
def setup(bot: Bot):
    bot.add_cog(Moderation(bot))
