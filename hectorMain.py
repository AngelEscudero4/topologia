from Complejo import Complejo
from Complejo import getCarasDeSimplice

# EJEMPLO 1
# (1) Consideramos el 3-símplice
sc = Complejo([(0, 1, 2, 3)])
print(sc)

# (2) Conjunto de todas sus caras
print('(1) Caras: ', sc.getCaras())

# (3) Dimensión del símplice
print('(2) Dimension: ', sc.dim())

# (4 - 5 - 6 -7) Conjunto de caras agrupadas por su dimensión
for i in range(sc.dim() + 1):
    print('Caras dim ' + str(i) + ': ', sc.getCarasDim(i))

# (8) Característica de Euler
print('(3) Caract de Euler: ', sc.caract_euler())

# (9) Estrella de la arista (0,1)
print('(4) Estrella (0,1): ', sc.estrella((0, 1)))

# (10) Link de la arista (0,1)


# (11) Número de componentes conexas
print('(11) Componentes conexas: ', sc.num_componentes_conexas())


# EJEMPLO 2
# (12) Consideramos el 3-símplice
sc1 = Complejo()
print(sc1)

# (13) Conjunto de todas sus caras
print('(13) Caras: ', sc1.getCaras())

# (14) Dimensión del símplice
print('(14) Dimension: ', sc1.dim())

# (15) Estrella del vértice 0
print('(15) Estrella {0,1}: ', sc1.estrella([0, 1]))

# (16) Link del vértice 0

# (17) Característica de Euler
print('(17) Característica de Euler: ', sc1.caract_euler())

# (18) Número de componentes conexas
print('(18) Componentes conexas: ', sc1.num_componentes_conexas())

# EJEMPLO 3
# (19) Consideramos el 3-símplice
sc2 = Complejo([(0, 1), (1, 2, 3, 4), (4, 5), (5, 6), (4, 6), (6, 7, 8), (8, 9)])
print(sc2)

# (20) Conjunto de todas sus caras
print('(20) Caras: ', sc2.getCaras())

# (21) Dimensión del símplice
print('(21) Dimension: ', sc2.dim())

# (22) 1-Esqueleto

# (23) Estrella del vértice 4
print('(23) Estrella {0,1}: ', sc2.estrella((4,)))

# (24) Link del vértice 4

# (25) Característica de Euler
print('(24) Característica de Euler: ', sc2.caract_euler())

# (26) Número de componentes conexas
print('(25) Componentes conexas: ', sc2.num_componentes_conexas())