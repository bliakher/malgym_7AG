import random as r
import time

x = 1

we = int (input ("Kolik vsázíš: "))
time.sleep (1)
while (x == 1):
  tnum = int (input ("Typni si číslo karty (1-10): "))
  time.sleep (1)  
  tcol = input ("Typni si barvu karty (piky, káry, kříže, srdce): ")
  time.sleep (1)  
  colors = ["srdce", "káry", "kříže", "piky"]
  time.sleep (1)

  ha = input ("Jdeme na to? (a/n): ")


  if ha == "a":

    if tcol == r.choice (colors) and tnum == r.randrange (1, 10):
        print ("Gratulujeme, trefil jsi obojí!")
        print ("vsazené peníze byly ztrojnásobeny!")

        we = we*3
        
    elif  tcol == r.choice (colors) or tnum == r.randrange (1, 10):
        print ("Gratulujeme, trefil jsi si sice jen jedno, ale tvé jmění bylo zdvojnásobeno")

        we = we*2
        
    else:
        print ("Prohrál jsi, všechno tvé jmění propadlo nám!")

        we = 0
        x = 0
    time.sleep (2)  
    print ("Tvé aktuální jmění je:", we)
    time.sleep (1)
  else:
    print ("Škoda, měj se fajn!")
    x = 0
    
    
