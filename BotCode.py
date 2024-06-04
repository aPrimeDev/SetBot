#Importing discord
import random
import discord
import os
from dotenv import load_dotenv

#Initializing Variables
load_dotenv('TOKEN.env')
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intent = discord.Intents.default()
intents.members = True

clients = discord.Client(command_prefix = '!', intents=intents)


client = discord.Client(intents=intents)
token = os.getenv('TOKEN')

@client.event 
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message {user_message} by {username} on {channel}')

    if message.author == client.user:
        return

    if channel == "random":
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}')
            return
        elif user_message.lower() == "im a fan":
            await message.channel.send(f'{username} Hell Nah! https://tenor.com/view/kendrick-lamar-god-is-gangsta-u-ahhh-scream-gif-6349874768192364613')

@client.event
async def on_member_join(member):
    await member.channel.send(f"Yerrr"+ member)
    return

    

        
client.run(token)