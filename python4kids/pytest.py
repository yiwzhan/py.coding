import discord
import math
from math import sqrt
from discord.ext import commands
import random
#prefix
client = commands.Bot(command_prefix = ('yeet.', 'yeet '))
#startup
@client.event
async def on_ready():
    print("bot has connected to discord")
    game = discord.Game('Valorant sucks, play minecraft')
    await client.change_presence(status=discord.Status.idle, activity=game)