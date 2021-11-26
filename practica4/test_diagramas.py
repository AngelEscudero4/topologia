import diagramas
from practica1.Complejo import Complejo
import numpy as np


def imprimir_matriz(matriz):
    print(np.array(matriz))
    print("---------------------------------------------------------------------")


# complejo = Complejo([(1, 2, 3), (3, 4, 5), (0, 5, 6)])
# complejo = Complejo([(1, 2, 3)])
complejo = Complejo([])
complejo.anadirSimplice([(1,2,3)], 1)
complejo.anadirSimplice([(2,4,5)], 2)
complejo.anadirSimplice([(5,6,7)], 3)


matriz_borde_gen = diagramas.matriz_borde_generalizada(complejo)

imprimir_matriz(matriz_borde_gen)

matriz_borde_gen = diagramas.algoritmo_emparejamiento_nacimiento_muerte(matriz_borde_gen)

imprimir_matriz(matriz_borde_gen)

emparejamientos = diagramas.get_emparejamientos(matriz_borde_gen)
print("low-columna", emparejamientos)

# cogemos los simplices ordenados --> OJO QUE TIENEN QUE COINCIDIR CON LOS DE maatriz_borde_gen
simplices = complejo.getCaras()
simplices = list(simplices)
# ahora vamos a tener que ordenarlos por longitud (habria que mirar por peso tmbn)
simplices.sort(key=len)

diagramas.diagrama_barras(complejo, emparejamientos, simplices)
