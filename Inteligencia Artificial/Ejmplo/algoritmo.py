from Distancias_entre_ciudades import *
import random
import matplotlib.pyplot as plt

ciudades = [Londres, Venecia, Dunedin, Singapur, Beijing, Phoenix, Tokio, Victoria]

def generarPoblacionInicial(n):
    def crearEstadoAleatorio():
        estadoAleatorio = []
        ciudades = list(range(1, 9))
        n = len(ciudades)

        for i in range(0, n):
            ciudadEscogida = random.choice(ciudades)
            estadoAleatorio.append(ciudadEscogida)
            ciudades.remove(ciudadEscogida)

        return estadoAleatorio
        
    poblacion = []
    for i in range(0, n):
        poblacion.append(crearEstadoAleatorio())

    return poblacion

def funcionIdoneidad(estado):
    idoneidad = 0
    for i in range(0, len(estado) - 1):
        ciudad1 = ciudades[estado[i] - 1]
        ciudad2 = ciudades[estado[i + 1] - 1]
        distancia = city.distance(ciudad1, ciudad2)
        idoneidad += distancia

    return idoneidad

def getProbabilidades(poblacion):
    idoneidades = dict()
    total = 0
    for i in range(0, len(poblacion)):
        estado = poblacion[i]
        idoneidad = funcionIdoneidad(estado)
        idoneidades[tuple(estado)] = idoneidad
        total += idoneidad
    
    probabilidades = {}
    for i in range(0, len(poblacion)):
        estado = poblacion[i]
        idoneidad = idoneidades[tuple(estado)]
        probabilidad = int((1 - (idoneidad / total)) * 100 / (len(poblacion) - 1)) 
        probabilidades[tuple(estado)] = probabilidad
    
    return probabilidades

def seleccionarParaCruce(poblacion):
    def seleccionar(probabilidades):
        return random.choice([estado for estado in probabilidades for i in range(probabilidades[estado]) ])

    probabilidades = getProbabilidades(poblacion)
    estadosSeleccionados = []
    for i in range(0, len(poblacion)):
        estadosSeleccionados.append(seleccionar(probabilidades))
    
    return estadosSeleccionados

def cruzar(estado1, estado2):
    def orderedCrossover(padre1, padre2, n):
        hijo = [None] * len(padre1)
        pos = random.choice(range(0, len(hijo) - n + 1))
        for i in range(pos, pos + n):
            hijo[i] = padre1[i]
        
        posActual = 0
        for i in range(0, len(padre2)):
            if posActual == pos:
                posActual += n
            elem = padre2[i]
            if elem not in hijo:
                hijo[posActual] = elem
                posActual += 1
        return hijo

    hijo1 = orderedCrossover(estado1, estado2, 3)
    hijo2 = orderedCrossover(estado2, estado1, 3)

    return (hijo1, hijo2)

def cruzarPoblacion(poblacion):
    cruces = []
    estadosCruzar = seleccionarParaCruce(poblacion)
    for i in range(0, len(poblacion), 2):
        hijo1, hijo2 = cruzar(estadosCruzar[i], estadosCruzar[i + 1])
        cruces.append(hijo1)
        cruces.append(hijo2)
    
    return cruces

def mutarPoblacion(poblacion, probabilidad):
    def mutar(estado):
        posiciones = list(range(0, len(estado)))
        pos1 = random.choice(posiciones)
        posiciones.remove(pos1)
        pos2 = random.choice(posiciones)

        aux = estado[pos1]
        estado[pos1] = estado[pos2]
        estado[pos2] = aux
    
    probSeleccion = [True] * probabilidad + [False] * (100 - probabilidad)
    for i in range(0, len(poblacion)):
        if random.choice(probSeleccion):
            mutar(poblacion[i])

if __name__ == '__main__':
    poblacionActual = generarPoblacionInicial(4)
    poblacionActual.sort(key = funcionIdoneidad)
    mejorIdoneidadActual = 10000000000
    mejorEstadoActual = None

    generacionActual = 0
    generaciones = []
    idoneidades = []
    while mejorIdoneidadActual > 400:
        generaciones.append(generacionActual)

        nuevaGeneracion = cruzarPoblacion(poblacionActual)
        mutarPoblacion(nuevaGeneracion, 30)
        poblacionActual = nuevaGeneracion
        mejorHijo = min(poblacionActual, key = funcionIdoneidad)
        mejorIdoneidad = funcionIdoneidad(mejorHijo)
        #print(mejorIdoneidad)
        if mejorIdoneidad < mejorIdoneidadActual:
            mejorIdoneidadActual = mejorIdoneidad
            mejorEstadoActual = mejorHijo
        generacionActual += 1
        idoneidades.append(mejorIdoneidad)

    plt.plot(generaciones, idoneidades)
    print(mejorIdoneidadActual)
    print(mejorEstadoActual)
    print(generacionActual)
    plt.xlabel('generacion')
    plt.ylabel('idoneidad')
    plt.title('Idoneidad vs generacion')
    plt.show()
    print(mejorIdoneidadActual)
    print(mejorEstadoActual)
    print(generacionActual)