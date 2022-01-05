import discord
from discord.ext import commands
from Economy.eco import __register__,col,path_main
import pandas  as pd

class commands__ (commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def reg(self,ctx):
        userD = str(ctx.message.author.id)
        
        file = open(path_main)
        reader = pd.read_csv(file , names=col)
        
        uid = reader.userid.tolist()
        
        if userD in uid:
            await ctx.send('you already have a account')
        else :
            await ctx.send("Account created :white_check_mark: ")
            __register__(userD,ctx.message.author.name)
    @commands.command()
    async def wallet(self,ctx):
        uD = str(ctx.message.author.id)

        file = open(path_main)
        reader = pd.read_csv(file,names=col)
    
        user_id = reader.userid.tolist()  
        BKTC = reader.coins.tolist()

        if uD in user_id:
            index = user_id.index(uD)
            emet = discord.Embed(description = f"{ctx.message.author.name} wallet", color = discord.Color.orange())
            emet.set_thumbnail(url=ctx.author.avatar_url)
            emet.add_field(name = 'BKTC', value = BKTC[index])
            await ctx.send(embed = emet)
        else :
            await ctx.send("you dont have an account yet! do `B!reg` to create one")