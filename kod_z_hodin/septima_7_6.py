
slova = ["slovo", "luk", "jablko", "auto", "carodejnice"]

for slovo in slova:
    if len(slovo) > 4:
        print(slovo)
    


def prumer(pole):
    soucet = 0
    for cislo in pole:
        soucet += cislo
    prumer = soucet / len(pole)
    return prumer

p = prumer([1, 2, 3, 4, 5])
print(p) # vypise 3.0
    
def count(pole, prvek):
    count = 0
    for p in pole:
        if p == prvek:
            count += 1
    return count

c = count([1, 2, 2, 1, 1, 1], 1)
print(c) # vypise 4
