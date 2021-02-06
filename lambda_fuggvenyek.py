
# anonymus functions, lambda expressions - névtelen függvények, lambda képletek

def osszead1(a, b):
    return a+b
print(osszead1(10, 20))

osszead2 = lambda a, b: a + b
print(osszead2(20, 255))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
paros = list(filter(lambda x: x % 2 == 0, lista))
print(paros)

ista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
paros = filter(lambda x: x % 2 == 0, lista)
for p in paros:
    print(p)

muveletek = {
    "add": lambda a, b: a +b,
    "sub": lambda a, b: a -b,
    "mult": lambda a, b: a *b,
    "div": lambda a, b: a /b
}
print(muveletek["add"](323, 244))
add = muveletek["add"](323, 244)
print(add)

add = muveletek["add"]
print(add(222, 111))

muvelet = muveletek["sub"]
print(muvelet(222, 111))
