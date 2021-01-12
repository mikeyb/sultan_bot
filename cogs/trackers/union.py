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

class UnionTracker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn = sqlite3.connect(DATABASE_TRACKERS)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def is_owner(ctx):
        return str(ctx.message.author.id) == str(OWNER)

    @commands.group(
        name='union',
        description='Union tracker commands',
        aliases=['u', 'ut']
    )
    async def union(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.invoke(self.list)
        return

    @union.command()
    async def list(self, ctx,
        identifier: str = None
    ):
        channel_trackers = self.getTrackersChannel(ctx)

        try:
            if identifier is None:
                unionList = await self.getUnionList(ctx)
                embed = self.getUnionListMessage(ctx, unionList)

                return await channel_trackers.send(content='', embed=embed)
            else:
                union = await self.getUnionByIdentifier(ctx, identifier)

                if union is not None:
                    embed = self.getUnionMessage(ctx, union)
                    return await channel_trackers.send(content=None, embed=embed)
                else:
                    message = "{}, I was unable to find that union!".format(ctx.author.mention)
                    return await channel_trackers.send(message)
            return

        except Exception as e:
            await ctx.author.send(e)

        return None

    @union.command()
    @commands.check(is_owner)
    async def add(self, ctx,
        rank: str = None,
        name: str = None,
        unionId: str = None,
        initials: str = None,
        leader: str = None,
        leaderId: str = None
    ):
        channel_trackers = self.getTrackersChannel(ctx)

        if None in [rank,name,unionId,initials,leader,leaderId]:
            message = "!union add <rank> <name> <union id> <initials> <leader> <leader id>"
            return await channel_trackers.send(message)

        try:
            union = [rank,name,unionId,initials,leader,leaderId]
            added = await self.addUnion(ctx, union)
            if added:
                message = "Union {} Added!".format(name)
                await channel_trackers.send(message)

        except:
            return
            # message = self.getErrorMessage(ctx)
            # await ctx.author.send(message)

        return

    @union.command(aliases=['del'])
    @commands.check(is_owner)
    async def delete(self, ctx,
        identifier: str = None
    ):
        channel_trackers = self.getTrackersChannel(ctx)

        if None in [identifier]:
            message = "!union del <initials>"
            return await channel_trackers.send(message)

        try:
            union = self.getUnionByIdentifier(identifier)

            if union is not None:
                deleted = self.deleteUnion(union)

                message = "Union {} deleted!".format(union.name)
                await channel_trackers.send(message)

        except:
            return
            # message = self.getErrorMessage(ctx)
            # await ctx.author.send(message)

        return

    @union.command()
    @commands.check(is_owner)
    async def rank(self, ctx,
        identifier: str = None,
        rank: str = None
    ):
        channel_trackers = self.getTrackersChannel(ctx)

        if None in [identifier, rank]:
            message = "!union rank <initials> <rank>"
            return await channel_trackers.send(message)

        try:
            union = await self.getUnionByIdentifier(ctx, identifier)
            print('unionnnnn')
            print(union)
            if union is not None:
                updated = await self.updateUnionRank(ctx, union['id'], rank)

                message = "Union {} rank updated to {}!".format(union['name'], rank)
                await channel_trackers.send(message)

        except Exception as e:
            print('exception starting')
            print(e)
            await ctx.author.send(e)

        return

    @union.command()
    @commands.check(is_owner)
    async def owner(self, ctx,
        identifier: str = None,
        leader: str = None,
        leaderId: str = None
    ):
        if None in [identifier, leader, leaderId]:
            message = "!union owner <initials> <leader name> <leader id>"
            return await channel_trackers.send(message)

        channel_trackers = self.getTrackersChannel(ctx)

        try:
            union = self.getUnionByIdentifier(ctx, identifier)

            if union is not None:
                updated = self.updateUnionOwner(union.id, leader, leaderId)

                message = "Union {} owner updated to {} with player id {}".format(union.name, leader, leaderId)
                await channel_trackers.send(message)

        except:
            return
            # message = self.getErrorMessage(ctx)
            # await ctx.author.send(message)

        return

    def getErrorMessage(self, ctx):
        return """
        {} something went wrong.  Please try again in a few minutes.
        """.format(ctx.author.mention)

    def getTrackersChannel(self, ctx):
        return get(ctx.guild.channels, name=CHANNEL_TRACKERS)

    async def getUnionByIdentifier(self, ctx, identifier: str = None):
        try:
            if identifier is not None:
                query = "SELECT * FROM Unions WHERE initials = '{}' LIMIT 1".format(identifier)
                union = self.cursor.execute(query).fetchone()

                if union is not None:
                    return union

                else:
                    query = "SELECT * FROM Unions WHERE name LIKE '%{}%' LIMIT 1".format(identifier)
                    union = self.cursor.exectue(query).fetchone()

                    if union is not None:
                        return union

            return None
        except:
            message = self.getErrorMessage(ctx)
            await ctx.author.send(message)

    async def getUnionList(self, ctx):
        try:
            self.cursor.execute("""SELECT * FROM Unions ORDER BY rank ASC""")

            return self.cursor.fetchall()

        except Exception as e:
            message = self.getErrorMessage(ctx)
            await ctx.author.send(message)

        return None

    def getUnionListMessage(self, ctx, unionList: list = []):
        if unionList is not []:
            embed = Embed()
            embed.set_thumbnail(url='https://i.imgur.com/fr8ZSnI.jpg')

            for v in ['rank', 'name', 'initials']:
                values = ''
                for union in unionList:
                    try:
                        values = values + "{}\n".format(union[v])
                    except:
                        pass
                embed.add_field(name=v, value=values, inline=True)


        return embed

    def getUnionMessage(self, ctx, union):
        embed = Embed(
            title="Union - {}".format(union['name'])
        )
        embed.set_thumbnail(url='https://i.imgur.com/fr8ZSnI.jpg')

        embed.add_field(name="Name", value=union['name'], inline=True)
        embed.add_field(name="Initials", value=union['initials'], inline=True)
        embed.add_field(name="Rank", value=union['rank'], inline=True)
        embed.add_field(name="Leader", value=union['leader'], inline=True)
        embed.add_field(name="Leader Id", value=union['leaderId'], inline=True)

        return embed


    async def addUnion(self, ctx, union: list = []):
        try:
            # [rank,name,unionId,initials,leader,leaderId]
            query = "INSERT INTO Unions (rank, name, unionId, initials, leader, leaderId) VALUES ({},'{}',{},'{}','{}',{})".format(
                int(union[0]),
                union[1],
                int(union[2]),
                union[3],
                union[4],
                int(union[5])
            )
            self.cursor.execute(query)
            self.conn.commit()

            return True

        except:
            message = self.getErrorMessage(ctx)
            await ctx.author.send(message)

        return None

    async def delUnion(self, ctx, union):
        try:
            query = "DELETE FROM Unions WHERE id = {}".format(int(union.id))
            self.cursor.execute(query)
            self.conn.commit()

            return True

        except:
            message = self.getErrorMessage(ctx)
            await ctx.author.send(message)

        return None

    async def updateUnionRank(self, ctx, unionId: int = None, rank: int = None):
        try:
            query = "UPDATE Unions SET rank = {} WHERE id = {}".format(int(rank), int(unionId))
            self.cursor.execute(query)
            self.conn.commit()

            return True

        except:
            message = self.getErrorMessage(ctx)
            await ctx.author.send(message)

        return None


def setup(bot):
    bot.add_cog(UnionTracker(bot))