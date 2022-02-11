from logic import *

mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
characters = [mustard, plum, scarlet]

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom, kitchen, library]

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife, revolver, wrench]

symbols = characters + rooms + weapons


def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            print(f"{symbol}: YES")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")


# There must be a person, room, and weapon.
knowledge = And(
    Or(mustard, plum, scarlet),
    Or(ballroom, kitchen, library),
    Or(knife, revolver, wrench)
)

# Initial cards
knowledge.add(And( # plum no lo hizo, no sucedió en la librería, no se uso un cuchillo
    Not(plum), Not(library), Not(knife)
))

# Unknown card
knowledge.add(Or( # No lo pudo hacer escarlet en el salon de baile con un revolver
    Not(scarlet), Not(ballroom), Not(revolver)
))

# Known cards # mustard no lo hizo
knowledge.add(Not(mustard)) # Mustard no lo hizo
knowledge.add(Not(kitchen)) # No ocurrio tampoco en la cocina

check_knowledge(knowledge)
