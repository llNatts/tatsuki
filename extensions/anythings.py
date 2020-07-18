from discord.ext.commands import Cog, command, Bot
from discord.utils import get, find
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
    # @command(name='anúncio', usage='ta!anúncio', alias=['anuncio', 'ping', 'alerta'])
    # async def ping_myself(self, ctx):
    #     memberRole = get(ctx.message.author.guild.roles, id=733941266672386149)
    #     roles = ctx.author.roles

    #     for role in roles:
    #         if role.id == memberRole.id:
    #             await ctx.send(f'O cargo {memberRole.mention} foi adicionado')
    #             await ctx.author.add_roles(memberRole
def setup(bot: Bot):
    bot.add_cog(Anythings(bot)) 