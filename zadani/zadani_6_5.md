## Zadání 6. 5. 2022

*Řešení mi odevzdejte do Teams. Úkol nebudu známkovat, je to hlavně procvičení pro vás na test a pro mě přehled, co umíte.*

### Úloha 1

*Podívejte se na následující kousky kódu. U každého nejdřív rozmyslete, jaký bude výstup programu a svoje řešení **zapište** do souboru, který budete odevzdávat. 
Pak si kód zkopírujte a zkuste spustit. 
Podívejte se, jaký je výstup doopravdy. Pokud jste měli jiný výstup, ujistěte se, že rozumíte tomu, proč program dělá to, co dělá. Můžete se poradit s ostatními.*

Nepodvádějte, jedná se hlavně o procvičení pro vás.

1)
```python
x = 42

if x % 3 == 0:
  print("yes")
else:
  print("no")
```

2)
```python
i = 0
while i < 4:
  print(i)
  i += 1
```

3)
```python
i = 0
x = 5
while i < 4:
  print(x)
  i += 1
```

4)
```python
i = 0
x = 0
while i < 4:
  x += i
  i += 1
print(x)
```

5)
```python
i = 0
x = 0
while i < 4:
  x += i
  i += 1
  print(x)
```

6)
```python
pole = [1, 2, 3, 4]
i = 0
while i < len(pole):
  print(pole[i])
  i += 1
```

7)
```python
pole = [1, 2, 3, 4]
i = 0
while i < len(pole):
  print(pole[i])
  i += 2
```

8)
```python
pole = [1, 2, 3, 4]
i = len(pole) - 1
while i >= 0:
  print(pole[i])
  i -= 1
```
### Úloha 2

Funkce `print` vypisuje všechno, co ji dáme, na obrazovku. Když dáme funkci `print` několik argumentů - př. `print(1, 2, 3)` - vypíše je všechny postupně na řádek a mezi ně dá vždy jednu mezeru - tedy výstup bude `1 2 3`.

Znak, který print dává mezi argumenty, když je vypisuje můžeme změnit pomocí parametru `sep` - separátor. Parametr napíšeme do funkce `print` na konec, za všechno, co chceme vypsat. Výchozí nastavení (když tam nedáme nic) je jedna mezera, tedy `print(1, 2, 3, sep=" ")`.

Můžeme zkusit změnit separátor na něco jiného. Vyzkoušejte si, co se vypíše:

```python
print(1, 2, 3, sep="*")

print(1, 2, 3, sep="/")

print(1, 2, 3, sep="")
```

Funkce `print` má ještě další nepovinný parametr - `end` - tento parametr určuje znak, který se přidá na konec všeho, co vytiskne print. 
Výchozí hodnota (pokud parametr do printu nenapíšeme) je nový řádek, tedy po každém printu se odřádkuje. `print("ahoj", end="\n")`
`\n` je speciální znak, který značí nový rádek. 
Pokud nechceme, aby `print` po vytisknutí skočil na nový řádek, můžeme parametr `end` změnit.

Vyzkoušejte si jaký je rozdíl:

```python
# prvni varianta
print("Hello")
print("World")

# druha varianta
print("Hello", end="")
print("World", end="")
```

1) _Doplňte do funkce print parametr tak, aby se všechna X vypsala na jeden řádek._

Výstup bude:
```
XXX
```
```python
i = 0
while i < 3:
  print("X")
  i += 1
```

2) _Doplňte kód tak, aby se vytisklo:_
```
XXX
XXX
XXX
```
```python
i = 0
while i < 3:
  j = 0
  while j < 3:
    print("X")
    j += 1
  i += 1
```
