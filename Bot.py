import os
import discord
import asyncio
from discord.ext import commands  
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
token = os.getenv('TOKEN')

bot = discord.ext.commands.Bot(command_prefix = '!', intents = intents)


@bot.event
async def on_ready():
    print('We have logged in!') 

@bot.command()
async def jordanpoo(ctx):
    source = 'jordanpoo.mp3'
    voice_client = discord.utils.get(bot.voice_clients)

    if voice_client:
        await ctx.send('Connected to voice channel already')
        return

    try:
        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()
    except:
        await ctx.channel.send('Connect to VC')
    else:
        voice_client.play(discord.FFmpegPCMAudio(source = source, executable = "ffmpeg"), 
                after = lambda _ : asyncio.run_coroutine_threadsafe(coro=voice_client.disconnect(), loop = voice_client.loop))

@bot.command()
async def jordancool(ctx):
    source = 'jordancool.mp3'
    voice_client = discord.utils.get(bot.voice_clients)

    if voice_client:
        await ctx.send('Connected to voice channel already')
        return

    try:
        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()
    except:
        await ctx.channel.send('Connect to VC')
    else:
        voice_client.play(discord.FFmpegPCMAudio(source = source, executable = "ffmpeg"), 
                after = lambda _ : asyncio.run_coroutine_threadsafe(coro=voice_client.disconnect(), loop = voice_client.loop))

@bot.command()
async def fernando(ctx):
    source = 'fernando.mp3'
    voice_client = discord.utils.get(bot.voice_clients)

    if voice_client:
        await ctx.send('Connected to voice channel already')
        return

    try:
        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()
    except:
        await ctx.channel.send('Connect to VC')
    else:
        voice_client.play(discord.FFmpegPCMAudio(source = source, executable = "ffmpeg"), 
                after = lambda _ : asyncio.run_coroutine_threadsafe(coro=voice_client.disconnect(), loop = voice_client.loop))


@bot.command()
async def wednesday(ctx):
    await ctx.send('What day is it?')
    with open('frog.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    return

bot.run(token)