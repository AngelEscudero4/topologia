from Complejo import Complejo
from Complejo import getCarasDeSimplice

complex = Complejo([[0, 1, 2, 3]])

print(complex)
print('Caras: ', complex.getCaras())
print('Dimension: ', complex.dim())
for i in range(complex.dim() + 1):
    print('Caras dim ' + str(i) + ': ', complex.getCarasDim(i))
print('Caract de Euler: ', complex.caract_euler())
print('Estrella {0,1}: ', complex.estrella([0, 1]))
# FALLA ESTRELLA Y FALTA EL LINK
print('Componentes conexas: ', complex.num_componentes_conexas())
