class Agente :
    costo = 0
    result = []
    def __init__(self, sensor):
        sensor = Sensor()
        self._limpiar(sensor)
    
    def __limpiar(self, sensor):
        sensor.isClean()


class Sensor :
    vacummRoom = "A"
    roomA = 1
    roomB = 1
    def __init__(self) -> None: 
        vacummRoom = input("En que cuarto esta A o B \n")
        roomA = input("El cuarto A esta 0 (limpio) o 1 (sucio) \n")
        roomB = input("El cuarto B esta 0 limpio o 1 (sucio) \n ")
    
    
    def isClean(self) -> bool:
        if self.vacummRoom == "A" and self.roomA == "1":
            return True

        elif self.vacummRoom == "B" and self.roomB == 1:
            return True
        
        return False




if __name__ == "__main__":
    agente = Agente(Sensor())
    