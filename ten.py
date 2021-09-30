import discord
import random
from discord.ext import commands 

client = commands.Bot(command_prefix=".")

aliens = ["Cannonbolt", "Overflow", "Heatblast", "XLR8", "Four Arms", "Grey Matter", "Diamondhead", "Upgrade", "Stinkfly", "Wildvine", "Gax", "Shock Rock", "Slapback", "Humungousaur", "Rath", "Jetray", "Goop", "Way Big", "Surge", "Spidermonkey", "Buzzshock", "Big Chill", "Chromastone", "Ampfibian", "Ripjaws", "Wildmutt", "Upchuck", "Ditto", "Eye Guy", "Ghostfreak", "Brainstorm", "Echo Echo", "Lodestar", "JuryRigg", "The Worst", "Feedback", "Gravattack", "Walkatrout", "NRG"]

def generateAlienName(aliens):
    pickAlien = random.choice(aliens)
    return pickAlien

@client.event
async def on_ready():
    print("bot ready..")

@client.command(pass_context=True)
async def gen(ctx, member: discord.Member):
    generated = generateAlienName(aliens)
    await member.edit(nick=generated)
    aliens.remove(generated)
    # namesList = len(aliens)
    # print(namesList)
    # print(aliens)
    await ctx.send(f'User is morphed into {member.mention} ')


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

client.run("ODkzMDkxNDMzMjY1ODkzNDU2.YVWaNg.ifrgySRChu2qj5ncc3keKLMpL70")