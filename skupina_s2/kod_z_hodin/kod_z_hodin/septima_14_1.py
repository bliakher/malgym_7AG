import random as rnd
import time

"""
colors = ["red", "green", "blue"]

rnd_col = rnd.choice(colors)
print(rnd_col)

rnd_num = rnd.randint(1, 6)
print(rnd_num)
"""
num = int(input("Cislo od 1 do 6: "))
rnd_num = rnd.randint(1, 6)
time.sleep(3)
print("Hadali jste:", num, "vysledek byl:", rnd_num)

if num == rnd_num:
    print("Vyhrali jste")
else:
    print("Prohrali jste :)")

