cislo = int(input("Napis cislo:"))

if cislo == 69:
    print("Napsal jsi 69")
if cislo < 10:
    print("Toto cislo je hodne male")
elif 10 <= cislo < 100:
    print("Toto cislo je stredni")
elif 100 <= cislo < 1000:
    print("Toto je celkem velke cislo")
else:
    print("Toto je obrovske cislo")
