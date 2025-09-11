from operator import eq
from constraint import (
Problem, AllDifferentConstraint, InSetConstraint
)


COLORS = (
'yellow', 'blue', 'red', 'ivory', 'green'
)
PEOPLE = (
'Norwegian', 'Ukrainian', 'Englishman',
'Spaniard', 'Japanese'
)
DRINKS = (
'water', 'tea', 'milk', 'orange juice', 'coffee'
)
SMOKES = (
'Kools', 'Chesterfield', 'Old Gold',
'Lucky Strike', 'Parliament'
)
PETS = (
'fox', 'horse', 'snails', 'dog', 'zebra'
)


def right_of(a, b):
    return a == b + 1 

def neighbour(a, b):
    return abs(a - b) == 1


problem = Problem()


#  1. There are five houses.
problem.addVariables(COLORS, range(1, 6))
problem.addVariables(PEOPLE, range(1, 6))
problem.addVariables(DRINKS, range(1, 6))
problem.addVariables(SMOKES, range(1, 6))
problem.addVariables(PETS, range(1, 6))

problem.addConstraint(AllDifferentConstraint(), COLORS)
problem.addConstraint(AllDifferentConstraint(), PEOPLE)
problem.addConstraint(AllDifferentConstraint(), DRINKS)
problem.addConstraint(AllDifferentConstraint(), SMOKES)
problem.addConstraint(AllDifferentConstraint(), PETS)

#  2. The Englishman lives in the red house.
problem.addConstraint(eq, ('Englishman', 'red')) 

#  3. The Spaniard owns the dog.
problem.addConstraint(eq, ('Spaniard', 'dog'))

#  4. Coffee is drunk in the green house.
problem.addConstraint(eq, ('coffee', 'green'))

#  5. The Ukrainian drinks tea.
problem.addConstraint(eq, ('Ukrainian', 'tea'))

#  6. The green house is immediately to the right of the ivory house.
problem.addConstraint(right_of, ('green', 'ivory'))

#  7. The Old Gold smoker owns snails.
problem.addConstraint(eq, ('Old Gold', 'snails'))

#  8. Kools are smoked in the yellow house.
problem.addConstraint(eq, ('Kools', 'yellow'))

#  9. Milk is drunk in the middle house.
problem.addConstraint(InSetConstraint({3}), ('milk',))

# 10. The Norwegian lives in the first house.
problem.addConstraint(InSetConstraint({1}), ('Norwegian',))

# 11. The man who smokes Chesterfields lives in the house next to the man with the fox.
problem.addConstraint(neighbour, ('Chesterfield', 'fox'))

# 12. Kools are smoked in the house next to the house where the horse is kept.
problem.addConstraint(neighbour, ('Kools', 'horse'))

# 13. The Lucky Strike smoker drinks orange juice.
problem.addConstraint(eq, ('Lucky Strike', 'orange juice'))

# 14. The Japanese smokes Parliaments.
problem.addConstraint(eq, ('Japanese', 'Parliament'))

# 15. The Norwegian lives next to the blue house.
problem.addConstraint(neighbour, ('Norwegian', 'blue'))


solution = problem.getSolution()


def drinks_water():
    for person in PEOPLE:
        if solution[person] == solution['water']:
            return person

def owns_zebra():
    for person in PEOPLE:
        if solution[person] == solution['zebra']:
            return person
