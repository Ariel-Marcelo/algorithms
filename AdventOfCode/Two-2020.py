result = []
bandera = True


def start():
    # Read in the file
    entry = []
    with open("AdventOfCode\ent.txt", "r") as archivo:
        for linea in archivo:
            entry.append(linea)
    # String to int
    index = 0
    for i in entry:
        entry[index] = int(i)
        index += 1
    # Sort my Array
    entry.sort()
    # Solution
    # 3 punteros  al inicio en el medio  y otro al final
    # si la suma de los tres es mayor que el valor 2020
    # entonces el puntero final se mueve uno a la izquierda
    # si no, se mueve el puntero inferior
    # si el puntero inferior o seperior se llega a topar con el puntero del medio entonces..
    #  El puntero del medio se va a la mitad del arreglo no recorrido
    # ...el segundo puntero sube uno 
    # si no había espacio entre ellos, el puntero mayor de los dos se mueve uno a la derecha
    print(entry)
    i = 0
    j = 1
    k = len(entry)-1
    wanted = 2020
    while i < j and j < k:
        if entry[i] + entry[j] + entry[k] == wanted:
            print(entry[i], entry[j], entry[k])
            break
        elif entry[i] + entry[j] + entry[k] < wanted:
            while j > i + 1:
                i += 1
                if entry[i] + entry[j] + entry[k] == wanted:
                    print(entry[i], entry[j], entry[k])
                    break
                elif entry[i] + entry[j] + entry[k] > wanted:
                    break   

            j += 1
        elif entry[i] + entry[j] + entry[k] > wanted:
            k -= 1
            

    print(entry[i] , entry[j] , entry[k])
    #sol(entry, i, j, 1768, True)
    #print(result)

"""
def sol(entry, a, b, wanted, flag):
    bandera = flag
    i, j = a, b
    while i < j:
        if (entry[i] + entry[j]) == wanted:
            break
        elif (entry[i] + entry[j]) < wanted:
            i += 1
        elif (entry[i] + entry[j]) > wanted:
            j -= 1

    if bandera == True:
        sol(entry[0:i], 0, i-1, entry[i], False)
        sol(entry[0:j], 0, j-1, entry[j], False)
    
    result.append(entry[i])
    result.append(entry[j])
"""
start()
