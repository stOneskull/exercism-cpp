def score(x, y):
    if x == y == 0:
        return 10
    
    distance = (x**2 + y**2) ** 0.5

    points = {10: 0, 5: 1, 1: 5, 0: 10}

    for radius in points:
        if distance > radius:
            return points[radius]