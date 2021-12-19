import copy as cp
start = [
    [2, 8, 3],
    [1, 6, 4],
    [7, "", 5]
]
end = [
    [1, 2, 3],
    [8, "", 4],
    [7, 6, 5]
]
visitados = []
visitados.append(cp.deepcopy(end))
alternativePath = []
toEvaluate = []

def sol(start, end, read):
    if start == end:
        print("Solucion encontrada")
        return True
    a, b = blank(start)
    #a, b = start.index("")
    aux = None
    # necesito añadir a toEvaluate los caminos de alternativPath  
    move(start, a, b)

    if alternativePath != []:
        for i in alternativePath:
            c,d = blank(i)
            move(i, c, d)

    min = 100000000000000
    index = 0

    if toEvaluate != []:
      for i in toEvaluate:
        if h1(i, end) < min:
            print('mistakes', h1(i, end))
            min = h1(i, end)
            index = toEvaluate.index(i)
            if alternativePath != []:
                alternativePath.pop()
        elif h1(i, end) == min:
            alternativePath.append(cp.deepcopy(i))

      print('el mejor camino', toEvaluate[index])
      start = cp.deepcopy(toEvaluate[index])
      sol(start, end, read)

    else:
      print('No hay solucion')
      return False
    
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
                mistakes += 1 

def blank(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "":
                return i, j

def move(arr, a, b):
    if b != 0: #left
        aux = cp.deepcopy(arr)
        aux[a][b], aux[a][b-1] = aux[a][b-1], aux[a][b]
        if aux not in visitados:
            toEvaluate.append(cp.deepcopy(aux))
            visitados.append(cp.deepcopy(aux))
    if b != len(arr[0]) - 1: #right
        aux = cp.deepcopy(arr)
        aux[a][b], aux[a][b+1] = aux[a][b+1], aux[a][b]
        if aux not in visitados:
            toEvaluate.append(cp.deepcopy(aux))
            visitados.append(cp.deepcopy(aux))
    if a != 0: #up
        aux = cp.deepcopy(arr)
        aux[a][b], aux[a-1][b] = aux[a-1][b], aux[a][b]
        if aux not in visitados:
            toEvaluate.append(cp.deepcopy(aux))
            visitados.append(cp.deepcopy(aux))
    if a != len(arr) - 1: #down
        aux = cp.deepcopy(arr)
        aux[a][b], aux[a+1][b] = aux[a+1][b], aux[a][b]
        if aux not in visitados:
            toEvaluate.append(cp.deepcopy(aux))
            visitados.append(cp.deepcopy(aux))
    return aux

sol(start, end, 3)
