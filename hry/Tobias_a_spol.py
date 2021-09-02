import random
from math import sqrt
print("Vítám tě v programu na procvičení matematiky")
print("Můžeš si zde zábavně procvičit sčítání či vypočítat délku strany pomocí pythagorovy věty")
jmeno = input("Jak se jmenuješ? ")
nadavky = ["Víte, kdo je debžus, protože neumí číst? ", "Přečti si to po sobě!!!! Největší tupec, kterého znám: ", "Přečti si to po sobě!!!! Největší degenerát na světě je "]
maximum = int(input("Jen tak mimochodem, do kolika umíš počítat? "))


def jablka():
    jmeno = ["Petr", "Karel", "Franta", "Honza", "Pepa", "Jirka", "Stáňa", "Filip", "Michal", "Marcela", "Jitka", "Lucie", "Katka"]
    cislo1 = random.randint(0,maximum)
    cislo2 = random.randint(0,maximum-cislo1)
    odpoved = int(input(random.choice(jmeno) + " má " + str(cislo1) + " jablek, " + random.choice(jmeno) + " má " + str(cislo2) + " hrušek. Kolik mají dohromady ovoce? "))
    vysledek = cislo1 + cislo2

    if vysledek == odpoved:
        print("Správně!")
    else:
        print("Špatně! Správná odpověď je totiž " + str(vysledek))

    pokracovani = input("Chcete pokračovat? a/n ")
    if pokracovani == "a":
        vyber()
    else:
        print("Díky za účast")

def pythagorovavěta():
    chcivypocitat = input("Zadejte stranu, kterou potřebujete vypočítat - a/b/c: ")

    if chcivypocitat == "c":
        a = int(input("Napište délku strany a: "))
        b = int(input("Napište délku strany b: "))
        c = sqrt(a * a + b * b)
        print("Výsledek: Délka strany c je: " + str(c))

        pokracovani = input("Chcete pokračovat? a/n ")
        if pokracovani == "a":
             vyber()
        else:
            print("Díky za účast")
            
    elif chcivypocitat == "a":
        b = int(input("Napište délku strany b: "))
        c = int(input("Napište délku strany c: "))
    
        a = sqrt(c * c - b * b)
        print("Výsledek: Délka strany a je: " + str(a))

        pokracovani = input("Chcete pokračovat? a/n ")
        if pokracovani == "a":
            vyber()
        else:
            print("Díky za účast")

    elif chcivypocitat == "b":
        a = int(input("Napište délku strany a: "))
        c = int(input("Napište délku strany c: "))
        b = sqrt(c * c - a * a)
        print("Výsledek: Délka strany b je: " + str(b))

        pokracovani = input("Chcete pokračovat? a/n ")
        if pokracovani == "a":
            vyber()
        else:
            print("Díky za účast")

    else:
        print("Prosím, zkus to znovu")
        pythagorovavěta()

def hadanicisla():
            cislo = random.randint(0,maximum)
            print("Myslím si číslo v rozmezí od 0 do " + str(maximum))
            tip = int(input("Hádej, jaké to je: "))

            while True:
                        if tip == cislo:
                                  print("Gratuluji, jsi dobrý. Číslo je skutečně " + str(cislo))
                                  break
                        elif tip > cislo:
                                    if tip > maximum:
                                                print("Tak jsi senilní? Dej si deset dřepů a nauč se číst.")
                                                tip = int(input("Hádej, jaké to je: "))
                                    else:
                                                print("Litujeme, číslo je menší")
                                                tip = int(input("Hádej, jaké to je: "))
                        else:
                                print("Litujeme, číslo je větší")
                                tip = int(input("Hádej, jaké to je: "))

            pokracovani = input("Chcete pokračovat? a/n ")
            if pokracovani == "a":
                        vyber()
            else:
                        print("Díky za účast, " + jmeno)

def balitel():
     print("Vítej v prográmku, se kterým zaručeně zaboduješ!")
     pohlavi = input("Zadej pohlaví objektu svých vášní. Napiš muž/žena: ")
     vek = int(input ("Zadej věk objektu svých vášní: "))
     if pohlavi == "muž":
          if vek < 15:
               print("Ty prasnice! Na malé chlapečky, jo?")
          if vek >= 15 and vek < 49:
              print("Pěknej kluk jseš :-))")
              vyber()
          if vek >= 50 and vek < 89:
              print("Pěkný mládenec jste")
              vyber()
          elif vek > 90:
               print("Ty nechutná gerontofilko!")
               
     elif pohlavi == "žena":
          if vek < 15:
               print("Ty prase! Na malé holčičky, jo?")
               vyber()
          if vek >= 15 and vek < 49:
              print("Tvůj táta je pekař? Protože jsi pěkná buchta :-))")
              vyber()
          if vek >= 50 and vek < 89:
              print("Bolelo to, když jste spadla z nebe?")
              vyber()
          elif vek >= 90:
               print("Ty nechutnej gerontofile!")
               vyber()


def vyber():
    cochci = input("Co si zahraješ? Pro sčítání napiš s, pro pythagorovu větu napiš p, pro hádání čísla napiš h: ")
    if cochci == "s":
        jablka()
    elif cochci == "p":
        pythagorovavěta()
    elif cochci == "h":
        hadanicisla()
    elif cochci == "a":
        balitel()
    else:
        nadavka = random.choice(nadavky)
        print(nadavka + jmeno)
        vyber()

if jmeno == "Bela Lugosi":
        print("Beware of the big green dragon that sits on your doorstep! He eats little boys, puppy dog tails and big fat snails!")
        vyber()
else:
       vyber()
