#Definimos el grafo
grafo = {'S0': ['S10', 'S8', 'S9', 'S12'],

#El algoritmo DFS devuelve el camino hacia el estado_ganador
def DFS(array): 

    if (array[-1] not in grafo):
        return -1
    
    #Se comprueba que no hayan nodos repetidos en la búsqueda
    if set(grafo[array[-1]]).issubset(visitados):
        del array[-1]
        return DFS(array)

    #Va controlando que cada nodo esté en la visitados caso contrario lo agrega
    for elemento in grafo[array[-1]]:
        if elemento in visitados:
            continue
        visitados.append(elemento)
        array.append(elemento)
        
        #Si encuentra el elemento que buscamos retorna la visitados y el array llenados
        #anteriormente, caso contrario llama recursivamente a la función DFS
        if elemento == estado_ganador:
            return array
        else:
            return DFS(array)


#LLamamos al main
if __name__ == '__main__':
    #Se le pasa a la variable visitados el nodo inicial por donde vamos a buscar
    visitados = ['(0,0)']
    
    #Se iguala la función DFS a las variables solucion y nodos_visitados
    #para imprimir tanto la solución como el recorrido que se hizo para llegar 
    #a la solución esperada
    solucion, nodos_visitados = DFS(['(0,0)'])
    print('\nSolución: \n' + str(solucion) + '\n')
    print('Camino Recorrido: \n' + str(nodos_visitados))



