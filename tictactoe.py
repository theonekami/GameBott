import discord,openpyxl
from discord.ext import commands

class TicTacToe:
    def __init__(self, bot):
        self.bot=bot
        self.blank=":red_circle:"
        self.cross=":crossed_swords:"
        self.circle=":shield:"
        self.board_img=[
[":arrow_upper_left::one::two::three:\n"],
[":one:",self.blank,self.blank,self.blank,"\n"],
[":two:",self.blank,self.blank,self.blank,"\n"],
[":three:",self.blank,self.blank,self.blank,"\n"]
]

        self.board_array=[[0,0,0],[0,0,0],[0,0,0]]
        self.gs=False

    def board(self):
        x=""
        for i in self.board_img:
            for j in i:
                x+=j
        return x

    def game_on(self):
        return self.gs
    
    @commands.check(game_on)
    @commands.command()
    async def draw(self,ctx):
        em= discord.Embed(title="TicTacToe",description=self.board())
        await ctx.send(embed=em)
##        await ctx.send(x)

    @commands.command()
    async def play(self,ctx,*,args=None):
        if( args is None):
            await ctx.send("Where do i put it?")
            return
        args=args.split(',')
        y=self.board_img[int(args[0])][int(args[1])]
        if( y != self.blank):
            await ctx.send("Occupied")
            return
        self.board_img[int(args[0])][int(args[1])]=self.cross
        await ctx.send("ok so far so good")

def setup(bot):
    bot.add_cog(TicTacToe(bot)) 

##class RussianRoullete:
##    def __init__(self,bot):
##        self.bot=bot
##        
