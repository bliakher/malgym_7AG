"""
while True:
    print()
    if 1 > 2:
        break

# spocitej soucet cisel od 1 do 50

soucet = 0
i = 1
while i <= 50:
    soucet += i
    i += 1
print(soucet)

# spocitej soucet cisel od 1 do max

max = int(input("Napis maximum"))
soucet = 0
i = 1
while i <= max:
    soucet += i
    i += 1
print(soucet)
"""

cislo1 = 1
cislo2 = 5
cislo3 = 7
cislo4 = 18

cisla = [1, 5, 7, 18, 5] # pole / seznam

auta = ["Skoda", "BMW", "Fiat"]

ruzne = [1, "slovo"]

print(auta)
"""
prvni = cisla[0] # prvni cislo je na indexu 0
druhe = cisla[1]
print(prvni, druhe)

# vypsat posledni hodnotu z pole cisla

delka = len(cisla) # length
posledni = cisla[delka - 1]
posledni = cisla[len(cisla) - 1]
print(posledni)

posledni = cisla[-1]
print(posledni)

print(cisla)
cisla.append(3) # pridam na konec
print(cisla)
"""

# zjistit od uzivatele 3 nejoblibenejsi veci
"""
i = 1
ovoce = []
while i <= 3:
    o = input("Oblibene ovoce: ")
    ovoce.append(o)
    i += 1

print(ovoce)
"""

# zjistit jmena lidi ve tride

i = 1
vsichni = []
kluci = []
holky = []
pocet = int(input("Kolik lidi je ve tride: "))
while i <= pocet:
    jmeno = input("Jmeno: ")
    pohlavi = input("Pohlavi(m/f)")
    if pohlavi == "m":
        kluci.append(jmeno)
    else:
        holky.append(jmeno)
    vsichni.append(jmeno)
    i += 1

print(vsichni)
print(holky)
print(kluci)
























