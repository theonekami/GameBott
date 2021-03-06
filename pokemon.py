import discord
from discord.ext import commands
import json
import aiohttp
import random

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
        em = discord.Embed(title=y["name"].capitalize())
        em.set_thumbnail(url=img["sprites"]["front_default"])
        x=""
        for i in y["abilities"]:
            x+=i["ability"]["name"].capitalize()+"\n"
        em.add_field(name="**Abilities**", value=x)
        x=""
        w=0
        for j in range(0,6):
            x+= y['stats'][5-j]['stat']['name'].capitalize() +" : "+ str(y['stats'][5-j]['base_stat'])+"\n"
            w+=y['stats'][j]['base_stat']
        x+="BST : " + str(w)
        em.add_field(name="**Stats**", value=x)
        await ctx.send(embed=em)

    @commands.command()   
    async def randpoke(self, ctx):
        re=random.randint(1,803)
        async with aiohttp.get(pokemon2+str(re)) as r:
            y=json.loads(await r.text())
        r.close()
        async with aiohttp.get(y["forms"][0]["url"]) as r:
            img=json.loads(await r.text())
        r.close()        
        em = discord.Embed(title=y["name"].capitalize())
        em.set_thumbnail(url=img["sprites"]["front_default"])
        x=""
        for i in y["abilities"]:
            x+=i["ability"]["name"].capitalize()+"\n"
        em.add_field(name="**Abilities**", value=x)
        x=""
        w=0
        for j in range(0,6):
            x+= y['stats'][5-j]['stat']['name'].capitalize() +" : "+ str(y['stats'][j]['base_stat'])+"\n"
            w+=y['stats'][j]['base_stat']
        x+="BST : " + str(w)
        em.add_field(name="**Stats**", value=x)
        await ctx.send(embed=em)
                

def setup(bot):
    bot.add_cog(Pokemon(bot))
