def sum_of_multiples(limit, multiples):
    return sum(
        set(
            num for num in range(limit)
            for each in multiples
            if each and not num % each
            )
        )