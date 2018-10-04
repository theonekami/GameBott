import discord
from discord.ext import commands


class Battle:
    def __init__(self):
        self.top="```"
        self.mid="\n----------------------------------------"
        self.end="```"
        self.enemies=[]
        self.allies=[]

    def rete(self):
        x=""
        for i in enemies:
            x+=i+" "
        return x

    def reta(self):
        x=""
        for i in enemies:
            x+=i+" "
        return x

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
        self.msg=self.b.top + self.b.rete()+self.b.mid+self.b.reta()+self.b.end
        await ctx.send(self.msg)
        
    

def setup(bot):
    bot.add_cog(Fite(bot))
