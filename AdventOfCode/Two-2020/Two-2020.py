def read():
    passwordsVailable = 0
    entry = []
    with open("AdventOfCode\Two-2020\ent.txt", "r") as archivo:
        for linea in archivo:
            entry.append(linea.split())

    # [range, letter, number]
    for i in entry:
      if isVailable(i):
        passwordsVailable += 1

    print(passwordsVailable)

def isVailable(key):
    # key = [key_positions, letter, password]
    letter = key[1].split(":") 
    key_positions = key[0].split("-")
    password = key[2]
    val = int (key_positions[0]) - 1
    val2 = int (key_positions[1]) - 1
    if password[val] == letter[0] and password[val2] != letter[0]:
      return True
    elif password[val] != letter[0] and password[val2] == letter[0]:
      return True

    return False



read()