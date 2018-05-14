import discord,openpyxl
from discord.ext import commands

class TicTacToe:
    def __init__(self, bot):
        self.bot=bot
        board_img="""



:arrow_upper_left::one::two::three: 
:one::large_blue_circle::large_blue_circle::large_blue_circle:
:two::large_blue_circle::large_blue_circle::large_blue_circle:
:three::large_blue_circle::large_blue_circle::large_blue_circle:



"""
        board_array=[[0,0,0],[0,0,0],[0,0,0]]

    @commands.command()
    async def draw(self,ctx):
        em= discord.Embed(title="Tic Tac Toe.",description=self.board_img)
        await ctx.send(embed=em)
##        await ctx.send(x)

def setup(bot):
    bot.add_cog(TicTacToe(bot)) 

##class RussianRoullete:
##    def __init__(self,bot):
##        self.bot=bot
##        
