from helpers.animals_data import Animals
from helpers.colors import *

animal_names = []

a = Animals("./data/anage_data.csv")

input_animal = ""

while input_animal.lower() != "q":
    input_animal = input("Zadej další zvíře (Q pro konec): ")
    if input_animal != "q":
        animal_names.append(input_animal)

animals = a.get_specific_animals(animal_names)

for animal in animals:
    if animal["Adult weight (g)"]:
        try:
            celsius = float(animal["Temperature (K)"].split(".")[0]) - 273.15
            celsius += float("0." + animal["Temperature (K)"].split(".")[1])
            celsius = "{0:.1f}".format(celsius)
            temperature_str = str(celsius)
        except (KeyError, ValueError):
            temperature_str = None

        print(BLUE + animal["Common name"] + COLOR_RESET + " váží v průměru: " + GREEN +
              str(float(animal["Adult weight (g)"])/1000) + "kg" + COLOR_RESET, end="")
        print((", průměrná teplota: " + RED +
              temperature_str + "°C" + COLOR_RESET) if temperature_str else "")
