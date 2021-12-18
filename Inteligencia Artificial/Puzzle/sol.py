import copy as cp
start = [ # Este es mi estado inicial
    [2, 8, 3],
    [1, 6, 4],
    [7, "", 5]
]
end = [ # Este es mi estado objetivo
    [1, 2, 3],
    [8, "", 4],
    [7, 6, 5]
]
visitados = [] # Guardo los estados visitados para no volver
visitados.append(cp.deepcopy(start)) # El primer visitado es mi estado de partida
alternativePath = [] # En caso de encontrar 2 posibles caminos guardo aqui el camino
alternativePath.append(cp.deepcopy(start))# alternativo

def sol(nodoActual, end, read): # Solución del ejercicio
    
    toEvaluate = [] # mi lista para evaluar

    # necesito añadir a toEvaluate los caminos de alternativPath 
    for i in nodoActual:
        if i == end: # si el estado actual es igual al final lo he conseguido
            print("Solucion encontrada")
            return True
    
        a, b = blank(i) # coordenadas del espacio en blanco
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

    min = 100000000000000
    alternativePath = []
    
    for i in toEvaluate: # Escojer el o los mejores caminos de partida

        if h1(i, end) < min: # busco el camino con menor heuristica

            if alternativePath != []: # tengo un nuevo minimo
                alternativePath = [] # saca el ultimo camino alternativo

            print('mistakes', h1(i, end))
            min = h1(i, end)
            alternativePath.append(cp.deepcopy(i))

        elif h1(i, end) == min: # si encuentro otro min es otro camino alternativo
            alternativePath.append(cp.deepcopy(i))

    print('el o los mejores caminos son: ', alternativePath)
    sol(alternativePath, end, read)

def h1(arr, end):
    mistakes = 0
    for i in arr:
        for j in i:
            if j != end[arr.index(i)][i.index(j)]:
                mistakes += 1
    return mistakes

def blank(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "":
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

sol(alternativePath, end, 3)
