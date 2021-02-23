
feladat1 = ""

# írj két függvényt
# 1. konvertáljon celsiusból farenheitbe
# 2. konvertáljon farenheitből celsiusba

# a visszaadott értékek 1 tizedes számot adjanak vissza

# f = c *9/5 + 32
# c = (f - 32) * 5/9

#f = farenheit
#c = celsius

def cel_to_far(c):
    return round(c * 5/9 + 32, 1)
print(cel_to_far(30))
print(cel_to_far(40))
        # a round- al kerekítek 1 tizedesre

def far_to_cel(f):
    return round((f - 32) * 5/9, 1)
print(far_to_cel(30))
print(far_to_cel(40))
        # a round- al kerekítek 1 tizedesre