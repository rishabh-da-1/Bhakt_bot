import discord
from discord.ext import commands
from Economy.eco import col,__increase_BKTC__,cool_down

class events__(commands.Cog):
    def __init__(self,bot):
        self.bot= bot
    
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.content == 'ram':
            __increase_BKTC__(message.author.id)
            
        if message.content == 'Ram':
            __increase_BKTC__(message.author.id)
        if message.content == 'RAM':
            __increase_BKTC__(message.author.id)
        if message.content == 'राम':
            __increase_BKTC__(message.author.id)
        if message.content.startswith(''):
            cool_down(message.author.id)

