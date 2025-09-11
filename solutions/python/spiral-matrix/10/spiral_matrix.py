from operator import attrgetter
from collections import namedtuple


def spiral_matrix(size):
    if not size: return []

    mappit = namedtuple('mapping', 'number, x, y')
    
    x, y = 0, 0
    arrow = 0                           # heading east
    
    mapping = [mappit(1, x, y)]         # one done
    nums = list(range(2, size*size+1))  # more to go

    lengths = reversed(range(1, size))  # plank lengths

    for length in lengths:
        planks = 3 if length == size-1 else 2

        for plank in range(planks):     # lay down plank
            
            for step in range(length):  
                if arrow == 0:   x += 1
                elif arrow == 1: y += 1
                elif arrow == 2: x -= 1
                elif arrow == 3: y -= 1
                mapping.append(         
                    mappit(nums.pop(0), x, y))

            arrow += 1; arrow %= 4      # quarterturn

    mapping = sorted(mapping, key=attrgetter('x'))
    mapping = sorted(mapping, key=attrgetter('y'))

    return [
    [mapping.pop(0).number for column in range(size)]
    for row in range(size)
    ]
