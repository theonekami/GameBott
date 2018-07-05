import discord
from discord.ext import commands
import json

pokemon= "http://pokeapi.co/api/v2/pokemon/"

class Pokemon:
    def __init__(self, bot):
        self.bot=bot
        
    async def poke(self, ctx,args):
        em = discord.Embed()
        async with aiohttp.get(pokemon+args) as res:
            y=json.loads(r.text)
        res.close()
        await ctx.send(y['name'])


                

def setup(bot):
    bot.add_cog(Pokemon(bot))
