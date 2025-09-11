from operator import eq
from constraint import Problem, AllDifferentConstraint, InSetConstraint

COLORS = ('yellow', 'blue', 'red', 'ivory', 'green')
PEOPLE = ('Norwegian', 'Ukrainian', 'Englishman', 'Spaniard', 'Japanese')
DRINKS = ('water', 'tea', 'milk', 'orange juice', 'coffee')
SMOKES = ('Kools', 'Chesterfield', 'Old Gold', 'Lucky Strike', 'Parliament')
PETS = ('fox', 'horse', 'snails', 'dog', 'zebra')


def right_of(a, b):
    return a == b + 1
    
def neighbour(a, b):
    return abs(a - b) == 1


problem = Problem()

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

problem.addConstraint(eq, ('Englishman', 'red')) 
problem.addConstraint(eq, ('Spaniard', 'dog'))
problem.addConstraint(eq, ('coffee', 'green'))
problem.addConstraint(eq, ('Ukrainian', 'tea'))
problem.addConstraint(right_of, ('green', 'ivory'))
problem.addConstraint(eq, ('Old Gold', 'snails'))
problem.addConstraint(eq, ('Kools', 'yellow'))
problem.addConstraint(InSetConstraint({3}), ('milk',))
problem.addConstraint(InSetConstraint({1}), ('Norwegian',))
problem.addConstraint(neighbour, ('Chesterfield', 'fox'))
problem.addConstraint(neighbour, ('Kools', 'horse'))
problem.addConstraint(eq, ('Lucky Strike', 'orange juice'))
problem.addConstraint(eq, ('Japanese', 'Parliament'))
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
