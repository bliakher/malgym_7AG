from turtle import *
"""
# ctverec
i = 0
while i < 4:
    forward(100)
    right(90)
    i += 1


a = int(input("cislo: "))
b = int(input("cislo: "))

print(a+b)

i = 0
while i < 5:
    print(i)
    i += 1


x = int(input("kolik cisle chcete secist? "))
soucet = 0
kolikaty_cyklus = 0
while kolikaty_cyklus < x :
    a = int(input("cislo: "))
    soucet = soucet + a # soucet += a
    kolikaty_cyklus += 1

print(soucet)
"""


while True:
    puvodni = int(input("puvodni:"))
    sleva =int(input("sleva:"))
    nova = puvodni - puvodni / 100 * sleva
    print(nova)
    # zeptam se uzivatele,
    # jestli chce pokracovat dal
    odpoved = input("Chcete pokracovat? ano/ne")

    # pokud rekne ne -> skoncim
    if odpoved == "ne":
        break
    











