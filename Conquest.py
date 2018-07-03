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
        em = discord.Embed(color=discord.Color.from_rgb(r=39,g=151,b=253))
        Name= "Glass Evans"
        quote= '"*Might is Right*"'
        ace= "Kyurem-Black"
        img="https://cdn.discordapp.com/attachments/404266499516268554/462605945550274560/black_kyurem_by_hasegawavega-d5rxah8.jpg"
        em.add_field(name="**Name**", value=Name,inline=False)
        em.add_field(name="**Quote**", value=quote,inline=False)
        em.add_field(name="**Ace**", value=ace,inline=False)
        em.set_image(url=img)
        await ctx.send(embed=em)

    @cq.command(name= "fire")
    async def cq_fire(self, ctx):
        em = discord.Embed(color=discord.Color.from_rgb(r=240,g=127,b=47))
        Name= "Razan Atmadh"
        quote= '*"The dead see all."*'
        ace= "Mega-Houndoom"
        img="https://cdn.discordapp.com/attachments/456079885769768961/462283728241164288/mega_houndoom_by_theblacksavior-d7ivyjl.png"
        em.set_image(url=img)
        em.add_field(name="**Name**", value=Name,inline=False)
        em.add_field(name="**Quote**", value=quote,inline=False)
        em.add_field(name="**Ace**", value=ace,inline=False)
        await ctx.send(embed=em)


    @cq.command(name= "fairy")
    async def cq_fairy(self, ctx):
        em = discord.Embed(color=discord.Color.from_rgb(r=240,g=127,b=47))
        Name= " President Atraxias"
        quote= '*"Some of the stranger machinations in the world turn out to be curiosities, wonders of the eye we never anticipated; it is best to keep an eye out for such events and creatures."*'
        ace= "Magearnas"
        img="https://i.pinimg.com/originals/a7/fe/4c/a7fe4ce4d1300f7caec745ff0d59e1da.jpg"
        em.set_image(url=img)
        em.add_field(name="**Name**", value=Name,inline=False)
        em.add_field(name="**Quote**", value=quote,inline=False)
        em.add_field(name="**Ace**", value=ace,inline=False)
        await ctx.send(embed=em)


    @cq.command(name= "ghost")
    async def cq_ghost(self, ctx):
        
        em = discord.Embed(color=discord.Color.from_rgb(r=169,g=111,b=247))        
        Name= "Anri of the mountain's peak"
        quote= '*"Welcome to the boundry of life and death"*'
        ace= "Giratina"
        img="https://cdn.discordapp.com/attachments/433160058617200642/462652822224371713/image.jpg"
        em.set_image(url=img)
        em.add_field(name="**Name**", value=Name,inline=False)
        em.add_field(name="**Quote**", value=quote,inline=False)
        em.add_field(name="**Ace**", value=ace,inline=False)
        await ctx.send(embed=em)

    @cq.command(name= "flying")
    async def cq_fly(self, ctx):
        em = discord.Embed(color=discord.Color.from_rgb(r=179,g=157,b=247))
        Name= "Prince Yusuf"
        quote= '*"muntar se Amar" (immortal from magic)*'
        ace= "Lugia"
        img="https://cdn.discordapp.com/attachments/407115849539911682/462497100215746563/test.jpg"
        em.set_image(url=img)
        em.add_field(name="**Name**", value=Name,inline=False)
        em.add_field(name="**Quote**", value=quote,inline=False)
        em.add_field(name="**Ace**", value=ace,inline=False)
        await ctx.send(embed=em)

    @cq.command(name= "rock")
    async def cq_rock(self, ctx):
        em = discord.Embed(color=discord.Color.from_rgb(r=208,g=151,b=2))
        Name= "Andrew Arslon"
        quote= '*"Those that lose wars are ones that start them. Those who win wars are the ones who bide their time."*'
        ace= "Terrakion"
        img="https://cdn.discordapp.com/attachments/455576163562291211/462523425311948800/unknown.png"
        em.set_image(url=img)
        em.add_field(name="**Name**", value=Name,inline=False)
        em.add_field(name="**Quote**", value=quote,inline=False)
        em.add_field(name="**Ace**", value=ace,inline=False)
        await ctx.send(embed=em)

    @cq.command(name= "bug")
    async def cq_bug(self, ctx):
        em = discord.Embed(color=discord.Color.from_rgb(r=162,g=162,b=179))
        Name= "Erwin von Blutzenburg"
        quote= '*"Liberty in Peace, Resilience in War."*'
        ace= "Mega-Scizor(???)"
        img="https://cdn.discordapp.com/attachments/407525090184658956/462635803533901824/6845f9cc188a4b232565775451c34f5f.jpg"
        em.set_image(url=img)
        em.add_field(name="**Name**", value=Name,inline=False)
        em.add_field(name="**Quote**", value=quote,inline=False)
        em.add_field(name="**Ace**", value=ace,inline=False)
        await ctx.send(embed=em)

    @cq.command(name= "psychic")
    async def cq_psychic(self, ctx):
        em = discord.Embed(color=discord.Color.from_rgb(r=254,g=122,b=249))
        Name= "Smeero Tykunaki"
        quote= '*"Tuhaf topraklar, herkesin en öngörülebilir alanıdır." (The land of strange is the most predictable land of all.)*'
        ace= "Tapu-Lele"
        img="https://cdn.discordapp.com/attachments/462678865706352641/462679903138217997/Untitled222.png"
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
