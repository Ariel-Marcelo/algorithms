def sol():
    # Read in the file
    entry = []
    with open("AdventOfCode\ent.txt","r") as archivo:
        for linea in archivo:
            entry.append(linea)
    # String to int
    index = 0
    for i in entry:
        entry[index] = int (i)
        index+=1
    # Sort my Array
    entry.sort()
    # Solution
    # 2 punteros uno al inicio y otro al final
    # si la suma de los dos es mayor que el valor 2000
    # entonces el puntero final se mueve uno a la izquierda
    # si no, el puntero inicial se mueve uno a la derecha
    i = 0
    j = len(entry)-1
    while i < j:
        if (entry[i] + entry[j]) == 2020:
            break
        elif (entry[i] + entry[j]) < 2020:
            i+=1
        elif (entry[i] + entry[j]) > 2020:
            j-=1

    print(entry[i]*entry[j])

sol()