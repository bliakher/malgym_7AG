
print(1, 2, 3, end="konec\n")
print("dalsi")

i = 0
while i < 3:
  j = 0
  while j < 3:
    print("X",end="")
    j += 1
  print ()

  i += 1


"""

*
**
***
****


  *
 ***
*****

   *
  o*o
 *****
o*****o
"""


# print("*" * pocet)
pocet = 1
j = 0
while j < pocet:
    print("*",end="")
    j += 1
print()

pocet = 2
j = 0
while j < pocet:
    print("*",end="")
    j += 1
print()

pocet = 3
j = 0
while j < pocet:
    print("*",end="")
    j += 1
print()




patro = 1
while patro <= 4:
    j = 0
    while j < patro:
        print("*",end="")
        j += 1
    print()
    patro += 1


# hledani maxima v poli

cisla = [1, 2, 3]
nejvetsi = cisla[len(cisla) - 1] # cisla[-1]

cisla = [1, 3, 2, 45, 31, 12]
cisla.sort()
print(cisla)
nejvetsi = cisla[len(cisla) - 1]
print(nejvetsi)


cisla = [1, 3, 2, 45, 31, 12]
max = cisla[0]
i = 0
while i < len(cisla):
    cislo = cisla[i]
    if cislo > max :
        max = cislo
    i += 1

print("max:", max)

cisla = [1, 3, 2, 45, 31, 12]
min = cisla[0]
i = 0
while i < len(cisla):
    cislo = cisla[i]
    if cislo < min :
        min = cislo
    i += 1

print("min:", min) 






















    
