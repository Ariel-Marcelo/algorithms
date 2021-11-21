def sol():
    entry = []
    with open("AdventOfCode\ent.txt","r") as archivo:
        for linea in archivo:
            entry.append(linea)

    index = 0
    for i in entry:
        entry[index] = int (i)
        index+=1

    entry.sort()
    print(entry)
    

sol()