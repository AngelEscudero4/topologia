import practica1.Complejo
import numpy as np


def sumar_dos_filas(array, fila_base, fila_objetivo):
    """
    Recibimos un array del que vamos a hacer fila_base+fila_objetivo y la vamos a dejar en fila_objetivo
    Los dos valores fila se pasan como entero y sera el numero de fila que queremos
    """
    fila_aux = np.zeros(1,len(array[0]))
    #para cada elemento de la fila obtenemos su suma en Z2
    for elem_fila in len(array[0]):
        fila_aux[1][elem_fila] = sumar_elems_z2(array(fila_base, elem_fila), array(fila_objetivo, elem_fila))
    array[fila_objetivo]=fila_aux
    return array


def sumar_dos_columnas(array, col_base, col_objetivo):
    """
    Recibimos un array del que vamos a hacer col_base+col_objetivo y la vamos a dejar en col_objetivo
    Los dos valores col se pasan como entero y sera el numero de columna que queremos
    """
    col_aux = np.zeros(len(array[:][0], 1))
    #para cada elemento de la col obtenemos su suma en Z2
    for elem_col in len(array[:][0]):
        col_aux[elem_col][1] = sumar_elems_z2(array(elem_col, col_base), array(elem_col, col_objetivo))
    array[:][col_objetivo]=col_aux[:]
    return array

def sumar_elems_z2(elem1, elem2):
    """
    Dados dos elementos en Z2 devuelve su suma en Z2
    """
    res = None
    #ambos 1
    if elem1 and elem2:
        res = 0
    #xor -> uno de ellos es 1 y el otro 0
    elif elem1 ^ elem2:
        res = 1
    #ambos 0
    else:
        res = 0
    return res

def forma_normal_Smith(matriz):
    """
    Recibimos una matriz borde y valculamos su forma normal de Smith
    """
    forma_NS = None
    return forma_NS

