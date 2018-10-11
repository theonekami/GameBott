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
        if(not len(y)):
            em = discord.Embed(title=y['cards'][0]['name'])
            em.set_image(url=y['cards'][0]['imageUrl'])
            await ctx.send(embed= em)
        else:
            await ctx.send("Card name " + str(args) + " not found")

def setup(bot):
    bot.add_cog(Magic(bot))
