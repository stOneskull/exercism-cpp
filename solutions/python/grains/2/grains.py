def checknum(square):
    if not 0 < square < 65:
        raise ValueError('bad square')

def on_square(square):
    checknum(square)
    return 1 << (square - 1)

def total_after(square):
    checknum(square)
    return (1 << square) - 1
