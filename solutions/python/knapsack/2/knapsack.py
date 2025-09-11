def maximum_value(mx_weight, items):
    from itertools import combinations
    
    results = [
    sum(item["value"] for item in combo)
    for num in range(len(items)+1)
    for combo in combinations(items, num)
    if sum(item["weight"] for item in combo) <= mx_weight
    ]

    return max(results) if results else 0
