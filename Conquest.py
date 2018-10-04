import discord
from discord.ext import commands


class Battle:
    def __init__(self):
        self.top="```"
        self.mid="\n----------------------------------------\n"
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

    @battle.command(name="adde")
    async def battle_addenemy(self,ctx,*,args):
        self.b.enemies.append(str(args))
        ctx.send(args+" has been added on the enemy side")
        
    @battle.command(name="adda")
    async def battle_addallie(self,ctx,*,args):
        self.b.allies.append(str(args))
        ctx.send(args+" has been added on the ally side")
    
    @battle.command(name="show")
    async def battle_show(self, ctx):
        self.msg=self.b.top + self.b.rete()+self.b.mid+self.b.reta()+self.b.end
        await ctx.send(self.msg)
        
    

def setup(bot):
    bot.add_cog(Fite(bot))
