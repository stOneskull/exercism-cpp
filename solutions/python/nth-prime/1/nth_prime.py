def nth_prime(n):
    if n < 1: raise ValueError('positive n please')
    primes = [2, 3, 5, 7, 11]
    if n <= len(primes):
        return primes[n-1]
    at = 11
    while True:
        at += 2
        if not any(at%i==0 for i in primes):
            primes.append(at)
            if len(primes) == n:
                break
    return primes[-1]
