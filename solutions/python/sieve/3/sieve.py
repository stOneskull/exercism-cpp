def primes(limit):
    sieve = list(range(limit + 1))
    iters = int(limit ** 0.5) + 1

    for num in sieve[2:iters]:
        if num == 0: continue
        multiple = num * 2
        while multiple <= limit:
            sieve[multiple] = 0
            multiple += num

    return [num for num in sieve[2:] if num]
