def primitive_triplets(b):
    if b % 2: raise ValueError('number must be even')
    triplets = set()
    for m in range(1, b+1):
        for n in range(1, b+1):
            if b == 2*m*n and m > n:
                if all(m%i or n%i for i in range(2, n+1)):
                    a = m**2 - n**2
                    c = m**2 + n**2
                    triplets.add(tuple(sorted((a, b, c))))
    return triplets


def triplets_in_range(a, range_end):
    triplets= set()
    b = a+1
    while a != range_end:
        c = (a**2 + b**2)**0.5
        if int(c) == c and not c > range_end:
                triplets.add((a, b, c))
        b += 1
        if b > range_end:
            a += 1
            b = a+1
    return triplets


def is_triplet(triplet):
    a, b, c = sorted(triplet)
    return a**2 + b**2 == c**2
