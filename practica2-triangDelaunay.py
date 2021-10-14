import numpy as np
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import matplotlib.colors
from math import dist
from Complejo import Complejo

# import matplotlib as mpl

"""
DUDA: ¿Sacar dentro de alphaComplejo coords de puntos o indexPuntos?
OJO: Mirar si al hacer dist saca distancia o distancia**2




Para la triangulacion nos devuelve los triangulos a partir de los puntos que forman los vertices aqui:
    (simplicesDelaunay)
[[0 1 2], [0 1 3], ...]
Vamos a usar esos valores para luego obtener las coordenadas de esos puntos y obtener su 
circuncentro de forma numerica
    (points): -> nuestra variable con las coords de los puntos (se corresponden los indices con los de la lista anterior)

Nombre  -> Coords
punto 0 -> points[0]  
"""


def filtracionAlphaComplejo(r: float, alpha_complejo: Complejo):
    return alpha_complejo.filtration(r)



# Diagrama de Voronoi
def alphaComplejo(points):
    """
    :return:
    """

    vor = Voronoi(points)
    # printeo voronoy y puntos
    fig = voronoi_plot_2d(vor, show_vertices=False, line_width=2, line_colors='red')
    plt.plot(points[:, 0], points[:, 1], 'ko')
    Del = Delaunay(points)
    simplicesDelaunay = Del.simplices
    print("------------------------------------------------------------")
    print(simplicesDelaunay)
    print("------------------------------------------------------------")

    #ordenar lista de listas
    simplicesDelaunay = ordenar(simplicesDelaunay)
    print("------------------------------------------------------------")
    print(simplicesDelaunay)
    print("------------------------------------------------------------")


    print("SIMPLCES: ",
          simplicesDelaunay)  # printea array de simplices formados por los puntos (indica su indice en el array de points)

    # plt.plot(vor.vertices[:, 0], vor.vertices[:, 1], 'bo') # mostrar los vertices interseccion entre triangulos

    # printeo triangulos y puntos con etiquetas para ver que se corresponde al indice
    # plt.triplot(points[:, 0], points[:, 1], simplicesDelaunay)
    # plt.plot(points[:, 0], points[:, 1], 'o')
    # for j, p in enumerate(points):
    #     plt.text(p[0] - 0.01, p[1] + 0.01, j, ha='right')  # label the points
    # plt.show()

    print("PUNTOS: ", points)

    # Triangulacion de Delaunay
    c = np.ones(len(points))
    cmap = matplotlib.colors.ListedColormap("limegreen")
    plt.tripcolor(points[:, 0], points[:, 1], simplicesDelaunay, c, edgecolor="k", lw=2, cmap=cmap)
    plt.plot(points[:, 0], points[:, 1], 'ko')
    plt.show()

    # Triangulación de Delaunay sobre el diagrama de Voronoi
    # fig = voronoi_plot_2d(vor, show_vertices=False, line_width=2, line_colors='blue')
    # c = np.ones(len(points))
    # cmap = matplotlib.colors.ListedColormap("limegreen")
    # plt.tripcolor(points[:, 0], points[:, 1], simplicesDelaunay, c, edgecolor="k", lw=2, cmap=cmap)
    # plt.plot(points[:, 0], points[:, 1], 'ko')
    # plt.show()

    # los vertices se añaden al alphaComplejo
    alphaComplejo = Complejo([])

    for index, point in enumerate(points):
        alphaComplejo.anadirSimplice([(index,)], 0)

    for simplice in simplicesDelaunay:

        # extraer los tres puntos del triangulo
        trianglePointsCoords = []
        puntos = []
        for indexPoint in simplice:
            trianglePointsCoords.append(list(points[indexPoint]))
            puntos.append(indexPoint)

        trianglePointsTuplesIndice = tuple(puntos)

        # calcular circuncentro
        circuncentro = circumcenter(trianglePointsCoords)
        circunradio = dist(trianglePointsCoords[0], circuncentro)

        alphaComplejo.anadirSimplice([trianglePointsTuplesIndice], circunradio)

        # definir las aristas
        arista01 = [trianglePointsCoords[0], trianglePointsCoords[1]]
        arista12 = [trianglePointsCoords[1], trianglePointsCoords[2]]
        arista02 = [trianglePointsCoords[0], trianglePointsCoords[2]]

        arista01Tuples = (trianglePointsTuplesIndice[0], trianglePointsTuplesIndice[1])
        arista12Tuples = (trianglePointsTuplesIndice[1], trianglePointsTuplesIndice[2])
        arista02Tuples = (trianglePointsTuplesIndice[0], trianglePointsTuplesIndice[2])

        # calculamos el punto medio para cada una de las aristas
        for (arista, aristaTupla) in [(arista01, arista01Tuples), (arista12, arista12Tuples),
                                      (arista02, arista02Tuples)]:
            medio = puntoMedio(arista)
            radio = dist(medio, arista[0])
            hayPuntoDentro = False

            for point in points:
                if dist(medio, point) < radio:
                    # caso arista ya añadida
                    if aristaTupla in alphaComplejo.simplices:
                        # actualizamos el valor del peso
                        if alphaComplejo.pesos[alphaComplejo.simplices.index(aristaTupla)] > circunradio:
                            alphaComplejo.pesos[alphaComplejo.simplices.index(aristaTupla)] = circunradio
                    else:
                        alphaComplejo.anadirSimplice([aristaTupla], circunradio)
                    hayPuntoDentro = True
                    break
            if not hayPuntoDentro:
                # añadir arista -> quedarse con el menor peso
                if aristaTupla in alphaComplejo.simplices:
                    if alphaComplejo.pesos[alphaComplejo.simplices.index(aristaTupla)] > 2 * radio:
                        alphaComplejo.pesos[alphaComplejo.simplices.index(aristaTupla)] = 2 * radio
                else:
                    alphaComplejo.anadirSimplice([aristaTupla], 2 * radio)

    return alphaComplejo


def puntoMedio(arista: list):
    return [(arista[0][0] + arista[1][0]) / 2, (arista[0][1] + arista[1][1]) / 2]


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


def ordenar(listaDeListas):
    for eachLista in listaDeListas:
        eachLista.sort()
    listaDeListas.sort()
    return listaDeListas



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

puntos = np.random.rand(10, 2)  # añadir como param
complejo = alphaComplejo(puntos)
print(complejo)
