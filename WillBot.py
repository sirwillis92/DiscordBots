# bot.py
import os
import discord
import asyncio

TOKEN = (xxxxxxxxxxxxxxxx)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    channel = client.get_channel(xxxxxxxxxxxxxxxxxxx)
    print(f'{client.user} has connected to Discord!')
    await channel.send('I have awakened')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!willbot'):
        await message.channel.send(f'Hi {message.author.name}! I\'m WillBot!')

    if message.content.startswith('!think'):
        channel = message.channel
        await channel.typing()
        await asyncio.sleep(5)
        await channel.send('Too much think')

    if message.content.startswith('!clear'):
        channel = message.channel
        await channel.purge(bulk=True, limit=10)

client.run(TOKEN)
