import random
from helpers.colors import *

animal_list = ["vydra", "tucnak", "ptakopysk", "panda", "koala", "peso"]

animal = random.choice(animal_list)

animal_guess = ""

while animal_guess.lower() != animal.lower():
    animal_guess = input("Na jake zvire myslim?: ")
    if animal_guess.lower() != animal.lower():
        print(RED + "Spatne, nemyslim na: " + BLUE + animal_guess + COLOR_RESET)
        # if animal_guess in animal_list:
        #     animal_list.remove(animal_guess)
        # print("Zbyvajici moznosti jsou: " + BLUE + (COLOR_RESET + ", " + BLUE).join(animal_list) + COLOR_RESET)

print(GREEN + "Spravne, myslel jsem na: " + BLUE + animal + COLOR_RESET)
