# uloha - nacist 2 cisla a vypsat jejich soucet
"""
a = int(input("Napis cislo "))
b = int(input("Napis druhe cislo "))
soucet = a + b
print("Soucet je", soucet)
"""
# uloha - to stejne, ale podil
"""
a = int(input("Napis cislo "))
b = int(input("Napis druhe cislo "))

if b == 0:
    print("Nelze delit")
else:
    podil = a // b
    print("Podil je", podil)    
"""

"""
if podminka:
    podminka plati
else:
    podminka neplati

==, != , < , > , <= , >=
x = 10 - prirazeni vs x == 10 - porovnani
"""

# uloha - nacist cislo - vypisu jestli je kladne nebo zaporne
"""
cislo = int(input("Napis cislo "))

if cislo > 0:
    print("Kladne")
else:
    if cislo == 0:
        print("Nula")
    else:
        print("Zaporne")

if cislo > 0:
    print("Kladne")
elif cislo == 0:
    print("Nula")
else:
    print("Zaporne")


# uloha - kalkulacka

a = int(input("Napis cislo "))
op = input("Operace ")
b = int(input("Napis druhe cislo "))

if op == "+":
    vysledek = a + b
elif op == "-":
    vysledek = a - b
elif op == "*":
    vysledek = a * b
elif op == "/":
    if b != 0:
        vysledek = a / b
    else:
        vysledek = "Neplatny"

print(f"Vysledek operace {a} {op} {b} je {vysledek}.")
"""
# du - nacist cislo a spocitat jeho absolutni hodnotu

# hra FizzBuzz
# delitelne 3 - Fizz
# delitelne 5 - Buzz
# delitelne obema - FizzBuzz

# zadame cislo - vypise, co mame rict
# modulo % - zbytek po deleni


a = int(input("Napis cislo "))
if a % 3 == 0 and a % 5 == 0:
    print("FizzBuzz")
elif a % 5 == 0:
    print("Buzz")
elif a % 3 == 0:
    print("Fizz")
else:
    print(a)


# slozene podminky - and , or


