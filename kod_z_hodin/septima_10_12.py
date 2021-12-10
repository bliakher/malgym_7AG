# ahoj

def secti_pole(a,b):
  c=[]
  i=0
  while i<len(a):
    c.append(a[i]+b[i])
    i+=1
  return c

def secti_pole2(pole1, pole2):
  i = 0
  pole3 = []
  
  while len(pole1) > len(pole2):
      pole2.append(0)
  
  while len(pole2) > len(pole1):
      pole1.append(0)

  while i < len(pole2):
      pole3.append(pole1[i] + pole2[i])
      i += 1
  return pole3

def secti_pole3(pole1, pole2):
  i = 0
  pole3 = []
  
  if len(pole1) > len(pole2):
    delsi = pole1
    kratsi = pole2
    delka_kratsiho = len(pole2)
  else:
    delsi = pole2
    kratsi = pole1
    delka_kratsiho = len(pole1)

  while i < delka_kratsiho:
      pole3.append(pole1[i] + pole2[i])
      i += 1

  if len(pole1) != len(pole2):
    prebyva = delsi[i:]
    pole3.extend(prebyva)

  return pole3

a = [1,2,3,4,5,2,3,4]
b = [2,4,5,6,8,9]
print(secti_pole3(a,b))
print("a:", a, "b:", b)
print(secti_pole2(a, b))
print("a:", a, "b:", b)

a = [1, 2, 3, 4]
b = [2, 2, 3, 3]

c = secti_pole(a, b) # c = [3, 4, 6, 7]
print(c)

print(a[:])



a = [1,2,3,4,5,2,3,4]

# slovnik - dictionary

# klic - hodnota
# dobry den - hello


cz_en = {
  "dobry den" : "hello",
  "kocka" : "cat"
}

print(a[3])
print(cz_en["kocka"])
print(cz_en["dobry den"])

a[3] = 5
cz_en["kocka"] = "kitty"
cz_en["pes"] = "dog"

print(a[3])
print(cz_en["kocka"])
print(cz_en["dobry den"])
print(cz_en)


nakupni_seznam = {
  "vejce" : 12,

}


