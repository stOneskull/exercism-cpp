def sum_of_multiples(limit, multiples):
    return sum(
        set(
            num for each in multiples
            for num in range(limit)
            if each and not num % each
            )
        )