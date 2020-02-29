# import: do tvého programu se nahrají funkce/třídy z jiných knihoven, zde například z knihovny "random"
# Zatím to nemusíš moc řešit
import random

# list: skupina proměnných, můžou to být libovolné proměnné
# tj. např. stringy (=slova/znaky v uvozovkách jako to je zde), čísla, jiné listy...
animal_list = ["vydra", "tucnak", "ptakopysk", "panda", "koala", "peso"]

# input(): funkce pro získání vstupu od uživatele z příkazové řádky
name = input("Napis sve jmeno: ")

if name.lower() == "rebyska".capitalize():
    animal = random.choice(["vydra", "panda"])
# elif: Pokračování podmínky, elif = "else if", tzn. řádek pod elif se provede jen pokud neplatila původní podmínka
# ale zároveň platí uvedená nová podmínka, tzn. n je "Honzík"
# elif může být uveden 0-nekonečně krát
elif name.lower() == "honzík":
    animal = "tucnak"
# else: Konec podmínky, pokud se nesplnila ani jedna z výše uvedených podmínek, provede se řádek pod else:
else:
    # Využití funkce "random.choice()" pro získání náhodného zvířátka
    animal = random.choice(animal_list)
# Pro upřesnění: Do proměnné "animal" se vloží "vydra", pokud je jméno (proměnná n) "Rebyska", pokud je jméno
# "Honzík", tak se tam uloží "tucnak", pokud jméno není ani "Rebyska" ani "Honzík", tak se vybere náhodné zvíře z
# listu "animal_list"

# print(): funkce pro výpis stringu (skupiny znaků) do příkazové řádky
print(name + ", tve nejoblibenejsi zvire je: " + animal)
