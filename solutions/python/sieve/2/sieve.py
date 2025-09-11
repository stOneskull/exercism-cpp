def primes(limit):
    num_range = range(2, limit + 1)
    bingo_board = list(num_range) 

    for i, num in enumerate(num_range):
        stamp = num * 2
        while stamp <= limit:
            if stamp in bingo_board:
                bingo_board.remove(stamp)
            stamp += num
        if i > limit ** 0.5: break

    return bingo_board
