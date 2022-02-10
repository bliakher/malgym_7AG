znamky = [1, 1.5, 2, 2, 3, 5]
vahy = [10, 10, 7, 3, 4, 3]
"""
# prumer
i = 0
soucet = 0
soucet = sum(znamky)
prumer = soucet / len(znamky)

print("prumer je: {:.2f}".format(prumer))

stud1 = [1, 1.5, 2, 2, 3, 5]
stud2 = [3, 1, 1.5, 2, 2, 3]

i = 0
soucet = 0
soucet = sum(stud1)
prumer = soucet / len(stud1)

print("prumer 1.studenta: {:.2f}".format(prumer))

i = 0
soucet = 0
soucet = sum(stud2)
prumer = soucet / len(stud2)

print("prumer 2.studenta: {:.2f}".format(prumer))
"""

def prumer(znamky):
    #znamky  = [1, 1.5, 2, 2, 3, 5]
    
    i = 0
    soucet = sum(znamky)
    prumer = soucet / len(znamky)
    
    #print("prumer 2.studenta: {:.2f}".format(prumer))
    return prumer

"""
stud1 = [1, 1.5, 2, 2, 3, 5]
stud2 = [3, 1, 1.5, 2, 2, 3]

p1 = prumer(stud1)
print("prumer je: {:.2f}".format(p1))
p2 = prumer(stud2)
print(p2)


predmet = "matematika"
znamky  = [1, 1.5, 2, 2, 3, 5]
znamky2  = [1, 1.5, 2, 2, 3, 5]
"""

def vypis(predmet, znamky):
    # predmet = "matika"
    # znamky = [1, 1.5, 2, 2, 3, 5]
    print(predmet)
    idx = 0
    while idx < len(znamky):
        print(znamky[idx])
        idx += 1


def nacti_znamky():
    znamky = []
    predmet = input("predmet: ")
    pocet = int(input("Kolik znamek? "))
    i = 0
    while i < pocet:
        znamka = int(input("znamka: "))
        znamky.append(znamka)
        i += 1
    return predmet, znamky

predmet, znamky = nacti_znamky()
vypis(predmet, znamky)
p = prumer(znamky)
print("prumer", p)














