# bylo vice moznosti jak ulohu resit, nektera vase reseni:

list = [1,3,5,4,7]

find = int(input("Zadej číslo na hledaném indexu: "))
for index in range(len(list)):
    if find == list[index]:
        print(index)
        break
else:
    print(-1)
    
# nebo

pole = [1, 3, 5, 4, 7, 4] 
x = int(input("N: "))
exist = False

for i in range(len(pole)):
    if pole[i] == x:
        print(i)
        exist = True
        break
if exist == False:
    print("-1")
    
# pomoci while cyklu

cislo = int(input())
pozice = 0

pole = [1, 3, 5, 4, 7, 4]

while (pozice < len(pole) and pole[pozice] != cislo):
	pozice += 1

if (pozice == len(pole)):
	print(-1)
else:
	print(pozice)
  
