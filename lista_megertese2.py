
# list comperhensins - lista megértések 2. resz

matrix_zeros =[[0 for x in range(4)] for y in range(4)]
print(matrix_zeros)
print()   # ezzel a kiiratásnál tudok egy üre sort is beiktatni

matrix_print = lambda mat: [print(row) for row in mat]
matrix_print(matrix_zeros)
print()    #ezzel a kiiratásnál tudok egy üre sort is beiktatni

matrix_identity = [[1 if x==y else 0 for x in range(9)] for y in range(9)]
matrix_print(matrix_identity)

# matrix_identity = ([[1 if x==y else 0 for x in range(9)] for y in range(9)], print())
                                            #ezzel a kiiratásnál tudok egy üre sort is beiktatni
                                            # ha zárójelek közé teszem és printelem