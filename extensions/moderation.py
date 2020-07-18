from discord.ext.commands import Bot, Cog, command, has_permissions, bot_has_permissions, cooldown, BucketType
from discord import User, Member, Embed
from extensions import events
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
    async def unban_command(self, ctx, arg, reason='Por conselho melhor, o {target.mention} foi desbanido.'):
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

    @cooldown(1,8, BucketType.user)
    @has_permissions(administrator=True)
    @bot_has_permissions(administrator=True)
    @command(name='autorole', usage='!autorole <channel> <message> <role> <emoji>')
    async def react_role(self, ctx, *arg):
        raise events.CommandNotFound()

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

