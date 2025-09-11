def square(square):
    if not 0 < square < 65:
        raise ValueError('square must be between 1 and 64')
    return 1 << square - 1

def total():
    return (1 << 64) - 1
