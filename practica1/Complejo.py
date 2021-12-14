from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

import practica3.homologia as hom


class Complejo:
    """
    TIPO DE DATOS:
    - Complejo Simplicial --> [simplices] - [peso del simplice correspondiente]
    - Simplice --> Tup

    Para crear un complejo:

    1) SIN pesos --> Poner simplices maximales
    complejo = Complejo([(0, 1), (1, 2, 3, 4), (4, 5), (5, 6), (4, 6), (6, 7, 8), (8, 9)]) --> Se crea con pesos 0

    ------------------------------

    2) CON pesos
    sc = Complejo([])
    sc.anadirSimplice([(0, 1)], 1.0)
    sc.anadirSimplice([(1, 2), (2, 3), (2, 4)], 2.0)
    sc.anadirSimplice([(3, 4)], 3.0)
    sc.anadirSimplice([(2, 3, 4)], 4.0)

    """

    def __init__(self, maximal_simplice_list: list[tuple]):
        """
        Recibimos una lista con los simplices maximales (tuplas).
        Paralelamente tenemos una lista con los pesos.

        El peso en la posicion i corresponde al simplice en la posicion i de la otra lista
        """
        self.simplices = maximal_simplice_list
        self.pesos = [0.0] * len(maximal_simplice_list)  # incializamos los pesos a 0

    def __str__(self):
        return "---------------------------------\nComplejo: " + str(self.simplices) + "\nPesos: " + str(
            self.pesos) + "\n---------------------------------"

    def dim(self):
        """
        Devuelve la dimension del comp simplicial --> Max dimension de los simplices
        :return:
        """
        return len(max(self.simplices, key=len)) - 1  # -1 por ser una lista (si n eltos -> dim n-1)

    def getCaras(self):
        """
        Calcula todas las caras de los simplices de un complejo simplicial
        """
        caras = set()
        for cada_simplice in self.simplices:
            caras = caras.union(getCarasDeSimplice(cada_simplice))
        return caras

    def getCarasDim(self, dim):
        """
        Calcula las caras de dimension dada
        """
        return set(filter(lambda cara: (len(cara) - 1) == dim, self.getCaras()))

    def estrella(self, simpl):
        """
        Calcula la estrella del complejo simplicial para el símplice dado
        """
        return set(filter(lambda cocara: esCara(simpl, cocara), self.getCaras()))

    def link(self, simpl):
        """
        Calcula el link del complejo simplicial del símplice dado
        """
        estr = self.estrella(simpl)
        estr_cerrada = cerrarEstrella(estr)
        # hago la diferencia de conjuntos
        return estr_cerrada.symmetric_difference(estr)

    def esqueleto(self, num):
        """
        Calculamos el n-esqueleto del complejo simplicial siendo n el valor pasado como parámetro llamado 'num'
        """
        esqueleto = set()
        for i in range(num + 1):
            esqueleto = esqueleto.union(self.getCarasDim(i))
        return esqueleto

    def caract_euler(self):
        """
        Obtenemos la caracteristica de Euler del complejo simplicial
        """
        simplices = self.getCaras()
        pares = len(list(filter(lambda cara: (len(cara) - 1) % 2 == 0, simplices)))
        impares = len(simplices) - pares
        return pares - impares

    def num_componentes_conexas(self):
        """
        Calcula el numero de componentes conexas del complejo simplicial a traves del grafo asociado
        """
        G = nx.Graph()
        # Tengo que aplanarlos, por eso hago compresion
        dim0 = [item for lista in self.getCarasDim(0) for item in lista]
        # añado vertices al grafo
        G.add_nodes_from(dim0)

        # consigo aristas
        dim1 = self.getCarasDim(1)
        # paso lista de sets a lista de tuplas
        aristas = []
        for i in dim1:
            aristas.append(tuple(i))
        # añado aristas
        G.add_edges_from(aristas)
        # aplano las aristas para ver los vertices que no estan
        dim1 = [item for lista in dim1 for item in lista]

        symmetrical_difference = list(set(dim0).symmetric_difference(set(dim1)))

        # añado aristas a los que no estas conectados para evitar error
        for i in symmetrical_difference:
            G.add_edge(*(i, i))

        # mostrar grafo para poder verlo
        nx.draw(G, with_labels=True, font_weight="bold")
        plt.show()

        # devolvemos numero de comp conexas
        return len(list(nx.connected_components(G)))

    # si no esta la cara meter con peso y si esta quedarse con el mas pequeño
    def anadirSimplice(self, simplices: list[tuple], valor: float):
        """
        Dado un simplice nuevo lo añade al conjunto de simplices junto con su peso.
        Para sus caras en caso de que estuviera añadida previamente se queda con el menor peso.
        """
        aux = Complejo(simplices)
        for cara in aux.getCaras():
            if cara in self.simplices:
                self.pesos[self.simplices.index(cara)] = min(self.pesos[self.simplices.index(cara)], valor)
            else:
                self.simplices.append(cara)
                self.pesos.append(valor)

    def filtration(self, valor: float):
        """
        Calcula los simplices que tienen un peso menor o igual a 'valor'.
        """
        # primero ordeno los simplices segun su peso, luego almaceno los simplices hasta el de menor peso
        res = []
        for i in range(len(self.pesos)):
            if self.pesos[i] <= valor:
                res.append(self.simplices[i])
            else:
                return res
        return res

    def obtenerPesoDeSimplice(self, simplice):
        """
        Devuelve el peso asociado al simplice (su peso es el que se encuentra en el mismo indice en la lista de pesos)
        :param simplice:
        :return:
        """
        return self.pesos[self.simplices.index(simplice)]

    def filtrationOrder(self):
        res = []
        simplicesCopia = self.simplices[:]
        pesosCopia = self.pesos[:]
        for i in range(len(self.simplices)):
            indiceElemMin = pesosCopia.index(min(pesosCopia))
            res.append(simplicesCopia[indiceElemMin])
            simplicesCopia.pop(indiceElemMin)
            pesosCopia.pop(indiceElemMin)
        # ordena la estructura del complejo simplicial por pesos ademas de devolver los simplices ordenados
        self.simplices = res
        self.pesos.sort()
        return res

    def devolverPeso(self, simpl):
        """
        Devuelve el peso del simplice asociado -> Sera el minimo de sus cocaras
        :param simpl:
        :return:
        """
        peso_res = None
        for i in range(len(self.simplices)):
            # si es cara entonces actualizo su peso
            if esCara(simpl, self.simplices[i]):
                if peso_res is None:
                    peso_res = self.pesos[i]
                else:
                    peso_res = min(peso_res, self.pesos[i])

        return peso_res

    def matriz_borde(self, p):
        """
        Dado una dimension p construye la matriz borde de dimension p.
        Esta es una matriz de incidencia len(caras_dim_p-1)(v) x len(caras_dim_p)(h)

        PARA ACCEDER A ELEM DE MATRIZ cuando es listas: matriz[fila][col]
        PARA ACCEDER A ELEM DE MATRIZ cuando es numpy: matriz[fila, col]
        """
        simplices_dim_p1 = list(self.getCarasDim(p - 1))
        simplices_dim_p = list(self.getCarasDim(p))
        simplices_dim_p1.sort()
        simplices_dim_p.sort()

        # creo la matriz borde
        matriz_borde = np.zeros((len(simplices_dim_p1), len(simplices_dim_p)))

        # hay que poner un 1 en la casilla [i][j] si el simplice_dim_p1[i] es cara de simplice_dim_p[j]
        for i in range(len(simplices_dim_p1)):
            for j in range(len(simplices_dim_p)):
                if esCara(simplices_dim_p1[i], simplices_dim_p[j]):
                    matriz_borde[i, j] = 1

        # la paso a lista
        matriz_borde = matriz_borde.tolist()

        return matriz_borde

    def betti_number(self, p):
        """
        Calcula el numero de Betti p-dimensional
        :param p:
        :return:
        """
        # vamos a construir la matriz borde para param (en H) y param-1 (en V)
        # filas de 1's --> B_p-1
        # columnas - columnas de 1's --> Z_p
        # Numero de betti para dim p = B_p - Z_p
        # Si queremos el numero de betti para dim p tenemos que sacar la forma normal de Smith para p (Z_p)
        # y p+1 (B_p)
        # OBS: los numeros de betti tiene sentido calcularlos hasta dim(complejo) --> el resto son 0's

        # caso extremo --> dim 0 -> Zp es el num de puntos
        if p == 0:
            matriz_p1 = hom.forma_normal_Smith(self.matriz_borde(p + 1))
            matriz_p1_np = np.array(matriz_p1)
            Bp = np.linalg.matrix_rank(matriz_p1_np)
            Zp = len(self.getCarasDim(0))  # num de puntos

            betti = Zp - Bp
            return betti

        # caso extremo --> dim maxima --> Bp = 0
        elif p == self.dim():
            matriz_p = hom.forma_normal_Smith(self.matriz_borde(p))
            matriz_p_np = np.array(matriz_p)
            Zp = hom.num_columnas(matriz_p) - np.linalg.matrix_rank(matriz_p_np)
            return Zp  # asi porque Bp = 0 (trivial)

        # Si p es menor que cero o mayor que dim(complejo) su numero de betti es 0
        elif p < 0 or p > self.dim():
            return 0

        # caso general --> Calculo ambas matrices
        else:
            matriz_p = hom.forma_normal_Smith(self.matriz_borde(p))
            matriz_p1 = hom.forma_normal_Smith(self.matriz_borde(p + 1))

            # paso a numpy para calcular el rango
            matriz_p_np = np.array(matriz_p)
            matriz_p1_np = np.array(matriz_p1)

            Zp = hom.num_columnas(matriz_p) - np.linalg.matrix_rank(matriz_p_np)  # n cols -  rango --> Z_p
            Bp = np.linalg.matrix_rank(matriz_p1_np)

            betti = Zp - Bp
            return betti


# FUNCIONES GENERALES (no necesita el uso de self)

def esCara(cara, simplice):
    """
    Funcion auxiliar que nos indica si dados dos simplices, el primero es cara del segundo.
    Consigo todas las combinaciones de la misma longitud que la cara y miro si esta contenido
    """
    aux = set(combinations(simplice, len(cara)))
    return cara in aux


def getCarasDeSimplice(simplice):
    """
    Dado un simplice nos devuelve todas las caras de ese simplice
    """
    caras = set(())
    # cogemos todas las caras de dim 1 hasta max
    for i in range(1, len(simplice) + 1):  # +1 para que coja tambien el maximal
        caras = caras.union(set(combinations(simplice, i)))

    return caras


def cerrarEstrella(estrella):
    """
    Dado una estrella devuelve la estrella cerrada
    """
    estrella_cerrada = set()
    # obtenemos todas las caras de los simplices que forman la estrella
    for elem in estrella:
        estrella_cerrada = estrella_cerrada.union(getCarasDeSimplice(elem))
    return estrella_cerrada
