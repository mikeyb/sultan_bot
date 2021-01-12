import os
import sys
import sqlite3

from datetime import datetime,timezone
from dotenv import load_dotenv
from discord import Embed
from discord.ext import commands
from discord.utils import get

load_dotenv()

OWNER = os.getenv('OWNER')
CHANNEL_TRACKERS = os.getenv('CHANNEL_TRACKERS')
DATABASE_TRACKERS = os.getenv('DATABASE_TRACKERS')

class VizierTracker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn = sqlite3.connect(DATABASE_TRACKERS)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def is_owner(ctx):
        return str(ctx.message.author.id) == str(OWNER)

    @commands.group(
        name='vizier',
        description='Vizier tracker commands',
        aliases=['v', 'vt']
    )
    async def vizier(self, ctx,
        name: str = None
    ):
        subcommand = ctx.invoked_subcommand
        channel_trackers = self.getTrackersChannel(ctx)

        if subcommand is 'list':
            vizier = await self.getVizierByName(ctx, name)
            if vizier is not None:
                embed = await self.getVizierMessage(ctx, vizier)
                return await channel_trackers.send(content=None, embed=embed)
            else:
                message = "{}, I was unable to find that vizier!".format(ctx.author.mention)
                return await channel_trackers.send(message)

        return

    @vizier.command()
    async def list(self, ctx):
        channel_trackers = self.getTrackersChannel(ctx)

        try:
            vizierList = await self.getVizierList(ctx)
            embeds = await self.getVizierListMessage(ctx, vizierList)

            for embed in embeds:
                await channel_trackers.send(content='', embed=embed)
            return

        except Exception as e:
            print('list exception')
            print(e)

        return

    @vizier.command()
    @commands.check(is_owner)
    async def add(self, ctx):
        channel_trackers = self.getTrackersChannel(ctx)

        if None in [rank,name,unionId,initials,leader,leaderId]:
            message = "!vizier add ..."
            return await channel_trackers.send(message)

        try:
            pass
        except:
            return

        return

    @vizier.command()
    @commands.check(is_owner)
    async def delete(self, ctx):
        channel_trackers = self.getTrackersChannel(ctx)

        if None in [rank,name,unionId,initials,leader,leaderId]:
            message = "!vizier delete ..."
            return await channel_trackers.send(message)

        try:
            pass
        except:
            return

        return

    def getTrackersChannel(self, ctx):
        return get(ctx.guild.channels, name=CHANNEL_TRACKERS)

    async def getVizierByName(self, ctx, name: str = None):
        try:
            if name is not None:
                query = "SELECT * FROM Viziers WHERE name LIKE '%{}%' LIMIT 1".format(name)
                self.cursor.execute(query)
                vizier = self.cursor.fetchone()

                if vizier is not None:
                    return vizier

            return None

        except:
            return

    async def getVizierList(self, ctx):
        try:
            self.cursor.execute("SELECT * FROM Viziers ORDER BY id ASC")

            return self.cursor.fetchall()

        except:
            return

        return None

    async def getVizierListMessage(self, ctx, vizierList: list = []):
        try:
            if vizierList is not []:
                embeds = []
                # embed.set_thumbnail(url='')

                loops = int(len(vizierList) / 20)
                l = 1
                while l < (loops + 2):
                    embed = Embed()

                    try:
                        for v in ['name', 'primaryAttributes', 'grouping']:
                            n = 0
                            i = l * 20 - 20
                            values = ''
                            print(v)
                            while n < 20:
                                if i < len(vizierList):
                                    values = values + "{}\n".format(vizierList[i][v])
                                    n += 1
                                    i += 1
                                else:
                                    n = 20

                            embed.add_field(name=v, value=values)

                    except:
                        pass
                    embeds.append(embed)
                    l += 1

                return embeds

            return

        except Exception as e:
            print('except starting')
            print(e)

    async def getVizierMessage(self, ctx, vizier):
        embed = Embed(
            title="Vizier - {}".format(vizier['name'])
        )
        embed.set_thumbnail(url='')

        embed.add_field(name="Name", value=vizier['name'], inline=True)
        embed.add_field(name="Primary Attributes", value=vizier['primaryAttributes'], inline=True)
        embed.add_field(name="Group", value=vizier['grouping'], inline=True)
        embed.add_field(name="Description", value=vizier['description'])

        return embed


    async def addVizier(self, ctx, vizier: list = []):
        try:
            query = "INSERT INTO Vizier (name, description, primaryAttributes, grouping, consortId) VALUES ({},{},{},{},{})".format(
                int(vizier[0]),
                vizier[1],
                int(vizier[2]),
                vizier[3],
                vizier[4],
            )
            self.cursor.execute(query)
            self.conn.commit()

            return True

        except:
            return

        return None

    async def delUnion(self, ctx, vizier):
        try:
            query = "DELETE FROM Viziers WHERE id = {}".format(int(vizier.id))
            self.cursor.execute(query)
            self.conn.commit()

            return True

        except:
            return

        return None

def setup(bot):
    bot.add_cog(VizierTracker(bot))