#KOSTKY HAZARD

# co se muze hodit
#   import random as r
#   import time as t

#   num = r.randint
#   print(num)
#   t.sleep(3)

#   pole=['piky', 'kary']
#   k= r.choice (pole)


#---------------------------------------------------------------------------
#HRA

import random as r

#FUNKCE
def ochrana_penez ():
    global penize
    print("Ja ti dam. Odepisu ti 5 penez")
    print("BANK: ", penize)
    penize -= 5
    print("BANK: ", penize)

def vyhra(pocitac):
    global penize
    print("Vyhral jste, jste sikula!")
    penize += penize_vlozene
    print ("Pocitac mel ", pocitac)
    print("BANK: ", penize)
        
def prohra(pocitac):
    global penize
    print("Prohral jste, byl jste otupen :((")
    penize -= penize_vlozene
    print ("Pocitac mel ", pocitac)
    print("BANK: ", penize)
        
def remiza(pocitac):
    print("Tohle jsem vybral taky, trapaku, zkus to znova")
    print ("Pocitac mel ", pocitac)
    print("BANK: ", penize)

#--------------------------------------------------------------------------------

print("Vitejte v nasem svete her, u nas se muze stat milionarem kazdy")

penize = 100
print("Na zacatek Vam dame ", penize)

while True:
    otazka_hra = input("Chcete si zahrat kamen nuzky papir? (A/N) ")
    if otazka_hra == 'N':
        print("Tak priste trapaku, nashledanou")
        exit()
    elif otazka_hra =='A':
        if penize == 0:
            print("Haha, dosly Vam penize, troubo!")
            print("Priste se snaz vic")
            print("BANK: ", penize)
            print("KONEC HRY")
            exit()
        
        penize_vlozene = int(input("Kolik vsazite na svou mysl? "))
     
        if penize_vlozene > penize:
            print("Tolik penez nemas frajere, brzdi")
            b=ochrana_penez()
            continue #preskoci zbytek cyklu a skoci na zactek
        
        elif penize_vlozene <=0:
            print("To je moc malo, vidime zes nas chtel osidit, sejdiri.", end = " ")
            b = ochrana_penez()
            continue

        #----------------------------------------------------------------------------
        #MOZNOSTI A HRA
        hrac = input("Zvolte si svou moznost: ")

        moznosti =["kamen", "papir", "nuzky"]
        if hrac not in moznosti:
            print("Vyberte validni moznost")

        pocitac = r.choice(moznosti)
            
        if pocitac == hrac:
            remiza(pocitac)
            
        if pocitac == "kamen":
            if hrac == "nuzky":
                prohra(pocitac)
            elif hrac == "papir":
                vyhra(pocitac)
                
        if pocitac == "papir":
            if hrac == "kamen":
                prohra(pocitac)
            elif hrac == "nuzky":
                vyhra(pocitac)

        if pocitac == "nuzky":
            if hrac == "papir":
                prohra(pocitac)
            elif hrac == "kamen":
                vyhra(pocitac)
    else:
        print ("Takova moznost nejde zadat, zadej znovu")
    




