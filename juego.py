
def crea_tablero(fila, columna):
    salida = []
    for element in range(columna):
        lista2 = []
        for i in range(fila):
            lista2.append(0)
        salida.append(lista2)
    return salida

def juega(tablero, columna, valor_ficha):
    '''
    elegir la columna del tablero
    recorrer la columna desde atras hacia delante
       al encontrar el primer cero, lo sustituyo por valor_ficha
    '''

    c = tablero[columna]
    indice = len(c)-1
    while indice >= 0:
        if c[indice] == 0:
             c[indice] = valor_ficha
             break
        indice -=1 
    

def esta_llena(tablero, columna):
    '''
    seleccionar la columna que queremos comprobar (columna)
    comprobar si la columna tiene huecos con un in 
    devolver True o False
    '''
    c = tablero[columna]  
    return 0 not in c

def victoria_vertical_col(tablero, pos_columna, ficha):
    contador_iguales = 0
    columna = tablero[pos_columna]

    ix = 0
    while ix < len(columna):
        if columna[ix] == ficha:
            contador_iguales += 1
        else:
            contador_iguales = 0

        ix += 1
        if contador_iguales == 4:
            return True


    return False

def victoria(tablero, ficha):
    '''
    Obtener el numero de columnas de mi tablero
    iterar sobre range(num_columnas)
        para cada columna si es True devolver True
        si es False ir a la siguiente

    Si salgo del bucle, sigo buscando
    '''
    num_cols = len(tablero)
    for num_col in range(num_cols):
        if victoria_vertical_col(tablero, num_col, ficha):
            return True

    '''
    Obtener el numero de filas
    Iterar sobre range(num_filas)
        para cada fila si la victoria_horizontal es true, devuelvo True
        sigo en otro caso

    Si salgo del Bucle devolver false
    '''
    num_filas = len(tablero[0])
    for num_fila in range(num_filas):
        if victoria_horizontal_fila(tablero, num_fila, ficha):
            return True

    return False
        
def victoria_horizontal_fila(tablero, pos_fila, ficha):
    contador_iguales = 0
    
    for columna in tablero:
        if columna[pos_fila] == ficha:
            contador_iguales += 1
        else:
            contador_iguales = 0

        if contador_iguales == 4:
            return True
        
    return False
def victoria_diagonal(tablero, ficha):
    """
    Función para verificar si hay un 4 en raya diagonal en el tablero.
    """
    num_filas = len(tablero)
    num_columnas = len(tablero[0])

    # Verificar diagonales que van desde la esquina superior izquierda a la esquina inferior derecha
    for i in range(num_filas - 3):
        for j in range(num_columnas - 3):
            if tablero[i][j] == ficha and \
               tablero[i+1][j+1] == ficha and \
               tablero[i+2][j+2] == ficha and \
               tablero[i+3][j+3] == ficha:
                return True

    # Verificar diagonales que van desde la esquina superior derecha a la esquina inferior izquierda
    for i in range(3, num_filas):
        for j in range(num_columnas - 3):
            if tablero[i][j] == ficha and \
               tablero[i-1][j+1] == ficha and \
               tablero[i-2][j+2] == ficha and \
               tablero[i-3][j+3] == ficha:
                return True

    return False
