"""
Created on Wed Dec 16 12:12:44 2020
@author: Daliana Zambrano

"""

#Definimos el árbol con sus nodos
arbol = {'(0,0)': ['(4,0)', '(0,3)'],
         '(0,3)': ['(0,0)'],
         '(4,0)': ['(4,3)', '(1,3)'],
         '(4,3)': ['(4,0)'],
         '(1,3)': ['(1,0)'],
         '(1,0)': ['(0,1)'],
         '(0,1)': ['(4,1)'],
         '(4,1)': ['(2,3)'],
         '(2,3)': ['(4,1)']
         }

#Definimos la función DFS que tiene como entrada el nodo que le pasamos en el main
def BFS(array, value = 0): 
    #Se definen las variables globales lista y arbol
    global lista, arbol
    
    #Se comprueba que no hayan nodos repetidos en la búsqueda
    if set(arbol[array[value]]).issubset(lista):
        del array[value]
        return BFS(array, value)

    #Va controlando que cada nodo esté en la lista caso contrario lo agrega
    for elemento in arbol[array[value]]:
        if elemento in lista:
            continue
        lista.append(elemento)
        array.append(elemento)
        
        #Si encuentra el elemento que buscamos retorna la lista y el array llenados
        #anteriormente, caso contrario llama recursivamente a la función DFS
        if elemento == '(2,3)':
            return array, lista

    return BFS(array, value+1)

#LLamamos al main
if __name__ == '__main__':
    #Se le pasa a la variable lista el nodo inicial por donde vamos a buscar
    lista = ['(0,0)']
    
    #Se iguala la función DFS a las variables solucion y nodos_visitados
    #para imprimir tanto la solución como el recorrido que se hizo para llegar 
    #a la solución esperada
    solucion, nodos_visitados = BFS(['(0,0)'])
    print('\nSolución: \n' + str(solucion) + '\n')
    print('Camino Recorrido: \n' + str(nodos_visitados))
