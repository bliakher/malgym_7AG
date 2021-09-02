
# hledani druheho nejvetsiho prvku

# najit max, odstranit ho, max znova
"""
pole = [1, 3, 2, 0, 4, 5, 6]
# a=3
# b=2

m = max(pole)
pole.remove(m)
m2 = max(pole)
print(m2)

# hledame max a max2 zaroven

a = pole[0] # max
b = a   # druhe max
for prvek in pole:
    if prvek > a:
        b = a
        a = prvek
    else if prvek > b:
        b = prvek
        
print(a)
"""

# funkce
# priklady: print(), max(pole), remove(), index()

def jmeno_fce(parametry):
    # telo funkce
    pass

jmeno_fce(3)

def soucet(a, b):
    print(a + b)

soucet(1, 2)
soucet(3, 4)

def prumer(a, b):
    p = (a + b) / 2
    print(p)

prumer(3, 4)

# procedury - funkce, ktere nic nevraci
# funkce - muzou neco vracet
# navratova hodnota

p = [1, 2, 3]
m = max(p)

# y = x^2
# y = na_druhou(x)


def prumer2(a, b):
    p = (a + b) / 2
    return p

pr = prumer2(3, 7)
print("Prumer je: ", pr)

# funkce vydel() - vezme 2 cisla, vydeli, vypise vysledek

a = 12
b = 6
# c jejich podil

if b != 0:
    c = a / b
    print(c)
else:
    print("Nesmis delit 0")

def vydel(a, b):
    if b != 0:
        c = a / b
        print(c)
    else:
        print("Nesmis delit 0")


vydel(2, 4)
vydel(3, 0)

# funkce bere pole, vraci maximum pole
def nase_max(pole):
    # pole = [1, 2, 3, 4]
    m = pole[0]
    for i in pole:
        if i > m:
            m = i
    return m

max = nase_max([1, 2, 3, 4])
print(max)

def nase_min(pole):
    m = pole[0]
    for i in pole:
        if i < m:
            m = i
    return m


def min_max(pole):
    min = nase_min(pole)
    max = nase_max(pole)
    print(pole, "ma min", min)
    print(pole, "ma max", max)

min_max([2, 5, 7])








