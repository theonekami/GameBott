import discord,openpyxl
from discord.ext import commands

class TicTacToe:
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def draw(self,ctx):
        x="""
```

  ¦    ¦    ¦    ¦
  ----------------
  ¦    ¦    ¦    ¦
  ----------------
  ¦    ¦    ¦    ¦
```
"""
        await ctx.send(x)

def setup(bot):
    bot.add_cog(TicTacToe(bot)) 

##class RussianRoullete:
##    def __init__(self,bot):
##        self.bot=bot
##        
