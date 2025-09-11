from itertools import combinations


def maximum_value(maximum_weight, items):
    results = []
    
    for i in range(1, len(items)+1):
        combos = combinations(items, i)
        for combo in combos:
            weights = [item["weight"] for item in combo]
            values = [item["value"] for item in combo]
            if not sum(weights) > maximum_weight:
                results.append(sum(values))

    return max(results) if results else 0
