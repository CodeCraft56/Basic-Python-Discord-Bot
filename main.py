import discord
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents, case_insensitive=True)
bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help Command", description="!ping - View the ping of the bot", color=discord.Color.blue())
    await ctx.channel.send(embed=embed)

@bot.command()
async def ping(ctx):
    await ctx.reply("Pong! 🏓")

bot.run("") #Replace with your token here
