import os
import discord
from dotenv import load_dotenv

from discordBot.Services.botService import BotService

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('/r6bot rankUs'):
        await message.channel.send(BotService.rankUs())


client.run(os.getenv('TOKEN'))