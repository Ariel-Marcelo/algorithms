class Agente :
    costo = 0
    result = []
    def __init__(self):
        sensor = Sensor()
     



class Sensor :
    vacummRoom = "A"
    roomA = 1
    roomB = 1
    def __init__(self) -> None: 
        vacummRoom = input("En que cuarto esta A o B \n")
        roomA = input("El cuarto A esta 0 (limpio) o 1 (sucio) \n")
        roomB = input("El cuarto B esta 0 limpio o 1 (sucio) \n ")
        print(vacummRoom)
    
    def isClean(self) -> bool:
        pass
        if self.vacummRoom == "A" and self.roomA == "1":
            return True

        elif self.vacummRoom == "B" and self.roomB == 1:
            return True
        
        return False


sensor = Sensor()
myAgent = Agente(sensor)
myAgent.limpiar
