from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt


class Complejo:
    # recibe lista de los simplices maximales
    def __init__(self, maximal_simplice_list):
        self.simplices = maximal_simplice_list

    def __str__(self):
        return "Complejo: " + str(self.simplices)

    def dim(self):
        # la dimension del complejo es su simplice (lista) mas larga - 1
        return len(max(self.simplices, key=len)) - 1

    def getCaras(self):
        """
        Calcula todas las caras de los simplices maximales de un complejo
        """
        caras = []
        # recorremos los simplices maximales para construir las caras
        for cada_simplice in self.simplices:
            caras = caras + getCarasDeSimplice(cada_simplice)
        return caras

    def getCarasDim(self, dim):
        """
        Calcula las caras de longitud dim+1
        """
        return list(filter(lambda cara: (len(cara) - 1) == dim, self.getCaras()))

    def estrella(self, simpl):
        return list(filter(lambda cara: esCara(cara, simpl), self.getCaras()))

    def link(self, simpl):
        link=[]
        estr = self.estrella(simpl)
        print('Estrella: ',estr)
        set_estr = set(())
        for i in estr:
            set_estr.add(set(i))
        estr_cerrada = cerrarEstrella(estr)
        set_estr_cerrada = set(())
        for i in estr_cerrada:
            set_estr_cerrada.add(set(i))
        print('Cerrada: ',estr_cerrada)
        #hago la diferencia de conjuntos
        #link = list(set(estr_cerrada).symmetric_difference(set(estr)))
        link= list(set_estr_cerrada.symmetric_difference(set_estr))
        
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
    aux = list(combinations(simplice, len(cara)))
    lista_caras = [list(x) for x in aux]
    res = cara in lista_caras
    return res


def getCarasDeSimplice(simplice):
    """
    Dado un simplice nos devuelve todas las caras de ese simplice
    """
    aux = []
    # cogemos todas las caras de dim 1 hasta max
    for i in range(1, len(simplice) + 1):  # +1 para que coja tambien el maximal
        aux = aux + list(combinations(simplice, i))
    # como combinations nos devuelve tuplas -> casteamos a listas
    # tambien tenemos que eliminar los repetidos ya que [0,1] y [0,2] generan dos veces el 0
    aux = list(set(aux))
    caras = [list(x) for x in aux]
    caras.sort(key=len)  # ordenar por tamaño de simplices
    return caras


def cerrarEstrella(estrella):
    """
    Dado una estrella devuelve la estrella cerrada
    """
    estrella_cerrada = []
    # obtenemos todas las caras de los simplices que forman la estrella
    for elem in estrella:
        estrella_cerrada = estrella_cerrada + getCarasDeSimplice(elem)
    return estrella_cerrada
