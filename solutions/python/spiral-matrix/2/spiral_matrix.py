def spiral(size):
    if not size: return []
    
    from collections import namedtuple
    
    Pos = namedtuple('Position', 'num, x, y')
    
    x, y = 0, 0                         # start
    entries = [Pos(1, x, y)]            # one done
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
                entries.append(         # plonk each step
                    Pos(nums.pop(0), x, y))
                
            arrow += 1; arrow %= 4      # turn clockwise
    
    entries = sorted(entries, key=lambda pos: pos.y)
    entries = sorted(entries, key=lambda pos: pos.x)
    mapped = [pos.num for pos in entries]
                
    return [[mapped.pop(0) for column in range(size)] 
            for line in range(size)]

