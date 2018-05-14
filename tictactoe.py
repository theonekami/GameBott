import discord,openpyxl
from discord.ext import commands

class TicTacToe:
    def __init__(self, bot):
        self.bot=bot
        self.blank="red_circle"
        self.cross="crossed_swords"
        self.circle="shield"
        self.board_img=[
[":arrow_upper_left::one::two::three:\n"],
[":one:",self.blank,self.blank,self.blank,"\n"],
[":two:",self.blank,self.blank,self.blank,"\n"],
[":three:",self.blank,self.blank,self.blank,"\n"]
]

        self.board_array=[[0,0,0],[0,0,0],[0,0,0]]

    def board(self):
        x=""
        for i in board_img:
            for j in i:
                x+=j
        return x

    @commands.command()
    async def draw(self,ctx):
        em= discord.Embed(title="TicTacToe",description=self.board())
        await ctx.send(embed=em)
##        await ctx.send(x)

def setup(bot):
    bot.add_cog(TicTacToe(bot)) 

##class RussianRoullete:
##    def __init__(self,bot):
##        self.bot=bot
##        
