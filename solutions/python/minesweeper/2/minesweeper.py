def board(pool):
    if not pool:
        return pool

    sweep = {}
    height, width = len(pool), len(pool[0])

    for row_num, row in enumerate(pool):
        if len(row) != width:
            raise ValueError('inconsistent row sizes')
        sweep[row_num] = {}

        for col, char in enumerate(row):
            if char == '*':
                sweep[row_num][col] = '*'
            elif char != ' ':
                raise ValueError(f'invalid char: {char}')

    for row in range(height):
        for col in range(width):
            if pool[row][col] == ' ':
                sweep = check_square(sweep, row, col)

    return [
        ''.join(str(sweep[r][c]) for c in range(width))
        for r in range(height)
        ]


def check_square(sweep, row, col):
    sweep[row][col] = 0

    for r in (row-1, row, row+1):
        for c in (col-1, col, col+1):
            if (r in sweep and c in sweep[r]
                and sweep[r][c] == '*'):
                sweep[row][col] += 1

    if sweep[row][col] == 0:
        sweep[row][col] = ' '

    return sweep