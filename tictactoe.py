import discord,openpyxl
from discord.ext import commands


async def game_on(ctx):
    return ctx.cog.gs

async def joins_open(ctx):
    return ctx.cog.js


class TicTacToe:
    def __init__(self, bot):
        self.bot=bot

        self.gs=False
        self.users=[]
        self.no_of_players=2
        self.players_joined=0
        self.no_of_turns=0;
        self.js=False
        
        self.blank=":red_circle:"
        self.cross=":crossed_swords:"
        self.circle=":shield:"
        self.current_turn=[]
        self.board_img=[
[":arrow_upper_left::one::two::three:\n"],
[":one:",self.blank,self.blank,self.blank,"\n"],
[":two:",self.blank,self.blank,self.blank,"\n"],
[":three:",self.blank,self.blank,self.blank,"\n"]
]


    def end(self):
        self.gs=False
        self.players_joined=0
        self.users.clear()
        self.current_turn.clear()
        self.board_img.clear()
        self.no_of_turns=0
        self.board_img=[
[":arrow_upper_left::one::two::three:\n"],
[":one:",self.blank,self.blank,self.blank,"\n"],
[":two:",self.blank,self.blank,self.blank,"\n"],
[":three:",self.blank,self.blank,self.blank,"\n"]
]

    
    @commands.command()
    async def Forcestop(self,ctx):
        self.end()
        await ctx.send("The game is STOP")

    async def draw(self,ctx):
        em= discord.Embed(title="TicTacToe",description=self.board())
        await ctx.send(embed=em)


    def board(self):
        x=""
        for i in self.board_img:
            for j in i:
                x+=j
        return x

    async def construct(self,ctx):
        self.current_turn.append(self.users[0])
        self.current_turn.append(self.cross)
        self.current_turn.append(1)
        await self.draw(ctx)
        await ctx.send(self.current_turn[0].mention+"**Use** `.play row,column` **to play**")

    def switch(self):
        if(self.current_turn[2]>0):
            self.current_turn[0]=self.users[1]
            self.current_turn[1]=self.circle
            self.current_turn[2]=-1
        else:
            self.current_turn[0]=self.users[0]
            self.current_turn[1]=self.cross
            self.current_turn[2]=1

    def wincon(self):
        win=""
        x=self.cross
        y=self.circle
        for i in range(1, 4):
            if (self.board_img[i][1]==self.board_img[i][2]==self.board_img[i][3]):
                win=self.board_img[i][1]
                break
            elif(self.board_img[1][i]==self.board_img[2][i]==self.board_img[3][i]):
                win=self.board_img[1][i]
                break
        if( (win is "") and self.board_img[1][1]==self.board_img[2][2]==self.board_img[3][3]):
            win=self.board_img[1][1]
        elif( (win is "") and self.board_img[1][3]==self.board_img[2][2]==self.board_img[3][1]):
            win=self.board_img[1][1]

        if( win == x):
            return 1
        elif(win==y):
            return 0
        else:
            return -1
    
    @commands.check(joins_open)
    @commands.command()
    async def join(self,ctx):
        for i in self.users:
            if ctx.author==i:
                return
        self.players_joined+=1
        self.users.append(ctx.author)
        if(len(self.users)==self.no_of_players):
            self.gs=True
            await self.construct(ctx)
            self.js=False
        

    @commands.command()
    async def tictactoe(self,ctx):
        await ctx.send("**Use** `.join` **To join**")
        self.js=True
            
    @commands.check(game_on)
    @commands.command()
    async def drawb(self,ctx):
        await self.draw(ctx)

    @commands.check(game_on)
    @commands.command()
    async def play(self,ctx,*,args=None):
        if (ctx.author != self.current_turn[0]):
            return
        if( args is None):
            await ctx.send("Where do i put it?")
            return

        args=args.split(',')
        y=self.board_img[int(args[0])][int(args[1])]
        if( y != self.blank):
            await ctx.send("Occupied")
            return
        self.no_of_turns+=1
        self.board_img[int(args[0])][int(args[1])]=self.current_turn[1]

        self.switch()
        await self.draw(ctx)
        if(self.wincon()<0 and self.no_of_turns != 8):
            await ctx.send(self.current_turn[0].mention+"**Use** `.play row,column` **to play**")
        elif(self.no_of_turns==8):
            await ctx.send("It's a TIEEEEE!!!!")
            self.end()            
        else:
            await ctx.send(self.users[self.wincon()].mention+"WONN!!")
            self.end()


def setup(bot):
    bot.add_cog(TicTacToe(bot)) 

##class RussianRoullete:
##    def __init__(self,bot):
##        self.bot=bot
##        
