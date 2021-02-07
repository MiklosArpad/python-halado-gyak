
# list comperhensins - lista megértések 1. resz


szamok = [x for x in range(1, 21)]
szamok2 = [x for  x in range(20)]
print(szamok, szamok2)

paros = [x for  x in  range(20) if x % 2 == 0]
paratlan = [x for x in  range(20) if x % 2 != 0]
print(paros, paratlan)

nevek = ["lali", "pali", "vali", "mari,", "buksi", "mirci"]
print(nevek)
nevek = [nev.capitalize() for nev in nevek]
print(nevek)

nevek_M = [nev for nev in nevek if nev.startswith("M")]
print(nevek_M)