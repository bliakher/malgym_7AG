"""
name = ["Anna", "Emma", "Max"]
surname = ["Karenina", "Stone", "Brod"]


idx = 0
while idx < len(name):
    print("Hello, " + name[idx] + " " + surname[idx] + "!")
    idx += 1
"""

jmeno = "Otto"
darky = ["LP", "rukavice"]


print("Milý Ježíšku,\n přeju si:")
i = 0
while i < len(darky):
    darek = darky[i]
    print("- " + darek)
    i += 1

print(jmeno)
"""
print("Milý Ježíšku,\n přeju si:")

for darek in darky:
    print("- " + darek)

print(jmeno)


cisla = [1, 2, 3]

for cislo in cisla:
    cislo += 1

print(cisla)

cisla[0] = 3

i = 0
while i < len(cisla):
    cislo = cisla[i]
    cislo += 1

print(cisla)

"""

def vypis(jmeno, darky):
    print(jmeno)
    for darek in darky:
        print("- " + darek)


prani = {
    "Otto" : ["LP", "rukavice"],
    "Anička" :  ["ponozky", "kote"]
    }

prani["Michal"] = ["ponozky"]

darky_Anicky = prani["Anička"]
#vypis("Anička", darky_Anicky)

for jmeno in prani:
    darky = prani[jmeno]
    vypis(jmeno, darky)


prani = {
    "Otto" : "LP",
    "Anička" :  "ponozky",
    "Michal" : "ponozky"
    }

objednavky = {
    }


for jmeno in prani:
    darek = prani[jmeno]
    if darek in objednavky:
        objednavky[darek] += 1
    else:
        objednavky[darek] = 1

print(objednavky)
        
        



















