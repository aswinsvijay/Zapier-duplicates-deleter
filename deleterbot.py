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

    key = message.content.split('\n')[0]        #first line of the message content taken as the key

    #history() gives messages in reverse chronological order
    #flag is used to skip the first occurence(the latest message)
    flag = False
    async for i in message.channel.history():
        if key == i.content.split('\n')[0]:     #if key match is found
            if not flag:                        #set flag to True the first time
                flag = True
            else:                               #delete when found the next time
                await i.delete()

client.run(TOKEN)