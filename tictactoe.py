import discord,openpyxl
from discord.ext import commands


async def game_on(ctx):
    return ctx.cog.gs

async def joins_open(ctx):
    if ctx.cog.no_of_players>ctx.cog.players_joined:
        return True
    else:
        return False


class TicTacToe:
    def __init__(self, bot):
        self.bot=bot

        self.gs=False
        self.users=[]
        self.no_of_players=2
        self.players_joined=0
        
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


    def draw(self):
        em= discord.Embed(title="TicTacToe",description=self.board())
        return em

    def board(self):
        x=""
        for i in self.board_img:
            for j in i:
                x+=j
        return x

    @commands.check(joins_open)
    @commands.command()
    async def join(self,ctx):
        self.users.append(ctx.author)
        if(len(self.users)==self.no_of_players):
            self.gs=True
        self.players_joined+=1

    @commands.command()
    async def tictactoe(self,ctx):
        await ctx.send(embed=self.draw())
        await ctx.send("**Use** `.join` **To join**")
    
    @commands.check(game_on)
    @commands.command()
    async def drawb(self,ctx):
        await ctx.send(embed=self.draw())

    @commands.check(game_on)
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
        self.board_array[int(args[0]-1)][int(args[1])-1]
        await ctx.send(embed=self.draw())
        await ctx.send("ok so far so good")

def setup(bot):
    bot.add_cog(TicTacToe(bot)) 

##class RussianRoullete:
##    def __init__(self,bot):
##        self.bot=bot
##        
