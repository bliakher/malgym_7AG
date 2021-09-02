import time


"""
a = 3

if a < 0 or a > 0:
    print(0)

if a != 0:
    print(0)

if a < 0 and a > 0:
    print(0)

if False:
    print("Lez")

if True:
    print("Pravda")

# boolean - bool - True / False

cislo = cislo + 1
cislo += 1

"""

zacatek = 254
klientu_za_den = 100
limit = zacatek + klientu_za_den

cislo = zacatek
"""
while cislo <= limit:

    print("Dalsi v poradi je cislo:", cislo)
    jmeno = input("Zadej jmeno a prijmeni: ")
    print("Zpracovavam klienta: " + jmeno)
    time.sleep(2)
    print("--> Prepazka c. 3")
    cislo += 1

print("Pristi klient zitra")
"""
# lepsi system - volba akce -> prepazka

while cislo <= limit:

    print("Dalsi v poradi je cislo:", cislo)
    jmeno = input("Zadej jmeno a prijmeni: ")
    akce = input("Co chcete provest [obcanka/matrika]")
    print("Zpracovavam klienta: " + jmeno)
    time.sleep(2)
    if akce == "obcanka":
        print("--> Prepazka c. 3")
    elif akce == "matrika":
        print("--> Prepazka c. 1")
    else:
        print("Akci nelze provest")
    cislo += 1

print("Pristi klient zitra")













