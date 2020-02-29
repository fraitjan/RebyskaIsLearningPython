import random

BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
COLOR_RESET = '\033[0m'

animal_list = ["vydra", "tucnak", "ptakopysk", "panda", "koala", "peso"]

animal = random.choice(animal_list)

animal_guess = None

while animal_guess != animal:
    animal_guess = input("Na jake zvire myslim?: ")
    if animal_guess != animal:
        print(RED + "Spatne, nemyslim na: " + BLUE + animal_guess + COLOR_RESET)
#       animal_list.remove(animal_guess)
#       print("Zbyvajici moznosti jsou: " + BLUE + (COLOR_RESET + ", " + BLUE).join(animal_list) + COLOR_RESET)

print(GREEN + "Spravne, myslel jsem na: " + BLUE + animal + COLOR_RESET)
