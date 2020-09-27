import os
import sqlite3
import discord

from datetime import datetime,timezone
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get

load_dotenv()

OWNER = os.getenv('OWNER')
TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD = os.getenv('DISCORD_GUILD')
CHANNEL_TIMERS = os.getenv('CHANNEL_TIMERS')
DATABASE_TIMERS = os.getenv('DATABASE_TIMERS')

conn = sqlite3.connect(DATABASE_TIMERS)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

client = discord.Client()

@client.event
async def on_ready():
    print('Connected...')
    await process_timers()
    return await client.logout()



async def process_timers():
    try:
        now = int(datetime.now(timezone.utc).strftime('%s'))
        query = "SELECT * FROM Timers WHERE endTime < ?"
        results = cursor.execute(query, (now,)).fetchall()

        if results:

            for row in results:
                guild = get(client.guilds, name='YMOC')
                user = guild.get_member(int(row['userId']))

                if row['type'] == 'A':
                    type = 'Academy'
                if row['type'] == 'C':
                    type = 'Companion Hall'
                if row['type'] == 'H':
                    type = 'Heir'

                await user.send('Your {} timer is complete'.format(type))

                query="DELETE FROM Timers WHERE id=?"
                print(row['id'])
                cursor.execute(query, (row['id'],))
                conn.commit()
    except Exception as error:
        print('There was an exception in running Timers crons: {}'.format(error))


client.run(TOKEN, bot=True, reconnect=True)
