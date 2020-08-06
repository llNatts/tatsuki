from discord.ext.commands import Bot, Cog, command, has_permissions, bot_has_permissions, cooldown, BucketType
from discord import User, Member, Embed
from asyncio import TimeoutError, sleep
from discord.utils import get, find
import asyncio

class Moderation(Cog):

    def __init__(self, bot: Bot):
        self.bot = bot


    @cooldown(1,8,BucketType.user)
    @command(name='clear', usage='t!clear <quantidade de mensagem>')
    @has_permissions(manage_messages=True)
    @bot_has_permissions(manage_messages=True)
    async def clear_message(self, ctx, arg=None):
        channel = ctx.message.channel
        if not arg: 
            await ctx.send('Você não especificou a quantidade de mensagem')
        else:
            await channel.purge(limit=int(arg)+ 1)
            await channel.send(f'Deletei as {arg} mensagens que você pediu {ctx.author.mention}')

def setup(bot: Bot):
    bot.add_cog(Moderation(bot))

