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

def unknown():
    r = random.random()
    a = random.random()
    if r < .742:
        # 1 star.
        if a < .98:
            # Not awakened.
            m = random.randrange(0, len(elem1))
            return elem1[m]
        else:
            # Awakened.
            m = random.randrange(0, len(awake_elem1))
            return awake_elem1[m]
    elif r < .986:
        # 2 star.
        if a < .98:
            # Not awakened.
            m = random.randrange(0, len(elem2))
            return elem2[m]
        else:
            # Awakened.
            m = random.randrange(0, len(awake_elem2))
            return awake_elem2[m]
    else:
        # 3 star.
        m = random.randrange(0, len(elem3)-1)
        return elem3[m]

def mystical():
    r = random.random()
    a = random.random()
    if r < .915:
        # 3 star.
        if a < .98:
            # Not awakened.
            m = random.randrange(0, len(elem3))
            return elem3[m]
        else:
            # Awakened.
            m = random.randrange(0, len(awake_elem3))
            return awake_elem3[m]
    elif r < .995:
        # 4 star.
        if a < .98:
            # Not awakened.
            m = random.randrange(0, len(elem4))
            return elem4[m]
        else:
            # Awakened.
            m = random.randrange(0, len(awake_elem4))
            return awake_elem4[m]
    else:
        # 5 star.
        m = random.randrange(0, len(elem5)-1)
        return elem5[m]

def legendary():
    r = random.random()
    a = random.random()
    if r < .935:
        # 4 star.
        if a < .98:
            # Not awakened.
            m = random.randrange(0, len(elem4))
            return elem4[m]
        else:
            # Awakened.
            m = random.randrange(0, len(awake_elem4))
            return awake_elem4[m]
    else:
        # 5 star.
        m = random.randrange(0, len(elem5)-1)
        return elem5[m]

def ld():
    r = random.random()
    a = random.random()
    if r < .9365:
        # 3 star.
        if a < .98:
            # Not awakened.
            m = random.randrange(0, len(ld3))
            return ld3[m]
        else:
            # Awakened.
            m = random.randrange(0, len(awake_ld3))
            return awake_ld3[m]
    elif r < .9965:
        # 4 star.
        if a < .98:
            # Not awakened.
            m = random.randrange(0, len(ld4))
            return ld4[m]
        else:
            # Awakened.
            m = random.randrange(0, len(awake_ld4))
            return awake_ld4[m]
    else:
        # 5 star.
        m = random.randrange(0, len(ld5)-1)
        return ld5[m]

def summon(type, amt):
    methods = [unknown, mystical, legendary, ld]
    summoned = []
    for i in range(amt):
        summoned.append(methods[type]())
    return summoned
