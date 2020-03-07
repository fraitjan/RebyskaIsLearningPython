import random

BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
COLOR_RESET = '\033[0m'

holky = ["Rebyska", "Miska", "Martinka"]
kluci = ["Honzik", "Filip", "Misak"]
zviratka = ["tucnacka", "vydrinku", "psika"]

"""
Použij while smyčku, která skončí, až se některý list vyprázdní (nic v něm nebude).
Z listu odebereš prvek pomocí list.remove(prvek) - v tomto případě např. holky.remove["Rebyska"]
Vždy se vybere náhodná holka, náhodný kluk a náhodné zvíře.
Vypiš je podle příkladu, který jsem ti napsal na Messenger - i s barvičkama
"""

