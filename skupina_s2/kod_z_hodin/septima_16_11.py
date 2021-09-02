
# cykly

# while cyklus
#while _podminku_:
#   prikaz
#   prikaz

#vypsat cisla od 1 do max

"""
max = int(input("max"))  #5
i = 1

while i <= max:
    print(i)
    i += 1

#cisla od x do min

x = int(input("x"))
min = 1

while x >= min:
    print(x) # -> x, x-1, x-2, ..., min
    x -= 1
"""

#vypsat licha cisla od 1 do max -> 1, (2), 3, (4), 5, 6 ..max(pokud je liche)

"""
max = int(input("max"))  #7
i = 1 #2

while i <= max:
    if i % 2 == 1:
        print(i)
        i += 1
    elif i % 2 == 0:
        i += 1


while i <= max:
    if i % 2 == 1:
        print(i)
    i += 1

while i <= max:
    print(i)
    i += 2
"""

# DRY - don't repeat yourself
    

# for cyklus

#for _promenna_ in _pres_co_iterujeme:
#   prikaz


word = "ahoj!"

for letter in word:
    print(letter)

"""
pismeno = ""   
while neni konec slova:
    pismeno = dalsi pismeno
    print(pismeno)

"""
kolikrat = 6

# range(5) -> 0, 1, 2, 3, 4 (0, n-1)

for i in range(kolikrat):
    print(i)
    print("ahoj")

print("konec prvniho cyku\n")

i = 0
while i < kolikrat:
    print(i)
    print("ahoj")
    i += 1








