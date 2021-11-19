from practica1.Complejo import Complejo
from practica3.betti_incremental import betti_incremental

# Ejemplo del algoritmo Betti Incremental

sc = Complejo([(0, 1), (4, 5), (5, 6), (4, 6), (8, 9)])
# deberia dar b0 = 1, b1 = 1
print(betti_incremental(sc))
