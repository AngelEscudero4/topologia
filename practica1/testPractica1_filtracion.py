from practica1.Complejo import Complejo

sc = Complejo([])
sc.anadirSimplice([(0, 1)], 1.0)
sc.anadirSimplice([(3, 4)], 3.0)
sc.anadirSimplice([(2, 3, 4)], 4.0)
sc.anadirSimplice([(1, 2), (2, 3), (2, 4)], 2.0)

print('(74) Caras: ', sc.getCaras())

K1 = sc.filtration(1.0)
K2 = sc.filtration(2.0)
K3 = sc.filtration(3.0)
K4 = sc.filtration(4.0)

print('(80) Caras filtracion 1.0: ', K1)
print('(81) Caras filtracion 2.0: ', K2)
print('(82) Caras filtracion 3.0: ', K3)
print('(83) Caras filtracion 4.0: ', K4)

print('(84) Complejo ordenado por pesos: ', sc.filtrationOrder())

print(sc.simplices)
print(sc.pesos)
