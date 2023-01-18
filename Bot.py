import os
import discord
import time
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
    try:
        voice_channel = ctx.author.voice.channel
    except:
        await ctx.channel.send('Connect to VC')
    else:
        connection = await voice_channel.connect()
        connection.play(discord.FFmpegPCMAudio(source = "./Desktop/Bot/sample.mp3", executable = "./Desktop/ffmpeg/bin/ffmpeg.exe"), after=lambda e: print('Test text'))
        while connection.is_playing():
            time.sleep(0.1)
        await connection.disconnect()

@bot.command()
async def fernando(ctx):
    await ctx.send('@Lerggio#5880 What day is it?')
    with open('./Desktop/Bot/frog.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    return

''''
@commands.command()
async def check_voice(ctx):
    try:
        voice_channel = ctx.author.voice.channel
    except:
        await ctx.channel.send('Connect to VC')
    else:
        connection = await voice_channel.connect()
        connection.play(discord.FFmpegPCMAudio(source="./Desktop/Bot/sample.mp3", executable="./Desktop/ffmpeg/bin/ffmpeg.exe"), after=lambda e: print('Test text'))
        while connection.is_playing():
            time.sleep(0.1)
        await connection.disconnect()

        
          
@commands.command()
async def voice_dc(ctx):
    vc = ctx.voice_client
    await vc.disconnect()
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.lower() == 'fernando':
        await message.channel.send('@Lerggio#5880 What day is it?')
        with open('./Desktop/Bot/frog.png', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)
        return

    if message.content.lower() == 'jordan':
        await check_voice(message)
        #await voice_dc(client.user)

'''
bot.run(token)
#client.run(token)