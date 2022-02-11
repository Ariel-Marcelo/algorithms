# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 17:04:31 2020

@author: myriam.hernandez
"""
import numpy as np

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

print(city.distance(Phoenix, Beijing))
    





    