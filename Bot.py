import os
import discord
import asyncio
from discord.ext import commands  
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
#client = discord.Client(intents=intents)
token = os.getenv('TOKEN')

bot = discord.ext.commands.Bot(command_prefix = '!', intents = intents)


@bot.event
async def on_ready():
    print('We have logged in!') 

@bot.command()
async def jordan(ctx):
    source = 'jordan.mp3'
    try:
        voice_channel = ctx.author.voice.channel
    except:
        await ctx.channel.send('Connect to VC')
    else:
        try:
            connection = await voice_channel.connect()
        except:
            print('Already connected')
        else:
            connection.play(discord.FFmpegPCMAudio(source = source, executable = "ffmpeg"), 
                after = lambda _ : asyncio.run_coroutine_threadsafe(coro=connection.disconnect(), loop = connection.loop))

@bot.command()
async def fernando(ctx):
    await ctx.send('@Lerggio#5880 What day is it?')
    with open('frog.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    return

bot.run(token)
#client.run(token)