def num_filas(M):
    """
    Nos dice el número de filas de una matriz.
    """
    return len(M)


def num_columnas(M):
    """
    Nos dice el número de columnas de una matriz.
    """
    return len(M[0])


def sumar_dos_filas(matriz, fila_base, fila_objetivo):
    """
    Recibimos un array del que vamos a hacer fila_base+fila_objetivo y la vamos a dejar en fila_objetivo
    Los dos valores fila se pasan como entero y sera el numero de fila que queremos
    """
    # para cada elemento de la fila obtenemos su suma en Z2
    matriz[fila_objetivo][:] = [(x[0] + x[1]) % 2 for x in zip(matriz[fila_base], matriz[fila_objetivo])]


def sumar_dos_columnas(matriz, col_base, col_objetivo):
    """
    Recibimos un array del que vamos a hacer col_base+col_objetivo y la vamos a dejar en col_objetivo
    Los dos valores col se pasan como entero y sera el numero de columna que queremos
    """
    col_res = [(x[col_base] + x[col_objetivo]) % 2 for x in matriz]
    for i in range(num_filas(matriz)):
        matriz[i][col_objetivo] = col_res[i]


def cambiar_filas(matriz, fila1, fila2):
    """
    Tomo los valores de la fila1 y los pongo en la fila2, y al reves
    """
    filaAux = matriz[fila1]
    matriz[fila1] = matriz[fila2]
    matriz[fila2] = filaAux


def cambiar_columnas(matriz, columna1, columna2):
    """
    Tomo los valores de la columna1 y los pongo en la columna2, y al reves
    """
    # copio columna
    columnaAux = [x[columna1] for x in matriz]

    # voy elto a elto intercambiandolos
    i = 0
    for x in matriz:
        x[columna1] = x[columna2]
        x[columna2] = columnaAux[i]
        i = i + 1


def buscar_1(matriz, pos):
    """
    recibe una matriz y busca un uno a partir de una posicion recibida
    La posicion tiene que ser o una lista o una tupla
    """
    index = [-1, -1]

    for i in range(pos[0], num_filas(matriz)):
        for j in range(pos[1], num_columnas(matriz)):
            if matriz[i][j]:
                return [i, j]
    return index


def forma_normal_Smith(matriz):
    """
    Recibimos una matriz borde y calculamos su forma normal de Smith
    """
    pivote = [0, 0]
    while True:
        # miramos si hay un uno a partir del pivote (incluido)
        pos_1 = buscar_1(matriz, pivote)

        # si no hemos encontrado ningun 1 hemos acabado o porque hayamos llegado al final
        if pos_1 == [-1, -1]:
            return matriz

        # si no hay un 1 en la pos del pivote entonces cambiamos las posiciones -> cambiar fila y columna
        if pos_1 != pivote:
            cambiar_filas(matriz, pos_1[0], pivote[0])
            cambiar_columnas(matriz, pos_1[1], pivote[1])

        # si tenemos por derecha algun 1 lo quitamos sumando columnas
        for i in range(pivote[1] + 1, num_columnas(matriz)):
            # recorremos las columnas buscando un 1
            if matriz[pivote[0]][i] == 1:
                sumar_dos_columnas(matriz, pivote[1], i)
        # si tenemos algun 1 abajo lo quitamos sumando filas
        for j in range(pivote[0] + 1, num_filas(matriz)):
            # recorremos las filas buscando un 1
            if matriz[j][pivote[1]] == 1:
                sumar_dos_filas(matriz, pivote[0], j)

        # avanzamos el pivote
        pivote[0] += 1
        pivote[1] += 1
