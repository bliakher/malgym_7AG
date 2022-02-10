
"""
def funkce(param1, param2): #hlavicka
    # telo funkce
    
    print(param1, param2)



#funkce(1, 2)
#funkce("ahoj", "cau")

# soucet

def soucet(a, b):
    soucet = a + b
    print(soucet)

def podil(a, b):
    if b != 0:
        print(a/b)
    else:
        print("b nesmi byt 0")

def soucet_vracejici(a, b):
    soucet = a + b
    return soucet

def podil_vracejici(a, b):
    podil = 0
    if b != 0:
        podil = a/b
    else:
        podil = None

    return podil

soucet(1, 2)
soucet(3, 4)
podil(3, 0)

# 1 + 2 + 3
s = soucet_vracejici(1, 2)
vys = soucet_vracejici(s, 3)
print(s)


vys = podil(3, 0)
if vys == None:
    print("deleni 0")
else:
    print(vys)

vys = podil(1, 2)
print(vys)




pole = [1, 2, 3, 4, 5, 3]
vys = pole.count(13)
print(vys)


pole = [1, 2, 3, 4, 5, 3]
prvek = 3
pocitadlo = 0
i = 0
while i < len(pole):
    if pole[i] == prvek:
        pocitadlo += 1
    i += 1

print(pocitadlo)



def count(pole, prvek):
    pocitadlo = 0
    i = 0
    while i < len(pole):
        if pole[i] == prvek:
            pocitadlo += 1
        i += 1

    return pocitadlo



print(count([1, 2, 3, 3], 3))
print(count([1, 2, 3, 3], 13))

"""


pole1 = [1, 2, 3, 4, 5, 3]
pole2 = pole1

print(pole1)
print(pole2)

pole1[0] = 17

print(pole1)
print(pole2)

def copy(pole):
    kopie = []
    i = 0
    while i < len(pole):
        prvek = pole[i]
        kopie.append(prvek)
        i += 1

    return kopie


pole1 = [1, 2, 3, 4, 5, 3]
pole2 = copy(pole1)

print(pole1)
print(pole2)

pole1[0] = 17

print(pole1)
print(pole2)

#reverse

def reverse(pole):
    rev = []
    i = len(pole) - 1
    while i >= 0:
        prvek = pole[i]
        rev.append(prvek)
        i -= 1
    return rev

def reverse2(pole):
    rev = []
    i = -1
    while i >= -len(pole):
        prvek = pole[i]
        rev.append(prvek)
        i -= 1
    return rev


print(reverse2(pole1))








