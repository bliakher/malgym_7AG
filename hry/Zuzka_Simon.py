import random as r
import time as t
pole = [1, 2, 3, 4, 5, 6]
bank = 5000
print("Zahrajeme si kostky!")

pokracovani = True
while pokracovani == True:
    if bank > 0:
        print("Hra začíná, máte ", bank, "Kč!", sep='')
        cislo = int(input("Na jaké číslo sázíte? "))
        obnos = int(input("Kolik vsadíte? "))
        print("Jaké číslo padne?")
        t.sleep(2)
        i = r.choice(pole)
        print("Padlo číslo", i)
        if cislo == i:
            bank += obnos
            print("Výhra! Částka v banku narostla na", bank, "Kč.")
        else:
            bank -= obnos
            print("Částka v banku se snížila na ", bank, "Kč.", " Zkuste to ještě jednou!", sep='')
    else:
        print("Hra skončila, nemáte peníze.")
        break
    if input("Chcete hrát dál? ") != "ano":
        pokracovani = False
    
if bank > 0:
    if input("Přejete si vybrat peníze? ") == "ano":
        print("Vybrali jste ", bank, "Kč.", sep='')
