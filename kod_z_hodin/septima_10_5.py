
"""
# strings - retezce

a = "hello"

for letter in a:
    print(letter)

first = a[0] # index

for i in range(5):
    print(a[i])

# slice

end = a[2:]
print(end)
"""
"""
# pole - array, list

cislo1 = 1
cislo2 = 3
cislo3 = 7
cislo4 = 17

print(cislo1)
print(cislo2)
print(cislo3)
print(cislo4)

# ulozit vic dat pohromade

pole = [1, 3, 7, 17]

auta = ["Skoda", "BMW", "Fiat"]
    #       0       1       2

x = [5, "ahoj", True, 1.4]

a = "hello" # ['h', 'e', 'l', 'l', 'o']

skoda = auta[0]
print(skoda)

print(auta)
auta[1] = "Citroen"
print(auta)

auta.append("Mazda")
print(auta)

pocet_prvku = len(auta)
print(pocet_prvku)
"""

pole = [1, 3, 7, 17]

print(pole[0])
print(pole[1])
print(pole[2])
print(pole[3])


# for var in iterable

for prvek in pole:
    print(prvek)

# ke vsem prvkum pole pricist 1
"""
print(pole)

# tohle nefunguje
for prvek in pole:
    # prvek = pole[0]
    prvek += 1
print(pole)
"""
# tenhle for umoznuje pouze cist - nemuzu menit pole

pole[1] = 5
print(pole)

pole[0] += 1
pole[1] += 1
pole[2] += 1
pole[3] += 1

print(pole)

for index in range(len(pole)):
    pole[index] += 1

print(pole)

# secist vsechny prvky pole

pole = [1, 3, 7, 17]

soucet = 0

for i in range(0, 4):
    soucet += pole[i]
print(soucet)

soucet += pole[0]
soucet += pole[1]
#..

soucet2 = 0
for prvek in pole:
    soucet2 += prvek
print(soucet2)

# du

name = ["Anna", "Emma", "Max"]
surname =  ["Karenina", "Stone", "Brod"]

# reseni
# napoveda - cyklus




















