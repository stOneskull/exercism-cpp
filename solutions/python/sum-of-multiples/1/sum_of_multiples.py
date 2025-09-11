def sum_of_multiples(limit, multiples):

    return sum(set(
        num for num in range(limit)
        for each in multiples
        if not num % each)
        )