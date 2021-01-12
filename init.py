import os
import discord

from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()

OWNER = os.getenv('OWNER')
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

def get_prefix(client, message):
    prefixes = ['!', '!!']
    return commands.when_mentioned_or(*prefixes)(client, message)

bot = commands.Bot(
    owner_id = OWNER,
    command_prefix = get_prefix,
    case_insensitive = True
)

cogs = [
    'cogs.admin.loading',
    'cogs.timers.academy',
    'cogs.timers.companion',
]

@bot.event
async def on_ready():
    print('Connected...')
    for cog in cogs:
        print('loading extension: ' + cog)
        bot.load_extension(cog)

if __name__ == '__main__':
    bot.run(TOKEN, bot=True, reconnect=True)