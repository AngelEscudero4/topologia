from practica1.Complejo import Complejo

'''
----------------------------------------------------------------------
----------------------------------------------------------------------
----------------------------------------------------------------------
                            PRACTICA 1
----------------------------------------------------------------------
----------------------------------------------------------------------
----------------------------------------------------------------------
'''

sc = Complejo([])
sc.anadirSimplice([(0, 1)], 1.0)
sc.anadirSimplice([(1, 2), (2, 3), (2, 4)], 2.0)
sc.anadirSimplice([(3, 4)], 3.0)
sc.anadirSimplice([(2, 3, 4)], 4.0)

print('(74) Caras: ', sc.getCaras())

K1 = sc.filtration(1.0)
K2 = sc.filtration(2.0)
K3 = sc.filtration(3.0)
K4 = sc.filtration(4.0)

print('(80) Caras: ', K1)
print('(81) Caras: ', K2)
print('(82) Caras: ', K3)
print('(83) Caras: ', K4)

# NO ENTIENDO COMO LO ESTAS ORDENANDO EN EL PDF SI LOS METES CON EL PESO ORDENADO TAL CUAL
# sc.filtrationorder

print('(84) Caras: ', sc.filtrationOrder())

print(sc.simplices)
print(sc.pesos)
