
znamky = [1, 2, 1, 1, 4, 3]

print(znamky)
"""
print(znamky[0])
print(znamky[1])
print(znamky[2])
"""

i = 0
print(znamky[i])

"""
1
2
1
1
...
"""

i = 0
while i < len(znamky):
    znamka = znamky[i]
    print(znamka)
    i += 1


pocet = len(znamky)
soucet = 0
i = 0
while i < len(znamky):
    znamka = znamky[i]
    soucet += znamka
    i += 1


print("soucet", soucet)
print("prumer", soucet / pocet)


znamky = [1, 2, 1, 1, 4, 3]
vahy = [7, 2, 3, 3, 6, 10 ]

soucet_vah = 0
i = 0
while i < len(vahy):
    vaha = vahy[i]
    soucet_vah += vaha
    i += 1

citatel = 0
i = 0
while i < len(vahy):
    znamka = znamky[i]
    vaha = vahy[i]
    citatel += znamka * vaha
    i += 1

print("vazeny prumer", citatel / soucet_vah)

citatel = 0
soucet_vah = 0
i = 0
while i < len(vahy):
    znamka = znamky[i]
    vaha = vahy[i]
    citatel += znamka * vaha
    soucet_vah += vaha
    i += 1

print("vazeny prumer", citatel / soucet_vah)
    

soucet = sum(znamky)
print("prumer", soucet / len(znamky))


studenti = ["Eliska", "Honza", "Martin"]
znamky = [1, 2, 1]

"""
Eliska ma 1
Honza ma 2
...
"""













    
