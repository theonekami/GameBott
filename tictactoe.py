import discord,openpyxl
from discord.ext import commands

class TicTacToe:
    def __init__(self, bot):
        self.bot=bot
        self.board_img="""



:arrow_upper_left::one::two::three: 
:one::red_circle::red_circle::red_circle:
:two::red_circle::red_circle::red_circle:
:three::red_circle::red_circle::red_circle:



"""
        self.blank="red_circle"
        self.cross="crossed_swords"
        self.circle="shield"
        self.board_array=[[0,0,0],[0,0,0],[0,0,0]]

    @commands.command()
    async def draw(self,ctx):
        em= discord.Embed(description=self.board_img)
        await ctx.send(embed=em)
##        await ctx.send(x)

def setup(bot):
    bot.add_cog(TicTacToe(bot)) 

##class RussianRoullete:
##    def __init__(self,bot):
##        self.bot=bot
##        
