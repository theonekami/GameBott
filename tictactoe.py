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
        self.no_of_turns=0;
        
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

        self.board_array=[[0,0,0],[0,0,0],[0,0,0]]


    def end(self):
        self.gs=False
        self.players_joined=0
        self.users.clear()
        self.board_array=[[0,0,0],[0,0,0],[0,0,0]]
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
        s1=0
        s2=0
        s3=0
        s4=0
        for i in range(0,3):
            s3+=self.board[i][i]
            s4+=self.board[i][2-i]
            for j in range(0,3):
               s1+= self.board_array[i][j]
               s2+= self.board_array[j][i]
        if( s1 ==3 or s2== 3 or s3==3 or s4 == 3):
            return 0
        elif( s1 ==-3 or s2==-3 or s3==-3 or s4 == -3):
            return 1
        else:
            return-1


    
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
        

    @commands.command()
    async def tictactoe(self,ctx):
        await ctx.send("**Use** `.join` **To join**")
            
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
        self.board_img[int(args[0])][int(args[1])]=self.current_turn[1]
        self.board_array[int(args[0])-1][int(args[1])-1]=self.current_turn[2]
        self.switch()
        await self.draw(ctx)
        if(self.wincon()<0):
            await ctx.send(self.current_turn[0].mention+"**Use** `.play row,column` **to play**")
        else:
            await ctx.send(self.users[self.wincon()].mention+"WONN!!")

def setup(bot):
    bot.add_cog(TicTacToe(bot)) 

##class RussianRoullete:
##    def __init__(self,bot):
##        self.bot=bot
##        
