from discord.ext import commands

class testCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong')


def setup(bot):
    bot.add_cog(testCommands(bot))