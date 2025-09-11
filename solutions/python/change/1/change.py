def find_minimum_coins(change, coins):
    needed = []
    if not change: return needed
    for i, coin in enumerate(reversed(coins)):
        if coin > change:
            continue
        while change >= coin:
            change -= coin
            needed.append(coin)
            if not change:
                return list(reversed(needed))

