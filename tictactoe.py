import discord,openpyxl
from discord.ext import commands

class TicTacToe:
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def draw(self,ctx):
        x="""
```

    ¦    ¦    ¦
  ----------------
    ¦    ¦    ¦
  ----------------
    ¦    ¦    ¦
```
"""
        ctx.send(x)

    
        

##class RussianRoullete:
##    def __init__(self,bot):
##        self.bot=bot
##        
