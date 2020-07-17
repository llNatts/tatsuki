from discord.ext.commands import Bot, Cog, Context
from discord import Message, Member, Game, Reaction, Embed
from discord.utils import get, find
from discord.ext.commands.errors import *
from discord.errors import *
from difflib import get_close_matches
from asyncio import TimeoutError

class Events(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_member_join(self, member: Member):
        memberEmbed = Embed(title='🥳 | Seja bem vindo', colour=member.color, description=f'Bem vindo ao servidor {member.mention}, espero que você fique a vontade para conversar com nossa comunidade XD')
        memberEmbed.set_author(name=member.name,icon_url=member.avatar_url if member.avatar_url else member.default_avatar_url)
        memberEmbed.set_image(url="https://1.bp.blogspot.com/-Zy9fqOW8GFY/XOWeahMi46I/AAAAAAAAcS4/-QsUIa7bGigVsdfXCxCr3Am-r3BGnh49wCLcBGAs/s1600/kawaii-cute-fofo-anime-gif%2B%252817%2529.gif")

        channel = get(member.guild.text_channels, id=732046615170515005)
        memberRole = get(member.guild.roles, name="[Membro]")
        await member.add_roles(memberRole)
        await channel.send(embed=memberEmbed)
        
    @Cog.listener()
    async def on_ready(self):
        print("="*20)
        print('Logged in as:')
        print('Username: ' + self.bot.user.name)

    @Cog.listener()
    async def on_command_error(self, ctx: Context, error: CommandError):
        if isinstance(error, CommandNotFound):
            matches = get_close_matches(ctx.invoked_with, self.bot.commands_calls) 
            if matches:
                await ctx.message.add_reaction('❔')

                def check(reaction, user) -> bool:
                    return str(reaction.emoji) == '❔' and \
                           reaction.message.id == ctx.message.id and \
                           user == ctx.author

                try:
                    await self.bot.wait_for("reaction_add", check=check, timeout=30)
                except TimeoutError:
                    pass
                else:
                    commands = '.'.join(matches)
                    await ctx.send(f"Os comandos parecidos com `{ctx.invoked_with}` são:```{commands}.```Para saber como utiliza-los, use o comando `{ctx.prefix}help nome_do_commando`!")

            else:
                await ctx.message.add_reaction('❌')

        elif isinstance(error, MissingPermissions):
            missing_permissions = ', '.join(error.missing_perms)
            await ctx.send(f"Você não possuí permissões o suficientes para executar este comando.\nPermissões faltantes: `{missing_permissions}`")

        elif isinstance(error, MissingRequiredArgument):
            parameters = [f"[{param}]" for param in ctx.command.clean_params]
            parameters = ' '.join(parameters)
            await ctx.send(f"```{ctx.invoked_with} {parameters}```")

        elif isinstance(error, BotMissingPermissions):
            missing_permissions = ', '.join(error.missing_perms)
            await ctx.send(f"Eu não possuo permissões o suficientes para executar este comando.\nPermissões faltantes: `{missing_permissions}`")

        elif isinstance(error, BadArgument):
            await ctx.send(f"Você me passou uma informação errada para o comando `{ctx.invoked_with}`!")

        elif isinstance(error, CommandInvokeError):
            if isinstance(error.original, NotImplementedError):
                message = "O comando `{}` ainda não foi implementado.".format(
                    ctx.invoked_with
                )
                await ctx.send(message)
            else:
                raise error
        else:
            raise error

def setup(bot: Bot):
    bot.add_cog(Events(bot))