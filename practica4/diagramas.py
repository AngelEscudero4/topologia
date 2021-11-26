from practica1 import Complejo
import numpy as np
from practica3 import homologia


def matriz_borde_generalizada(complejo: Complejo):
    """
    Dado un complejo simplicial calculamos su matriz borde generalizada
    *** MATRIZ [FILAS][COL] ***
    """
    # primero sacamos todos los simplices posibles
    simplices = complejo.getCaras()
    # ahora vamos a tener que ordenarlos por longitud (habria que mirar por peso tmbn)
    simplices.sort(key=len)
    # ahora tenemos que hacer la matriz de incidencia
    matriz = np.zeros(len(simplices), len(simplices))
    matriz = matriz.tolist()
    # hay que poner un 1 en la casilla [i][j] si el simplice_dim_p1[i] es cara de simplice_dim_p[j]
    for i in range(homologia.num_filas(matriz)):
        for j in range(homologia.num_columnas(matriz)):
            if len(simplices[i]) == len(simplices[j]) - 1 and Complejo.esCara(simplices[i], simplices[j]):
                matriz[i][j] = 1
    return matriz


def algoritmo_emparejamiento_nacimiento_muerte_y_otras_cosas_que_todavia_no_hemos_demostrado_que_funcionan_pero_acabaremos_demostrando(
        matriz):
    """
    Recibida una matriz vamos a calculas los emparejamientos nacimiento-muerte
    """
    # dada una columna sacamos su low()
    # miramos en las columnas de su izqda y si tienen el mismo low borramos ese low en la de la izqda
    for i in range(homologia.num_columnas(matriz)):
        index_low = get_low(get_columna(matriz, i))
        # si existe low en esa columna
        if index_low != -1:
            # borramos los low iguales de columnas anteriores
            for otro_i in range(i):
                # si tienen el mismo low
                if get_low(get_columna(matriz,otro_i)) == index_low:
                    # sumamos las dos columnas
                    homologia.sumar_dos_columnas(matriz, index_low, otro_i)

def get_low(col):
    """
    Recibimos una columna y calculamos su 1 mas abajo.
    Devolvemos su indice.
    """
    indice = -1
    for i in range(len(col)):
        if col[i] == 1:
            indice = i
    return indice


def get_columna(matriz, indice):
    return [x[indice] for x in matriz]

