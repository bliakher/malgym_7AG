import sys

"""
print("ahoj")
a = 5
print(a)
b = 4
c = 3
print(a, b, c)
print(a, b, c, sep=" ") # vychozi
# separator
print(a, b, c, sep=', ')
print(a, b, c, sep=' * ')

print(a, b, c, end='\n') # vychozi
# \n znak konce radku - new line
# \t tabulator
print("Ahoj\nsvete")
print(a, b, c, end=' ')
print("Ahoj")

print(123, file=sys.stdout) # vychozi - standardni vystup
print(123, file=sys.stderr) # chybovy vystup

"""
"""
*
**
***
****
"""

# nacist cislo a vypsat tolik hvezdicek na radek
"""
x = 5
print("*" * x)

for i in range(x):
    print("*", end='')
"""
patra = 4 # patra
# 1. patro - x = 1
# 2. patro - x = 2
# 3. patro - x = 3
# 4. patro - x = 4

"""
x = 1
for i in range(x):
    print("*", end='')
print()

x = 2
for i in range(x):
    print("*", end='')
print()

x = 3
for i in range(x):
    print("*", end='')
print()
"""

for i in range(1, patra + 1):
    print("*" * i)

for patro in range(1, patra + 1):
    for j in range(patro):
        print("*", end='')
    print(end='\n')





