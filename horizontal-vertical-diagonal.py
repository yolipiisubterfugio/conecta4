def gana_horizontal(tablero, columna):
    for fila in tablero:
        if fila[columna] == "__":
            return False
    return True

def esta_llena_vertical(tablero, columna):
 
    return all(fila[columna] != "__" for fila in tablero)