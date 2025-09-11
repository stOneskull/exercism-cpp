def total(basket):
    prices = {1: 800, 2: 1520, 3: 2160, 4: 2560, 5: 3000}

    groups = []

    while basket:
        bookset = set(basket)
        for book in bookset:
            basket.remove(book)
        groups.append(len(bookset))

    # replace any pair of groups 5 and 3 with 4 and 4

    while 5 in groups and 3 in groups:
        groups.remove(5)
        groups.remove(3)
        groups += [4, 4]

    return sum(prices[group] for group in groups)
