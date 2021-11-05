"""
pole = [1, 2, 3, 4, 5]

prvni = pole[0]

posledni = pole[4]
posledni = pole[len(pole) - 1]

print(posledni)

print(pole)

pole[2] = 7

posledni = 7

print(pole)

pole.append(7)

print(pole)

i = 1
ovoce = []
while i <= 3:
    o = input("Oblibene ovoce: ")
    ovoce.append(o)
    i += 1
print(ovoce)


poradi = 0
o = ovoce[poradi]
print(o)
o = ovoce[1]
print(o)
o = ovoce[2]
print(o)


poradi = 0
while poradi < len(ovoce):
    o = ovoce[poradi]
    print(o)
    poradi += 1

je_kiwi = False
poradi = 0
while poradi < len(ovoce):
    o = ovoce[poradi]
    if o == "kiwi":
        je_kiwi = True
    poradi += 1

if je_kiwi == True:
    print("Hura kiwi")
else:
    print("Fuj")
"""

cisla = [5, 7, 18, 9, 27, 45]

# vypsat cisla vetsi nez 10
i = 0
while i < len(cisla):
    cislo = cisla[i]
    if cislo > 10:
        print(cislo)
    i += 1

# ke kazdemu cislu v poli pricist 1

i = 0
while i < len(cisla):
    cisla[i] *= 2
    i += 1

print(cisla)














