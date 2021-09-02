"""
a = int(input())
b = int(input())
c = int(input())

if a == b:
	if b == c:
		print("rovnostranný")
	else:
		print("rovnoramenný")
else:
        if b == c:
                print("rovnoramenný")
elif a == c:
	print("rovnoramenný")
else:
	print("obecný")


if a == b and b == c:
        print("rovnostranný")
elif a == b or b == c or c == a:
        print("rovnoramenný")
else:
        print("obecný")

"""

# cykly
# while _podminka_:
#       prikaz

"""
a = 5

while a != 0:
        print(a)
        a = a - 1

print("konec cyklu")


a = int(input())
b = int(input())

while b == 0:
        print("nelze delit 0")
        b = int(input("zadaje jine cislo"))

print(a//b)
"""

# nacte cislo x
# cisla od 1 do x

"""
max = int(input())

a = 1

while a <= max:
        print(a)
        a = a + 1

"""
# bool - boolean - True / False

"""
while True:

        x = int(input())

        if x % 2 == 0:
                print("sude")
        else:
                print("liche")

print("konec")
"""

"""
a = int(input())

while True:
        b = int(input())
        if b != 0:
                break

print(a//b)

"""

# FizzBuzz
# delitelne 3 - Fizz
# delitelne 5 - Buzz
# delitelne obema - FizzBuzz

# 1, 2, Fizz, 4, 5, Fizz, ... 30

max = 30
x = 1

while x <= max:
        if x % 3 == 0 and x % 5 == 0:
                print("FizzBuzz")
        elif x % 3 == 0:
                print("Fizz")
        elif x % 5 == 0:
                print("Buzz")
        else:
                print(x)
        x += 1








