from practica1.Complejo import Complejo

# EJEMPLO 1
sc = Complejo([(0, 1, 2, 3)])
print(sc.matriz_borde(1))
print(sc.matriz_borde(2))
print(sc.matriz_borde(3))

print(sc.Betti_number(0), sc.Betti_number(1), sc.Betti_number(2), sc.Betti_number(3))

# EJEMPLO 2
sc1 = Complejo(list(sc.getCarasDim(2)))  # dos esfera
print(sc1.Betti_number(0), sc1.Betti_number(1), sc1.Betti_number(2))

# EJEMPLO 3
sc = Complejo([(0, 1), (1, 2, 3, 4), (4, 5), (5, 6), (4, 6), (6, 7, 8), (8, 9)])
print(sc.matriz_borde(1))
print(sc.matriz_borde(2))
print(sc.matriz_borde(3))
print(sc.Betti_number(0), sc.Betti_number(1), sc.Betti_number(2), sc.Betti_number(3))
