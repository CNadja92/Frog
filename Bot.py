import os
import discord
import time
from discord.ext import commands  
from dotenv import load_dotenv

load_dotenv()

intents=discord.Intents.all()
client = discord.Client(intents=intents)
token = os.getenv('TOKEN')
#os.chdir("C:\Users\\nc119\Desktop\Test Bot")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

""""
@commands.command()
async def check_voice(ctx):
    voice_channel = ctx.author.voicestate.channel
    if voice_channel == None:
        await ctx.channel.send('Connect to VC')
    else:
        connection = await voice_channel.connect()
        connection.play(client.FFmpegAudio(source="./Desktop/Bot/sample.mp3", executable="./Desktop/ffmpeg/bin/ffmpeg.exe", 
            after=lambda e: connection.disconnect()))
        #check if lambda is necessary, otherwise run disconnect after play
"""


 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.lower() == 'fernando':
        await message.channel.send('@Lerggio#5880 What day is it?')
        #await message.channel.send(file=discord.File('Frog.png'))
        with open('./Desktop/Bot/frog.png', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)
        return

    if message.content.lower() == 'jordan':
        await check_voice(client.user)




client.run(token)