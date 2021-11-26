import diagramas
from practica1.Complejo import Complejo
import numpy as np


def imprimir_matriz(matriz):
    print(np.array(matriz))
    print("---------------------------------------------------------------------")


complejo = Complejo([(1, 2, 3), (3, 4, 5), (0, 5, 6)])
# complejo = Complejo([(1, 2, 3)])

matriz_borde_gen = diagramas.matriz_borde_generalizada(complejo)

imprimir_matriz(matriz_borde_gen)

imprimir_matriz(diagramas.algoritmo_emparejamiento_nacimiento_muerte(matriz_borde_gen))

