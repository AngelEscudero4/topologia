from Complejo import Complejo, esCara
from itertools import combinations

from Complejo import Complejo

ejemplo_1 = Complejo([[0, 1, 2], [1, 3, 4], [0, 7, 9, 8], [6, 5, 7]])
ejemplo_2 = Complejo([[0, 1], [1, 3, 4], [4, 0, 7, 9, 8], [8, 6, 5]])
ejemplo_3 = Complejo([[0, 1, 2, 3], [1, 3, 4], [0, 7, 9, 8], [6, 5, 9]])
ej_diapos = Complejo([[0, 1, 2], [2, 3], [3, 4]])

print('--------------------------------------------------------------------')
for j in [ejemplo_1, ejemplo_2, ejemplo_3, ej_diapos]:
    print(j)
    print('Dimension: ', j.dim())
    print('Caras: ', j.getCaras())
    for i in range(3):
        print('Caras dim' + str(i + 1) + ': ', j.getCarasDim(i + 1))
    print('Estrella 2: ', j.estrella([2]))
    print('--------------------------------------------------------------------')
