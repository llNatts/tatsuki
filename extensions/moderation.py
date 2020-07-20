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
    @command(name='clear', usage='t!clear <quantidade de mensagem>')
    @has_permissions(manage_messages=True)
    @bot_has_permissions(manage_messages=True)
    async def clear_message(self, ctx, arg=None):
        channel = ctx.message.channel
        if not arg: 
            await ctx.send('Você não especificou a quantidade de mensagem')
        else:
            await channel.purge(limit=int(arg)+ 1)
            await channel.send(f'Deletei algumas mensagens')

    @cooldown(1,8,BucketType.user)
    @has_permissions(ban_members=True)
    @bot_has_permissions(ban_members=True)
    @command(name='ban', usage='t!ban <user> <reason>')
    async def ban_member(self, ctx, target: Member, reason='O usuário quebrou as regras.'):
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

