# Problema , encontrar el camino más corto por DFS Y BFS
# Recorrer un conjunto de datos por DFS mostrando todo el camino hacia el objetivo
# Recorrer un conjunto de datos por BFS mostrando el camino hacia el objetivo
# De los caminos encontrados elija el más corto osea con menos nodos

grafo = {'Salina Cruz': [ 'Tehuantepec','Huatulco'],
        'Huatulco': ['Puerto Escondido'],
        'Tehuantepec': ['Juchitán','Oxaca'],
        'Juchitán': ['Ayucan', 'Tonalá', 'Ixtepec'],
        'Oxaca': ['Puebla'],
        'Ayucan': ['Veracruz', 'Minatitlán'],
        'Tonalá': [],
        'Ixtepec': [],
        'Puebla': ['Ciudad de México', 'Orizaba'],
        'Ciudad de México': [],
        'Orizaba': ['Cordoba'],
        'Veracruz': ['Poza Rica', 'Xalapa', 'Cordoba'],
        'Poza Rica': ['Tuxpan'],
        'Xalapa': [],
        'Cordoba': [],
        'Tuxpan': ['Tampico'],
        'Tampico': ['Matamaros'],
        'Matamaros': ['Ciudad Reynosa'],
        'Puerto Escondido': [],
        'Minatitlán': [],
        'Ciudad Reynosa': []}

ciudades = list(grafo.keys())
visitados = []
pila = []
camino = []
caminoMásCorto = []

def solFBS(grafo, destino):
    # Primero en entrar primero en salir
    # Se acaba cuando la pila se agote
    while pila:
        puntoPartida = pila.pop(0)
        # A partir del punto de partida visitar solo los nodos no visitados
        for puedeVisitar in grafo[puntoPartida]:
            if puedeVisitar not in visitados:
                visitados.append(puedeVisitar)
                pila.append(puedeVisitar)
                print('pila', pila)
                print('visitados', visitados)
                print(puedeVisitar)
        else: 
            print ('estoy vacío')


def solDBS(grafo, destino):
    # Primero en entrar ultimo en salir
    # Se acaba cuando la pila se agote
    while pila:
        puntoPartida = pila.pop()
        # A partir del punto de partida visitar solo los nodos no visitados
        for puedeVisitar in grafo[puntoPartida]:
            if puedeVisitar not in visitados:
                visitados.append(puedeVisitar)
                pila.append(puedeVisitar)
                print('pila', pila)
                print('visitados', visitados)

        if destino in visitados: 
            print('You are in your destiny')
            break


if __name__ == '__main__':
    pila.append('Salina Cruz')
    solFBS(grafo, 'Ciudad Reynosa')

