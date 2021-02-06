
# funtions as first class citizens
# függvényt adunk egy másik függvény bemetnek - függvény a függvényben

import math    # ez az import a python sajátja

def negyzet(x):
    return x*x
def gyok(x):
    return x**0.5

def muvelet(funct, szam):
    return funct(szam)

m1 = muvelet(negyzet, 10)
print(m1)

m2 = muvelet(gyok, 100)
print(m2)

m3 = muvelet(math.sin, 5)
m4 = muvelet(math.cos, 5)
m5 = muvelet(math.tan, 5)
m6 = muvelet(math.exp, 5)

print(m3, m4, m5, m6)

m7 = muvelet(lambda x: x*x*x, 13)
print(m7)