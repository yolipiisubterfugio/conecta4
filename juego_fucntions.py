def tablero(colum, row):
    res = []
    for i in range(colum):
        res2 = []
        for j in range(row):
            res2.append("__")
        res.append(res2)
    return res

def juega(tablero, columna, valor_ficha):
    