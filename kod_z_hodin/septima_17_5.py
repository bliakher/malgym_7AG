
znamky = [1, 1, 3, 2, 4, 5, 1.5, 3.5]

# z jednoho testu - stejna vaha
# prumer


soucet = 0
for znamka in znamky:
    soucet += znamka

prumer = soucet / len(znamky)
print(prumer)


# bakalare - dochazka

pritomni = ["Dan Petrasek", "Simon Barton"]

# precteme jmeno od uzivatele
# odpovime jestli byl nebo nebyl na hodine

pritomni = ["Franta", "Pepa", "Hana", "Jirka", "Jana"]

otazka = input("Ověř si, zda byl žák přítomen: ")

nasli = False
for i in pritomni:
  if i == otazka:
    nasli = True

if nasli == True:
    print("Přítomen")
else:
    print("Nepřítomen")

# v pythonu syntaxe in

if otazka in pritomni:
  print("Přítomen")

else:
  print("Nepřítomen")


# mame pole
# chceme vytvorit nove pole,
# ve kterem budou hodnoty v opacnem poradi

# v pythonu funkce reversed
rev = reversed(jmena)
print(rev)

# bez ni

a=[5, 8 , 90 , 79, 4, 37]
b = []
idx = len(a - 1) # posledni prvek

while a >= 0:
    b.append(a[idx])
    idx -= 1
print(a)
    

# nevytvarime nove pole
# prohodime prvky na miste v puvodnim poli

a=[5, 8 , 90 , 79, 4, 37]
for i in range(0,len(a) // 2):
  c = a[i]
  a[i]= a[len(a) - 1 - i]
  a[len(a) - 1 - i] = c
print(a)  


