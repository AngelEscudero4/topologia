from practica3.homologia import num_filas


def cambiarColumnas(matriz, columna1, columna2):
    """
    Tomo los valores de la fila1 y los pongo en la fila2, y al reves
    """
    columnaAux = [0]*num_filas(matriz)
    matriz[:][columna1] = matriz[:][columna2]
    matriz[:][columna2] = columnaAux

    print(matriz)


matriz = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
cambiarColumnas(matriz, 1, 2)
