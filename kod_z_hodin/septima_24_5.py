
# bakalari - zak pritomny na hodine

pritomni = ["Jan Novotny", "Michal Pekny", "Pert Jerhot"] # zaci pritomni na hodine
jmeno = input("Zadejte jmeno zaka:") # nactu jmeno od uzivatele

for clovek in pritomni:
    if clovek == jmeno:
        print("Pritomny")
    else:
        print("Nepritomny")
    
# tohle nefunguje -> vypisuje neco pro kazdou polozku v poli

# poznamename si, jestli jsme v poli nasli jmeno
# vypiseme jednou az na konci

nasli = False
for clovek in pritomni:
    if clovek == jmeno:
        nasli = True
    
if nasli:
    print("Pritomny")
else:
    print("Nepritomny")
    
# hledani maxima v poli

cisla = [3, 1, 2, 57, 42]

# v pythonu funkce max

maximum = max(cisla)

# pokud mame setridene pole -> posleni prvek

setridene = [1, 2, 3, 42, 57]
maximum = setridene[-1]

# obecne

# prochazim prvky v poli
# kazdy dalsi porovnam s maximem predchozich

maximum = 0
for cislo in cisla:
  if cislo > maximum:
    maximum = cislo
    
print(maximum)



