import json

with open("bestiary_data.json") as f:
    bestiary = json.load(f)

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
        monsters.append(monster)
with open("elem1.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "fire" or monster["fields"]["element"] == "wind" or monster["fields"]["element"] == "water") \
    and monster["fields"]["natural_stars"] == 2 \
    and monster["fields"]["obtainable"] == True \
    and monster["fields"]["is_awakened"] == False:
        monsters.append(monster)
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
        monsters.append(monster)
with open("elem3.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "fire" or monster["fields"]["element"] == "wind" or monster["fields"]["element"] == "water") \
    and monster["fields"]["natural_stars"] == 4 \
    and monster["fields"]["obtainable"] == True \
    and monster["fields"]["is_awakened"] == False:
        monsters.append(monster)
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
    and not(monster["fields"]["name"] == "Phoenix" and monster["fields"]["element"] == "water") \
    and not(monster["fields"]["name"] == "Valkyrja" and monster["fields"]["element"] == "wind") \
    and not(monster["fields"]["name"] == "Lightning Emperor" and monster["fields"]["element"] == "fire"):
        monsters.append(monster)
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
    and not(monster["fields"]["name"] != "Magical Archer" and monster["fields"]["element"] == "light") \
    and monster["fields"]["name"] != "Fairy Queen":
        monsters.append(monster)
with open("ld3.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "light" or monster["fields"]["element"] == "dark") \
    and monster["fields"]["natural_stars"] == 4 \
    and monster["fields"]["obtainable"] == True \
    and monster["fields"]["is_awakened"] == False:
        monsters.append(monster)
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
    and not(monster["fields"]["name"] != "Paladin" and monster["fields"]["element"] == "light"):
        monsters.append(monster)
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
        monsters.append(monster)
with open("awake_elem1.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "fire" or monster["fields"]["element"] == "wind" or monster["fields"]["element"] == "water") \
    and monster["fields"]["natural_stars"] == 2 \
    and monster["fields"]["obtainable"] == True \
    and monster["fields"]["is_awakened"] == True:
        monsters.append(monster)
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
        monsters.append(monster)
with open("awake_elem3.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "fire" or monster["fields"]["element"] == "wind" or monster["fields"]["element"] == "water") \
    and monster["fields"]["natural_stars"] == 4 \
    and monster["fields"]["obtainable"] == True \
    and monster["fields"]["is_awakened"] == True:
        monsters.append(monster)
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
        monsters.append(monster)
with open("awake_ld3.json", "w") as out:
    json.dump(monsters, out)

monsters = []
for monster in bestiary:
    if monster["model"] == "bestiary.monster" \
    and (monster["fields"]["element"] == "light" or monster["fields"]["element"] == "dark") \
    and monster["fields"]["natural_stars"] == 4 \
    and monster["fields"]["obtainable"] == True \
    and monster["fields"]["is_awakened"] == True:
        monsters.append(monster)
with open("awake_ld4.json", "w") as out:
    json.dump(monsters, out)