from itertools import \
    combinations_with_replacement as combor

def find_fewest_coins(coins, change):
    if not change:
        return []

    if change < min(coins):
        raise ValueError('No coin small enough')

    for n in range(change):
        for combo in combor(coins, n):
            if sum(combo) == change:
                return sorted(combo)

    raise ValueError('No correct change')
