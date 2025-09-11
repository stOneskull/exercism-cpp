def total(basket):
    prices = {1: 800, 2: 1520, 3: 2160, 4: 2560, 5: 3000}

    groups = []

    while basket:
        bookset = set(basket)
        groups.append(len(bookset))
        for book in bookset:
            basket.remove(book)

    # replace any pair of groups 5 and 3 with 4 and 4
    for i, hunt in enumerate(groups):
        if hunt == 5:
            for j, match in enumerate(groups):
                if match == 3:
                    groups[i] = groups[j] = 4
                    break

    return sum(prices[group] for group in groups)
