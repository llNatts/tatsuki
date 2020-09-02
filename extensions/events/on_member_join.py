from discord.ext.commands import Bot, Cog, Context
from discord import Member, Reaction, Embed
from discord.utils import get, find
import database.usersdb

class events(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_member_join(self, member: Member):
        try: 
            memberEmbed = Embed(title='🥳 | Seja bem-vinda(o)', colour=member.color, description=f'Bem vinda(o) ao servidor {member.mention}, espero que você fique a vontade para conversar com nossa comunidade XD')
            memberEmbed.set_author(name=member.name,icon_url=member.avatar_url if member.avatar_url else member.default_avatar_url)
            memberEmbed.set_image(url="https://i.imgur.com/34M2TPI.png")
            memberEmbed.set_thumbnail(url=member.avatar_url)
            channel = get(member.guild.text_channels, id=732046615170515005)
            memberRole = get(member.guild.roles, id=750831828990034010)
            await member.add_roles(memberRole)i
            await channel.send(embed=memberEmbed)
        except Exception as error:
            print(f'LOG: {member.guild.name}: ocorreu um erro com {member}, erro: {error}')
def setup(bot: Bot):
    bot.add_cog(events(bot))
