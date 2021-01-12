from dotenv import load_dotenv
load_dotenv()

import os
TOKEN = os.getenv("DISCORD_TOKEN")

import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} is ready.')

@client.event
async def on_message(message : discord.Message):
    if message.author == client.user:           #if message is from this bot itself, ignore
        return

client.run(TOKEN)
