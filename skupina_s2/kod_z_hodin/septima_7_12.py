pismena = ["a", "b", "c"]

b = pismena[1]

pismena[1] = "d"

len(pismena)

pismena.append("f")

for x in pismena:
    print(x)


cisla = [1,2,4,18]

for x in cisla:
    x += 1

print(cisla)


index = 0

while index < 4:
    cisla[index] += 1
    index += 1

print(cisla)

for index in range(4): # 0, 1, 2, 3
    cisla[index] += 1

#nacteni cisel do pole

cisla = []
a = int(input())
while a != -1:
    cisla.append(a)
    a = int(input())

print(cisla)


    
