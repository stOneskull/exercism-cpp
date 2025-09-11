def sieve(limit):
    num_list = range(2, limit + 1)
    bingo_board = [each for each in num_list]

    for num in num_list:
        stamp = num * 2
        while stamp <= limit:
            if stamp in bingo_board:
                bingo_board.remove(stamp)
            stamp += num

    return bingo_board