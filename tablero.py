def tablero(colum, row):
    res = []
    for i in range(colum):
        res2 = []
        for j in range(row):
            res2.append("__")
        res.append(res2)
    return res

def imprimir_tablero(tablero):
    for columna in zip(*tablero):
        print(columna)

mi_tablero = tablero(7, 6)
imprimir_tablero(mi_tablero)



