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

class CompanionTimer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.dbtimers = sqlite3.connect(DATABASE_TIMERS)
        self.dbtimers.row_factory = sqlite3.Row
        self.dbuserprefs = sqlite3.connect(DATABASE_USER_PREFS)
        self.cursortimers = self.dbtimers.cursor()
        self.cursoruserprefs = self.dbuserprefs.cursor()

    @commands.group(
        name='companion',
        description='Companion Hall timer commands',
        aliases=['c', 'ct', 'paint', 'music', 'room']
    )
    async def companion(self, ctx):
        if ctx.invoked_subcommand is None:
            try:

                user = ctx.author.id
                channel_timers = self.getTimersChannel(ctx)
                channel_companion_hall = self.getCompanionHallChannel(ctx)

                activeTimer = self.getActiveTimer(user)
                if activeTimer:
                    message = """{} you already have an Companion Hall timer running.  Stop or restart your timer instead:\n`!companion stop`\n`!companion restart`""".format(ctx.author.mention)
                    await channel_timers.send(message)

                else:
                    self.startTimer(user)

                    message = """{} your Companion Hall timer is set to expire in 2 hours!""".format(ctx.author.mention)
                    await channel_timers.send(message)

                    message = "@everyone {} has started a Companion Hall room! Go get it.".format(ctx.author.mention)
                    await channel_companion_hall.send(message)
            except Exception as error:
                print(error)
        return

    @companion.command()
    async def stop(self, ctx):
        try:
            user = ctx.author.id
            channel_timers = self.getTimersChannel(ctx)

            activeTimer = self.getActiveTimer(user)

            if activeTimer:
                self.stopTimer(activeTimer)

                message = """{} your Companion Hall timer has been stopped!""".format(ctx.author.mention)
                await channel_timers.send(message)
            else:
                message = """{} you have no active Companion hall timers.  Start one by typing `!companion`""".format(ctx.author.mention)
                await channel_timers.send(message)
        except:
            message = self.getErrorMessage(ctx)
            return await ctx.author.send(message)

    @companion.command()
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

            message = """{} your Companion Hall timer set to expire in 2 hours!""".format(ctx.author.mention)
            await channel_timers.send(message)

            message = "@everyone {} has started a Companion Hall room! Go get it.".format(ctx.author.mention)
            await channel_companion_hall.send(message)

        except:
            message = self.getErrorMessage(ctx)
            return await ctx.author.send(message)

    @companion.command()
    async def help(self, ctx):
        message = """```!companion\n
This command will start a timer for 3 hours and remind you when your Companion Hall is complete.  It will also notify everyone in #{} to join your room!\n\n
!companion stop\n
This command will remove your timer for the Companion Hall\n\n
!companion restart\n
This command will restart your timer for the Companion Hall\n\n
Shortcuts: !c, !ct, !paint, !music, !room
        ```""".format(CHANNEL_COMPANION_HALL)
        return await ctx.send(message)

    def getErrorMessage(self, ctx):
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

            return self.cursortimers.execute(query, (user, now, 'C')).fetchone()

        except sqlite3.Error as error:
            print("Failed to getActiveTimer record from table", error)

    def startTimer(self, user):
        try:
            endTime = self.timeNow() + (60 * 60 * 2)
            query = "INSERT INTO Timers (userId, endTime, type) VALUES (?, ?, ?)"

            self.cursortimers.execute(query, (user, endTime, 'C'))
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
    bot.add_cog(CompanionTimer(bot))