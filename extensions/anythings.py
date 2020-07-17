from discord.ext.commands import Cog, command, Bot
from discord import Member, Embed, User


class Anythings(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @command(name="avatar", usage="t!avatar <usuário>")
    async def teste_command(self, ctx, member: Member=None):
        """
            Pegue o avatar seu ou de algum amigo XD.
        """
        if not member:
            member = ctx.author
        imgEmbed = Embed(title="Temos um ladrão de fotos", description=f"O {ctx.author.mention} roubou o avatar de {member.mention}",colour=ctx.author.color)
        imgEmbed.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
        imgEmbed.set_image(url=member.avatar_url)
        try:
            await ctx.send(embed=imgEmbed)
        except Exception as error:
            await ctx.send('Ocorreu um erro: ' + error)

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
    bot.add_cog(Anythings(bot))