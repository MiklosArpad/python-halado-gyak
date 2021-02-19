
# closures - bezárások 1. rész

def kulso():
    szam = 21
    def belso():
        nonlocal szam  # a nonlocal kulcszó használatával tudom a belső függvényben növeltetni a változó értékét
        szam += 11      # ennélkül nem engedi a charm
        print(szam)
    return belso
f1 = kulso()
f1()

# clsures _ bezárások 2. rész
# operator factory closure functions

def op_factory(oper, num):
    def oeration(value):
        if oper == "**":            # a ** hatványozó érték
            return value ** num
        elif oper == "*":
            return value * num
        elif oper == "/":
            return value / num
        else:
            return "Nut supported operator!"

    return oeration                  # nem kell a zárójel, mert nem kell meghívni csak értéket visszaadni



negyzet = op_factory("**", 2)
kob = op_factory("**", 3)
print(negyzet(5), kob(5))

test1 = op_factory("$", 5)
print(test1(5))

mult4 = op_factory("*", 4)
print(mult4(8))

div_by_5 = op_factory("/", 5)
print(div_by_5(45))