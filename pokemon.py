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
        em = discord.Embed(title="*"+y["Name"]+"*")
        em.set_thumbnail(url=y["image"])


                

def setup(bot):
    bot.add_cog(Pokemon(bot))
