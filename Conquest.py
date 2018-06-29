import discord
from discord.ext import commands

class Conquest:
    def __init__(self, bot):
        self.bot=bot

    @commands.group()
    async def cq(self, ctx):
        pass

    @cq.command(name= "ice")
    async def cq_ice(self, ctx):
        em = discord.Embed()
        Name= "Glass Evans"
        quote= '"*Might is Right*"'
        ace= "Kyurem-Black"
        img="https://pre00.deviantart.net/02b7/th/pre/i/2012/064/6/4/black_kyurem_by_namh-d4rrv3d.jpg"
        em.add_field(name="**Name**", value=Name,inline=False)
        em.add_field(name="**Quote**", value=quote,inline=False)
        em.add_field(name="**Ace**", value=ace,inline=False)
        em.set_image(url=img)
        await ctx.send(embed=em)

##    @cq.command(name= "fire")
##    async def cq_fire(self, ctx):
##        em = discord.Embed()
##        Name= "Razan Atmadh"
##        quote= "*The Dead See All*"
##        ace= "Mega-Houndoom"
##        img="https://pre00.deviantart.net/c584/th/pre/f/2014/138/7/b/mega_houndoom_by_theblacksavior-d7ivyjl.jpg"
##        em.set_image(url=img)
##        em.add_field(name="**Name**", value=Name,inline=False)
##        em.add_field(name="**Quote**", value=quote,inline=False)
##        em.add_field(name="**Ace**", value=ace,inline=False)
##        await ctx.send(embed=em)

##    @cq.command(name= "Flying")
##    async def cq_ice(ctx):
##        em = discord.Embed()
##        name= "Glass Evans"
##        quote= "Might is Right"
##        ace= "Kyurem-Black"
##        
                

def setup(bot):
    bot.add_cog(Conquest(bot))
