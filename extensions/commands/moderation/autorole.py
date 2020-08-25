from discord.ext.commands import Bot, Cog, command, has_permissions, bot_has_permissions, cooldown, BucketType, CheckFailure
from discord import User, Member, Embed
from discord.ext.commands.errors import CheckFailure
from asyncio import TimeoutError, sleep
from discord.utils import get, find
from database import reactiondb as db
import asyncio

class reactionRole(Cog): 
    def __init__(self, bot: Bot):
        self.bot = bot
    @cooldown(1,8,BucketType.user)
    @has_permissions(ban_members=True)
    @bot_has_permissions(ban_members=True)
    @command(name='autorole', usage='t!autorole criar', parent='criar')

    async def autorole_command(self, ctx):
        message = await ctx.send('Deseja criar um cargo atribuido automáticamente?\n - Reaja para continuar.')
        await sleep(0.2)
        await message.add_reaction('✅')

        def check(r, u):
            start = str(r.emoji) == '✅' and r.message.id == message.id and u == ctx.author
            return start
        def check_message(m):
            start = m.author == ctx.author and m.channel == message.channel
            return start
        try:
            await self.bot.wait_for("reaction_add", check=check, timeout=60)
            await message.clear_reaction('✅')
            await message.edit(content="Iniciando a configuração de cargo automático...")
            await sleep(0.3)
            await message.edit(content='Por favor digite no chat o id do canal que você irá usar.')
            channel = await self.bot.wait_for('message', check=check_message, timeout=180)
            await message.edit(content='Por favor, informe o id da mensagem que você quer adicionar a reação.')
            rmessage = await self.bot.wait_for('message', check=check_message, timeout=180)
            await message.edit(content='Por favor, informe o id do cargo em que você irá querer.')
            role = await self.bot.wait_for('message', check=check_message, timeout=180)
            await message.edit(content='Por favor, informe o emoji que irá utilizar.')
            emoji = await self.bot.wait_for('message', check=check_message, timeout=180)
            await ctx.send('Verificando a atual configuração...')
            
            ##Geral verification
            try:
                channel = await self.bot.fetch_channel(int(channel.content))
                rmessage = await channel.fetch_message(int(rmessage.content))
                role = ctx.guild.get_role(int(role.content))
            except Exception as error:
                print(error)
            #Embed
            embed = Embed(title='Configuração de cargo automático!',description=f'Você concorda com a configuração abaixo?', colour=ctx.author.color)
            embed.set_author(name=f'{message.author}', icon_url=f'{message.author.avatar_url}')
            embed.add_field(name='Canal:', value=f'{channel.mention}')
            embed.add_field(name='Mensagem:', value=f'{message.id}')
            embed.add_field(name='Cargo:', value=role.mention)
            embed.add_field(name='Emoji:', value=emoji.content)
            message = await ctx.send(embed=embed)
            await message.add_reaction('✅')
            cache = {
                "channel": channel.id,
                "message": rmessage.id,
                "role": role.id,
                "emoji": emoji.id
            }
            self.bot.raw_reactionlist.append(cache)
            try:
                await self.bot.wait_for("reaction_add", check=check, timeout=60)
                await ctx.send('Configuração criada com sucesso.')
                await rmessage.add_reaction(emoji.content)
            except TimeoutError:
                await ctx.send('O comando foi cancelado')
                return
        except TimeoutError:
            await ctx.send('O comando foi cancelado')
            return
def setup(bot:Bot):
    bot.add_cog(reactionRole(bot))