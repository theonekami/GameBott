import discord
from discord.ext import commands
import json
import aiohttp

pokemon= "http://api.tanvis.xyz/pokedex/"

class Pokemon:
    def __init__(self, bot):
        self.bot=bot

    @commands.command()   
    async def poke(self, ctx,args):
        async with aiohttp.get(pokemon+str(args)) as r:
            y=json.loads(await r.text())
        r.close()
        em = discord.Embed(title="*"+y["name"]+"*")
        em.set_thumbnail(url=y["image"])
        x=""
        for i in y["abilities"]:
            x+=i+" "
        em.add_field(name="**Abilities**", value=x)
        x=""
        for i in y["baseStats"].keys():
            x+=str(i) + y["basestats"][i] + "\n"
        
        em.add_field(name="**Stats**", value=x)
        await ctx.send(embed=em)


                

def setup(bot):
    bot.add_cog(Pokemon(bot))
