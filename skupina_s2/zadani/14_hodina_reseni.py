# pole obecne --------------------------------------------

#pole je datová struktura, do které můžeme uložit prvky
#pole = [] 
#přidání prvku: "název pole".append("prvek")
#přistoupení k prvku na indexu: "název pole"["index"] 
#délka pole: len("název pole")
#count, index, min, max...funkce prochazi pole 

# zvetsit kazdy prvek o tri -------------------------------

pole=[1, 2, 3, 5, 4]
for i in range(len(pole)):
  pole[i]+=3
  
print(pole)

# hledani maxima a minima ----------------------------------

pole=[1, 2, 3, 5, 4]

max = pole [0]
for i in pole:
  if i > max:
    max = i
print(max)

min = pole [0]
for i in pole:
  if i < min:
    min = i
print(min)

# druhy nejvetsi prvek na dva pruchody polem ---------------

max = pole[0]
for i in range(len(pole)):
  if pole[i] > max:
    max = pole[i]
    max_idx = i
pole.pop(max_idx)
max2 = pole [0]
for i in pole:
  if i > max2:
    max2 = i
print(max2)

# na jeden pruchod -----------------------------------------

if pole[0] > pole[1]: #resime problem, ze nejvetsi prvek muze byt prvnim prvkem pole
  max = pole[0]
  druhyMax = pole[1]
else:
  max = pole[1]
  druhyMax = pole[0]

for a in pole:  #jeden pruchod polem
  if a > max:
    druhyMax = max
    max = a
  elif a > druhyMax and a != max:
    druhyMax = a
print(max, druhyMax)





