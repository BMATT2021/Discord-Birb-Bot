# bot.py
import os

import discord 
import random 
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} has connected to Discord!'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - ' .join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}') 

bot = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!chirp'):
        msg = '*chirp chirp* {0.author.mention}'.format(message)
        channel = client.get_channel(684920301431291986)
        await channel.send(msg) 

@bot.event
async def on_message(message):
    if message.author == client.user:
        return
        
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, Yo *chirp* Thanks for Joining *chirp* !')
   
client.run(TOKEN)

