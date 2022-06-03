
znamky = [1, 2, 1, 1, 4, 3]

pocet = len(znamky)
soucet = 0
i = 0
while i < len(znamky):
    znamka = znamky[i]
    soucet += znamka
    i += 1

print("prumer", soucet / pocet)

znamky2 = [1, 2, 4, 3]

pocet = len(znamky2)
soucet = 0
i = 0
while i < len(znamky2):
    znamka = znamky2[i]
    soucet += znamka
    i += 1


print("prumer", soucet / pocet)


def pozdrav():
    print("hello")

def pozdrav_jmeno(jmeno):
    print("Hello,", jmeno)

pozdrav()
pozdrav_jmeno("Evgenia")
pozdrav_jmeno("Eliska")

def prumer_znamek(znamky):
    pocet = len(znamky)
    soucet = 0
    i = 0
    while i < len(znamky):
        znamka = znamky[i]
        soucet += znamka
        i += 1

    print("prumer", soucet / pocet)

znamky = [1, 2, 1, 1, 4, 3]
znamky2 = [1, 2, 4, 3]
prumer_znamek(znamky)
prumer_znamek(znamky2)

def soucet(cislo1, cislo2):
    vysledek = cislo1 + cislo2
    print(cislo1, "+", cislo2, "=", vysledek)

soucet(1, 2)
soucet(2, 3)

rozdil(7, 5)








    
