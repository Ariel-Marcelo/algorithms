def partOne(arr:list):
    aux =set()
    for i in arr:
        if i not in aux:
            aux.add(2020-i)
        else:
            return i * (2020 - i)
    return 0

def partTwo(arr:list):
    for i in range(0,len(arr)-2):
        for j in range(i+1,len(arr)-1):
            if arr[i]+arr[j]<=2020:
                for k in range(j+1,len(arr)):
                    if arr[i]+arr[j]+arr[k] == 2020:
                        return arr[i] * arr[j] * arr[k]
    return 0
    
def getList():
    with open("AdventOfCode\ent.txt") as f:
        return [int(line.strip()) for line in f]
        
print(partTwo(getList()))