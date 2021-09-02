
a = 3

if a > 0:
    a = a - 1
else:
    a = a + 1


a = 3
a = a - 1

a -= 1
a += 1

a /= 2
a *= 3

# absolutni hodnota
# program nacte cislo, spocita abs. hodnotu a vypise vysledek
"""
a = int(input())

if a < 0:
     #result = a - 2*a
     result = -a
else:   # a >= 0
    result = a

print(result)

# typ trojuhelniku

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))


if a == b:
    if b == c:
        print("rovnostranný")
    else: # b!=c
        print("rovnoramenný")

else: # a!=b
    if b == c:
        print("rovnoramenný")
    else: # b!=c
        if a == c:
            print("rovnoramenný")
        else: # a!=c
            print("obecný")

# zkracene

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a==b and a==c:
    print("Je rovnostranny")
elif a==b or a==c or b==c:
    print("Je rovnoramenny")
else:
    print("Je obecny")



# CYKLY - cycles, loops


# while podminka:
#       neco delej

# skonci cyklus, pokracuj dal

# vypsat cisla od 1 do 10

i = 1
print(i)
i += 1
print(i)
i += 1
print(i)
i += 1
print(i)
i += 1
print(i)
#...
# dokud i <= 10



i = 1
while i <= 10:
    print(i)
    i += 1

print("konec")


i = 1
while i <= 10:
    print("*")
    i += 1
"""

# nekonecny cyklus
"""
i = 1
while i <= 10:
    print("*")
"""

while True:
    a = int(input("Cislo: "))

    if a < 0:
         #result = a - 2*a
         result = -a
    else:   # a >= 0
        result = a

    print(result)



# FizzBuzz
# vypsat napovedu od 1 do 30

num = 1
while num <= 30:

    num=int(input("Your number?"))
    if num%3==0 and num%5==0:
        print("Fizzbuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)

    num += 1































    
