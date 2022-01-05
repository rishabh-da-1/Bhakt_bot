import discord
from discord.ext import commands


class __chat_commands__(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.content.startswith("jai shree ram"):
            await message.channel.send("jaieee shree ram!")
        if message.content.startswith('hello'):
           await message.channel.send('namaste')
 
    @commands.Cog.listener()
    async def on_ready(self):
        #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Bhakti songs'))

        print("logged in") 
    @commands.command()
    async def userinfo(self , ctx, member=discord.Member):
        await ctx.send(ctx.message.author.id)
        __user_info_embed__ = discord.Embed(colour = member.color, timestamp=ctx.message.created_at)
        __user_info_embed__.set_author(name = f"User Info = {member}")
        __user_info_embed__.set_thumbnail(url=member.avatar.url)
        __user_info_embed__.set_footer(text = f"Requested by = {ctx.author}",icon_url=ctx.author.avatar_url)
        __user_info_embed__.add_field(name = "ID",value=member.id)
        __user_info_embed__.add_field(name = "Name",value = member.display_name)
        __user_info_embed__.add_field(name = "Created at",value = member.created_at)
 
    
        