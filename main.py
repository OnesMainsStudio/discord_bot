import discord
from discord.ext import commands
import random as r
from settings import *
from bot_logic import gen_pass
from bot_logic import random_funfact
# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='.', intents=intents)
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
#client = discord.Client(intents=intents)
list_of_commands=[
    "help", #0
    "hello", #1
    "are_you_here", #2
    "give_me_random_funfact", #3
    "generate_password", #4
    "add_numbers" #5
]
@bot.event
async def on_ready():
    print(f'You got logged into: {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć')
@bot.command()
async def heh(ctx, count=5):
    for i in range(count):
        await ctx.send('he')
#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return
#    if message.content.startswith("."):
#        if message.content.startswith(list_of_commands[0]):
#            await message.channel.send("List of commands:")
#            print("writing command:", list_of_commands[0])
#            
#            for i in range(len(list_of_commands)):
#                await message.channel.send(list_of_commands[i])
#                
#        elif message.content.startswith(list_of_commands[1]):
#            await message.channel.send("Hello!")
#            print("writing command:", list_of_commands[1])
#            
#        elif message.content.startswith(list_of_commands[2]):
#            await message.channel.send("Yes I'am Here :laughing:")
#            print("writing command:", list_of_commands[2])
#            
#        elif message.content.startswith(list_of_commands[3]):
#            await message.channel.send(random_funfact())
#            await message.channel.send("how cool is that :sunglasses:")
#            print("writing command:", list_of_commands[3])
#        elif message.content.startswith(list_of_commands[4]):
#            await message.channel.send('your password:')
#            await message.channel.send(gen_pass(25))
#        elif message.content.startswith(list_of_commands[5]):
#                pass

bot.run(settings['TOKEN'])
