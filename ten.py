from itertools import cycle
import discord
import random
import requests
from discord.ext import commands, tasks 
from itertools import cycle
import os
import json


client = commands.Bot(command_prefix=".")
STATUS_TIME = 2000


aliens = ["Cannonbolt", "Overflow", "Heatblast", "XLR8", "Four Arms", "Grey Matter", "Diamondhead", "Upgrade", "Stinkfly", "Wildvine", "Gax", "Shock Rock", "Slapback", "Humungousaur", "Rath", "Jetray", "Goop", "Way Big", "Surge", "Spidermonkey", "Buzzshock", "Big Chill", "Chromastone", "Ampfibian", "Ripjaws", "Wildmutt", "Upchuck", "Ditto", "Eye Guy", "Ghostfreak", "Brainstorm", "Echo Echo", "Lodestar", "JuryRigg", "The Worst", "Feedback", "Gravattack", "Walkatrout", "NRG"]
randomWords = ["soooxy woooonkie on the boonkie", "AWGOOOOOOOOOOO GOOOOOOOAAA BOOOOOOOOOO", "booonkie woonkie", "soooooxys 4 lite", "big ZOINKSYER HEHE", "mooooooooooooooooooooooooooooooonkay", "the soooooxi squid", "HAHSKDHASJHDAKJSHDUWADJAHSDKJASDJKAHDJASHDJASHDJA - splitzzy"]
status = cycle(["big zoinks.", "slap grandpa max", "goms"])
soosImage = "https://tenor.com/view/boiled-soundcloud-boiled-boiled-irl-boiled-utsc-boiled-cheesestick-agem-soundcloud-gif-20049996"
# api

def generateMeme():
    global response
    global preview
    response = requests.get("https://meme-api.herokuapp.com/gimme")
    preview = response.json()['preview'][2]

generateMeme()

# def genMit():
#     path = r"./images/"
#     global random_filename
#     random_filename = random.choice([
#         x for x in os.listdir(path)
#         if os.path.isfile(os.path.join(path, x))
#     ])


def generateAlienName(aliens):
    pickAlien = random.choice(aliens)
    return pickAlien

@client.event
async def on_ready():
    change_status.start()
    print("bot ready..")

@tasks.loop(seconds=STATUS_TIME)
async def change_status():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(next(status)))

@client.command(pass_context=True)
async def gen(ctx, member: discord.Member):
    generated = generateAlienName(aliens)
    await member.edit(nick=generated)
    aliens.remove(generated)
    await ctx.send(f'User is morphed into {member.mention} ')

@gen.error
async def gen_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("make sure you at the user using @...")


# simple clear function clears chat :)
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def cls(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

# kick player
@client.command()
async def kick(ctx, member : discord.Member, *, reason="None"):
    await member.kick(reason=reason)
    await ctx.send(f"Alien {member} got whooped!")

# ban player
@client.command()
async def ban(ctx, member : discord.Member, *, reason="None"):
    await member.ban(reason=reason)
    await ctx.send(f"Zoinked {member.mention} out!")

# unban perm
@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Alien X Resed {user.mention}")
            return


# error commands
@client.event 
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("bad command zoinks. hehee")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


# mute function command
@client.command(description="shutting people up :)")
@commands.has_permissions(manage_messages=True)
async def mute(ctx,member:discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages= False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"zipped {member.mention} mouth for reason: {reason}")
    await member.send(f"your mouth got shut in the server {guild.name} for reason:  {reason}")


# unmute
@client.command(description="unshuts their boonkie moooouth")
@commands.has_permissions(manage_messages= True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"unzipped ur doonkie mooouth, {member.mention}")
    await member.send(f"you got unzoinked in the server, come speak again >> {ctx.guild.name}")

# random iamges of mit
# @client.command()
# @commands.has_permissions(kick_members=True)
# async def mit(ctx):
#     genMit()
#     await ctx.send(file=discord.File(f"./images/{random_filename}"))
#     randomOutput = random.choice(randomWords)
#     await ctx.send(randomOutput)

@client.command()
async def meme(ctx):
    generateMeme()
    await ctx.send(preview)


@client.command()
async def joke(ctx):
    await ctx.send(f"your a joke... ")


@client.command()
async def gom(ctx):
    await ctx.send("@everyone ayo woooski soooxies anyone wooona hoopster onster to gom")


@client.command()
async def soos(ctx):
    await ctx.send(soosImage)

client.run("ODkzMDkxNDMzMjY1ODkzNDU2.YVWaNg.ifrgySRChu2qj5ncc3keKLMpL70")