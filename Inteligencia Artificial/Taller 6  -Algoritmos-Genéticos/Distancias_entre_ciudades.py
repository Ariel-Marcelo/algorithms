# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 17:04:31 2020

@author: myriam.hernandez
"""
from typing import Callable
import numpy as np
import random
import copy as cp

class city:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance
    
    def _repr_(self):
        return "(" + str(self.x) + "," + str(self.y)+ ")"


Londres = city(x=int(51.509865), y=int(-0.118092))
Venecia= city(x=int(45.438759), y=int(12.327145))
Dunedin = city(x=int(-45.8742), y=int(170.5036))
Singapur = city(x=int(1.290270),y=int(103.851959))
Beijing = city(x=int(39.916668),y=int(116.383331))
Phoenix = city(x=int(33.448376),y=int(-112.074036))
Tokio = city(x=int(35.652832),y=int(139.839478))
Victoria = city(x=int(48.407326),y=int(-123.329773))

#Ejemplo de par de distancia entre par de ciudades

print(city.distance(Venecia, Beijing))

myCities = {1: Londres, 2: Venecia, 3: Dunedin, 4: Singapur, 5: Beijing, 6: Phoenix, 7: Tokio, 8: Victoria}

def generar_camino():
    muestra = [1, 2, 3, 4, 5, 6, 7, 8]
    return random.sample(muestra, 8)

def crear_poblacion(numHabitantes = 4):
    poblacion = []
    for i in range(numHabitantes):
        camino = generar_camino()
        poblacion.append(camino)
    return poblacion
    
def idoneidad (camino):
    valor = 0
    for i in range(1, len(camino)):
        valor += city.distance(myCities[camino[i-1]], myCities[camino[i]])
    
    return valor

def seleccion (poblacion):
    puntajes = [(idoneidad(i), i) for i in poblacion]
    #print("Puntajes: ", puntajes)
    puntajes = [i[1] for i in sorted(puntajes)]
    selecteds = puntajes[:3]

    return selecteds

def crossover (padre1, padre2):
    # Seleccionar un punto aleatorio de inicio y fin
    start, end = sorted([random.randrange(len(padre1)) for _ in range(2)])
    descendiente1 = [-1] * len(padre1)

    for j in range(start, end + 1):
        descendiente1[j] = padre1[j]

    #print("start: ", start, "end: ", end)
    #print(descendiente1)

    for k in range(end + 1, len(descendiente1)):
        for i in range(k, len(padre2)):
            if padre2[i] not in descendiente1:
                descendiente1[k] = padre2[i]
                break

        if descendiente1[k] == -1:
            for i in range(0, k):
                if padre2[i] not in descendiente1:
                    descendiente1[k] = padre2[i]
                    break

    for k in range(0, start):
        for i in range(k, len(padre2)):
            if padre2[i] not in descendiente1:
                descendiente1[k] = padre2[i]
                break

        if descendiente1[k] == -1:
            for i in range(0, k):
                if padre2[i] not in descendiente1:
                    descendiente1[k] = padre2[i]
                    break
    
    return descendiente1


def mutation (poblacion):
    poblacion_mutada = cp.deepcopy(poblacion)
    for camino in poblacion_mutada:
        
        point1, point2 =  sorted([random.randrange(len(camino)) for _ in range(2)])

        cambio = camino[point1]
        camino[point1] = camino[point2]
        camino[point2] = cambio

    return poblacion_mutada


def algoritmo_genetico ():
    
    poblacion = crear_poblacion(4)
    print("Poblacion inicial: ", poblacion)
    
    for i in range(14):
        poblacion = seleccion(poblacion) # Seleccionar los 3 mejores
        print ("Mejor distancia", idoneidad(poblacion[0]), "Camino: ", poblacion[0])
        new_poblacion = []
        # Cruzar los 3 mejores y generamos 4 nuevos
        for j in range(1, len(poblacion)):
            descendiente1 = crossover(poblacion[0], poblacion[j])
            new_poblacion.append(descendiente1)
            descendiente2 = crossover(poblacion[0], poblacion[j])
            new_poblacion.append(descendiente2)

        poblacion = cp.deepcopy(new_poblacion) # Actualizar la poblacion
        poblacion = mutation(poblacion) # mutamos toda la población

        
        
        


algoritmo_genetico()
#print (idoneidad([1, 2, 7, 5, 3, 4, 6, 8]))
#print(crossover ([5, 2, 1, 8, 6, 7, 4, 3], [2, 5, 7, 6, 8, 1, 3, 4]) )
#print(seleccion([[5, 2, 1, 8, 6, 7, 4, 3], [2, 5, 7, 6, 8, 1, 3, 4], [3, 5, 7, 2, 1, 6, 4, 8], [3, 4, 8, 7, 6, 1, 2, 5]]))