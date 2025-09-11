def valid(sides):
    m = max(sides)
    return m <= sum(sides) - m


def equilateral(sides):
    return all(sides) and(
        sides[0] == sides[1] == sides[2])


def isosceles(sides):
    return all(sides) and valid(sides) and(
        sides[0] == sides[1] or
        sides[0] == sides[2] or
        sides[1] == sides[2])


def scalene(sides):
    return all(sides) and valid(sides) and(
        sides[0] != sides[1] != sides[2] != sides[0])

