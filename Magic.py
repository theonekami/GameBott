import discord
from discord.ext import commands
import json
import aiohttp

class Magic:
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def card(self,ctx,args):
        x=str(args)
        y=None
        async with aiohttp.get('https://api.magicthegathering.io/v1/cards?name="'+x+'"') as res:
            print(res.status)
            y=json.loads(await res.text())
        res.close()
        try:
            em = discord.Embed(title=y['cards'][0]['name'])
            em.set_image(url=y['cards'][0]['imageUrl'])
            await ctx.send(embed= em)
        except:
            await ctx.send("Card name " + str(args) + " not found")


class HS:
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def hscard(self,ctx,args):
        x=str(args)
        x=x.replace(" ","%20")
        y=None
        async with aiohttp.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/"+x,headers={"X-Mashape-Key": "nZsSdxxcN1mshskGiEd18AIpXDksp19XabQjsn8LotoIfnfv54","Accept": "application/json"})) as res:
            print(res.status)
            y=json.loads(await res.text())
        res.close()
        try:
            em = discord.Embed(title=y[[0]['name'])
            em.set_image(url=y[0]['img'])
            await ctx.send(embed= em)
        except:
            await ctx.send("Card name " + str(args) + " not found")

def setup(bot):
    bot.add_cog(Magic(bot))
    bot.add_cog(HS(bot))
