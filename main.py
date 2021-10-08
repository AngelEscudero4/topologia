from Complejo import Complejo



ejemplos = (
    # Complejo([(0, 1, 2), (1, 3, 4), (0, 7, 9, 8), (6, 5, 7)]),
    # Complejo([(0, 1), (1, 3, 4), (4, 0, 7, 9, 8), (8, 6, 5)]),
    # Complejo([(0, 1, 2, 3), (1, 3, 4), (0, 7, 9, 8), (6, 5, 9)]),
    Complejo([(0, 1, 2), (2, 3), (3, 4)]),
    # Complejo([(0,), (1, 2)])
)

print('--------------------------------------------------------------------')
for j in ejemplos:
    print(j)
    print('Dimension: ', j.dim())
    print('Caras: ', j.getCaras())
    for i in range(j.dim() + 1):
        print('Caras dim ' + str(i) + ': ', j.getCarasDim(i))
    print('Estrella {2}: ', j.estrella((2,)))
    print('Caract de Euler: ', j.caract_euler())
    print('Componentes conexas: ', j.num_componentes_conexas())
    print('link: ', j.link((2,)))
    j.anadirSimplice([(1, 7), (1, 8)], 2.0)
    print(j.devolverPeso((1, 7)))
    print('--------------------------------------------------------------------')
