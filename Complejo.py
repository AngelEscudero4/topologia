from itertools import combinations


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
    #cogemos todas las caras de dim 1 hasta max
    for i in range(1, len(simplice)+1): #+1 para que coja tambien el maximal
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
    #obtenemos todas las caras de los simplices que forman la estrella
    for elem in estrella:
        estrella_cerrada = estrella_cerrada + getCarasDeSimplice(elem)
    return estrella_cerrada
