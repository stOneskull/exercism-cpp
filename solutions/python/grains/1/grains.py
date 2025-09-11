def on_square(square):
    checknum(square)
    return 2 ** (square - 1)


def total_after(squares):
    checknum(squares)
    return sum(
        on_square(square)
        for square in range(1, squares + 1)
        )

def checknum(square):
    if not 0 < square < 65:
        raise ValueError('give num from 1 to 64')
