from Complejo import Complejo, getCarasDeSimplice#, esCara
from itertools import combinations

from Complejo import Complejo

ejemplos=[
 Complejo([[0, 1, 2], [1, 3, 4], [0, 7, 9, 8], [6, 5, 7]]),
 Complejo([[0, 1], [1, 3, 4], [4, 0, 7, 9, 8], [8, 6, 5]]),
 Complejo([[0, 1, 2, 3], [1, 3, 4], [0, 7, 9, 8], [6, 5, 9]]),
 Complejo([[0, 1, 2], [2, 3], [3, 4]])
]

print('--------------------------------------------------------------------')
for j in ejemplos:
    print(j)
    print('Dimension: ', j.dim())
    print('Caras: ', j.getCaras())
    for i in range(j.dim()+1):
        print('Caras dim ' + str(i) + ': ', j.getCarasDim(i))
    print('Estrella 2: ', j.estrella([2]))
    print('--------------------------------------------------------------------')
print(getCarasDeSimplice([1,2,3]))