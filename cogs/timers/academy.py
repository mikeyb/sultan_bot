import os
import sys
import sqlite3

from datetime import datetime,timezone
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get

load_dotenv()

CHANNEL_COMPANION_HALL = os.getenv('CHANNEL_COMPANION_HALL')
CHANNEL_TIMERS = os.getenv('CHANNEL_TIMERS')
DATABASE_TIMERS = os.getenv('DATABASE_TIMERS')
DATABASE_USER_PREFS = os.getenv('DATABASE_USER_PREFS')

class AcademyTimer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.dbtimers = sqlite3.connect(DATABASE_TIMERS)
        self.dbtimers.row_factory = sqlite3.Row
        self.dbuserprefs = sqlite3.connect(DATABASE_USER_PREFS)
        self.cursortimers = self.dbtimers.cursor()
        self.cursoruserprefs = self.dbuserprefs.cursor()

    @commands.group(
        name='academy',
        description='Academy timer commands',
        aliases=[]
    )
    async def academy(self, ctx):
        if ctx.invoked_subcommand is None:
            try:

                user = ctx.author.id
                channel_timers = self.getTimersChannel(ctx)
                channel_companion_hall = self.getCompanionHallChannel(ctx)

                activeTimer = self.getActiveTimer(user)
                if activeTimer:
                    message = """{} you already have an Academy timer running.  Stop or restart your timer instead:\n`!academy stop`\n`!academy restart`""".format(ctx.author.mention)
                    await channel.send(message)

                else:
                    self.startTimer(user)

                    message = """{} your Academy timer is set to expire in 2 hours!""".format(ctx.author.mention)
                    await channel_timers.send(message)

                    message = "@everyone {} has started an Academy room! Go get it.".format(ctx.author.mention)
                    await channel_companion_hall.send(message)
            except:
                message = self.getErrorMessage(ctx)
                await channel.send(message)
        return

    @academy.command()
    async def stop(self, ctx):
        try:
            user = ctx.author.id
            channel = self.getTimersChannel(ctx)

            activeTimer = self.getActiveTimer(user)

            if activeTimer:
                self.stopTimer(activeTimer)

                message = """{} your Academy timer has been stopped!""".format(ctx.author.mention)
                await channel.send(message)
            else:
                message = """{} you have no active Academy timers.  Start one by typing `!academy`""".format(ctx.author.mention)
                await channel.send(message)
        except:
            message = self.getErrorMessage(ctx)
            await channel.send(message)

    @academy.command()
    async def restart(self, ctx):
        try:
            user = ctx.author.id
            channel_timers = self.getTimersChannel(ctx)
            channel_companion_hall = self.getCompanionHallChannel(ctx)

            activeTimer = self.getActiveTimer(user)

            if activeTimer:
                self.stopTimer(activeTimer)
                self.startTimer(user)
            else:
                self.startTimer(user)

            message = """{} your Academy timer set to expire in 2 hours!""".format(ctx.author.mention)
            await channel_timers.send(message)

            message = "@everyone {} has started an Academy room! Go get it.".format(ctx.author.mention)
            await channel_companion_hall.send(message)

        except:
            message = self.getErrorMessage(ctx)
            await channel.send(message)

    @academy.command()
    async def help(self, ctx):
        message = """
This command will start a timer for 2 hours and announce to the union you have opened an Academy room.
        """
        return

    def getErrorMessage(ctx):
        return """
        {} something went wrong.  Please try again in a few minutes.
        """.format(ctx.author.mention)

    def getTimersChannel(self, ctx):
        return get(ctx.guild.channels, name=CHANNEL_TIMERS)

    def getCompanionHallChannel(self, ctx):
        return get(ctx.guild.channels, name=CHANNEL_COMPANION_HALL)

    def getActiveTimer(self, user):
        try:
            now = self.timeNow()
            query = "SELECT * FROM Timers WHERE userId = ? AND endTime > ? AND type = ? ORDER BY endTime DESC LIMIT 1"

            return self.cursortimers.execute(query, (user, now, 'A')).fetchone()

        except sqlite3.Error as error:
            print("Failed to getActiveTimer record from table", error)

    def startTimer(self, user):
        try:
            endTime = self.timeNow() + (60 * 60 * 2)
            query = "INSERT INTO Timers (userId, endTime, type) VALUES (?, ?, ?)"

            self.cursortimers.execute(query, (user, endTime, 'A'))
            self.dbtimers.commit()

            return True
        except sqlite3.Error as error:
            print("Failed to insert startTimer record to table", error)

    def stopTimer(self, timer):
        try:
            query = "DELETE FROM Timers WHERE id=?"
            self.cursortimers.execute(query, (timer['id'],))
            self.dbtimers.commit()
            return True
        except sqlite3.Error as error:
            print("Failed to delete record from table", error)

    def timeNow(self):
        return int(datetime.now(timezone.utc).strftime('%s'))

def setup(bot):
    bot.add_cog(AcademyTimer(bot))