# read file and count the number of 1 in each position
numLineas = 0
oxigen = []
CO2 = []
with open('AdventOfCode/Three-2021/ent.txt', 'r') as archivo:
    for linea in archivo:
      oxigen.append(linea)
      CO2.append(linea)
      numLineas += 1

index = 0
while(len(oxigen) != 1):
    numUnos = 0
    for linea in oxigen:
      if linea[index] == '1':
        numUnos += 1

    if numUnos >= len(oxigen) / 2 :
      for linea in oxigen:
          if linea[index] == '0':
            oxigen.remove(linea)
    elif numUnos < len(oxigen) / 2:
      for linea in oxigen:
          if linea[index] == '1':
            oxigen.remove(linea) 
    index += 1
          
print (oxigen, 'OXIGENO')

print('oxigen', oxigen)
print('CO2', CO2)


totalGamma = 0
totalEpsilon = 0
# binary to decimal
for i in range(len(oxigen)):
    if oxigen[i] == 1:
        totalGamma += 2**(len(oxigen)-i-1)
    else:    
        totalEpsilon += 2**(len(CO2)-i-1)

print('total',totalGamma*totalEpsilon)
