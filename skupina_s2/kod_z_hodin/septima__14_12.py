
cisla = [1, 2, 3, 5, 4, 12, 5]


# prvek na indexu 3 - cisla[3]
# vypsat suda cisla z pole
#1
#2
#3
"""
print(cisla)

for cislo in cisla:
    if cislo % 2 == 0:
        print(cislo)

for index in range(6):
    prvek = cisla[index]
    if prvek % 2 == 0:
        print(prvek)


a = 4
if a % 2 == 0:
    print(a)
"""

cisla = [1, 2, 3, 5, 4, 12, 5]

#print(cisla.count(5))


#hledany_prvek = int(input("Napis cislo"))
#print(cisla.count(hledany_prvek))

# spocitat, kolikrat tam je
# vypsat

# nacte cislo, projde pole, pokazde, kdyz narazi na prvek,
# vypise "Nasel jsem"

"""
prvek = int(input("Napis cislo"))

for cislo in cisla:
    if cislo == prvek:
        print("Nasel jsem")
"""
# plna verze
cisla = [1, 2, 3, 5, 4, 12, 5]
"""
prvek = int(input("Napis cislo"))

pocet = 0
for cislo in cisla:
    if cislo == prvek:
        pocet += 1

print(pocet)
"""

# vypsat vsechny pozice, na kterych je nejaky prvek

cisla = [1, 2, 3, 5, 4, 12, 5]
# 5 -> 3, 6
# 5 je na pozici 3
# 5 je na pozici 6

"""
hledany = int(input("Napis cislo"))

for index in range(len(cisla)):
    cislo = cisla[index]
    if cislo == hledany:
        print(cislo, " je na pozici ", index )


print(cisla.index(5))
"""

# hledani maxima v poli

cisla = [1, 2, 3, 5, 4, 12, 5]

max = 0 
for cislo in cisla:
    if cislo > max:
        max = cislo

print(max)
        





    
    









