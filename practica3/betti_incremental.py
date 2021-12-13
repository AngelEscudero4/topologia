from practica1.Complejo import Complejo


def betti_incremental(complejo: Complejo):
    """
        Recibimos un complejo simplicial.
        En funcion de los 0, 1, 2 simplices vamos a variar los numeros de betti 0 y 1.

        Empezaremos con un complejo que sean los puntos y con B0
        Para las aristas que vayamos añadiendo miramos sin son positivas o negativas y vamos sumando.
        Las caras siempre tapan agujeros (B1 resta en 1 cada vez que añadimos)
    """
    # cogemos las caras y las ordenamos por dimension
    caras = complejo.getCaras()
    lista_caras = []
    for cara in caras:
        lista_caras.append(list(cara))
    lista_caras.sort(key=len)

    # inicializamos los nums de betti
    betti0, betti1 = 0, 0

    # voy guardando y actualizando las comp conexas aqui
    componentes_conexas = []

    # vamos por cada simplice actualizando los nums de betti en funcion del simplice que se añada
    for cara in lista_caras:
        if len(cara) == 1:
            betti0 += 1
            componentes_conexas.append(cara)
        elif len(cara) == 3:
            betti1 -= 1
        else:
            if misma_componente_conexa(cara, componentes_conexas):
                betti1 += 1
            else:
                betti0 -= 1
    return betti0, betti1


def misma_componente_conexa(arista, componentes_conexas):
    """
    Comprueba si la arista une la misma componente conexa o distintas, actualizandola en este caso a una unica
    :param arista:
    :param componentes_conexas:
    :return:
    """
    for componente_conexa in componentes_conexas:
        if arista[0] in componente_conexa and arista[1] in componente_conexa:
            return True
    # si no es true entonces tenemos que unir las componentes conexas y devolver false
    componentes_a_unir = []
    for componente_conexa in componentes_conexas:
        if arista[0] in componente_conexa or arista[1] in componente_conexa:
            componentes_a_unir.append(componente_conexa)
    union = []
    for elem in componentes_a_unir:
        union.extend(elem)
        componentes_conexas.remove(elem)
    componentes_conexas.append(union)
    return False

# [[0,1,2,3], [4,5]]
