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
    
    if message.content.startswith('/r6bot mmr'):
        await message.channel.send(BotService.mmr())
    
    if message.content.startswith('/r6bot kill chart'):
        await message.channel.send(file=discord.File(BotService.charts(), 'kd_charts.png'))


client.run(os.getenv('TOKEN'))