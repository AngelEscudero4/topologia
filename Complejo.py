from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt


class Complejo:
    # recibe lista de los simplices maximales
    def __init__(self, maximal_simplice_list: list):
        self.simplices_maximales = set(maximal_simplice_list)

    def __str__(self):
        return "Complejo: " + str(self.simplices_maximales)

    def dim(self):
        # la dimension del complejo es su simplice (lista) mas larga - 1
        return len(max(self.simplices_maximales, key=len)) - 1

    def getCaras(self):
        """
        Calcula todas las caras de los simplices maximales de un complejo
        """
        caras = set()
        # recorremos los simplices maximales para construir las caras
        for cada_simplice in self.simplices_maximales:
            caras = caras.union(getCarasDeSimplice(cada_simplice))
        return caras

    def getCarasDim(self, dim):
        """
        Calcula las caras de longitud dim+1
        """
        return set(filter(lambda cara: (len(cara) - 1) == dim, self.getCaras()))

    def estrella(self, simpl):
        return set(filter(lambda cocara: esCara(simpl, cocara), self.getCaras()))

    def link(self, simpl):
        link = set()
        estr = self.estrella(simpl)
        estr_cerrada = cerrarEstrella(estr)
        # hago la diferencia de conjuntos
        link = estr_cerrada.symmetric_difference(estr)
        return link

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

        # G.add_edges_from([(“A”,”C”), (“B”,”D”), (“B”,”E”), (“C”, “E”)])
        dim1 = self.getCarasDim(1)
        # paso lista de listas a lista de tuplas
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

        nx.draw(G, with_labels=True, font_weight="bold")
        plt.show()

        return len(list(nx.connected_components(G)))


def esCara(cara, simplice):
    """
    Funcion auxiliar que nos indica si dados dos simplices, el primero es cara del degundo
    """
    res = False
    aux = set(combinations(simplice, len(cara)))
    # lista_caras = [list(x) for x in aux]
    res = cara in aux
    return res


def getCarasDeSimplice(simplice):
    """
    Dado un simplice nos devuelve todas las caras de ese simplice
    """
    aux = set(())
    # cogemos todas las caras de dim 1 hasta max
    for i in range(1, len(simplice) + 1):  # +1 para que coja tambien el maximal
        aux = aux.union(set(combinations(simplice, i)))
    # como combinations nos devuelve tuplas -> casteamos a listas
    # # tambien tenemos que eliminar los repetidos ya que [0,1] y [0,2] generan dos veces el 0
    # aux = list(set(aux))

    return aux


def cerrarEstrella(estrella):
    """
    Dado una estrella devuelve la estrella cerrada
    """
    estrella_cerrada = set()
    # obtenemos todas las caras de los simplices que forman la estrella
    for elem in estrella:
        estrella_cerrada = estrella_cerrada.union(getCarasDeSimplice(elem))
    return estrella_cerrada
