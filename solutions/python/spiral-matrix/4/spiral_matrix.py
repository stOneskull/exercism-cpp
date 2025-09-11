def spiral(size):
    if not size: return []
    
    from operator import attrgetter as useby
    from collections import namedtuple
    
    Posi = namedtuple('Posituple', 'num, x, y')
    
    x, y = 0, 0                         # start
    mapping = [Posi(1, x, y)]           # one done
    nums = list(range(2, size*size+1))  # more to go
    arrow = 0                           # heading east
    lengths = reversed(range(1, size))  # plank lengths
                                        # size-1 down to 1
    for length in lengths:
        if length == size-1: planks = 3 
        else: planks = 2                # 3 planks of size-1
                                        # then 2 planks for rest
        for plank in range(planks):
            
            for step in range(length):  # walk along plank
                if arrow == 0: y += 1
                elif arrow == 1: x += 1
                elif arrow == 2: y -= 1
                elif arrow == 3: x -= 1
                mapping.append(         # plonk each step
                    Posi(nums.pop(0), x, y))
                
            arrow += 1; arrow %= 4      # turn clockwise
    
    mapping = sorted(mapping, key = useby('y'))
    mapping = sorted(mapping, key = useby('x'))
    mapped = [posi.num for posi in mapping]
                
    return [[mapped.pop(0) for column in range(size)] 
            for line in range(size)]

