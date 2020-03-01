from helpers.animals_data import Animals
from helpers.colors import *

animal_name = ["penguin"]

a = Animals("./data/anage_data.csv")
animals = a.get_specific_animal(animal_name)
for animal in animals:
    if animal["Adult weight (g)"]:
        print(BLUE + animal["Common name"] + COLOR_RESET + " váží v průměru: " + GREEN +
              str(float(animal["Adult weight (g)"])/1000) + "kg" + COLOR_RESET)
