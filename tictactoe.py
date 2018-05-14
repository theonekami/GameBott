import discord,openpyxl
from discord.ext import commands

class TicTacToe:
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def draw(self,ctx):

        x="""
:large_blue_circle::large_blue_circle::large_blue_circle:
:large_blue_circle::large_blue_circle::large_blue_circle:
:large_blue_circle::large_blue_circle::large_blue_circle:
"""
        em= discord.Embed(title="Tic Tac Toe.",discription=x)
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(TicTacToe(bot)) 

##class RussianRoullete:
##    def __init__(self,bot):
##        self.bot=bot
##        
