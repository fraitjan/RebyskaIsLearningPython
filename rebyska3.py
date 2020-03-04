from helpers.animals_data import Animals
from helpers.colors import *

animal_name = ["dog"]

a = Animals("./data/anage_data.csv")
animals = a.get_specific_animal(animal_name)
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
