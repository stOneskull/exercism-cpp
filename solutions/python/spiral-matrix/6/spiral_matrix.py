def spiral(size):
    if not size: return []

    from operator import attrgetter
    from collections import namedtuple

    mappit = namedtuple('mapping', 'num, x, y')

    mapping = [mappit(1, 0, 0)]         # one done
    nums = list(range(2, size*size+1))  # more to go

    arrow = 0                           # heading east

    lengths = reversed(range(1, size))  # plank lengths
                                        # (size-1 down to 1)
    x, y = 0, 0                         # ready, set
                                        # go
    for length in lengths:
        if length == size-1:
            planks = 3
        else:
            planks = 2

        for plank in range(planks):     # lay down plank

            for step in range(length):      # walk along plank
                if arrow == 0:   x += 1
                elif arrow == 1: y += 1
                elif arrow == 2: x -= 1
                elif arrow == 3: y -= 1
                mapping.append(             # plonk each step
                    mappit(nums.pop(0), x, y))

            arrow += 1; arrow %= 4      # quarterturn for next plank

    mapping = sorted(mapping, key=attrgetter('x'))
    mapping = sorted(mapping, key=attrgetter('y'))

    mapped = [posi.num for posi in mapping]

    return [
        [mapped.pop(0) for column in range(size)]
            for row in range(size)
            ]
