import discord
from discord.ext import commands


class Battle:
    def __init__(self):
        self.top="```"
        self.mid="----------------------------------------"
        self.end="```"

class Fite:
    def __init__(self, bot):
        self.bot=bot
        self.b=Battle()
        self.msg=self.b.top +self.b.mid+self.b.end

    @commands.command()
    async def show(self, ctx):
        await ctx.send(self.msg)
                

def setup(bot):
    bot.add_cog(Battle(bot))
