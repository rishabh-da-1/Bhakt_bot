import discord
import os
from discord.ext import commands
import pandas as pd

from src.info import __info__
from src.gif import __gifs__


from cog_commands import commands__
from cog_events import events__
from Economy.eco import __register__,__increase_BKTC__,col,cool_down

token = __info__["token"] 
prefix = __info__["prefix"]

client = commands.Bot(command_prefix="B!")

client.add_cog(commands__(client))
client.add_cog(events__(client))

@client.event
async def on_ready():
    print('logged in ')
    await client.change_presence(activity=discord.Activity
                    (  type=discord.ActivityType.listening, name='Bhakti songs'))


client.run(token)