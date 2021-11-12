import practica1.Complejo
import numpy as np


def sumar_dos_filas(array, fila_base, fila_objetivo):
    """
    Recibimos un array del que vamos a hacer fila_base+fila_objetivo y la vamos a dejar en fila_objetivo
    Los dos valores fila se pasan como entero y sera el numero de fila que queremos
    """
    fila_aux = np.zeros(1,len(array[0]))
    #para cada elemento de la fila obtenemos su suma en Z2
    for elem_fila in range(len(array[0])):
        fila_aux[1][elem_fila] = sumar_elems_z2(array(fila_base, elem_fila), array(fila_objetivo, elem_fila))
    array[fila_objetivo]=fila_aux
    return array


def sumar_dos_columnas(array, col_base, col_objetivo):
    """
    Recibimos un array del que vamos a hacer col_base+col_objetivo y la vamos a dejar en col_objetivo
    Los dos valores col se pasan como entero y sera el numero de columna que queremos
    """
    col_aux = np.zeros(len(array[:][0]))
    #para cada elemento de la col obtenemos su suma en Z2
    for elem_col in range(len(array[:][0])):
        col_aux[elem_col][1] = sumar_elems_z2(array(elem_col, col_base), array(elem_col, col_objetivo))
    array[:][col_objetivo]=col_aux[:]
    return array

def sumar_elems_z2(elem1, elem2):
    """
    Dados dos elementos en Z2 devuelve su suma en Z2
    """
    return  (elem1 + elem2) % 2

def forma_normal_Smith(matriz):
    """
    Recibimos una matriz borde y valculamos su forma normal de Smith
    """
    forma_NS = None
    #si a11 = 0 buscamos un elemento que sea 1 y los cambiamos de posicion

    #si tenemos por debajo algun 1 lo quitamos sumando filas

    #si tenemos a la dcha algun 1 lo quitamos sumando columnas

    #cambiamos al siguiente pivote y volvemos a empezar

    return forma_NS

def buscar_1(matriz, pos):
    """
    recibe una matriz y busca un uno a partir de una posicion recibida
    La posicion tiene que ser o una lista o una tupla
    """
    pos_actual = pos
    index =[-1, -1]

    for i in range(pos[0],len(matriz)):
        for j in range(pos[1], len(matriz[0])):
            if matriz[i,j]:
                return (i,j)
    return index