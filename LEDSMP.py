import discord
from discord.ext import commands
import requests

################### change these to your liking ###################

token = "OTczNDcxMDM5ODQzNTk4MzY2.GxtxOl.nqHIF6j1QyU4XiEycweDh-m2foqBn1NHGuxZxY"
prefix = "!"
title = "IP"
desc ="LEDSMPQZ8a.aternos.me Version: 1.17.1"
field = "LEDSMPQZ8a.aternos.me"
###################################################################


client = commands.Bot(command_prefix = prefix)
client.remove_command('help')

@client.event
async def on_ready():
    print('')
    print('----------------')
    print('LED SMP BOT ON  ')
    print('----------------')

main = discord.Embed(title=title,description=desc,color=0xcf4948)

@client.command()
async def ip(ctx):
    await ctx.send('Check Your DM')
    await ctx.author.send(embed=main)
  





client.run(token)