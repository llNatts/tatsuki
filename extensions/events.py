from discord.ext.commands import Bot, Cog, Context
from discord import Message, Member, Game, Reaction, Embed
from discord.utils import get, find

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

def setup(bot: Bot):
    bot.add_cog(Events(bot))