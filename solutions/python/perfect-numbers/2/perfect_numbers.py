def classify(number):
    if number < 1:
        raise ValueError('Classification is only possible for positive integers.')
    if number == 1:
        return 'deficient'

    tot = sum(
        n + (number // n if n != number // n else 0)
        for n in range(1, int(number ** 0.5) + 1)
        if number % n == 0
    )

    tot -= number

    return (
        'abundant' if tot > number
        else 'deficient' if tot < number
        else 'perfect'
    )
