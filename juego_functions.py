def tablero(colum, row):
    res = []
    for i in range(colum):
        res2 = []
        for j in range(row):
            res2.append("__")
        res.append(res2)
    return res

def juega(tablero, columna, valor_ficha):
    indice = len(c)-1
    while incice >=0:
        if c(indice) == 0:
            c[indice] = valor_ficha
            break
        indice -=1
        
def esta_llena(tablero, columna):
    