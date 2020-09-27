import os
import sqlite3

from datetime import datetime
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

DATABASE = os.getenv('DATABASE_USER_PREFS')

class UserPrefs(commands.Cog):

    def __init__(self):
        pass
