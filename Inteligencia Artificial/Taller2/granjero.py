nodo0 = {'estado' : int('0000', 2) , 'sucesores' : [1, 2, 3, 4]}
nodo1 = {'estado' : int('1000', 2) , 'sucesores' : list()}
nodo2 = {'estado' : int('1100', 2) , 'sucesores' : list()}
nodo3 = {'estado' : int('1010', 2) , 'sucesores' : [6]}
nodo4 = {'estado' : int('1001', 2) , 'sucesores' : list()}
nodo5 = {'estado' : int('0010', 2) , 'sucesores' : [6, 7]}
nodo6 = {'estado' : int('1110', 2) , 'sucesores' : [8, 9]}
nodo7 = {'estado' : int('1011', 2) , 'sucesores' : [10, 11]}
nodo8 = {'estado' : int('0110', 2) , 'sucesores' : list()}
nodo9 = {'estado' : int('0100', 2) , 'sucesores' : [12, 13]}
nodo10 = {'estado' : int('0001', 2) , 'sucesores' : [13, 14]}
nodo11 = {'estado' : int('0011', 2) , 'sucesores' : list()}
nodo12 = {'estado' : int('1100', 2) , 'sucesores' : list()}
nodo13 = {'estado' : int('1110', 2) , 'sucesores' : [16]}
nodo14 = {'estado' : int('1001', 2) , 'sucesores' : list()}
nodo15 = {'estado' : int('0101', 2) , 'sucesores' : [17]}
nodo16 = {'estado' : int('1111', 2) , 'sucesores' : list()}

nodos = [nodo0, nodo1, nodo2, nodo3, nodo4, nodo5, nodo6, nodo7, nodo8, nodo9, nodo10, nodo11, nodo12, nodo13, nodo14, nodo15, nodo16]
abierto = list()
cerrado = list()

estadoFinal = False
def seAlcanzoEstadoFinal():
    return estadoFinal
def esEstadoFinal(nodo):
    global estadoFinal
    estadoFinal = nodo['estado'] == int('1111', 2)
    return estadoFinal
def contieneEstadoFinal(nodos):
    for nodo in nodos:
        if(esEstadoFinal(nodo)):
            return True
    return False

def getSucesores(nodo):
    print(type(nodo))
    indicesSucesores = nodo['sucesores']
    sucesores = list()
    for indiceSucesor in indicesSucesores:
        sucesores.append(nodos[indiceSucesor])
    return sucesores

trayectoria = list()
if __name__ == '__main__':
    abierto.append(nodos[0])
    while len(abierto) != 0 and not seAlcanzoEstadoFinal():
        nodoX = abierto[0]
        abierto.remove(nodoX)
        if nodoX not in cerrado:
            cerrado.append(nodoX)
            sucesores = getSucesores(nodoX)
            if len(sucesores) != 0 and not contieneEstadoFinal(sucesores):
                abierto.extend(sucesores)
        trayectoria.append(nodoX)
    
    if seAlcanzoEstadoFinal():
        print('Exito')
    else:
        print('Fracaso')

