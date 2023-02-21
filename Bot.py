import os
import discord
import asyncio
import disnake
import requests
import sqlite3
from bs4 import BeautifulSoup
from disnake.ext import commands
from discord.ext import commands  
from dotenv import load_dotenv

load_dotenv()

# sets intents and env token
intents = discord.Intents.all()
token = os.getenv('TOKEN')

# sets command prefix
bot = discord.ext.commands.Bot(command_prefix = '!', intents = intents)

# help command configuration
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

async def one_piece():
    await bot.wait_until_ready()

    #  text channels
    Test_id = 1062734654634999861
    
    Shiba_id = 245706289550852098

    while not bot.is_closed():
        
        # connect to database to get chapter number
        conn = sqlite3.connect('data.db') # connects to database
        cursor = conn.cursor() # creates a cursor to execute SQL queries
        cursor.execute("SELECT ChapterNum FROM MangaChapter WHERE Name='One Piece'")
        result = cursor.fetchone()[0] # fetch the query result

        # get html content for one piece
        response = requests.get('https://onepiecechapters.com/mangas/5/one-piece')
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        chapter = '-' + str(result)

        # find href with manga chapter number
        link = soup.find('a', href=lambda href: href and chapter in str(href))
        if link is not None: # if href exists, post link and update database
            href_value = link['href']

            # send to Test channel
            channel = bot.get_channel(Test_id)
            await channel.send('https://onepiecechapters.com' + href_value)

            # send to Shiba channel
            channel = bot.get_channel(Shiba_id)
            await channel.send('https://onepiecechapters.com' + href_value)

            next_ch = result+1
            cursor.execute("UPDATE MangaChapter SET ChapterNum = ? WHERE Name = ?", (next_ch, 'One Piece'))
            conn.commit() # commit executed changes
        # close the connection and cursor
        cursor.close()
        conn.close()

        # run every 4 hours
        print('Checking for the One Piece!')
        await asyncio.sleep(14400)

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
async def coffee(ctx):
    source = 'coffee.mp3'
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
async def chipotle(ctx):
    source = 'chipotle.mp3'
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

async def test():
    channel = bot.get_channel(1062734654634999861)
    await channel.send('Test')

async def background_test():
    await bot.wait_until_ready()
    while not bot.is_closed():
        await asyncio.sleep(30)
        await test()


async def start():
    async with bot:
        bot.loop.create_task(one_piece())
        await bot.start(token)

#bot.run(token)
asyncio.run(start())