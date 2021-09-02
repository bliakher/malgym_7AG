# zdravici funkce --------------------------------

def pozdrav(name):
  print ("Ahoj,", name)
  
pozdrav("Emil")

# zdravici funkce - pole --------------------------

def hodne_pozdravu(pole):
  for jmena in pole:
    pozdrav(jmena)

jmena = ["Anna","Nikola","Katka","Max","Tom"]
hodne_pozdravu(jmena)

# nacitani jmen - vic moznosti --------------------

def vypiska ():
  vypis = []
  while True:
    vstup = input("jméno (pro ukončení zadejte K)")
    if(vstup == "K"):
      break
    else: 
      vypis.append(vstup)
  #print(vypis)
  return vypis

def nacti_jmeno ():
  pole=[]
  n = int(input("Kolik jmen chceš načíst? "))
  for i in range(n):
    jmeno = input("Napis jmeno ")
    pole.append(jmeno)
  return pole

# kombinace ---------------------------------------

pole_jmena = vypiska()
hodne_pozdravu(pole_jmena)

# prumer pole -------------------------------------

def prumer(pole):
  suma = 0
  for prvek in pole:
    suma += prvek
  print("Průměr je " + str(suma/len(pole)))
  
poleCisel = [1,2,3,4,5,6,7,8,9]
prumer(poleCisel)



