from practica1 import Complejo
import numpy as np
from practica3 import homologia
from matplotlib import pyplot as plt


def simplices_ordenados(complejo: Complejo):
    # primero sacamos todos los simplices posibles, luego los ordenamos tanto por longitud como por los eltos
    simplices = complejo.getCaras()
    simplices = list(simplices)
    simplices.sort(key=len)

    simplicesCopia = []

    # aqui ya los tenemos en longitud, ahora cogemos de cada longitud y los ordenamos
    for i in range(1, len(simplices[-1])):
        y = filter(lambda x: (len(x) == i), simplices)
        y = list(y)
        y.sort()
        simplicesCopia = simplicesCopia + y

    return simplicesCopia


def matriz_borde_generalizada(complejo: Complejo):
    """
    Dado un complejo simplicial calculamos su matriz borde generalizada
    *** MATRIZ [FILAS][COL] ***
    """
    simplices = complejo.simplices
    print(simplices)
    # ahora tenemos que hacer la matriz de incidencia
    matriz = np.zeros((len(simplices), len(simplices)))
    matriz = matriz.tolist()
    # hay que poner un 1 en la casilla [i][j] si el simplice_dim_(p-1)[i] es cara de simplice_dim_p[j]
    for i in range(homologia.num_filas(matriz)):
        for j in range(homologia.num_columnas(matriz)):
            if len(simplices[i]) == len(simplices[j]) - 1 and Complejo.esCara(simplices[i], simplices[j]):
                matriz[i][j] = 1.0
    return matriz


def algoritmo_emparejamiento_nacimiento_muerte(matriz):
    """
    Recibida una matriz borde gen vamos a calculas los emparejamientos nacimiento-muerte
    """
    # dada una columna sacamos su low() miramos en las columnas de su izqda y si tienen el mismo low borramos ese low
    # en la de la dcha, repetimos proceso hasta que no se repita posicion low con ninguno de su izqda
    for i in range(homologia.num_columnas(matriz)):
        repetir = True  # True pq queremos que lo ejeute al menos una vez (equiv a do:while)
        while repetir:
            repetir = False  # Si no modificamos la columna es pq no hay un low igual
            index_low = get_low(get_columna(matriz, i))
            # si existe low en esa columna
            if index_low != -1:
                # buscamos lows anteriores en el mismo sitio
                for otro_i in range(i):
                    # si tienen el mismo low
                    if get_low(get_columna(matriz, otro_i)) == index_low:
                        # sumamos las dos columnas, en la que estamos actualmente ponemos el resultado
                        homologia.sumar_dos_columnas(matriz, otro_i, i)
                        # si encontramos otro low ahora este ha sido modificado y debriamos mirar si este nuevo se
                        # vuelve a repetir desde la primera columna
                        repetir = True
                        break
    return matriz


def get_low(col):
    """
    Recibimos una columna y calculamos el indice de su 1 mas abajo.
    Devuelve -1 en caso de ser all 0's
    """
    indice = -1
    for i in range(len(col)):
        if col[i] == 1:
            indice = i
    return indice


def get_columna(matriz, indice):
    return [x[indice] for x in matriz]


def get_emparejamientos(matriz):
    """
    Dada una matriz de borde generalizada calculamos el algoritmo para reducir la matriz.
    Despues calculamos los emparejamientos para cada columna

    Emparejamientos son [low(j),j]
    """
    emparejamientos = []

    # recorremos las columnas
    for j in range(homologia.num_columnas(matriz)):
        # sacamos su low y creamos una parejita
        index_low = get_low(get_columna(matriz, j))
        # metemos la pareja
        emparejamientos.append((index_low, j))

    return emparejamientos


