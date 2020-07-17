from discord.ext.commands import Bot, Cog, Context, errors
from discord.ext.commands.errors import *
from difflib import get_close_matches

class Erros(Bot):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_command_error(self, ctx, error):
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

        elif isinstance(error, (MissingRequiredArgument, BadArgument)):
            command = ctx.command
            await ctx.send("```" + command.usage + "```")

        elif isinstance(error, BotMissingPermissions):
            await ctx.send(f"Eu não possuo permissões o suficientes para executar este comando.\nPrecisa das seguintes permissões:```{pontuar(error.missing_perms)}.```")

        elif isinstance(error, MissingPermissions):
            await ctx.send(f"Você não possui permissões o suficientes para executar este comando.\nVocê precisa das seguintes permissões:```{pontuar(error.missing_perms)}.```")

        else:
            return error

def setup(bot: Bot):
    bot.add_listener(Erros(bot))