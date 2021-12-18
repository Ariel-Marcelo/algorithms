heuristic = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Timisoara': 329,
    'Urziceni': 80,
    'Zerind': 374,
    'Sibiu': 253,
    'Vaslui': 199,
    'Hirsova': 151,
    'Iasi': 226,
}

def printPath(path):
    #Asume que el camino es una lista de nodos
    result = ''
    for i in range(len(path)):
        result = result + str(path[i]) # str convierte a string el nodo indicado
        if i != len(path)-1:
            result = result + '-->'
    return result


def aStar(graph, start, end, toPrint = False):
    """ f = g + heuristic"""
    node = start
    openList= []
    closedList = [start]
    g = 0
    while True:
        cities = []
        cityCosts = []
        for value in graph.childrenOf(node): #recorre las ciudades hijas de la ciudad inicial
            if type(value) == Node:
                if value not in openList:
                    cities.append(value)
            else :
                cityCosts.append(value)
    
        if cities == []:
            return None

        f = g + cityCosts[0] + heuristic[cities[0].getName()] #f = g + heuristic
        index = 0

        for i in range(len(cities)):
           
           
            costo = cityCosts[i]
            h = heuristic[cities[i].getName()]
            aux = (g + costo) + h

            if cities[i] == end:
                f = aux
                g+=costo
                
                print (cities[index], "f: ", f, "g: ", g, "h: ", h)
                closedList.append(cities[index])
                return closedList
            elif aux < f: # ir a la ciudad con menor f
                f = aux
                index = i
            
            if cities[i] not in openList: 
                openList.append(cities[i])

        closedList.append(cities[index]) # la lista cerrada almacenará el camino a seguir
        node = cities[index] # el nodo actual será el nodo con menor f
        g += cityCosts[index] # actualizar el costo de la ruta
        print (cities[index], "f: ", f, "g: ", g, "h: ", heuristic[cities[index].getName()])

def shortestPath(graph, start, end, toPrint = False): 
    return aStar(graph, start, end, toPrint)

class Node(object):
    def __init__(self, name):#inicializa el nodo
        """Asume que name es un string"""
        self.name = name
    def getName(self): #retorna el nombre del nodo
        return self.name
    def __str__(self): #imprime el nombre del nodo
        return self.name

class Edge(object):
    def __init__(self, src, dest, cost): #inicializa el objeto edge
        """Asume que src y dest son nodos"""
        self.src = src
        self.dest = dest
        self.cost = cost
    def getSource(self): #retorna el nodo origen
        return self.src
    def getDestination(self): #retorna el nodo destino
        return self.dest
    def getCost(self): #retorna el costo del objeto edge
        return self.cost
    def __str__(self): #str se llama por defecto al solicitar un string de un objeto edge
        return self.src.getName() + '->' + self.dest.getName() # este es el que se usa para imprimir el grafo en consola (print)
      

class Digraph(object):
    """edges está en un diccionario con una lista conectada a sus 
    hijos"""
    def __init__(self): #inicializa el grafo
        self.edges = {}
    def addNode(self, node):#agrega un nodo al grafo
        if node in self.edges:
            raise ValueError('Nodo duplicado')
        else:
            self.edges[node] = []
    def addEdge(self, edge):#agrega una arista al grafo
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Nodo no está en el grafo')
        self.edges[src].append(dest)
        self.edges[src].append(edge.getCost())

    def childrenOf(self, node): #retorna los hijos de un nodo
        return self.edges[node]
    def hasNode(self, node): #retorna true si el nodo esta en el grafo
        return node in self.edges
    def getNode(self, name): #retorna el nodo con el nombre indicado
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    def __str__(self):#str se llama por defecto al solicitar un string de un objeto digraph
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                         + dest.getName() + '\n'
        return result[:-1] #omita la nueva línea al final
        
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
    
def buildCityGraph(graphType):#crea un grafo de ciudades
    g = graphType() 
    for name in ('Arad', 'Sibiu', 'Zerind', 'Oradea', 'Rimnicu Vilcea',
     'Timisoara', 'Lugoj', 'Mehadia', 'Dobreta', 'Craiova','Pitesti',
     'Fagaras', 'Giurgiu', 'Iasi', 'Neamt', 'Vaslui',
     'Hirsova', 'Bucharest', 'Eforie', 'Urziceni'):

        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Arad'), g.getNode('Zerind'), 75))
    g.addEdge(Edge(g.getNode('Arad'), g.getNode('Timisoara'), 118))
    g.addEdge(Edge(g.getNode('Arad'), g.getNode('Sibiu'), 140))
    g.addEdge(Edge(g.getNode('Zerind'), g.getNode('Oradea'), 71))
    g.addEdge(Edge(g.getNode('Oradea'), g.getNode('Sibiu'), 151))
    g.addEdge(Edge(g.getNode('Lugoj'), g.getNode('Timisoara'), 111))
    g.addEdge(Edge(g.getNode('Lugoj'), g.getNode('Mehadia'),  70))
    g.addEdge(Edge(g.getNode('Mehadia'), g.getNode('Dobreta'), 75))
    g.addEdge(Edge(g.getNode('Dobreta'), g.getNode('Craiova'), 120))
    g.addEdge(Edge(g.getNode('Craiova'), g.getNode('Pitesti'), 138))
    g.addEdge(Edge(g.getNode('Craiova'), g.getNode('Rimnicu Vilcea'), 146))
    g.addEdge(Edge(g.getNode('Pitesti'), g.getNode('Bucharest'), 101))
    g.addEdge(Edge(g.getNode('Sibiu'), g.getNode('Rimnicu Vilcea'), 80))
    g.addEdge(Edge(g.getNode('Sibiu'), g.getNode('Fagaras'), 99))
    g.addEdge(Edge(g.getNode('Rimnicu Vilcea'), g.getNode('Pitesti'), 97))
    g.addEdge(Edge(g.getNode('Fagaras'), g.getNode('Bucharest'), 211))
    g.addEdge(Edge(g.getNode('Bucharest'), g.getNode('Giurgiu'), 90))
    g.addEdge(Edge(g.getNode('Bucharest'), g.getNode('Urziceni'), 85))
    g.addEdge(Edge(g.getNode('Urziceni'), g.getNode('Hirsova'), 98))
    g.addEdge(Edge(g.getNode('Hirsova'), g.getNode('Eforie'), 86))
    g.addEdge(Edge(g.getNode('Urziceni'), g.getNode('Vaslui'), 142))
    g.addEdge(Edge(g.getNode('Vaslui'), g.getNode('Iasi'), 92))
    g.addEdge(Edge(g.getNode('Iasi'), g.getNode('Neamt'), 87))
    return g

def testSP(source, destination):#testea el algoritmo de aStar y DFS
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination), toPrint = True)
                      
    if sp != None:
        print('Camino más corto desde ', source, 'a',
              destination, 'es', printPath(sp))
    else:
        print('No hay camino desde', source, 'a', destination)
        
testSP('Lugoj', 'Bucharest')
