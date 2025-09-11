def collatz_steps(number):
    if number < 1:
        raise ValueError('number must be positive')

    steps = 0

    while number > 1:
        steps += 1

        number = (
            number / 2 if number % 2 == 0
            else 3 * number + 1
        )

    return steps
