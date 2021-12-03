# Tenemos una pila
# Tenemos una lista Actual
# state = granjero , lobo, cabra,col
# orillas = 0 , 1
# nodo = key: (state, visitado , nodo1, nodo2, nodo3 ....)

grafo = {'a': [(0, 0, 0, 0), False, 'OK', 'b', 'c', 'd'],
         'b': [(1, 0, 1, 0), False, 'OK', 'e'],
         'c': [(1, 0, 0, 1), False, 'ERROR'],
         'd': [(1, 1, 0, 0), False, 'ERROR'],
         'e': [(0, 0, 1, 0), False, 'OK', 'h', 'f'],
         'f': [(1, 1, 1, 0), False, 'OK', 'g'],
         'g': [(0, 1, 1, 0), False, 'ERROR'],
         'h': [(1, 0, 1, 1), False, 'OK', 'i', 'j'],
         'i': [(0, 0, 1, 1), False, 'ERROR'],
         'j': [(0, 0, 0, 1), False, 'OK', 'k', 'l'],
         'k': [(1, 0, 1, 1), False, 'OK', 'i'],
         'l': [(1, 1, 0, 1), False, 'OK', 'm', 'o'],
         'm': [(0, 1, 0, 0), False, 'OK', 'n'],
         'n': [(1, 1, 0, 0), False, 'ERROR'],
         'o': [(0, 1, 0, 1), False, 'OK', 'p'],
         'p': [(1, 1, 1, 1), False, 'FINAL']
         }

actual = []
cola = []

def existeLlave(key, dicObj):
    if key in dicObj:
        return True
    else:
        return False

def solucion():
    actual = []
    origen = "a"
    print("\nSolución por medio del  recorrido en anchura\n")
    # Verificamos que el nodo origen sea válido
    if (existeLlave(origen, grafo)) == False:
        print("El nodo origen no existe en el gráfo")
    elif grafo[origen][2] == 'OK':
        # poner nodo OK en la cola
        # listar todos los nodos que no han sido visitados y son OK o FiNAL
        # Si un nodo llega a un ESTADO ERROR
        #  Y NO TIENE MÁS NODOS NO VISITADOS ENTONCES SE ELIMINA
        # Si llega a un nodo FINAL se termina el juego
        cola.append(origen)
        while cola:
            aux = cola.pop(0)
            actual.append(aux)  # sacar vertice de la cola
            if grafo[aux][1] == False:  # si no se ha visitado el vertice actual
                grafo[aux][1] = True  # Este vertice ahora esta visitado
            if len(grafo[aux]) >= 3:  # si el vertice actual tiene mas de 3 elementos
                # guardar los nodos posibles en la cola
                for i in range(3, len(grafo[aux])):
                    keyPuedoIr = grafo[aux][i]
                    if grafo[keyPuedoIr][1] == False and grafo[keyPuedoIr][2] == 'OK':
                        cola.append(keyPuedoIr)
                    elif grafo[aux][2] == 'FINAL':
                        print('El camino para llegar al estado final p es:\n', actual)
                        return True
                    elif grafo[aux][2] == 'ERROR':
                        pass # no se mete a la
    
        print('El camino para llegar al estado final p es:\n', actual)
    elif grafo[origen][2] == 'ERROR':
        print("No puede partir de este nodo, pues si lo hace ya ha perdido")

    elif grafo[origen][2] == 'FINAL':
        print("Ya esta en el nodo final")

solucion()
