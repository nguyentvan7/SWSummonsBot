from discord.ext import commands
import csv
import summon
class Cog_Summon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def name_element(self, monsters, min_star):
        m = []
        for monster in monsters:
            if monster["natural_stars"] < min_star:
                continue
            if monster["natural_stars"] == 4:
                if monster["is_awakened"] == True \
                and (monster["name"] != "CHUN-LI" or monster["name"] != "DHALSIM") \
                and monster["archetype"] != "UNKNOWN":
                    m.append("__" + monster["name"] + "__")
                else:
                    m.append("__" + monster["element"].capitalize() + " " + monster["name"] + "__")
            elif monster["natural_stars"] == 5:
                m.append("**" + monster["element"].capitalize() + " " + monster["name"] + "**")
            else:
                m.append(monster["element"].capitalize() + " " + monster["name"])
        return m

    def count_stars(self, monsters):
        count = [0, 0, 0, 0, 0]
        for monster in monsters:
            count[monster["natural_stars"]-1] += 1
        return count


    @commands.command(name='sum', help='Summons a scroll of specified type and amount. [uk, ms, leg, ld, trans, sf, ss]')
    async def summon_command(self, ctx, type: str, amt: int, min_star: int=1):
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
        else:
            await ctx.send("Invalid summoning options")
            return
        counts = self.count_stars(s)
        stats = "\n3\u2b50: {star_3}\n4\u2b50: {star_4}\n5\u2b50: {star_5}".format(star_3=counts[2], star_4=counts[3], star_5=counts[4])
        mes = await ctx.send("<@" + str(ctx.author.id) + "> " + ', '.join(self.name_element(s, min_star)) + stats)

        
def setup(bot):
    bot.add_cog(Cog_Summon(bot))        