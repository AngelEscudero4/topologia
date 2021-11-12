import practica1.Complejo


def num_filas(M):
    """
    Nos dice el número de filas de una matriz.
    @param M: una matriz
    @type M: matriz
    @return: número de filas
    """
    return len(M)


def num_columnas(M):
    """
    Nos dice el número de columnas de una matriz.
    @param M: una matriz
    @type M: matriz
    @return: número de columnas
    """
    return len(M[0])


def sumar_dos_filas(matriz, fila_base, fila_objetivo):
    """
    Recibimos un array del que vamos a hacer fila_base+fila_objetivo y la vamos a dejar en fila_objetivo
    Los dos valores fila se pasan como entero y sera el numero de fila que queremos
    """
    # para cada elemento de la fila obtenemos su suma en Z2
    matriz[fila_objetivo][:] = [(x[0] + x[1]) % 2 for x in zip(matriz[fila_base], matriz[fila_objetivo])]
    print(matriz)


def sumar_dos_columnas(matriz, col_base, col_objetivo):
    """
    Recibimos un array del que vamos a hacer col_base+col_objetivo y la vamos a dejar en col_objetivo
    Los dos valores col se pasan como entero y sera el numero de columna que queremos
    """
    col_res = [(x[col_base] + x[col_objetivo]) % 2 for x in matriz]
    for i in range(num_filas(matriz)):
        matriz[i][col_objetivo] = col_res[i]

def forma_normal_Smith(matriz):
    """
    Recibimos una matriz borde y valculamos su forma normal de Smith
    """
    forma_NS = None
    pivote = [1, 1]
    # si a11 = 0 buscamos un elemento que sea 1 y los cambiamos de posicion
    while not (matriz(pivote)):
        pos_1 = buscar_1(matriz, pivote)
        # si no hemos encontrado ningun 1 hemos acabado
        if pos_1 == [-1, -1]:
            return forma_NS
        # si hay algun otro 1 entonces cambiamos las posiciones -> cambiar fila y cambiar columnas
        matriz[pivote[0]][pivote[1]] = 1
        matriz[pos_1[0]][pos_1[1]] = 0
        # si tenemos por debajo algun 1 lo quitamos sumando filas
        for i in range(matriz[pivote[0]], len(matriz)):
            # recorremos la columna buscando un 1
            if matriz[pivote[0]][i] == 1:
                # sumamos la fila del pivote con la que tiene un 1
                sumar_dos_filas(matriz, pivote[1], i)
        # si tenemos algun 1 a la derecha lo quitamos sumando columnas
        for j in range(matriz[pivote[1]], len(matriz[0])):
            # recorremos la fila buscando un 1
            if matriz[j][pivote[1]] == 1:
                # sumamos la fila del pivote con la que tiene un 1
                sumar_dos_columnas(matriz, pivote[0], j)
        # aqui ya deberia estar limpio para el pivote

        # avanzamos el pivote
        pivote[0] += 1
        pivote[1] += 1
    # asignamos el resultado
    forma_NS = matriz
    return forma_NS


def buscar_1(matriz, pos):
    """
    recibe una matriz y busca un uno a partir de una posicion recibida
    La posicion tiene que ser o una lista o una tupla
    """
    pos_actual = pos
    index = [-1, -1]

    for i in range(pos[0], len(matriz)):
        for j in range(pos[1], len(matriz[0])):
            if matriz(i, j):
                return [i, j]
    return index


def cambiar_filas(matriz, fila1, fila2):
    """
    Tomo los valores de la fila1 y los pongo en la fila2, y al reves
    """
    filaAux = matriz[fila1]
    matriz[fila1]=matriz[fila2]
    matriz[fila2]=filaAux

    print(matriz)

def cambiar_columnas(matriz, columna1, columna2):
    """
    Tomo los valores de la columna1 y los pongo en la columna2, y al reves
    """
    columnaAux = [x[columna1] for x in matriz]

    i = 0

    for x in matriz:
        x[columna1] = x[columna2]
        x[columna2] = columnaAux[i]
        i = i + 1

