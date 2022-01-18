import random
import matplotlib.pyplot as plt

def crearEstado(cadena:str):
    estado = []
    columnaActual = 0
    for caracter in cadena:
        estado.append((int(caracter), columnaActual))
        columnaActual += 1
    return estado

def estaEnMedio(pos1, posMedia, pos2):
    
    def distanciaRelativa(pos1, pos2):
        i1, j1 = pos1
        i2, j2 = pos2

        return (i1 -i2) **2 + (j1 - j2) ** 2
    
    def pendiente(pos1, pos2):
        i1, j1 = pos1
        i2, j2 = pos2

        return (i1 - i2) / (j1- j2)
    
    if pendiente(pos1, posMedia) == pendiente(pos2, posMedia):
        if pos1[1] == pos2[1]: #misma columna    
            if pos1[0] < pos2[0]:
                return pos1[0] < posMedia[0] and pos2[0] > posMedia[0]
            else:
                return pos1[0] > posMedia[0] and pos2[0] < posMedia[0]    
        else:
            if pos1[1] < pos2[1]:
                return pos1[1] < posMedia[1] and pos2[1] > posMedia[1]
            else:
                return pos1[1] > posMedia[1] and pos2[1] < posMedia[1]                            
        #dis1 = distanciaRelativa(pos1, pos2)
        #dis2 = distanciaRelativa(pos1, posMedia)


        
    
    return False




def seAtacan(pos1, pos2):

    i1, j1 = pos1
    i2, j2 = pos2

    if(i1 == i2): #misma fila
        return True 
    if(j1 == j2): #misma columna
        return True

    if(abs(i1 - i2) == abs(j1 - j2)):
        return True
    
    return False

def estaEnMedioAlgunaReina(pos1, pos2, posiciones):
    for posicion in posiciones:
        if posicion == pos1 or posicion == pos2:
            continue
        if(estaEnMedio(pos1, posicion, pos2)):
            return True
    return False
def getIdoneidad(estado):
    numPares = 28
    for i in range(len(estado)):
        for j in range(i + 1, len(estado)):
            pos1 = estado[i]
            pos2 = estado[j]
            if seAtacan(estado[i], estado[j]) :

                #print(f'Se atacan {estado[i]} y {estado[j]}')
                numPares -= 1

    return numPares

def getSucesores(estado : list):
    def esValida(pos):
        return pos[0] >= 0 and pos[0] < 8 and pos[1] >= 0 and pos[0] < 7

    sucesores = []
    for i in range(len(estado)):
        pos = estado[i]
        sucesor1 = estado.copy()
        posCambio = (pos[0] + 1, pos[1])
        if esValida(posCambio):
            sucesor1[i] = posCambio
            sucesores.append(sucesor1)
        posCambio2 = (pos[0] - 1, pos[1])
        sucesor2 = estado.copy()
        if esValida(posCambio2):
            sucesor2[i] = posCambio2
            sucesores.append(sucesor2)
    
    return sucesores

estado = crearEstado('24415417')

def crearEstadoAleatorio():
    estado = []
    for i in range(8):
        fila = random.randint(0, 7)
        estado.append((fila, i))
    return estado
def hillClimbing(estadoInicial, getSucesores, funcionEvaluacion, iteraciones):
    estadoActual = estadoInicial
    valorActual = funcionEvaluacion(estadoInicial)
    x = []
    evaluaciones = []
    iteraciones = 0
    while iteraciones < iteraciones:
        x.append(iteraciones)
        evaluaciones.append(valorActual)
        sucesores = getSucesores(estadoActual)
        estadoActual = max(sucesores, key = funcionEvaluacion)
        valorActual = funcionEvaluacion(estadoActual)
        iteraciones += 1
        
        print(f'{estadoActual} evaluacion: {valorActual}')
    
    #print(estadoActual)
    #print(valorActual)
    #plt.plot(x, evaluaciones)
    #plt.xlabel('iteracion')
    #plt.ylabel('evaluacion')
    #plt.show()
    return estadoActual


if __name__ == '__main__':

    

    valorActual = 0

    while valorActual < 28:
        estadoActual = crearEstadoAleatorio()
        estadoActual = hillClimbing(estadoActual, getSucesores, getIdoneidad, 50)
        valorActual = getIdoneidad(estadoActual)
        print(f'{estadoActual} evaluacion: {valorActual}')


    
