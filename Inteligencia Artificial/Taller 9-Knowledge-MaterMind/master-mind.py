from logic import *
from itertools import permutations

colors = ["Red", "Blue", "Green", "Yellow"]

blue = Symbol("Blue")
red = Symbol("Red")
green = Symbol("Green")
yellow = Symbol("Yellow")

symbols = []

knowledge = And()

# Todas las posibles permutaciones sin repetición
cases = list(permutations(colors, 4))

# Tengo que saber  todas las combinaciones que pueden estar ubicadas correctamente
for case in cases:
    symbols.append(Symbol(case))
 
knowledge.add(Or(
        symbols[0],
        symbols[1],
        symbols[2],
        symbols[3],
        symbols[4],
        symbols[5],
        symbols[6],
        symbols[7],
        symbols[8],
        symbols[9],
        symbols[10],
        symbols[11],
        symbols[12],
        symbols[13],
        symbols[14],
        symbols[15],
        symbols[16],
        symbols[17],
        symbols[18],
        symbols[19],
        symbols[20],
        symbols[21],
        symbols[22],
        symbols[23]
))

# Cada caso podría implicar que 1 letra este mal o que  2 lo estén  o 3 estén mal ubicadas 
for case in symbols:
    knowledge.add(Or(
            Implication(case,And(Not(blue),Not(red),Not(green),Not(yellow))),
            Implication(case,Or(Not(And(blue,yellow,red)),Not(And(blue,yellow,green)),Not(And(blue,red,green)),Not(And(yellow,red,green)))),
            Implication(case,Or(Not(And(blue,yellow)),Not(And(blue,red)),Not(And(blue,green)),Not(And(yellow,green)),Not(And(yellow,red)),Not(And(red,green)))),
            Implication(case, And(blue, red, green, yellow))
        )
    )
    
# Puesto que cada caso es único entonces no pueden exisitr 2 casos ubicados en la posición correcta 
for case1 in cases:
    for case2 in cases:
        if case1 != case2:
            knowledge.add(
                Implication(Symbol(case1), Not(Symbol(case2)))
            )


for symbol in symbols:
     if model_check(knowledge, symbol):
         print(f"{symbol}:YES" )
     elif model_check(knowledge, Not(symbol)):
         print(f"{symbol}:Maybe" )

# for person in people:
#     for house in houses:
#         symbols.append(Symbol(f"{person}{house}"))
# # Each person belongs to a house.
# for person in people:
#     knowledge.add(Or(
#         Symbol(f"{person}Gryffindor"),
#         Symbol(f"{person}Hufflepuff"),
#         Symbol(f"{person}Ravenclaw"),
#         Symbol(f"{person}Slytherin")
#     ))
# # Only one house per person.
# for person in people:
#     for h1 in houses:
#         for h2 in houses:
#             if h1 != h2:
#                 knowledge.add(
#                     Implication(Symbol(f"{person}{h1}"), Not(Symbol(f"{person}{h2}")))
#                 )

# # Only one person per house.
# for house in houses:
#     for p1 in people:
#         for p2 in people:
#             if p1 != p2:
#                 knowledge.add(
#                     Implication(Symbol(f"{p1}{house}"), Not(Symbol(f"{p2}{house}")))
#                 )

# # Gildroy no pertenece a gryffindor
# knowledge.add(
#     Or(Symbol("GilderoyGryffindor"), Symbol("GilderoySlytherin"))
# )
# #  Pomona no pertenece a Ravenclaw
# knowledge.add(
#     Not(Symbol("PomonaRavenclaw"))
# )
# # Minerva pertenece a griffindor
# knowledge.add(
#     Symbol("MinervaGryffindor")
# )

# for symbol in symbols:
#     if model_check(knowledge, symbol):
#         print(symbol)
