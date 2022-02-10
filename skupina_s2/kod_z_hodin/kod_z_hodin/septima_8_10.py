# nacist 2 cisla, vypsat mensi z nich
"""
a = int(input("Cislo: "))
b = int(input("Cislo: "))

if a < b:
    print(a)
elif b < a:
    print(b)
else:
    print("jsou stejne")

# nacist cislo, vypsat jesti je sude nebo liche

a = int(input("Cislo: "))

if a % 2 == 0:
    print("sude")
else:
    print("liche")

#cyklus:
    
# while podminka:
#    neco delam
# konec

pumpnuti = 0

while pumpnuti < 10:
    # pumpnu
    #pumpnuti = pumpnuti + 1
    print(pumpnuti)
    pumpnuti += 1

print("Konec")


x = 1

while x <= 10:
    print(x)
    x += 1

# vypsat cisla od 10 do 1

x = 10

while x >= 1:
    print(x)
    x -= 1

# vypsat cisla od 1 do 20, delitelna 3

x = 1

while x <= 20:
    if x % 3 == 0:
        print(x)
    x += 1

limit = int(input("Napis limit pro FizzBuzz: "))

a = 1
while a <= limit:
    if a % 3 == 0 and a % 5 == 0:
        print("FizzBuzz")
    elif a % 5 == 0:
        print("Buzz")
    elif a % 3 == 0:
        print("Fizz")
    else:
        print(a)
    a += 1
"""

cislo = int(input("Zadej čílo: "))
nasob = cislo
while nasob <= cislo * 10:
    print(nasob)
    nasob = nasob + cislo

cislo = int(input("Zadej čílo: "))
nasobitel = 1
while nasobitel <= 10:
    print(f"{cislo} * {nasobitel} = {cislo * nasobitel}")
    print(cislo, "*", nasobitel, "=", cislo * nasobitel)
    nasobitel += 1






    














