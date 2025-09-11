def spiral(size):
    if not size: return []
    
    nums = list(range(2, size**2 + 1))
    mapping = [(1, 0, 0)]
    x, y = 0, 0
    forward = 0
    legsizes = reversed(range(1, size))
    
    for legsize in legsizes:
        for leg in range(
            3 if legsize == size-1 else 2):
                for move in range(legsize):
                    
                    if forward == 0: y += 1
                    elif forward == 1: x += 1
                    elif forward == 2: y -= 1
                    elif forward == 3: x -= 1

                    mapping.append((nums.pop(0), x, y))
                
                forward += 1; forward %= 4
        
    mapped = sorted(
        sorted(mapping, key = lambda tup: tup[2]), 
            key = lambda tup: tup[1])
            
    snake = [tup[0] for tup in mapped]
    return [
        [snake.pop(0) for num in range(size)] 
            for line in range(size)]

