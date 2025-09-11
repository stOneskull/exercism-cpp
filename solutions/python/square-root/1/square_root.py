def square_root(number):
    root = 1
    while (square := root * root) != number:
        if square < number:
            root *= 2
        else:
            root -= 1
    return root
    