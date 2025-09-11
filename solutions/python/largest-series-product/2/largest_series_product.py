def largest_product(series, size):
    if size < 0:
        raise ValueError("span must be positive length")
    if size > len(series):
        raise ValueError("span given longer than series")

    totals = []
    start = 0

    while not start+size > len(series):
        total = 1
        for num in series[start:start+size]:
            total *= int(num)
        totals.append(total)
        start += 1

    return max(totals)