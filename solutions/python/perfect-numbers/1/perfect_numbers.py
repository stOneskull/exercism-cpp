def classify(number):
    if number < 1:
        raise ValueError('number must be positive')

    tot = sum(
        n for n in range(1, number // 2 + 1)
        if not number % n
        )

    return(
        'abundant' if tot > number
        else 'deficient' if tot < number
        else 'perfect'
        )
