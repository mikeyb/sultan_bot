import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
OWNER = os.getenv('OWNER')

class Loading(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def is_owner(ctx):
        return str(ctx.message.author.id) == str(OWNER)

    @commands.command()
    @commands.check(is_owner)
    async def load(self, ctx, extension_name : str = None):
        if extension_name is not None:
            try:
                self.bot.load_extension(extension_name)

            except (AttributeError, ImportError) as e:
                return await ctx.send("```{}: {}```".format(type(e).__name__, str(e)))

            await ctx.send("{} loaded.".format(extension_name))

    @commands.command()
    @commands.check(is_owner)
    async def unload(self, ctx, extension_name : str = None):
        if extension_name is not None:
            try:
                self.bot.unload_extension(extension_name)

            except (AttributeError, ImportError) as e:
                return await ctx.send("```{}: {}```".format(type(e).__name__, str(e)))

            await ctx.send("{} unloaded.".format(extension_name))

    @commands.command()
    @commands.check(is_owner)
    async def reload(self, ctx, extension_name : str = None):
        if extension_name is not None:
            try:
                self.bot.unload_extension(extension_name)
                self.bot.load_extension(extension_name)

            except (AttributeError, ImportError) as e:
                return await ctx.send("```{}: {}```".format(type(e).__name__, str(e)))

            await ctx.send("{} reloaded.".format(extension_name))


def setup(bot):
    bot.add_cog(Loading(bot))