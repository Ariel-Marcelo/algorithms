#read file and count the number of 1 in each position
numLinea = 0
gamma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
with open ('AdventOfCode/Three-2021/ent.txt', 'r') as archivo:
    for linea in archivo:
      numLinea += 1
      for i in range(len(linea)):
        if linea[i] == '1':
          gamma[i] += 1

epsilon = []
totalGamma = 0
totalEpsilon = 0
#generate gamma an epsion binary
for i in range(len(gamma)):
    if gamma[i]  > numLinea/2:
        gamma[i] = 1
        epsilon.append(0)
    else:
        gamma[i] = 0
        epsilon.append(1)

# binary to decimal
for i in range(len(gamma)):
    if gamma[i] == 1:
        totalGamma += 2**(len(gamma)-i-1)
    else:    
        totalEpsilon += 2**(len(epsilon)-i-1)

print('total',totalGamma*totalEpsilon)
