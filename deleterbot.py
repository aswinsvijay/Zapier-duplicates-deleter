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

    message.content = message.content.split()   #split the content by whitespaces

    #finding the email from the message
    for i in message.content:
        if '@' in i:
            mail = i
            break

    #history() gives messages in reverse chronological order
    #flag is used to skip the first occurence(the latest message)
    flag = False
    async for i in message.channel.history():
        if mail in i.content:                   #if mail is present in the message
            if not flag:                        #set flag to True the first time
                flag = True
            else:                               #delete when found the next time
                await i.delete()

client.run(TOKEN)