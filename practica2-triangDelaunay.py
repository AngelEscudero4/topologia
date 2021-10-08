import numpy as np
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib as mpl

points = np.random.rand(10, 2)
vor = Voronoi(points)
fig = voronoi_plot_2d(vor, show_vertices=False, line_width=2, line_colors='red')
plt.plot(points[:, 0], points[:, 1], 'ko')
Del = Delaunay(points)
# print(Del)
print(Del.simplices)

c = np.ones(len(points))
cmap = matplotlib.colors.ListedColormap("limegreen")
plt.tripcolor(points[:, 0], points[:, 1], Del.simplices, c, edgecolor="k", lw=2, cmap=cmap)
plt.plot(points[:, 0], points[:, 1], 'ko')
plt.show()

fig = voronoi_plot_2d(vor, show_vertices=False, line_width=2, line_colors='blue')
c = np.ones(len(points))
cmap = matplotlib.colors.ListedColormap("limegreen")
plt.tripcolor(points[:, 0], points[:, 1], Del.simplices, c, edgecolor="k", lw=2, cmap=cmap)
plt.plot(points[:, 0], points[:, 1], 'ko')
plt.show()


# calcular delaunay
# meter arrays a formato de simplices y ordenamos lexicografico -> lo metemos como cocmplejo simplicial
# Crear nuevo complejo simplicial vacio -> añadir vertces, recorrer triang e introducir con los pesos del critero y despues aristas

# Luego representacion grafica


# Añadir verts con peso 0
# Añadir triang con peso (lo da algoritmo)
# Luego aristas (peso algoritmo)

# Asi consigo triang de delaunay con pesos (son los circunradios que los debo poder sacar de alguna de las clases)
