
A = [1,2,3,4]
B = [2, 4,6, 8]


C = []

i = 0
while i < len(A):
    a = A[i]
    b = B[i]
    c = a + b
    C.append(c)
    i += 1

print(C)

def secti_pole(A, B):
    C = []
    i = 0
    while i < len(A):
        a = A[i]
        b = B[i]
        c = a + b
        C.append(c)
        i += 1
    return C

print(secti_pole(A, B))
pole1 = [1, 1]
pole2 = [2, 2]
print(secti_pole(pole1, pole2))

def soucet(cislo1, cislo2):
    vysledek = cislo1 + cislo2
    print(cislo1, "+", cislo2, "=", vysledek)


def soucet2(cislo1, cislo2):
    vysledek = cislo1 + cislo2
    return vysledek

soucet(1,2)
s = soucet2(1, 2)
v = soucet2(s, 3)
print(v)
print(soucet2(2,3))


def max2(pole):
    m = pole[0]
    i = 0
    while i < len(pole):
        if pole[i] > m:
            m = pole[i]
        i += 1
    return m

A = [1,2,3,4]
m = max2(A)
print(m)


def pocet(pole, hodnota):
    pass

A = [1, 2, 3, 4, 1, 2, 1]
print(pocet(A, 1)) # 3
print(pocet(A, 2)) # 2
print(pocet(A, 17)) # 0




