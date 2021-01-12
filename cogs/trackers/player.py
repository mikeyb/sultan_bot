import os
import sys
import sqlite3

from datetime import datetime,timezone
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get

load_dotenv()

CHANNEL_TRACKERS = os.getenv('CHANNEL_TRACKERS')
DATABASE_TRACKERS = os.getenv(DATABASE_TRACKERS)

class PlayerTracker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn = sqlite3.connect(DATABASE_TRACKERS)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    @commands.group(
        name='player',
        description='Player tracker commands',
        aliases=['p', 'pt']
    )
    async def player(self, ctx):
        if ctx.invoked_subcommand is None:
            pass

def setup(bot):
    bot.add_cog(PlayerTracker(bot))