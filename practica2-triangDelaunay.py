import numpy as np
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import matplotlib.colors
from math import dist

# import matplotlib as mpl

"""
DUDA: ¿Sacar dentro de alphaComplejo coords de puntos o indexPuntos?
OJO: Mirar si al hacer dist saca distancia o distancia**2




Para la triangulacion nos devuelve los triangulos a partir de los puntos que forman los vertices aqui:
    (Del.simplices)
[[0 1 2], [0 1 3], ...]
Vamos a usar esos valores para luego obtener las coordenadas de esos puntos y obtener su 
circuncentro de forma numerica
    (points): -> nuestra variable con las coords de los puntos (se corresponden los indices con los de la lista anterior)

Nombre  -> Coords
punto 0 -> points[0]  
"""


# Diagrama de Voronoi
def alphaComplejo(r: float):
    """
    Dado un valor 'r' obtenemos el
    :param r:
    :return:
    """

    points = np.random.rand(10, 2)
    vor = Voronoi(points)
    # printeo voronoy y puntos
    fig = voronoi_plot_2d(vor, show_vertices=False, line_width=2, line_colors='red')
    plt.plot(points[:, 0], points[:, 1], 'ko')
    Del = Delaunay(points)
    print("SIMPLCES: ",
          Del.simplices)  # printea array de simplices formados por los puntos (indica su indice en el array de points)

    # plt.plot(vor.vertices[:, 0], vor.vertices[:, 1], 'bo') # mostrar los vertices interseccion entre triangulos

    # printeo triangulos y puntos con etiquetas para ver que se corresponde al indice
    # plt.triplot(points[:, 0], points[:, 1], Del.simplices)
    # plt.plot(points[:, 0], points[:, 1], 'o')
    # for j, p in enumerate(points):
    #     plt.text(p[0] - 0.01, p[1] + 0.01, j, ha='right')  # label the points
    # plt.show()

    print("PUNTOS: ", points)

    # Triangulacion de Delaunay
    c = np.ones(len(points))
    cmap = matplotlib.colors.ListedColormap("limegreen")
    plt.tripcolor(points[:, 0], points[:, 1], Del.simplices, c, edgecolor="k", lw=2, cmap=cmap)
    plt.plot(points[:, 0], points[:, 1], 'ko')
    plt.show()

    # Triangulación de Delaunay sobre el diagrama de Voronoi
    # fig = voronoi_plot_2d(vor, show_vertices=False, line_width=2, line_colors='blue')
    # c = np.ones(len(points))
    # cmap = matplotlib.colors.ListedColormap("limegreen")
    # plt.tripcolor(points[:, 0], points[:, 1], Del.simplices, c, edgecolor="k", lw=2, cmap=cmap)
    # plt.plot(points[:, 0], points[:, 1], 'ko')
    # plt.show()

    # los vertices se añaden al alphaComplejo
    alpha_complejo = []
    for point in points:
        alpha_complejo.append(list(point))

    for simplice in Del.simplices:

        # extraer los tres puntos del triangulo
        trianglePoints = []
        for indexPoint in simplice:
            trianglePoints.append(list(points[indexPoint]))

        # calcular circuncentro
        circuncentro = circumcenter(trianglePoints)
        circunradio = dist(trianglePoints[0], circuncentro)
        if r >= circunradio:
            alpha_complejo.append(trianglePoints)

        # definir las aristas
        arista01 = [trianglePoints[0], trianglePoints[1]]
        arista12 = [trianglePoints[1], trianglePoints[2]]
        arista02 = [trianglePoints[0], trianglePoints[2]]

        # calculamos el punto medio para cada una de las aristas
        for arista in [arista01, arista12, arista02]:
            medio = puntoMedio(arista)
            radio = dist(medio, arista[0])
            hayPuntoDentro = False

            for point in points:
                if dist(medio, point) < radio:
                    alpha_complejo.append(arista)
                    hayPuntoDentro = True
                    continue
            if hayPuntoDentro and 2 * r >= dist(arista[0], arista[1]):
                alpha_complejo.append(arista)


def puntoMedio(arista: list):
    return [arista[0][0] + arista[1][0], arista[0][1] + arista[1][1]]


def circumcenter(trianglePoints: list):
    """
    Partiendo de una lista con tres puntos de la forma (x,y), obtenemos el centro de
    la circunferencia que pasa por los tres

    :param trianglePoints: [ [ax, ay], [bx, by], [cx, cy] ]
    :return: [circuncentro.x, circuncentro.y]
    """
    [ax, ay] = trianglePoints[0]
    [bx, by] = trianglePoints[1]
    [cx, cy] = trianglePoints[2]

    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
    return [ux, uy]


# def barycentre(points: list):
#     """
#
#     Dada una lista de puntos en coords (x,y) nos devuelve el baricentro de la lista
#     :imput [[X1,Y1],[X2,Y2],...]
#     :return [BarX, BarY]
#     """
#     bar = [0,0]
#     #aux para calcular la suma de las coords
#     sum = [0,0]
#     for eachPoint in points:
#         #coords x
#         sum[0] = sum[0] + eachPoint[0]
#         #coords y
#         sum[1] = sum[1] + eachPoint[1]
#     bar[0] = sum[0] / len(points)
#     bar[1] = sum[1] / len(points)
#
#     return bar


# calcular delaunay meter arrays a formato de simplices y ordenamos lexicografico -> lo metemos como cocmplejo
# simplicial
# Crear nuevo complejo simplicial vacio -> añadir vertces, recorrer triang e introducir con los pesos del
# critero y despues aristas

# Luego representacion grafica

# Añadir verts con peso 0
# Añadir triang con peso (lo da algoritmo)
# Luego aristas (peso algoritmo)

# Asi consigo triang de delaunay con pesos (son los circunradios que los debo poder sacar de alguna de las clases)

alphaComplejo(10000000)
