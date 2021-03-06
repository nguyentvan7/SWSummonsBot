from discord.ext import commands, tasks
from prettytable import PrettyTable
from prettytable import PLAIN_COLUMNS
from discord import Embed
import json
import summon
import asyncio


class Cog_Summon(commands.Cog):
    longmes = "Too many monsters, increasing minimum stars to "
    stats = {}

    def __init__(self, bot):
        self.bot = bot
        # Open statistics csv.
        if not bool(Cog_Summon.stats):
            try:
                with open('stats.json', 'r') as stats_file:
                    Cog_Summon.stats = json.load(stats_file)
            except FileNotFoundError:
                print("No stats file found.")
        self.autosave.start()

    def save():
        with open('stats.json', 'w') as stats_file:
            json.dump(Cog_Summon.stats, stats_file)

    @tasks.loop(seconds=3600)
    async def autosave(self):
        Cog_Summon.save()
        print("Autosaved")

    def name_element(self, monsters, min_star):
        m = []
        for monster in monsters:
            if monster["natural_stars"] < min_star:
                continue
            if monster["natural_stars"] <= 3:
                if monster["is_awakened"] == True:
                    m.append(monster["name"])
                else:
                    m.append(monster["element"].capitalize() +
                             " " + monster["name"])
            elif monster["natural_stars"] == 4:
                if monster["is_awakened"] == True \
                        and (monster["name"] != "CHUN-LI" and monster["name"] != "DHALSIM") \
                        and monster["archetype"] != "UNKNOWN":
                    m.append("__" + monster["name"] + "__")
                else:
                    m.append(
                        "__" + monster["element"].capitalize() + " " + monster["name"] + "__")
            elif monster["natural_stars"] == 5:
                m.append(
                    "**" + monster["element"].capitalize() + " " + monster["name"] + "**")
            else:
                m.append(monster["element"].capitalize() +
                         " " + monster["name"])
        return m

    def count_stars(self, monsters):
        count = [0, 0, 0, 0, 0]
        mons = [[], [], [], [], []]
        for monster in monsters:
            count[monster["natural_stars"]-1] += 1
            mons[monster["natural_stars"]-1].append(monster)
        return count, mons

    @commands.command(name='sum', help='Summons a scroll of specified type and amount. [uk, ms, leg, ld, trans, sf, ss]')
    async def summon_command(self, ctx, type: str, amt: int = 1, min_star: int = 3):
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
        elif type == "ss":
            s = summon.summon(6, amt)
        elif type == "pp":
            s = summon.summon(1, amt*11)
        elif type == "nat5":
            s = summon.summon(7, amt)
        elif type == "ld5":
            s = summon.summon(8, amt)
        elif type == "ss5":
            s = summon.summon(9, amt)
        elif type == "swc":
            s = summon.summon(10, amt)
        elif type == "swc5":
            s = summon.summon(11, amt)
        else:
            await ctx.send("Invalid summoning options")
            return

        # Change type for nat5, pp and ld5.
        if type == "nat5":
            type = "ms"
        elif type == "pp":
            type = "ms"
        elif type == "ld5":
            type = "ld"
        elif type == "ss5":
            type = "ss"
        elif type == "swc5":
            type = "swc"

        counts, split_mons = self.count_stars(s)
        total = sum(counts)
        cost = total*summon.costs[summon.types.index(type)]
        counts_str = "\n3\u2b50: {star_3}\n4\u2b50: {star_4}\n5\u2b50: {star_5}\nCost: ${cost:,.2f}".format(
            star_3=counts[2], star_4=counts[3], star_5=counts[4], cost=cost)
        user = str(ctx.author.id)
        mes = "<@" + user + "> " + \
            ', '.join(self.name_element(s, min_star)) + counts_str
        while len(mes) > 2000:
            min_star += 1
            mes = "<@" + user + "> " + \
                ', '.join(self.name_element(s, min_star)) + counts_str
            await ctx.send(self.longmes + str(min_star) + ".")
        await ctx.send(mes)
        # Blessing
        blessing = []
        if counts[4] > 0 and (type == "ms" or type == "leg" or type == "trans"):
            for i in range(counts[4]):
                bless = summon.summon(4, 1)
                while bless[0] == split_mons[4][i]:
                    bless = summon.summon(4, 1)
                blessing.extend(bless)
            mes = "<@" + user + "> You have been blessed **" + str(counts[4]) + "** time" + (
                "s" if counts[4] > 1 else "") + "!\n" + ', '.join(self.name_element(blessing, min_star))
            await ctx.send(mes)

        # Stats tracking.
        try:
            Cog_Summon.stats[user]
        except KeyError:
            Cog_Summon.stats[user] = {}
        try:
            Cog_Summon.stats[user][type]
        except KeyError:
            Cog_Summon.stats[user][type] = {}
            Cog_Summon.stats[user][type]["3_star"] = 0
            Cog_Summon.stats[user][type]["4_star"] = 0
            Cog_Summon.stats[user][type]["5_star"] = 0
        Cog_Summon.stats[user][type]["3_star"] += counts[2]
        Cog_Summon.stats[user][type]["4_star"] += counts[3]
        Cog_Summon.stats[user][type]["5_star"] += counts[4]

    @commands.command(name='stats', help='Prints stats on your summoning history')
    async def stats_command(self, ctx):
        if not ctx.message.mentions:
            user = str(ctx.author.id)
        else:
            user = str(ctx.message.mentions[0].id)
        try:
            user_stats = Cog_Summon.stats[user]
        except KeyError:
            await ctx.send("<@" + user + "> You haven't summoned anything")
            return
        mes = "<@" + user + "> You have summoned:\n"
        table = PrettyTable(["Type", "3\u2b50", "4\u2b50",
                             "5\u2b50", "Total", "5\u2b50Rate", "Cost"])
        table.set_style(PLAIN_COLUMNS)
        totals = [0, 0, 0, 0, 0]
        rows = 0
        for type in summon.types:
            try:
                row = []
                counts = Cog_Summon.stats[user][type]
                type_total = counts["3_star"] + \
                    counts["4_star"] + counts["5_star"]
                row.append(type)
                row.append("{:,}".format(counts["3_star"]))
                totals[0] += counts["3_star"]
                row.append("{:,}".format(counts["4_star"]))
                totals[1] += counts["4_star"]
                row.append("{:,}".format(counts["5_star"]))
                totals[2] += counts["5_star"]
                row.append("{:,}".format(type_total))
                totals[3] += type_total
                row.append("{:.2f}%".format(counts["5_star"]/type_total*100))
                cost = type_total*summon.costs[summon.types.index(type)]
                row.append("${:,.0f}".format(cost))
                totals[4] += cost
                table.add_row(row)
                rows += 1
            except KeyError:
                continue
        row = []
        row.append("all")
        row.append("{:,}".format(totals[0]))
        row.append("{:,}".format(totals[1]))
        row.append("{:,}".format(totals[2]))
        row.append("{:,}".format(totals[3]))
        row.append("{:.2f}%".format(totals[2]/totals[3]*100))
        row.append("${:,.0f}".format(totals[4]))
        table.add_row(row)
        await ctx.send(mes + "```" + table.get_string() + "```")

    @commands.command(name='resetstats', help='Resets stats for the user')
    async def reset_stats_command(self, ctx):
        # Stats tracking.
        user = str(ctx.author.id)
        Cog_Summon.stats[user] = {}
        await ctx.send("<@" + user + "> Your stats have been reset.")

    @commands.command(name='save', help='Saves summoning stats data.')
    async def save_command(self, ctx):
        Cog_Summon.save()
        await ctx.send("Saved statistics.")


def setup(bot):
    bot.add_cog(Cog_Summon(bot))


def teardown(bot):
    Cog_Summon.save()
