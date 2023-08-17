import discord
from volonterstvo import Musoru_Shans
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Наш бот {bot.user} запущен!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def Musor(ctx):
    await ctx.send(Musoru_Shans())

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)



bot.run('TOKEN')