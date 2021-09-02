
# cykly
# while
# for

# for variable in iterable:
#   statements

# string - retezec
"""
name = "Evgenia"

first = name[0]

# index - poradi pismene ve slove
# indexujeme od 0

third = name[2]

print(first, third)

kousek = name[0:3] # slice
zacatek = name[:4]
konec = name[4:]

print(kousek, zacatek, konec)

first = name[0]
second = name[1]
# ...

for letter in name:
    # letter = name[0]
    print(letter)

"""
# for variable in range(X):
#   body of cycle
"""
i = 0
while i < 10:
    print(i)
    i += 1

for i in range(0, 10):
    print(i)

"""
# -------------------
"""
i = 0
while i < 10:
    print(i)
    i += 2

for i in range(0, 10, 2):
    print(i)
    

for i in range(10):
    print(i)
"""
# -------------------
"""
name = "Evgenia"
print(len(name))


for letter in name:
    print(letter)

name[0]

i = 0
while i < len(name) :
    print(name[i])
    i += 1

for i in range(0, len(name)):
    print(name[i])
"""
# -------------------

# vypsat cisla od 1 do 20, ktera jsou delitelna 3

"""
for i in range(0, 21, 3):
    print(i)

for i in range(1, 21):
    if i % 3 == 0:
        print(i)

"""
# du: nacist cislo ze vstupu,
# vypsat vsechny nasobky toho cisla mensi nebo rovne 100
# pouzit cyklus a podminku

"""

*
**
***
****
*****

"""

n = 5

# vypsat n-patrovy stromecek

patro = "*"

for i in range(n):
    print(patro)
    patro += "*"































    