def conseguir_puntos_diagrama(complejo):
    matriz_borde_gen = matriz_borde_generalizada(complejo)

    # si queremos ver la matriz podemos con esto
    # imprimir_matriz(matriz_borde_gen)

    # operamos para que no haya lows repetidos
    matriz_borde_gen = algoritmo_emparejamiento_nacimiento_muerte(matriz_borde_gen)
    # imprimir_matriz(matriz_borde_gen)

    # cogemos los emparejamientos por pares
    emparejamientos = get_emparejamientos(matriz_borde_gen)
    print("[low-columna]", emparejamientos)

    # cogemos los simplices ordenados --> OJO QUE TIENEN QUE COINCIDIR CON LOS DE maatriz_borde_gen
    simplices = complejo.simplices
    print(simplices)

    lista_puntos = []
    lista_aristas = []
    for (low, columna) in emparejamientos:  # simplices[low] es nacimiento y simplices[col] es muerte
        if low != -1:
            # si es un de H0 lo añado a los puntos, si H1 lo añado a aristas
            if complejo.devolverPeso(simplices[low]) == 0:
                # low sera la fila y col columna --> sacamos simplices para sus pesos y pintar el punto
                (x, y) = (0, complejo.devolverPeso(simplices[columna]))
                lista_puntos.append([x, y])
            else:
                (x, y) = (complejo.devolverPeso(simplices[low]), complejo.devolverPeso(simplices[columna]))
                # los que tienen una diferencia considerable los añado, ya que por precision de la maquina sino se
                # muestran muchisimos mas practicamente en la propia linea, asi al menos el de la circunferencia son
                # iguales por ej
                if y - x > 0.000001:
                    lista_aristas.append([x, y])

    # añadimos el punto del infinito que sabemos que siempre va a estar ahi peso de la comp conexa del 0
    maxPuntoY = 0
    maxAristaY = 0
    maximo = 0
    if len(lista_puntos) > 0:
        maxPuntoY = max(lista_puntos, key=lambda x: x[1])[1]

    if len(lista_aristas) > 0:
        maxAristaY = max(lista_aristas, key=lambda x: x[1])[1]

    if maxPuntoY != 0:
        maximo = maxPuntoY
    if maxAristaY != 0:
        maximo = max(maximo, maxAristaY)
    lista_puntos.append((0, maximo + 1))

    return lista_puntos, lista_aristas


def diagrama_barras(complejo):
    puntos_diagrama, aristas_diagrama = conseguir_puntos_diagrama(complejo)
    peso_max = puntos_diagrama[-1][1]
    altura = 0.5
    for [x, y] in puntos_diagrama:
        intervalo = np.linspace(x, y)
        plt.plot(intervalo, [altura] * len(intervalo), 'b')
        altura += 0.5

    altura += 0.25
    intervalo = np.linspace(-0.5, peso_max + 0.5)
    plt.plot(intervalo, [altura] * len(intervalo), 'k')
    altura += 0.75

    for [x, y] in aristas_diagrama:
        intervalo = np.linspace(x, y)
        plt.plot(intervalo, [altura] * len(intervalo), 'r')
        altura += 0.5

    plt.yticks([])
    plt.show()


def diagrama_persistencia(complejo):
    puntos_diagrama, aristas_diagrama = conseguir_puntos_diagrama(complejo)
    peso_max = puntos_diagrama[-1][1]

    # si tenemos puntos los pintamos (H0)
    if len(puntos_diagrama) > 0:
        puntos_diagrama = np.array(puntos_diagrama)
        plt.scatter(puntos_diagrama[:, 0], puntos_diagrama[:, 1], color="blue")
    # H1
    if len(aristas_diagrama) > 0:
        aristas_diagrama = np.array(aristas_diagrama)
        plt.scatter(aristas_diagrama[:, 0], aristas_diagrama[:, 1], color="red")

    # mostramos los ejes discontinuos
    intervalo = np.linspace(0, peso_max)
    plt.plot(intervalo, intervalo, 'k--')
    plt.plot(intervalo, [peso_max] * len(intervalo), 'k--')

    plt.show()
