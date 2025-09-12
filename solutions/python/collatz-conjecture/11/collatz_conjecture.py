def steps(n):
    if n < 1:
        raise ValueError('Only positive integers are allowed')
    
    step = 0
    
    while n > 1:
        n = 3*n + 1 if n % 2 else n // 2
        step += 1
        
    return step
