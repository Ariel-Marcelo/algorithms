diccionario = {}

diccionario['movie']=['a','perfect','world','my','perfect','woman','pretty','woman']
diccionario['song']=['a','perfect','day','electric','storm','another','rainy','day']
diccionario['consulta']=['perfect','storm']

#Almacenamos todos los elementos
myMovies = diccionario['movie']
mySongs = diccionario['song']
mySearch = diccionario['consulta']
total = mySearch+myMovies+mySongs

#Calculamos cuantos elementos estan repetidos
def same(item,clase) -> int:
    cont = 0
    for i in diccionario[clase]:
        if i == item:
            cont+=1
    return cont


#almacenamos todas las clases en un array
clases = []
clases = diccionario.keys()

#Almacenamos todos los elementos en un array
aux = []
aux = diccionario.values()
elementos = set()

#Recorremos todo el diccionario
for i in aux:
    for f in i:
        elementos.add(f) #Agregamos cada elemento y no se repetira

#Probabilidad para las clases
def probabilidadClase(a) -> float:
    probabilidad = 0
    if a in clases:
        total = len(clases)
        probabilidad = 1/total
        return probabilidad
    else:
        return 0
#Probabilidad total de un item
def probTotal(a):
    cont = same(a,total)
    return dividir(cont,len(total))

#Funcion que divide dos valores
def dividir(a,b) -> float:
    return a/b

#Definimos una probabilidad -> a dado b
def probCondicional(a,b) -> float:
    lenElem = 0
    numeroElem = 0
    probabilidad = 0

    if a in clases and b in elementos:
        print("--- Se aplica teorema de Bayes ---")

        lenElem = len(diccionario[a])
        numeroElem = same(b,a)
        clase = probabilidadClase(a)
        prob = dividir(numeroElem,lenElem)
        total =  probTotal(b)
        probabilidad = dividir(clase*prob,total)

    elif a in elementos and b in clases:
        lenElem = len(diccionario[b])
        numeroElem = same(a,b) 
        probabilidad = dividir(numeroElem,lenElem)
    return probabilidad

#Probabilidad con suavizamiento laplaciano
def probLaplac(a,b,k) -> float:
    
    lenElem =0
    numeroElem = 0
    probabilidad = 0
    val = len(elementos)
    if a in clases and b in elementos:
        print("--- Se aplica teorema de Bayes ---")
        lenElem = len(diccionario[a])
        numeroElem = same(b,a)
        clase = probabilidadClase(a)
        prob = dividir(numeroElem,lenElem)
        total =  probTotal(b)
        probabilidad = dividir(clase*prob,total)
    elif a in elementos and b in clases:
            lenElem = len(diccionario[b])
            numeroElem = same(a,b) 
            probabilidad = dividir(numeroElem + k,lenElem +k*val)
    return probabilidad

print('----- Probabilidades sin suavizamiento Laplaciano ---')
print('Probabilidad de perfect dado movie: '+ str(probCondicional('perfect','movie')))
print('Probabilidad de perfect dado song: ' +str(probCondicional('perfect','song')))
print('--- Probabilidades con suavizamiento Laplaciano con k = 1 ---')
print('Probabilidad de perfect dado movie con k = 1: ' +str(probLaplac('perfect','movie',1)))
print('Probabilidad de perfect dado song con k = 1: '+ str(probLaplac('perfect','song',1)))