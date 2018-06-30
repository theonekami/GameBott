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
        img="https://cdn.discordapp.com/attachments/404266499516268554/462127861428649984/Screen_Shot_2018-06-29_at_3.30.50_pm.png"
        em.add_field(name="**Name**", value=Name,inline=False)
        em.add_field(name="**Quote**", value=quote,inline=False)
        em.add_field(name="**Ace**", value=ace,inline=False)
        em.set_image(url=img)
        await ctx.send(embed=em)

    @cq.command(name= "fire")
    async def cq_fire(self, ctx):
        em = discord.Embed()
        Name= "Razan Atmadh"
        quote= "*The dead see all.*"
        ace= "Mega-Houndoom"
        img="https://cdn.discordapp.com/attachments/456079885769768961/462283728241164288/mega_houndoom_by_theblacksavior-d7ivyjl.png"
        em.set_image(url=img)
        em.add_field(name="**Name**", value=Name,inline=False)
        em.add_field(name="**Quote**", value=quote,inline=False)
        em.add_field(name="**Ace**", value=ace,inline=False)
        await ctx.send(embed=em)


    @cq.command(name= "ghost")
    async def cq_ghost(self, ctx):
        em = discord.Embed()
        Name= "Anri of the mountain's peak"
        quote= "*Welcome to the boundry of life and death*"
        ace= "Giratina"
        img="https://cdn.discordapp.com/attachments/433160058617200642/462447888320954388/Giratina.png"
        em.set_image(url=img)
        em.add_field(name="**Name**", value=Name,inline=False)
        em.add_field(name="**Quote**", value=quote,inline=False)
        em.add_field(name="**Ace**", value=ace,inline=False)
        await ctx.send(embed=em)

    @cq.command(name= "flying")
    async def cq_fly(self, ctx):
        em = discord.Embed()
        Name= "Prince Yusuf"
        quote= "*muntar se Amar* (immortal from magic)"
        ace= "Lugia"
        img="https://cdn.discordapp.com/attachments/407115849539911682/462497100215746563/test.jpg"
        em.set_image(url=img)
        em.add_field(name="**Name**", value=Name,inline=False)
        em.add_field(name="**Quote**", value=quote,inline=False)
        em.add_field(name="**Ace**", value=ace,inline=False)
        await ctx.send(embed=em)


##    @cq.command(name= "Flying")
##    async def cq_ice(ctx):
##        em = discord.Embed()
##        name= "Glass Evans"
##        quote= "Might is Right"
##        ace= "Kyurem-Black"
##        
                

def setup(bot):
    bot.add_cog(Conquest(bot))
