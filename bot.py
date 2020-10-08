import os
from discord.ext import commands
from dotenv import load_dotenv
import summon

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

def name_element(monsters):
    m = []
    for monster in monsters:
        if monster["fields"]["natural_stars"] == 4:
            m.append("*" + monster["fields"]["element"].capitalize() + " " + monster["fields"]["name"] + "*")
        elif monster["fields"]["natural_stars"] == 5:
            m.append("**" + monster["fields"]["element"].capitalize() + " " + monster["fields"]["name"] + "**")
        else:
            m.append(monster["fields"]["element"].capitalize() + " " + monster["fields"]["name"])
    return m

@bot.command(name='sum', help='Summons a scroll of specified type and amount.')
async def summon_command(ctx, type: str, amt: int):
    if type == "uk":
        s = summon.summon(0, amt)
        await ctx.send(', '.join(name_element(s)))
    elif type == "ms":
        s = summon.summon(1, amt)
        await ctx.send(', '.join(name_element(s)))
    elif type == "leg":
        s = summon.summon(2, amt)
        await ctx.send(', '.join(name_element(s)))
    elif type == "ld":
        s = summon.summon(3, amt)
        await ctx.send(', '.join(name_element(s)))

@bot.command(name='exit', help='Exit bot')
async def exit_command(ctx):
    exit()

bot.run(TOKEN)

