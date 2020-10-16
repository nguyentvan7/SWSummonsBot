import json

with open("minified.json") as f:
    bestiary = json.load(f)

def gen_mon(monster):
    m = {}
    m["name"] = monster["fields"]["name"]
    m["image_filename"] = monster["fields"]["image_filename"]
    m["element"] = monster["fields"]["element"]
    m["archetype"] = monster["fields"]["archetype"]
    m["natural_stars"] = monster["fields"]["natural_stars"]
    m["can_awaken"] = monster["fields"]["can_awaken"]
    m["is_awakened"] = monster["fields"]["is_awakened"]
    return m

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "fire" or monster["fields"]["element"] == "wind" or monster["fields"]["element"] == "water") \
    and monster["fields"]["natural_stars"] == 1 \
    and monster["fields"]["obtainable"] == True \
    and monster["fields"]["is_awakened"] == False \
    and monster["fields"]["name"] != "Angelmon" \
    and monster["fields"]["name"] != "Devilmon" \
    and monster["fields"]["name"] != "King Angelmon":
        monsters.append(gen_mon(monster))
with open("elem1.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "fire" or monster["fields"]["element"] == "wind" or monster["fields"]["element"] == "water") \
    and monster["fields"]["natural_stars"] == 2 \
    and monster["fields"]["obtainable"] == True \
    and monster["fields"]["is_awakened"] == False:
        monsters.append(gen_mon(monster))
with open("elem2.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "fire" or monster["fields"]["element"] == "wind" or monster["fields"]["element"] == "water") \
    and monster["fields"]["natural_stars"] == 3 \
    and monster["fields"]["obtainable"] == True \
    and monster["fields"]["is_awakened"] == False \
    and monster["fields"]["name"] != "Cow Girl":
        monsters.append(gen_mon(monster))
with open("elem3.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "fire" or monster["fields"]["element"] == "wind" or monster["fields"]["element"] == "water") \
    and monster["fields"]["natural_stars"] == 4 \
    and monster["fields"]["obtainable"] == True \
    and monster["fields"]["is_awakened"] == False \
    and monster["fields"]["name"] != "CHUN-LI" \
    and monster["fields"]["name"] != "DHALSIM":
        monsters.append(gen_mon(monster))
with open("elem4.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "fire" or monster["fields"]["element"] == "wind" or monster["fields"]["element"] == "water") \
    and monster["fields"]["natural_stars"] == 5 \
    and monster["fields"]["obtainable"] == True \
    and monster["fields"]["is_awakened"] == False \
    and monster["fields"]["name"] != "Ifrit" \
    and monster["fields"]["name"] != "Homunculus(Attack)" \
    and monster["fields"]["name"] != "M. BISON" \
    and monster["fields"]["name"] != "KEN" \
    and monster["fields"]["name"] != "RYU" \
    and not(monster["fields"]["name"] == "Phoenix" and monster["fields"]["element"] == "water") \
    and not(monster["fields"]["name"] == "Valkyrja" and monster["fields"]["element"] == "wind") \
    and not(monster["fields"]["name"] == "Lightning Emperor" and monster["fields"]["element"] == "fire") \
    and not(monster["fields"]["name"] == "Panda Warrior" and monster["fields"]["element"] == "fire"):
        monsters.append(gen_mon(monster))
with open("elem5.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "light" or monster["fields"]["element"] == "dark") \
    and monster["fields"]["natural_stars"] == 3 \
    and monster["fields"]["obtainable"] == True \
    and monster["fields"]["is_awakened"] == False \
    and monster["fields"]["name"] != "Cow Girl" \
    and not(monster["fields"]["name"] == "Magical Archer" and monster["fields"]["element"] == "light") \
    and monster["fields"]["name"] != "Fairy Queen":
        monsters.append(gen_mon(monster))
with open("ld3.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "light" or monster["fields"]["element"] == "dark") \
    and monster["fields"]["natural_stars"] == 4 \
    and monster["fields"]["obtainable"] == True \
    and monster["fields"]["is_awakened"] == False \
    and monster["fields"]["name"] != "CHUN-LI" \
    and monster["fields"]["name"] != "DHALSIM":
        monsters.append(gen_mon(monster))
with open("ld4.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "light" or monster["fields"]["element"] == "dark") \
    and monster["fields"]["natural_stars"] == 5 \
    and monster["fields"]["obtainable"] == True \
    and monster["fields"]["is_awakened"] == False \
    and monster["fields"]["name"] != "Ifrit" \
    and monster["fields"]["name"] != "Homunculus(Support)" \
    and monster["fields"]["name"] != "Vampire Lord" \
    and monster["fields"]["name"] != "M. BISON" \
    and monster["fields"]["name"] != "KEN" \
    and monster["fields"]["name"] != "RYU" \
    and not(monster["fields"]["name"] == "Paladin" and monster["fields"]["element"] == "light"):
        monsters.append(gen_mon(monster))
with open("ld5.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "fire" or monster["fields"]["element"] == "wind" or monster["fields"]["element"] == "water") \
    and monster["fields"]["natural_stars"] == 1 \
    and monster["fields"]["obtainable"] == True \
    and monster["fields"]["is_awakened"] == True \
    and not "Angelmon" in monster["fields"]["name"]:
        monsters.append(gen_mon(monster))
with open("awake_elem1.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "fire" or monster["fields"]["element"] == "wind" or monster["fields"]["element"] == "water") \
    and monster["fields"]["natural_stars"] == 2 \
    and monster["fields"]["obtainable"] == True \
    and monster["fields"]["is_awakened"] == True:
        monsters.append(gen_mon(monster))
with open("awake_elem2.json", "w") as out:
    json.dump(monsters, out)
    
monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "fire" or monster["fields"]["element"] == "wind" or monster["fields"]["element"] == "water") \
    and monster["fields"]["natural_stars"] == 3 \
    and monster["fields"]["obtainable"] == True \
    and monster["fields"]["is_awakened"] == True \
    and not monster["fields"]["name"] in ["Anne", "Hannah", "Sera"]:
        monsters.append(gen_mon(monster))
with open("awake_elem3.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "fire" or monster["fields"]["element"] == "wind" or monster["fields"]["element"] == "water") \
    and monster["fields"]["natural_stars"] == 4 \
    and monster["fields"]["obtainable"] == True \
    and monster["fields"]["is_awakened"] == True \
    and monster["fields"]["name"] != "CHUN-LI" \
    and monster["fields"]["name"] != "DHALSIM":
        monsters.append(gen_mon(monster))
with open("awake_elem4.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "light" or monster["fields"]["element"] == "dark") \
    and monster["fields"]["natural_stars"] == 3 \
    and monster["fields"]["obtainable"] == True \
    and monster["fields"]["is_awakened"] == True \
    and not monster["fields"]["name"] in ["Loren", "Cassie"] \
    and monster["fields"]["name"] != "Fami" \
    and monster["fields"]["name"] != "Fran":
        monsters.append(gen_mon(monster))
with open("awake_ld3.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "light" or monster["fields"]["element"] == "dark") \
    and monster["fields"]["natural_stars"] == 4 \
    and monster["fields"]["obtainable"] == True \
    and monster["fields"]["is_awakened"] == True \
    and monster["fields"]["name"] != "CHUN-LI" \
    and monster["fields"]["name"] != "DHALSIM":
        monsters.append(gen_mon(monster))
with open("awake_ld4.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "fire" or monster["fields"]["element"] == "wind" or monster["fields"]["element"] == "water") \
    and (monster["fields"]["name"] == "CHUN-LI" or monster["fields"]["name"] == "DHALSIM"):
        monsters.append(gen_mon(monster))
with open("sf_elem4.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "light" or monster["fields"]["element"] == "dark") \
    and (monster["fields"]["name"] == "CHUN-LI" or monster["fields"]["name"] == "DHALSIM"):
        monsters.append(gen_mon(monster))
with open("sf_ld4.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "fire" or monster["fields"]["element"] == "wind" or monster["fields"]["element"] == "water") \
    and (monster["fields"]["name"] == "M. BISON" or monster["fields"]["name"] == "RYU"):
        monsters.append(gen_mon(monster))
with open("sf_elem5.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "light" or monster["fields"]["element"] == "dark") \
    and (monster["fields"]["name"] == "M. BISON" or monster["fields"]["name"] == "RYU"):
        monsters.append(gen_mon(monster))
with open("sf_ld5.json", "w") as out:
    json.dump(monsters, out)