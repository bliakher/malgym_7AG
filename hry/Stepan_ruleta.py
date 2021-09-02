"""
import random as r
import time as t
#hod kostkou

x = r.randrange (1, 10)
"""
def ruskaruleta():
  import time
  import random as r
  
  # ruská ruleta
  jmeno = input ("Jak se jmenuješ(resp. jak tě oslovují): ")
  print ("Zahrajeme si ruskou ruletu,", jmeno, ".")
  time.sleep (2)
  print ("Pistole, kterou používáme má bubínek na šest nábojů", jmeno, ".")
  time.sleep (3)
  print ("Moment...")
  time.sleep (1)
  

  
  while True:
    y = 1
    naboje = 6

    guess = int (input ("Zkus si tipnout, po kolika kolech zemřeš: "))
    
    print ("Chvilka napětí...")
    time.sleep (1)
                 
    for i in range (4):
      print (".")
      time.sleep (0.5)
                 
    for index  in range (1, 7):  
      x = r.randrange (1, naboje)
      naboje -= 1
                 
      if x == y:
        print ("Prohrál jsi. Jsi mrtvý ", jmeno,"!")
        print ("Zahrajeme si ještě jednou!")
        print (jmeno)
      
        if guess == index:
              print ("Výborně, uhodl/a jsi to ", jmeno,"!")
              time.sleep (2)
              break 
        else:
              print ("Bohužel jsi se netrefil/a, třeba příště ", jmeno,".")
              break 
          
      else:
        for i in range (6):
          print (".")
          time.sleep (0.5)
          
        print ("Uff, nejsi mrtvý", jmeno, "!")
        time.sleep (5)
        print ("Jdeme na to znovu", jmeno, ".")
        time.sleep (2)

ruskaruleta()

