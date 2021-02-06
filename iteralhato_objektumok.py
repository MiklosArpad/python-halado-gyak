
# iterable unpacking - iteralhato objektumok kicsomagolása

# list
lista1 = range(10)
print(list(lista1))
print(*lista1)

lista2 = [1, 2, 3, 4, 5, 6]
lista3 = lista2

lista4 = lista2
lista4 = [*lista2]

lista3[0] = 111
print(lista2, lista3, lista4)

def funct(*args, **kwargs):
    print(args)
    print(kwargs)

funct(10, 20, 30, 40, 50, **{"név1":"Bözsi", "név2":"Eni", "név3":"Era", "név4":"Vera", "név5":"Teri"})

nevek = ["Bözsi", "Eni", "Era", "Vera", "Teri"]
korok = [33, 34, 33, 35, 43]
nev_kor = [*nevek], [*korok]
print(nev_kor)

szoveg = "Hello, hogy vagy? Jó, hogy vagy!"
betu_lista = [*szoveg]
print(betu_lista)
udv = "".join(betu_lista)
print(udv)