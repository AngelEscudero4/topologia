import diagramas
from practica1.Complejo import Complejo
import numpy as np


def imprimir_matriz(matriz):
    print(np.array(matriz))
    print("---------------------------------------------------------------------")


# complejo = Complejo([(1, 2, 3), (3, 4, 5), (0, 5, 6)])
# complejo = Complejo([(1, 2, 3)])
complejo = Complejo([])
complejo.anadirSimplice([(1,), (2,), (3,)], 0)
complejo.anadirSimplice([(1,2)], 1)
complejo.anadirSimplice([(2,3)], 2)
complejo.anadirSimplice([(1,3)], 2.4)
complejo.anadirSimplice([(1,2,3)], 3)

# complejo.anadirSimplice([(2,4,5)], 2)
# complejo.anadirSimplice([(5,6,7)], 3)



diagramas.diagrama_persistencia(complejo)
diagramas.diagrama_barras(complejo)
