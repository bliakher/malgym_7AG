# operace se stringy

"""
x = int(input())

print(x * "s")

a = "ahoj"

print(3 * a)

b = "cau"

# konkatenace stringu
c = a + b
print(c)
"""
"""
x = int(input("cislo"))
i = 1

while i <= x:
    print("*", end="")
    i += 1


x = int(input("cislo"))
i = 1
hvezdicky=""

while i <= x:
    hvezdicky += "*"
    i += 1
print(hvezdicky)
"""
"""
#for cyklus
slovo = "ahoj"

for pismeno in slovo:
    print(pismeno, end="")
print()

#for i in range(cislo, kolikrat se ma cyklus opakovat)
# i = 0, cislo - 1
# range(4) -> 0, 1, 2, 3

for i in range(4):
    print(i)

max = 4
i = 0
while i < max:
    print(i)
    i += 1

# range(min, max) -> min, min+1, ..., max-1
# range(0, 4) -> range(4)
for i in range(1, 5): # 1, 2, 3, 4
    print(i)
"""
"""
x = int(input())

for i in range(x):
    print("*", end="")
print()
"""
"""
*
**
***
****
"""

for x in range(1, 6):
    for i in range(x):
        print("*", end="")
    print()









    










