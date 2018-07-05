import discord
from discord.ext import commands

class Pokemon:
    def __init__(self, bot):
        self.bot=bot

    @commands.group()
    async def dt(self, ctx):
        pass

    
                

def setup(bot):
    bot.add_cog(Pokemon(bot))
