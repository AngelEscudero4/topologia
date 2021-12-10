import math

import matplotlib.pyplot as plt

import diagramas
import numpy as np

from practica2.triangDelaunay import alphaComplejo


def imprimir_matriz(matriz):
    print(np.array(matriz))
    print("---------------------------------------------------------------------")


pi = math.pi


def PointsInCircum(r, n=100):
    return [(math.cos(2 * pi / n * x) * r, math.sin(2 * pi / n * x) * r) for x in range(0, n + 1)]


def ruido(points):
    puntos_diagrama = np.array(points)
    plt.scatter(puntos_diagrama[:, 0], puntos_diagrama[:, 1], color="blue")
    plt.plot()
    noise = np.random.normal(0, 0.1, 101)
    lista = []
    for i in range(len(points)):
        lista.append([points[i][0] + noise[i], points[i][1] + noise[i]])
    # puntos_diagrama = np.array(signal)
    lista = np.array(lista)
    plt.scatter(lista[:, 0], lista[:, 1], color="red")
    plt.show()
    return lista


puntos = np.random.rand(100, 2)
# puntos = np.array([[0.12483073, 0.48058688],
#                    [0.66785431, 0.88640198],
#                    [0.7508529, 0.87369865],
#                    [0.64280474, 0.3082798],
#                    [0.5011471, 0.64743215]]),
#                    [0.63793728, 0.97318851]])
#
#
# puntos = np.array([[0.03653114, 0.15089326],
#                    [0.15831359, 0.89080055],
#                    [0.03897906, 0.15394904],
#                    [0.8451469, 0.02852358],
#                    [0.69744539, 0.33121205],
#                    [0.94312824, 0.48085139]])
print("------------------------------------------")
print("------------------------------------------")
print("------------------------------------------")
print(puntos)
print("------------------------------------------")
print("------------------------------------------")
print("------------------------------------------")

# puntos = ruido(PointsInCircum(1))


complejo = alphaComplejo(puntos)

diagramas.diagrama_persistencia(complejo)
# diagramas.diagrama_barras(complejo)

