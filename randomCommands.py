import random
from discord.ext import commands

class randomCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def flip(self, ctx):
        result = random.choice(['Heads', 'Tails'])
        await ctx.send(result)

    @commands.command()
    async def choose(self, ctx, *choices: str):
        await ctx.send(random.choice(choices))


def setup(bot):
    bot.add_cog(randomCommands(bot))
