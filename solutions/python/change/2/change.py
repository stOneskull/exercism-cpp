from itertools import combinations_with_replacement as combor

def find_minimum_coins(change, coins):
    if not change:
        return []
    if change < 0:
        raise ValueError('Negative')
    if change < min(coins):
        raise ValueError('No coin small enough')

    for n in range(change):
        for combo in combor(coins, n):
            if sum(combo) == change:
                return sorted(combo)

    raise ValueError('No combination found')
