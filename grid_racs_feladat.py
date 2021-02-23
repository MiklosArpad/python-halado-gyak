
feladat2 = ""

# írj egy függvény ami 2 dimenziós rácsos szerkezetet hoz létre
# a függvémynek 2 bemeneti paramétere legyen: row és column (sor és oszlop)
# töltsd ki a rácsot csak 0-val

# Pseudo kód
# függvény def
#   rács lista []
#   külső ciklus -y- (row)
#       rács listához hozzáadunk egy belső üres listát
#       belső ciklus -x- (column)
#           a rács lista belső listájába (rács lista az y indexnél) hozzáadunk egy 0-t
#    végül visszaadjuk a rács listát


#g = grid_create(10, 10)
#print(g)

# majd definiálj még egy függvémyt, ami egy rács bemenetet fogad és kiirja ezt a rácsot a konzolra, sorrol sorra

# az első függvény grid_create
# amásohik függvény grid_print

def grid_create(row, col):
    grid = []
    for y in range(row):
        grid.append([])
        for x in range(col):
            grid[y].append(0)
    return grid


def grid_print(grid):
    for row in grid:
        print(row)


g = grid_create(10, 10)
grid_print(g)