import discord
from discord.ext import commands
import json
import aiohttp

pokemon= "http://api.tanvis.xyz/pokedex/"
pokemon2="http://pokeapi.co/api/v2/pokemon/"

class Pokemon:
    def __init__(self, bot):
        self.bot=bot

    @commands.command()   
    async def poke(self, ctx,args):
        async with aiohttp.get(pokemon2+str(args)) as r:
            y=json.loads(await r.text())
        r.close()
        async with aiohttp.get(y["forms"][0]["url"]) as r:
            img=json.loads(await r.text())
        r.close()        
        em = discord.Embed(title="*"+y["name"]+"*")
        em.set_thumbnail(url=img["sprites"]["front_default"])
        x=""
        for i in y["abilities"]:
            x+=i["ability"]["name"].capitalize()+"\n"
        em.add_field(name="**Abilities**", value=x)
        x=""
        for j in range(0,6,-1):
            x+= y['stats'][j]['stat']['name'].capitalize() +" : "+ str(y['stats'][j]['base_stat'])+"\n"
        em.add_field(name="**Stats**", value=x)
        await ctx.send(embed=em)


                

def setup(bot):
    bot.add_cog(Pokemon(bot))
