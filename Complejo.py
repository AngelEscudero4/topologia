from itertools import combinations

class Complejo:
    #recibe lista de los simplices maximales
    def __init__(self, maximal_simplice_list):
        self.simplices = maximal_simplice_list
        
    def dim(self):
        #la dimension del complejo es su simplice (lista) mas larga - 1
        return len(max(self.simplices, key= len))-1

