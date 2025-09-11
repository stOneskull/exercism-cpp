from itertools import combinations as combos


def combinations(target, size, exclude):
    results = []
    for combo in combos(range(1, 10), size):
        if sum(combo) == target and not any(num in exclude for num in combo):
            results.append(sorted(combo))
    return results
