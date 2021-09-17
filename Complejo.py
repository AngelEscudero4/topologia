from itertools import combinations

class Complejo:
    #recibe lista de los simplices maximales
    def __init__(self, maximal_simplice_list):
        self.simplices = maximal_simplice_list

    def __print__(self):
        print(self.simplices)
        
    def dim(self):
        #la dimension del complejo es su simplice (lista) mas larga - 1
        return len(max(self.simplices, key= len))-1

    def getCaras(self):
        aux = []
        #recorremos los simplices maximales para construir las caras
        for cada_simplice in self.simplices:
            #para cada simplice construimos todas las caras (dimension menor que la del simplice)
            for i in range(1, len(cada_simplice)):
                aux = aux+list(combinations(cada_simplice, i))
            #como combinations nos devuelve tuplas -> casteamos a listas
        caras = [list(x) for x in aux]
        return caras


