"""
a = int(input())

if a >= 0:
    print(a)
else:
    print(-a)


x = 1
while x <= 10:
    print(x)
    x += 1

# secist 5 cisel ze vstupu a vypsat vysledek
limit = int(input("Kolik cisle chces secist:"))

soucet = 0
kolikate = 1
while kolikate <= limit:
    a = int(input(str(kolikate) + ". cislo: "))
    soucet += a
    kolikate += 1

print(soucet)
"""
"""
# nekonecny cyklus
soucet = 0
while True:
    a = input("cislo: ")
    if a == "stop":
        break
    else:
        a = int(a)
        soucet += a

print(soucet)



while True:
    a = int(input("Cislo na abs. hodnotu"))

    if a >= 0:
        print(a)
    else:
        print(-a)
    znova = input("Chcete spustit znova?")
    if znova == "ne":
        break

"""
"""
print(8, 2, 3)
# sep - separator
# default - mezera
print(15, 10, 2021, sep="/")
# end='\n'
print("Ahoj", end='')
print("5")
"""
"""
  *
 ***
*****
"""

def hvezdicka(x):
    i = 0
    while i < x:
        print("*", end='')
        i += 1
    print()

x = 3

"""
*
**
***
****
"""

patra_celkem = 4

patro = 1

while patro <= patra_celkem:
    hvezdicka(patro)
    patro +=1

while patro <= patra_celkem:
    x = patro
    i = 0
    while i < x:
        print("*", end='')
        i += 1
    print()
    patro +=1

while patro <= patra_celkem:
    print("*" * patro)
    patro +=1

"""
  *
 ***
*****
"""































