# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random
import sys,os
import aiohttp
import datetime,json
import math ##for funsies



# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = commands.Bot(description="Game Boty WHEEE", command_prefix=(".","gm ","Gm ","GM "), pm_help = False)

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.

def rolld(args):
        y=str(args).replace(" ","")
        x=""
        for i in y:
                if i in ('+','-','*','/'): 
                        break
                x+=i
        z=x.split('d')
        no=int(z[0])
        limit=int(z[1])
        rolls=list()
        for i in range(no):
                rolls.append(random.randint(1,limit))
        res="Roll(s):"
        for i in rolls:
                res+=" "+str(i)
        res+=" || Sum="
        s= str(sum(rolls))
        y=y.replace(x,s)
        res+=str(eval(y))
        return res

@client.event
async def on_ready():
        print('You are running BasicBot v2.1') #Do not change this. This will really help us support you, if you need support.
        print('Created by Kaminolucky')
        client.load_extension("Conquest")
        client.load_extension("Pokemon")



# This is a basic example of a call and response command. You tell it do "this" and it does it.
@client.command()
async def hi(ctx):
        """Experimental Command. Just says hi. And stuff."""
        await ctx.send("Hello I am game bot...Plz be my fren")

@client.command()
async def roll(ctx,*,args):
        """Rolls a dice. Formatted as  <no of dice>d<no of sides> eg. 3d10"""
        res=rolld(args)
        await ctx.send(res)

@client.command()
async def pick(ctx,*, args):
        """A pick device. Uses a list so i think any number of arguments can work"""
        y=str(args)
        x=random.choice(y.split(','))
        await ctx.send("I give you: "+x)

@client.command()
async def reload(ctx):
        client.load_extension("tictactoe")
        await ctx.send("Good job. It's Reloaded. Who do i kill?")
        
client.run('NDE1MTQ5Mzk5NjUyNTY0OTk0.DhdPFQ.mWjVTF5lf0oWWZJQn8uNhtZB4IQ')
