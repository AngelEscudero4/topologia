from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt


class Complejo:
    """
    INFORMACION DE LOS TIPOS DE DATOS:
    - Complejo Simplicial --> Set
    - Simplice --> Tuplas

    Ejemplo: {((vertex),Num),((vertex),Num),((vertex),Num)}

    simplice = (1,2,3) x = contructor([(), (), ()]) --> complejo = [simplice, ....] 1. Añadir simplice(simplNuevo)
    --> complejo = [simplice, ...., SimplNuevo] 2. x = añadir(tuplaExistente, peso)--> complejo = [(simplice, peso),
    .... , SimplNuevo] -> en caso de uno sin peso --> meter el 0
    """
    # # recibe lista de los simplices maximales
    # def __init__(self, maximal_simplice_list: list[tuple]):
    #     #[((),3), ((), 0)]
    #     for cada_tupla in maximal_simplice_list:
    #         cada_simplice = (cada_simplice, 0)
    #     self.simplices_maximales = set(maximal_simplice_list)

    # recibe lista de los simplices maximales
    def __init__(self, maximal_simplice_list: list[tuple]):
        self.simplices_maximales = set(maximal_simplice_list)

    def __str__(self):
        return "Complejo: " + str(self.simplices_maximales)

    def dim(self):
        # la dimension del complejo es su simplice (lista) mas larga - 1
        return len(max(self.simplices_maximales, key=len)) - 1

    def getCaras(self):
        """
        Calcula todas las caras de los simplices maximales de un complejo simplicial
        """
        caras = set()
        for cada_simplice in self.simplices_maximales:
            caras = caras.union(getCarasDeSimplice(cada_simplice))
        return caras

    def getCarasDim(self, dim):
        """
        Calcula las caras de longitud dim
        """
        return set(filter(lambda cara: (len(cara) - 1) == dim, self.getCaras()))

    def estrella(self, simpl):
        return set(filter(lambda cocara: esCara(simpl, cocara), self.getCaras()))

    def link(self, simpl):
        estr = self.estrella(simpl)
        estr_cerrada = cerrarEstrella(estr)
        # hago la diferencia de conjuntos
        return estr_cerrada.symmetric_difference(estr)

    def esqueleto(self, num):
        esqueleto = set()
        for i in range(num):
            esqueleto = esqueleto.union(self.getCarasDim(i))
        return esqueleto

    def caract_euler(self):
        simplices = self.getCaras()
        pares = len(list(filter(lambda cara: (len(cara) - 1) % 2 == 0, simplices)))
        impares = len(simplices) - pares
        return pares - impares

    def num_componentes_conexas(self):
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

        # añado ristas a los que no estas conectados para evitar error
        for i in symmetrical_difference:
            G.add_edge(*(i, i))

        # mostrar grafo para poder verlo
        nx.draw(G, with_labels=True, font_weight="bold")
        plt.show()

        # devolvemos numero de comp conexas
        return len(list(nx.connected_components(G)))

    def anadirSimplice(self, simpl: tuple):
        """
        Dado un simplice nuevo lo añade al conjuntos de simplices maximales.
        Esto solo ocurre si es nuevo
        """
        if simpl not in self.getCaras():
            self.simplices_maximales.add(simpl)


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
    # como combinations nos devuelve tuplas -> casteamos a listas
    # # tambien tenemos que eliminar los repetidos ya que [0,1] y [0,2] generan dos veces el

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
