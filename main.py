from Complejo import Complejo
from itertools import combinations

from Complejo import Complejo


ejemplo_1 = Complejo([[0,1,2],[1,3,4],[0,7,9,8],[6,5]])

print('Dimension: ', ejemplo_1.dim())
print('Caras: ', ejemplo_1.getCaras())
for i in range(3):
    print('Caras dim'+str(i+1)+': ', ejemplo_1.getCarasDim(i+1))
