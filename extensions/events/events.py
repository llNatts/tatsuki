from discord.ext.commands import Bot, Cog, Context
from discord import Message, Member, Game, Reaction, Embed, ActivityType, Activity
from discord.utils import get, find
from discord.ext.commands.errors import *
from discord.errors import *
from difflib import get_close_matches
from asyncio import TimeoutError
from discord.message import *

class events(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        
    @Cog.listener()
    async def on_ready(self):
        print("="*20)
        print('Logged in as:')
        print('Username: ' + self.bot.user.name)
        await self.bot.change_presence(activity=Activity(type=ActivityType.watching, name="Animes em: animeshouse.netㅤㅤㅤㅤㅤㅤㅤㅤㅤPrecisa de ajuda ? Me mencione"))


    
    @Cog.listener()
    async def on_command(self, ctx: Context):
        print(f'[LOG]: O usuário {ctx.author} usou o comando {ctx.command}')

    @Cog.listener()
    async def on_reaction_add(self,reaction: Reaction, member: Member):
        print(reaction,member)
    @Cog.listener()
    async def on_raw_reaction_add(self, payload):
        print(payload)

    @Cog.listener()
    async def on_command_error(self, ctx: Context, error: CommandError):
        if isinstance(error, CommandNotFound):
            await ctx.message.add_reaction('❔')

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
        elif isinstance(error, CommandOnCooldown):
            await ctx.send(f'Você está em cooldown, por favor tente novamente em {error.retry_after:.0f} segundos!')
        else:
            raise error
def setup(bot: Bot):
    bot.add_cog(events(bot))