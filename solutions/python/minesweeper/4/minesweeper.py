def annotate(board):
    if not board:
        return board

    sweep = {}
    height, width = len(board), len(board[0])

    for row_num, row in enumerate(board):
        if len(row) != width:
            raise ValueError('The board is invalid with current input.')
            
        sweep[row_num] = {}

        for col, char in enumerate(row):
            if char == '*':
                sweep[row_num][col] = '*'
            elif char != ' ':
                raise ValueError('The board is invalid with current input.')

    for row in range(height):
        for col in range(width):
            if board[row][col] == ' ':
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
