import copy as cp
start = [ # Este es mi estado inicial
    [7, 2, 4],
    [5, "", 6],
    [8, 3, 1]
]
end = [ # Este es mi estado objetivo
    ["", 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]
visitados = [] # Guardo los estados visitados para no volver
visitados.append(cp.deepcopy(start)) # El primer visitado es mi estado de partida
alternativePath = [] # En caso de encontrar 2 posibles caminos guardo aqui el camino
alternativePath.append(cp.deepcopy(start))# alternativo

def sol(nodoActual, end, read): # Solución del ejercicio
    toEvaluate = [] # mi lista para evaluar
    for i in nodoActual:
        if i == end: # si el estado actual es igual al final lo he conseguido
            print("Solucion encontrada")
            return True
    
        a, b = find(i, "") # coordenadas del espacio en blanco
        aux = None
        if b != 0:
            aux = move(i, a, b, "left") # puedo ir a la izquierda
            if aux not in visitados:
                toEvaluate.append(cp.deepcopy(aux))
                visitados.append(cp.deepcopy(aux))

        if b != len(i[0]) - 1:
            aux = move(i, a, b, "right") # puedo ir a la derecha

            if aux not in visitados:
                toEvaluate.append(cp.deepcopy(aux))
                visitados.append(cp.deepcopy(aux))

        if a != 0:
            aux = move(i, a, b, "up") # puedo subir

            if aux not in visitados:
                toEvaluate.append(cp.deepcopy(aux))
                visitados.append(cp.deepcopy(aux))

        if a != len(i) - 1:
            aux = move(i, a, b, "down") # puedo bajar
            
            if aux not in visitados:
                toEvaluate.append(cp.deepcopy(aux))
                visitados.append(cp.deepcopy(aux))

    min = 100000000000000000000000000000000000000000
    alternativePath = []
    #herusística = h1
    herusística = h2
    for i in toEvaluate: # Escojer el o los mejores caminos de partida
        if herusística(i, end) < min: # busco el camino con menor heuristica
            if alternativePath != []: # tengo un nuevo minimo
                alternativePath = [] # saca el ultimo camino alternativo
            min = herusística(i, end)
            alternativePath.append(cp.deepcopy(i))
        elif herusística(i, end) == min: # si encuentro otro min es otro camino alternativo
            alternativePath.append(cp.deepcopy(i))
    if toEvaluate == []: # si no encuentro un camino alternativo
        print("No se pudo encontrar la solución")
        return False
    read += 1
    printState(alternativePath, min,read) # imprimo los caminos alternativos
    sol(alternativePath, end, read)

def h1(arr, end):
    mistakes = 0
    for i in arr:
        for j in i:
            if j != end[arr.index(i)][i.index(j)]:
                mistakes += 1
    
    return mistakes

def h2(arr, end):
    mistakes = 0
    for i in arr:
        for j in i:
            if j != end[arr.index(i)][i.index(j)]:
                a,b = find(end, j)
                mistakes += abs(a - arr.index(i)) + abs(b - i.index(j))
    return mistakes

def find(arr, objetivo):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == objetivo:
                return i, j

def move(arr, a, b, direction):
    if direction == "left":
        aux = cp.deepcopy(arr)
        aux[a][b], aux[a][b-1] = aux[a][b-1], aux[a][b]
        return aux
    elif direction == "right":
        aux = cp.deepcopy(arr)
        aux[a][b], aux[a][b+1] = aux[a][b+1], aux[a][b]
        return aux
    elif direction == "up":
        aux = cp.deepcopy(arr)
        aux[a][b], aux[a-1][b] = aux[a-1][b], aux[a][b]
        return aux
    elif direction == "down":
        aux = cp.deepcopy(arr)
        aux[a][b], aux[a+1][b] = aux[a+1][b], aux[a][b]
    
    return aux

def printState(state, min, step):
    print("Paso # ",step,"El o los mejores caminos con el costo ", min," son: \n ")
    if len(state) != 0:
        for i in range(len(state[0])):
            toPrint = ""
            for j in state:
                toPrint += str(j[i]) + "      "
        
            toPrint += "\n"
            print(toPrint)

sol(alternativePath, end, 0)

"""
def printState(state, min):
    print(" El o los mejores caminos con el costo ", min," son: \n ")
    toPrint = ""
    for i in state:
        toPrint += "state: "+ str(i) + "\n"

    print(toPrint)
        
"""
