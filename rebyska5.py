import random

BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
COLOR_RESET = '\033[0m'

animals = {
    "vydrinka": ["Slovensko", "Cesko", "Singapore"],
    "tucnacik": ["Antarktida", "Chile", "Argentina"],
    "peso": ["Slovensko", "Cesko", "Anglie", "USA", "Nemecko"],
    "slonik": ["Rwanda", "Indie"],
    "pandicka": ["Cina"],
    "ptakopysk": ["Australie"]
}

all_countries = list()
for countries in animals.values():
    for country in countries:
        if country not in all_countries:
            all_countries.append(country)

points = 0
total_points = len(animals)

while animals:
    random_animal = random.choice(list(animals.keys()))
    random_country = random.choice(all_countries)
    answer = input("Zije " + BLUE + random_animal + COLOR_RESET + " v " + BLUE + random_country + COLOR_RESET + "?:")
    if answer.lower() == "ano":
        if random_country in animals[random_animal]:
            print(GREEN + "Spravne! " + random_animal + " zije v " + random_country + COLOR_RESET)
            points += 1
        else:
            print(RED + "Spatne! " + random_animal + " nezije v " + random_country + COLOR_RESET)
    if answer.lower() == "ne":
        if random_country not in animals[random_animal]:
            print(GREEN + "Spravne! " + random_animal + " nezije v " + random_country + COLOR_RESET)
            points += 1
        else:
            print(RED + "Spatne! " + random_animal + " zije v " + random_country + COLOR_RESET)
    del animals[random_animal]

print("Konec, ziskal jsi celkem " + BLUE + str(points) + "/" + str(total_points) + COLOR_RESET + " bodu.")
