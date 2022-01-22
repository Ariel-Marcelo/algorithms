from logic import *
from itertools import permutations

colors = ["Red", "Blue", "Green", "Yellow"]

hits = ["0","1", "2", "3", "4"]

blue = Symbol("Blue")
red = Symbol("Red")
green = Symbol("Green")
yellow = Symbol("Yellow")

symbols = []

knowledge = And()

cases = list(permutations(colors, 4))

# all possible symbols
for case in cases: 
    symbols.append(Symbol(case))

for case in cases:
    knowledge.add(symbols[cases.index(case)] == case)

for case in symbols:
    Implication(And(case,Symbol(hits[0])),And(Not(blue),Not(red),Not(green),Not(yellow)))
    Implication(And(case,Symbol(hits[1])),Or(Not(And(blue,yellow,red)),Not(And(blue,yellow,green)),Not(And(blue,red,green)),Not(And(yellow,red,green))))
    Implication(And(case,Symbol(hits[2])),Or(Not(And(blue,yellow)),Not(And(blue,red)),Not(And(blue,green)),Not(And(yellow,green)),Not(And(yellow,red)),Not(red,green)))
    Implication(And(case,Symbol(hits[3])),Or(Not(blue),Not(yellow),Not(green),Not(yellow)))
    Implication(And(case,Symbol(hits[4])),And(blue,red,green,yellow))

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
