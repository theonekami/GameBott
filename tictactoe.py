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

def setup(bot):
    bot.add_cog(draw(bot))      

##class RussianRoullete:
##    def __init__(self,bot):
##        self.bot=bot
##        
