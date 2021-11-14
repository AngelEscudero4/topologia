from practica1.Complejo import Complejo
import numpy as np


def imprimir_matriz(matriz):
    print("------------------------------------")
    print(np.array(matriz))
    print("------------------------------------")


# EJEMPLO 1
sc = Complejo([(0, 1, 2, 3)])
imprimir_matriz(sc.matriz_borde(1))
imprimir_matriz(sc.matriz_borde(2))
imprimir_matriz(sc.matriz_borde(3))

print("Nºs de Betti del tetraedro: ", sc.Betti_number(0), sc.Betti_number(1), sc.Betti_number(2),
      sc.Betti_number(3))

# EJEMPLO 2
sc1 = Complejo(list(sc.getCarasDim(2)))  # dos-esfera
print("Nºs de Betti del borde del tetraedro: ", sc1.Betti_number(0), sc1.Betti_number(1), sc1.Betti_number(2))

# EJEMPLO 3
sc = Complejo([(0, 1), (1, 2, 3, 4), (4, 5), (5, 6), (4, 6), (6, 7, 8), (8, 9)])
imprimir_matriz(sc.matriz_borde(1))
imprimir_matriz(sc.matriz_borde(2))
imprimir_matriz(sc.matriz_borde(3))
print(sc.Betti_number(0), sc.Betti_number(1), sc.Betti_number(2), sc.Betti_number(3))

# TORO
sc2 = Complejo([(1, 2, 4), (2, 4, 5), (2, 3, 5), (3, 5, 6), (1, 3, 6), (1, 4, 6),
                (4, 5, 7), (5, 7, 8), (5, 6, 8), (6, 8, 9), (4, 6, 9), (4, 7, 9), (1, 7, 8), (1, 2, 8),
                (2, 8, 9), (2, 3, 9), (3, 7, 9), (1, 3, 7)])
imprimir_matriz(sc2.matriz_borde(1))
imprimir_matriz(sc2.matriz_borde(2))
imprimir_matriz(sc2.matriz_borde(3))
print("Nºs de Betti del borde del toro: ", sc2.Betti_number(0), sc2.Betti_number(1), sc2.Betti_number(2))

# FALTA LA OTRA TRIANGULACION DEL TORO
