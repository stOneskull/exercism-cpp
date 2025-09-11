def checknum(square):
    if not 0 < square < 65:
        raise ValueError('square must be between 1 and 64')

def square(square):
    checknum(square)
    return 1 << (square - 1)

def total(square=64):
    checknum(square)
    return (1 << square) - 1
