"""
cisla = [1, 4, 3, 7, 11]

i = 0
while i < len(cisla):
    cislo = cisla[i]
    if cislo % 2 == 1:
        print(cislo)
    i += 1
"""

jidlo = ["bageta", "jablko", "parek v rohliku", "kava"]
ceny = [35, 10, 25, 30]

# najit nejdrazsi jidlo
# hledani maxima v poli

i = 0
maximum = ceny[0]
max_idx = 0
while i < len(ceny):
    cena = ceny[i]
    if cena > maximum:
        maximum = cena
        max_idx = i
    i += 1

print(jidlo[max_idx], maximum)
    
i = 0
maximum = ceny[0]
max_jidlo = jidlo[0]
while i < len(ceny):
    cena = ceny[i]
    j = jidlo[i]
    if cena > maximum:
        maximum = cena
        max_jidlo = j
    i += 1

print(max_jidlo, maximum)

# nejdelsi nazev jidla v nabidce

i = 0
maximum = jidlo[0]
while i < len(jidlo):
    j = jidlo[i]
    if len(j) > len(maximum):
        maximum = j
    i += 1

print("nejdelsi je:", maximum)


# bakalari

znamky = [1, 1.5, 2, 2, 3, 5]
vahy = [10, 10, 7, 3, 4, 3]

# prumer
i = 0
soucet = 0
while i < len(znamky):
    soucet += znamky[i]
    i+= 1

soucet = sum(znamky)

prumer = soucet / len(znamky)
print("prumer je: {:.2f}".format(prumer))

# vazeny prumer

i = 0
soucet = 0
while i < len(znamky):
    soucet += znamky[i] * vahy[i]
    i+= 1

prumer = soucet / sum(vahy)
print("vazeny prumer je: {:.2f}".format(prumer))


















    






