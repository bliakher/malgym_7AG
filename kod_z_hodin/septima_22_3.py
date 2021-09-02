
# delitelnost 2
"""
num = int(input("Enter number"))

if num % 2 == 0:
    print("Divisible by 2")
else:
    print("Not divisible by 2")
"""

# vypise: pokud je del 2 nebo je del 3 nebo neni delitelne ani 2 ani 3


# vyroky
# vyrok ma hodnotu - pravda x lez
# True x False

# slozene vyroky
# AND, OR

# koupili si zmrzlinu AND koupili si cokoladu   
#   True                    False

# cislo del 6
# cislo je del 2 AND cislo je del 3

# koupime si zmrzlinu OR koupime si cokoladu
# cislo je del 2 OR cislo je del 3
# del 2 nebo del 3 nebo del obema

# vypise: ( je del 2 nebo je del 3 ) nebo neni delitelne ani 2 ani 3

"""
num = int(input("Enter number"))

if num % 2 == 0 or num % 3 == 0:
    print("Divisible by 2 or 3")
else:
    print("Not divisible by 2 nor 3")
"""
# not(a or b) = not a and not b

# vypise: je del 2, je del 3, je del obema


# FizzBuzz

# pokud cislo del 3 -> Fizz
# pokud cislo del 5 -> Buzz
# pokud cislo del 3 i 5 -> FizzBuzz
# jinak -> cislo

# 1, 2, Fizz, 4, Buzz

# program - nacte cislo - vypise co mam rict ve hre


# reseni 1

num=int(input("Your number?"))
if num%3==0 and num%5==0:
    print("Fizzbuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:
    print(num)
    

# reseni 2

cislo= input("Zadej číslo, prosím! ")
zbytek= int(cislo)%15
if (zbytek==0):
    print ("FizzBuzz!")
else:
    zbytek2= int(cislo)%5
    if (zbytek2==0):
        print("Buzz!")
    else:
        zbytek3= int(cislo)%3
        if (zbytek3==0):
            print ("Fizz!")
        else: print (cislo)

# reseni 3

num=int(input("Your number?"))

if num % 3 == 0 and num % 5 != 0:
    print("Fizz")
if num % 3 != 0 and num % 5 == 0:
    print("Buzz")
if num % 3 == 0 and num % 5 != 0:
    print("FizzBuzz")







    
