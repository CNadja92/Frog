import os
import discord
import time
from dotenv import load_dotenv

load_dotenv()

intents=discord.Intents.all()
client = discord.Client(intents=intents)
token = os.getenv('TOKEN')
#os.chdir("C:\Users\\nc119\Desktop\Test Bot")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
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

#test
client.run(token)