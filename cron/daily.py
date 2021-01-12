import os
import discord

from dotenv import load_dotenv
from discord.utils import get

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD = os.getenv('DISCORD_GUILD')
CHANNEL_UNION = os.getenv('CHANNEL_UNION')

client = discord.Client()

@client.event
async def on_ready():
    await process_reset()
    return await client.logout()

async def process_reset():
    try:
        guild = get(client.guilds, name=DISCORD_GUILD)
        channel = get(guild.channels, name=CHANNEL_UNION)

        message = "@everyone :dancer: :dancer: :dancer: :dancer: :dancer: Daily Reset :dancer: :dancer: :dancer: :dancer: :dancer:"
        await channel.send(message)
    except Exception as error:
        print('There was an exception in running daily reset crons: {}'.format(error))


client.run(TOKEN, bot=True, reconnect=True)