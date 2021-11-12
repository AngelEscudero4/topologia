import practica1.Complejo
import numpy as np


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
    # si a11 = 0 buscamos un elemento que sea 1 y los cambiamos de posicion

    # si tenemos por debajo algun 1 lo quitamos sumando filas

    # si tenemos a la dcha algun 1 lo quitamos sumando columnas

    # cambiamos al siguiente pivote y volvemos a empezar

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
            if matriz[i, j]:
                return (i, j)
    return index
