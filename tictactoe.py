import discord,openpyxl
from discord.ext import commands

class TicTacToe:
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def draw(self,ctx):

        x="""
:arrow_upper_left::one: :two: :three: 
:one::large_blue_circle::large_blue_circle::large_blue_circle:
:two::large_blue_circle::large_blue_circle::large_blue_circle:
:three::large_blue_circle::large_blue_circle::large_blue_circle:
"""
        em= discord.Embed(title="Tic Tac Toe.",description=x)
        await ctx.send(embed=em)
##        await ctx.send(x)

def setup(bot):
    bot.add_cog(TicTacToe(bot)) 

##class RussianRoullete:
##    def __init__(self,bot):
##        self.bot=bot
##        
