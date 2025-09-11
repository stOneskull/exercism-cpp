def encode(plain):

    text = ''.join(
        letter for letter in plain
        if letter.isalnum()
        ).lower()

    root = len(text) ** 0.5

    rootplus = int(root) + 1

    if root == int(root):
        rowside = int(root)
        colside = int(root)
    else:
        rowside = rootplus
        if int(root) * rootplus >= len(text):
            colside = int(root)
        else:
            colside = rootplus

    rows = ['' for row in range(rowside)]

    for row, letter in enumerate(text):
        rows[row % rowside] += letter

    out = ''

    for row in rows:
        gap = colside - len(row)
        row += ' ' * gap
        out += row + ' '

    return out[:-1]
