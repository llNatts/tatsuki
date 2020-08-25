from discord.ext.commands import Cog, command, Bot
from discord.utils import get, find
from discord import Member, Embed, User
import database.usersdb


class Usuario(Cog):
	def __init__(self, bot: Bot):
		self.bot = Bot

	@command(name="profile", usage="t!profile <usuário>")
	async def profile_command(self, ctx, member: Member=None):
		if not member:
			member = ctx.author

		collection = database.usersdb.usersReturnList(member)
		print(collection)
		if not collection:
			await ctx.send("Não foi possivel encontrar alguma informação sua, por favor chame um administrador.")
			return
		pembed = Embed(title=f"{member.name} perfil", description=f"Aqui terá todas as informações do {member.name}")
		pembed.set_author(name=ctx.author.name, icon_url=member.avatar_url)
		pembed.set_thumbnail(url=member.avatar_url)
		pembed.add_field(name="Dinheiro total:", value=collection['coins'], inline=True)
		pembed.add_field(name="Respeito:", value="not implemented", inline=True)
		pembed.add_field(name="level:", value=collection['level'], inline=True)
		pembed.add_field(name="Avisos:", value="Not implemented", inline=False)
		pembed.add_field(name="Emblemas:", value="not implemented")
		await ctx.send(embed=pembed)
		
def setup(bot: Bot):
 	bot.add_cog(Usuario(bot)) 
