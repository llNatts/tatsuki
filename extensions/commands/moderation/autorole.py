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
    @command(name='autorole', usage='t!autorole')

    async def autorole_command(self, ctx):
        raise NotImplementedError()
        # message = await ctx.send('Você está pronto para configurar um autorole?')
        # await sleep(1)
        # await message.add_reaction('✅')
        # await sleep(1)
        # await message.add_reaction('🇽')

        # def check(r, u):
        #     return str(r.emoji) == '✅' and r.message.id == message.id and u == ctx.author

        # try:
        #     await self.bot.wait_for("reaction_add", check=check, timeout=120)
        # except TimeoutError:
        #     await message.edit(content="Você demorou demais...")
        #     return
        # await ctx.send('Por favor, digite o id do canal em que você quer adicionar o cargo por emoji')
        # textID = await self.bot.wait_for('message', check=None, timeout=120)
        # if textID.author != ctx.author:
        #     return
        # try:
        #     channel = get(ctx.guild.text_channels, id=int(textID.content))
        # except Exception as error:
        #     await ctx.send(f'Não foi possível adicionar encontrar este canal!\n Motivo: {error}')
        #     return
        # await ctx.send('Ótimo, agora me forneça o id da mensagem que você quer por o emoji')
        # messageID = await self.bot.wait_for('message', check=None, timeout=120)
        # if messageID.author != ctx.author:
        #     return
        # try:
        #     messager = await channel.fetch_message(int(messageID.content))
        # except Exception as error:
        #     await ctx.send(f'Não foi possível encontrar está mensagem\nMotivo: {error}')
        #     return
        # await ctx.send('E por ultimo, me forneça o emoji em que você quer adicionar')
        # emojiID = await self.bot.wait_for('message', check=None, timeout=120)

        # await messager.add_reaction(emojiID.content)
        # ctx.send('Você adicionou um Reaction Role')
def setup(bot: Bot):
    bot.add_cog(Moderation(bot))