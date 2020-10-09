import json
import random

with open("elem1.json") as f:
    elem1 = json.load(f)
with open("elem2.json") as f:
    elem2 = json.load(f)
with open("elem3.json") as f:
    elem3 = json.load(f)
with open("elem4.json") as f:
    elem4 = json.load(f)
with open("elem5.json") as f:
    elem5 = json.load(f)
with open("ld3.json") as f:
    ld3 = json.load(f)
with open("ld4.json") as f:
    ld4 = json.load(f)
with open("ld5.json") as f:
    ld5 = json.load(f)
with open("awake_elem1.json") as f:
    awake_elem1 = json.load(f)
with open("awake_elem2.json") as f:
    awake_elem2 = json.load(f)
with open("awake_elem3.json") as f:
    awake_elem3 = json.load(f)
with open("awake_elem4.json") as f:
    awake_elem4 = json.load(f)
with open("awake_ld3.json") as f:
    awake_ld3 = json.load(f)
with open("awake_ld4.json") as f:
    awake_ld4 = json.load(f)
with open("sf_elem4.json") as f:
    sf_elem4 = json.load(f)
with open("sf_ld4.json") as f:
    sf_ld4 = json.load(f)
with open("sf_elem5.json") as f:
    sf_elem5 = json.load(f)
with open("sf_ld5.json") as f:
    sf_ld5 = json.load(f)

def unknown():
    # Technically incorrect, should fix at some point.
    # awaken should be only done if the monster is awakened.
    r = random.random()
    a = random.random()
    if r < .742:
        # 1 star.
        if a < .98:
            # Not awakened.
            return random.choice(elem1)
        else:
            # Awakened.
            return random.choice(awake_elem1)
    elif r < .986:
        # 2 star.
        if a < .98:
            # Not awakened.
            return random.choice(elem2)
        else:
            # Awakened.
            return random.choice(awake_elem2)
    else:
        # 3 star.
        return random.choice(elem3)

def mystical():
    r = random.random()
    a = random.random()
    if r < .915:
        # 3 star.
        if a < .98:
            # Not awakened.
            return random.choice(elem3)
        else:
            # Awakened.
            return random.choice(awake_elem3)
    elif r < .995:
        # 4 star.
        if a < .98:
            # Not awakened.
            return random.choice(elem4)
        else:
            # Awakened.
            return random.choice(awake_elem4)
    else:
        # 5 star.
        return random.choice(elem5)

def legendary():
    r = random.random()
    a = random.random()
    if r < .935:
        # 4 star.
        if a < .98:
            # Not awakened.
            return random.choice(elem4)
        else:
            # Awakened.
            return random.choice(awake_elem4)
    else:
        # 5 star.
        return random.choice(elem5)

def ld():
    r = random.random()
    a = random.random()
    if r < .9365:
        # 3 star.
        if a < .98:
            # Not awakened.
            return random.choice(ld3)
        else:
            # Awakened.
            return random.choice(awake_ld3)
    elif r < .9965:
        # 4 star.
        if a < .98:
            # Not awakened.
            return random.choice(ld4)
        else:
            # Awakened.
            return random.choice(awake_ld4)
    else:
        # 5 star.
        return random.choice(ld5)

def trans():
    # 5 star.
    return random.choice(elem5)

def sf():
    r = random.random()
    if r < .846:
        # 4 star elemental.
        return random.choice(sf_elem4)
    elif r < .92:
        # 4 star ld.
        return random.choice(sf_ld4)
    elif r < .9962:
        # 5 star elemental.
        return random.choice(sf_elem5)
    else:
        # 5 star ld.
        return random.choice(sf_ld5)

def summon(type, amt):
    methods = [unknown, mystical, legendary, ld, trans, sf]
    summoned = []
    for i in range(amt):
        summoned.append(methods[type]())
    return summoned
