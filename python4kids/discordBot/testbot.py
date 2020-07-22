import discord
from discord.ext import commands
import random


list1=["stop","no","yes","ask again"]
bob=random.randint(1,len(list1))
client = commands.Bot(command_prefix = 'b.')


@client.event
async def on_ready():
    print("bot is ready ")

@client.command()
async def hi(ctx):
    await ctx.send(f"hi, {ctx.author.display_name}")

@client.command()
async def server(ctx):
    await ctx.send(f"this is, {ctx.guild.name}")

@ client.command()
async def embed(ctx):
    # help = {
    #     'hi':'says hi back',
    #     'server':'tells what server',
    #     'helplist':'shows helplist',
    #     'eightball':'hi'
    # }
    embed = discord.Embed(
        title = "hi",
        description = "hi"    
    )
    embed.add_field(name = "field", value = "   ___ ")
    await ctx.send(embed = embed)
    
    


@client.command()
async def eightball(ctx):
    bob=random.randint(1,len(list1))
    await ctx.send(list1[bob-1]) 

# @client.command()
# async def m(ctx):
#     await ctx.send("andrew")

client.run('NzMxOTY3MzE1NjQ1Njk0MDUz.XxSmQg.UbnZwiQEdwwPYgA1sWhMgI4sKt0')