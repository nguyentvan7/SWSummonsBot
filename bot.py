import os
from discord.ext import commands
from dotenv import load_dotenv
import csv
import summon

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

with open('user_info.csv', mode='r') as file:
    csvFile = csv.reader(file)



def name_element(monsters):
    m = []
    for monster in monsters:
        if monster["natural_stars"] == 4:
            m.append("*" + monster["element"].capitalize() + " " + monster["name"] + "*")
        elif monster["natural_stars"] == 5:
            m.append("**" + monster["element"].capitalize() + " " + monster["name"] + "**")
        else:
            m.append(monster["element"].capitalize() + " " + monster["name"])
    return m

@bot.command(name='sum', help='Summons a scroll of specified type and amount.')
async def summon_command(ctx, type: str, amt: int):
    if type == "uk":
        s = summon.summon(0, amt)
    elif type == "ms":
        s = summon.summon(1, amt)
    elif type == "leg":
        s = summon.summon(2, amt)
    elif type == "ld":
        s = summon.summon(3, amt)
    elif type == "trans":
        s = summon.summon(4, amt)
    elif type == "sf":
        s = summon.summon(5, amt)
    else:
        await ctx.send("Invalid summoning options")
    await ctx.send(', '.join(name_element(s)))

@bot.command(name='exit', help='Exit bot')
async def exit_command(ctx):
    exit()

bot.run(TOKEN)

