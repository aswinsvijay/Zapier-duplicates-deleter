from dotenv import load_dotenv
load_dotenv()

import os
TOKEN = os.getenv("DISCORD_TOKEN")

import re
import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} is ready.')

@client.event
async def on_message(message : discord.Message):
    if message.author == client.user:           #if message is from this bot itself, ignore
        return

    #regular expression to search is stored in the bot's nickname
    #command to set RegEx for primary key
    if message.content.startswith("!set-key"):
        await message.guild.me.edit(nick=client.user.name + message.content[8:])
        await message.delete()                      #command deleted from channel to avoid unnecessary cluttering
        return

    #command to reset RegEx setting
    if message.content == "!reset-key":
        await message.guild.me.edit(nick=client.user.name)
        await message.delete()                      #command deleted from channel to avoid unnecessary cluttering
        return

    if not message.guild.me.nick:                   #if nickname is a NoneType object(no nickname)
        key = message.content.split('\n')[0]        #first line as primary key(default behaviour)
    else:
        pattern = message.guild.me.nick[len(client.user.name)+1:]        #extracting RegEx from nickname
        for i in message.content.split('\n'):       #split by lines
            key = re.search(pattern,i)              #searching for the pattern
            if key:                                 #if match found
                key = i                             #that line is taken as the key
                break

    if key:
        #history() gives messages in reverse chronological order
        #flag is used to skip the first occurence(the latest message)
        flag = False
        async for i in message.channel.history():
            if key in i.content.split('\n'):        #if key match is found
                if not flag:                        #set flag to True the first time
                    flag = True
                else:                               #delete when found the next time
                    await i.delete()

client.run(TOKEN)