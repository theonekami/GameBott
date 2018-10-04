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

    @commands.group()
    async def battle(self,ctx):
        pass
    
    @battle.command(name="show")
    async def battle_show(self, ctx):
        await ctx.send(self.msg)
                

def setup(bot):
    bot.add_cog(Fite(bot))
