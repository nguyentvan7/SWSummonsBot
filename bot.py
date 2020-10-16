import os
from cog_summon import Cog_Summon
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

bot.load_extension("cog_summon")

@bot.command(name='exit', help='Exit bot')
async def exit_command(ctx):
    await bot.logout()

@bot.command(name='reload', help='Reload bot')
async def reload_command(ctx):
    bot.reload_extension("cog_summon")

bot.run(TOKEN)

