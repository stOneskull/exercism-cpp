def largest_product(series, size):

    if size < 0:
        raise ValueError("span must be positive length")
    if size > len(series):
        raise ValueError("span given longer than series")

    start = 0
    totals = []

    while start + size <= len(series):
        sub = series[start:start + size]
        total = 1
        for num in sub:
            total *= int(num)
        totals.append(total)
        start += 1

    return max(totals)