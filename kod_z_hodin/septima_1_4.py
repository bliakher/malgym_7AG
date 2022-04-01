from turtle import *

"""
puvodni = int(input("puvodni:"))
sleva =int(input("sleva:"))

nova = puvodni - puvodni / 100 * sleva
print(nova)
"""

"""
# usecka
forward(100)
"""
"""
# ctverec
i = 0
while i < 4:
    forward(100)
    right(90)
    i += 1
"""

# trojuhelnik
i = 0
while i < 3:
    forward(100)
    right(120)
    i += 1

"""
# petiuhelnik
i = 0
while i < 5:
    forward(100)
    right(72)
    i += 1
"""

"""
# hvezdice
i = 0
while i < 5:
    forward(100)
    right(144)
    i += 1
"""

"""
# spirala
i = 0
while i < 20:
    forward(i * 10)
    right(90)
    i += 1
"""

"""
# zigzag
right(45)
i = 0
while i < 10:
    forward(30)
    if i % 2 == 1:
        right(90)
    else:
        left(90)
    i += 1
"""

"""
# hradby
left(90)
i = 0
while i < 10:
    if i % 2 == 0:
        right(90)
        forward(30)
        right(90)
        forward(30)
    else:
        left(90)
        forward(30)
        left(90)
        forward(30)
    i += 1
"""

