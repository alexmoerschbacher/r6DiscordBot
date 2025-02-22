import os
import discord
from dotenv import load_dotenv
from discordBot.Services.botService import BotService

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

botService = BotService()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message: discord.message):
    if message.author == client.user:
        return
    
    if message.content.startswith('/r6bot rankUs'):
        await message.channel.send(botService.rankUs(message))
    
    if message.content.startswith('/r6bot mmr'):
        await message.channel.send(botService.mmr(message))
    
    if message.content.startswith('/r6bot kill chart'):
        charts = botService.charts(message)
        if isinstance(charts, (str)):
            await message.channel.send(charts)
        await message.channel.send(file=discord.File(charts, 'kd_charts.png'))
    
    if message.content.startswith('/r6bot help'):
        await message.channel.send(botService.help())

    if message.content.startswith('/r6bot add user'):
        await message.channel.send(botService.addUser(message))
    
    if message.content.startswith('/r6bot remove user'):
        await message.channel.send(botService.removeUser(message))


client.run(os.getenv('TOKEN'))