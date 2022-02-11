# Defino casos de prueba

def start():
  t = int (input())
  for i in range(t):
    m = int (input())
    a = 0
    b = 1

    if m == 0 : 
      print (1)
    else :
      for i in range(m):
        c = a + b
        a = b
        b = c

    print (b % 10)

start()