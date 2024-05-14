import discord
from discord.ext import commands
import asyncio
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

message = config.get('NUKER_SETTINGS', 'MESSAGE') 
token = config.get('NUKER_SETTINGS', 'TOKEN') 
channelName = config.get('NUKER_SETTINGS', 'CHANNELNAME') 
prefix = config.get('NUKER_SETTINGS', 'PREFIX') 
activity = config.get('NUKER_SETTINGS', 'ACTIVITY') 

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=activity))
async def send_message(channel, message):
    await channel.send(message)
@bot.command()
async def start(ctx):  
    guild = ctx.guild
    tasks = []
    for i in range(0,25): # changing to higher values risks discord to block ur ip for 15-20 min.
        new_channel = await guild.create_text_channel(channelName)
        tasks.append(send_message(new_channel, message))
    await asyncio.gather(*tasks)
bot.run(token)
