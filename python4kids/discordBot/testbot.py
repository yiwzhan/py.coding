
import discord
import math
from discord.ext import commands

client = commands.Bot(command_prefix = 'b.')


@client.event
async def on_ready():
    print("bot is ready ")

@client.command()
async def hi(ctx):
    await ctx.send(f"hi, {ctx.author.display_name}")

@client.command()
async def tell_server(ctx):
    await ctx.send(f"this is, {ctx.guild.name}")
@client.command()
async def andrew_is(ctx):
    await ctx.send("dumb" )

@client.command()
async def whos_better(ctx):
    await ctx.send(f"Im better than you")

@client.command()
async def g(ctx):
    await ctx.send(" ")
@client.command()
async def ad(ctx):
    await ctx.send("andrew")

client.run('NzMxOTY3MzE1NjQ1Njk0MDUz.Xwz17A.PcEkWF25zVXyRwEENi815FrWEDk')