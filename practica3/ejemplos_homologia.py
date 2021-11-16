from practica1.Complejo import Complejo
import numpy as np


def imprimir_matriz(matriz):
    print(np.array(matriz))
    print("---------------------------------------------------------------------")


# EJEMPLO 1 (Tetraedro)
print("EJEMPLO 1")
sc = Complejo([(0, 1, 2, 3)])

print("Matriz borde 1:")
imprimir_matriz(sc.matriz_borde(1))

print("Matriz borde 2:")
imprimir_matriz(sc.matriz_borde(2))

print("Matriz borde 3:")
imprimir_matriz(sc.matriz_borde(3))

print("Nºs de Betti del tetraedro: ", sc.Betti_number(0), sc.Betti_number(1), sc.Betti_number(2), sc.Betti_number(3))
print("---------------------------------------------------------------------")

# EJEMPLO 2 (2-Esfera)
print("EJEMPLO 2")
sc1 = Complejo(list(sc.getCarasDim(2)))

print("Nºs de Betti de la 2-esfera: ", sc1.Betti_number(0), sc1.Betti_number(1), sc1.Betti_number(2))
print("---------------------------------------------------------------------")

# EJEMPLO 3
print("EJEMPLO 3")
sc = Complejo([(0, 1), (1, 2, 3, 4), (4, 5), (5, 6), (4, 6), (6, 7, 8), (8, 9)])

print("Matriz borde 1:")
imprimir_matriz(sc.matriz_borde(1))

print("Matriz borde 2:")
imprimir_matriz(sc.matriz_borde(2))

print("Matriz borde 3:")
imprimir_matriz(sc.matriz_borde(3))

print("Nºs de Betti: ",sc.Betti_number(0), sc.Betti_number(1), sc.Betti_number(2), sc.Betti_number(3))
print("---------------------------------------------------------------------")

# EJEMPLO 4
print("EJEMPLO 4")
sc1 = Complejo(list(sc.getCarasDim(1)))

print("Nºs de Betti: ", sc1.Betti_number(0), sc1.Betti_number(1))
print("---------------------------------------------------------------------")

# EJEMPLO 5
print("EJEMPLO 5")
sc = Complejo([(0,1,2),(2,3),(3,4)])

print("Matriz borde 1:")
imprimir_matriz(sc.matriz_borde(1))

print("Matriz borde 2:")
imprimir_matriz(sc.matriz_borde(2))

print("Números de Betti: ", sc.Betti_number(0), sc.Betti_number(1), sc.Betti_number(2))
print("---------------------------------------------------------------------")

# EJEMPLO 6
print("EJEMPLO 6")
sc = Complejo([(1,2,4),(1,3,6),(1,4,6),(2,3,5),(2,4,5),(3,5,6)])

print("Matriz borde 1:")
imprimir_matriz(sc.matriz_borde(1))

print("Matriz borde 2:")
imprimir_matriz(sc.matriz_borde(2))

print("Números de Betti: ", sc.Betti_number(0), sc.Betti_number(1), sc.Betti_number(2))
print("---------------------------------------------------------------------")

# EJEMPLO 7
print("EJEMPLO 7")
sc1 = Complejo(list(sc.getCarasDim(1)))

print("Nºs de Betti: ", sc1.Betti_number(0), sc1.Betti_number(1))
print("---------------------------------------------------------------------")

# EJEMPLO 8
print("EJEMPLO 8")
sc = Complejo([(1, 2, 4), (2, 4, 5), (2, 3, 5), (3, 5, 6), (1, 3, 6), (1, 4, 6),
                (4, 5, 7), (5, 7, 8), (5, 6, 8), (6, 8, 9), (4, 6, 9), (4, 7, 9), (1, 7, 8), (1, 2, 8),
                (2, 8, 9), (2, 3, 9), (3, 7, 9), (1, 3, 7)])

print("Matriz borde 1:")
imprimir_matriz(sc.matriz_borde(1))

print("Matriz borde 2:")
imprimir_matriz(sc.matriz_borde(2))

print("Nºs de Betti del borde del toro: ", sc.Betti_number(0), sc.Betti_number(1), sc.Betti_number(2))
print("---------------------------------------------------------------------")

# FALTA LA OTRA TRIANGULACION DEL TORO

# EJEMPLO 8 (hay dos 8 XD)
print("EJEMPLO 8")
sc1 = Complejo(list(sc.getCarasDim(1)))

print("Nºs de Betti: ", sc1.Betti_number(0), sc1.Betti_number(1))
print("---------------------------------------------------------------------")

# EJEMPLO 9
print("EJEMPLO 9")
sc = Complejo([(1,2,6), (2,3,4), (1,3,4), (1,2,5), (2,3,5), (1,3,6),(2,4,6), (1,4,5), (3,5,6), (4,5,6)])

print("Matriz borde 1:")
imprimir_matriz(sc.matriz_borde(1))

print("Matriz borde 2:")
imprimir_matriz(sc.matriz_borde(2))

print("Nºs de Betti: ", sc.Betti_number(0), sc.Betti_number(1), sc.Betti_number(2))
print("---------------------------------------------------------------------")

# EJEMPLO 10
print("EJEMPLO 10")
sc = Complejo([(0,), (1,), (2,3), (4,5), (5,6), (4,6), (6,7,8,9)])

print("Matriz borde 1:")
imprimir_matriz(sc.matriz_borde(1))

print("Matriz borde 2:")
imprimir_matriz(sc.matriz_borde(2))

print("Nºs de Betti: ", sc.Betti_number(0), sc.Betti_number(1), sc.Betti_number(2), sc.Betti_number(3))
print("---------------------------------------------------------------------")
