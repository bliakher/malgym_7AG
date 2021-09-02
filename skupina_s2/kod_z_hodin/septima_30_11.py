
# while podminka:
#    telo cyklu

# for promenna in neco:
#   telo cyklu

"""
for i in range(6) # -> 0, 1, .., 6-1
    print(i)


i = 0
while i < 6:
    print(i)
    i += 1


for i in range(1, 6) #-> 1, 2, .., 5
    print(i)
"""    
# test
"""
max = int(input())
i = 0
while i <= max:
    if i % 2 == 0:
        print(i)
    i += 1

max = int(input())
for i in range(max + 1):
    if i % 2 == 0:
        print(i)

max = int(input())
i = 0
while i <= max:
    print(i)
    i += 2

# range(x)
# range(min, max)
# range(min, max, krok)

max = int(input())
for i in range(0, max + 1, 2):
    print(i)
"""
"""
for i in range(6, 0, -1):
    print(i)
"""

# pole - array

cislo1 = 1
cislo2 = 3
cislo3 = 7
cislo4 = 158

cisla = [1, 3, 7, 158]
#        0  1  2   3
#offset

prvni = cisla[0]
druhy = cisla[1]
"""
print(cisla[0])
print(cisla)
cisla[0] = 2
print(cisla)

auta = ["Skoda", "BMW", "Fiat"]
# bool - True, False

boolean = [True, False, True]

# pole(array) x seznam(list)
seznam = [1, "ahoj", False]


prazdne = []

pocet_prvku = len(cisla) #length
print(pocet_prvku)

cisla.append(10)
print(cisla)

delka_auta = len(auta)
print("Auta:", delka_auta)

prvni = auta[0]
posledni = auta[2]
posledni = auta[len(auta) - 1]
"""

slovo = "ahoj"
for pismeno in slovo:
    print(pismeno)

auta = ["Skoda", "BMW", "Fiat"]
for auto in auta:
    print(auto)


names = ["Anna", "Jan", "Max"]

# Hello, Anna!

for name in names:
    print("Hello, " + name + "!")

























































  






