import re

def es_correo_valido(correo):
    expresion_regular = r"(\D.\D+@universidad.edu.ec)"
    return re.match(expresion_regular, correo) is not None


def read():
  contador = 0
  with open('AdventOfCode/Plus/ent.txt', 'r') as archivo:
  
      for linea in archivo:
        try :
          if (es_correo_valido(linea)):
              contador += 1
        except: 
          print('error')
    
     

  print(contador)

read()