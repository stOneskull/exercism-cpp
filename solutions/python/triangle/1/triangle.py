def valid(sides):
    m = max(sides)
    return m <= sum(sides) - m


def is_equilateral(sides):
    return all(sides) and(
        sides[0] == sides[1] == sides[2])


def is_isosceles(sides):
    return all(sides) and valid(sides) and(
        sides[0] == sides[1] or
        sides[0] == sides[2] or
        sides[1] == sides[2])


def is_scalene(sides):
    return all(sides) and valid(sides) and(
        sides[0] != sides[1] != sides[2])

