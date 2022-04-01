# 1. 4. 2022

## Knihovna turtle

- knihovna na kreslení jednoduchých obrázků
- želva, která chodí po obrazovce podle našich instrukcí
- nechává za sebou stopu

- abychom mohli používat funkce knihovny, musíme na začátek souboru přidat:
```python
from turtle import *
```

- příkazy

```python
forward(100) # jít dopředu - do závorky napíšeme o kolik

right(90) # otočení doprava - do závorky o kolik stupňů

left(90) # otočení doleva
```

## Zadání

*Nakreslete obrázky podle předlohy.*


### Úsečka
![Screenshot 2022-03-31 at 11 31 01](https://user-images.githubusercontent.com/44325210/161030294-776412f8-fa7b-4cd1-9d0c-b2623c318e10.png)

### Čtverec
![Screenshot 2022-03-31 at 11 32 01](https://user-images.githubusercontent.com/44325210/161030303-79196c06-e6ab-46b4-a2dc-1493512580e1.png)

```python
# ctverec
i = 0
while i < 4:
    forward(100)
    right(90)
    i += 1

```

### Rovnostranný trojúhelník
![Screenshot 2022-03-31 at 14 43 51](https://user-images.githubusercontent.com/44325210/161057573-29e05334-a378-4514-9b2f-58c9803c0180.png)

```python
# trojuhelnik
i = 0
while i < 3:
    forward(100)
    right(120)
    i += 1

```


### Pětiúhelník
![Screenshot 2022-03-31 at 11 32 20](https://user-images.githubusercontent.com/44325210/161030314-8693abaa-8d4c-4565-bcd6-700d03460f63.png)

nápověda:
![pentagon](https://user-images.githubusercontent.com/44325210/161031123-289867e1-0a88-4035-883c-81915b94e8c5.GIF)

```python
# petiuhelnik
i = 0
while i < 5:
    forward(100)
    right(72)
    i += 1

```

### Pěticípá hvězda
![Screenshot 2022-03-31 at 11 59 37](https://user-images.githubusercontent.com/44325210/161030339-ca1b5a17-af07-410a-a078-3336e32ea076.png)

### Spirála
![Screenshot 2022-03-31 at 11 34 13](https://user-images.githubusercontent.com/44325210/161030435-08b7d3ab-2ab5-47d3-a552-1327e9b93130.png)

### Lomená čára
![Screenshot 2022-03-31 at 11 39 32](https://user-images.githubusercontent.com/44325210/161030474-443a281e-2bbc-44c8-8e57-811be11abbe1.png)

### Hradby
![Screenshot 2022-03-31 at 11 43 31](https://user-images.githubusercontent.com/44325210/161030492-25934497-f5ae-4161-b506-34bb25859e9b.png)
