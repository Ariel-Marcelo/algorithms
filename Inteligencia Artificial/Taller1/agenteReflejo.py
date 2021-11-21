def agent():
    myState = []
    a = input("En que cuarto esta A o B \n")
    b = input("El cuarto A esta 0 (limpio) o 1 (sucio) \n")
    c = input("El cuarto B esta 0 limpio o 1 (sucio) \n ")
    myState = [a,b,c]
 
    result = []

    while myState[1] != "0" or myState[2] != "0" :

        if myState[0] == "A" and myState[1] == "1":
            result.append("stuck")
            myState[1] = "0"
        elif myState[0] == "B" and myState[2] == "1":
            result.append("stuck")
            myState[2] = "0"
        elif myState[0] == "B":
            result.append("left")
            myState[0] = "A"
        elif myState[0] == "A":
            result.append("rigth")
            myState[0] = "B"


    print(result, "costo: ", len(result))

agent()
