def prime_factors(num):

    start = 2
    factors = []

    while num > 1:
        if num % start:
            start += 1
        else:
            factors.append(start)
            num /= start

    return factors
