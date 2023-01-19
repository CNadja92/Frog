import os
import discord
import asyncio
import disnake
from disnake.ext import commands
from discord.ext import commands  
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
token = os.getenv('TOKEN')

bot = discord.ext.commands.Bot(command_prefix = '!', intents = intents)

class MyHelp(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        filtered = await self.filter_commands(self.context.bot.commands, sort = True)  # returns a list of command objects
        names = [command.name for command in filtered] # iterating through the commands objects getting names
        available_commands = "\n".join(names) # joining the list of names by a new line
        embed  = disnake.Embed(description=available_commands)
        await self.context.send(embed=embed)

    async def send_error_message(self, error):
        channel = self.get_destination() # defaults to command context channel
        await channel.send(error)

bot.help_command = MyHelp()

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