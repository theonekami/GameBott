import discord
from discord.ext import commands
import json
import aiohttp

class Magic:
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def card(self,ctx,args):
        y=str(args)
        async with aiohttp.get('https://api.magicthegathering.io/v1/cards?name="'+y+'"') as res:
            if (res.status==200):
                y=json.loads(await res.text())
            else:
                await ctx.send("Card named" + str(args)+" not found")
                res.close()
                return
        res.close()
        em = discord.Embed(title=y['cards'][0]['name'])
        em.set_image(url=y['cards'][0]['imageUrl'])
        await ctx.send(embed= em) 

def setup(bot):
    bot.add_cog(Magic(bot))
