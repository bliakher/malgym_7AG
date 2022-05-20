
jidla = ["bageta", "jablko", "cokolada"]
ceny = [35, 10, 20]

print("Nabidka:")
i = 0
while i < len(jidla):
    jidlo = jidla[i]
    cena = ceny[i]
    print(jidlo, "-", cena)
    i += 1


i = 0
mincena = ceny[0]
minjidlo = jidla[0]
while i < len(jidla):
    jidlo = jidla[i]
    cena = ceny[i]
    if cena < mincena:
        mincena = cena
        minjidlo = jidlo
    i += 1

print("Nejlevnejsi je", minjidlo, "- stoji:", mincena)


objednavka = input("Co si date?")
i = 0
while i < len(jidla):
    jidlo = jidla[i]
    if jidlo == objednavka:
        print("zaplatte:", ceny[i])
    i += 1
    
