import discord
from discord.ext import commands
import re

class Battle:
    def __init__(self):
        self.top="```"
        self.mid="\n--------------------------------------------------------------------\n"
        self.end="```"
        self.enemies=[]
        self.allies=[]
        self.format=re.compile(r'\(\d+\)')

    def rete(self):
        x=""
        for i in range (0,len(self.enemies)):
            x+=str(i+1)+":" + self.enemies[i] +" "
        return x

    def reta(self):
        x=""
        for i in range (0,len(self.allies)):
            x+=str(i+1)+":" + self.allies[i] +" "
        return x

class Fite:
    def __init__(self, bot):
        self.bot=bot
        self.b=Battle()
        self.msg=self.b.top +self.b.mid+self.b.end

    @commands.group()
    async def battle(self,ctx):
        pass

    @battle.command(name="clear")
    async def battle_clr(self, ctx):
        self.b=Battle()
    
    @battle.command(name="adde")
    async def battle_addenemy(self,ctx,*,args):
        self.b.enemies.append(str(args))
        await ctx.send(args+" has been added on the enemy side")
        
    @battle.command(name="adda")
    async def battle_addallie(self,ctx,*,args):
        self.b.allies.append(str(args))
        await ctx.send(args+" has been added on the ally side")

    @battle.command(name="hp")
    async def battle_hp(self,ctx,*,args):
        
    
    @battle.command(name="show")
    async def battle_show(self, ctx):
        self.msg=self.b.top + self.b.rete()+self.b.mid+self.b.reta()+self.b.end
        await ctx.send(self.msg)
        
    

def setup(bot):
    bot.add_cog(Fite(bot))
