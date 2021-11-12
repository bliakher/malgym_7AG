"""
x = 1
while x <= 10:
    mocnina = x ** 2
    print(mocnina)
    x += 1
"""

jidlo = ["bageta", "jablko", "parek v rohliku", "kava"]
ceny = [35, 10, 25, 30]

print("Dnesni nabidka:")

idx = 0
while idx < len(jidlo):
    j = jidlo[idx]
    c = ceny[idx]
    print("- " + j + " - " + str(c) + "kc")
    idx += 1

"""
objednavka = input("Co si date? ")
idx = 0
while idx < len(jidlo):
    j = jidlo[idx]
    c = ceny[idx]
    if j == objednavka:
        print("Cena: " + str(c) + "kc")
        break
    idx += 1

"""

objednavka = input("Co si date? ")
celkova = 0

while objednavka != "nic":
    idx = 0
    idx_objednavky = -1
    while idx < len(jidlo):
        j = jidlo[idx]
        if j == objednavka:
            idx_objednavky = idx
            break
        idx += 1

    # idx_objednavky = jidlo.index(objednavka)

    if idx_objednavky == -1:
        print(objednavka + " - nemame v nabidce.")
    else:
        kolik = int(input("Kolik? "))
        celkova += ceny[idx_objednavky] * kolik

    objednavka = input("Co si date? ")

print("Cena: " + str(celkova) + "kc")

        
        

