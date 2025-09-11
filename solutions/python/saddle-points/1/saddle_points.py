def saddle_points(matrix):

    if matrix:
        length = len(matrix[0])
        for row in matrix:
            if len(row) != length:
                raise ValueError('inconsistent row length')

    rowbig = []
    coldict = {}
    collil = []

    for row, block in enumerate(matrix):
        for col, num in enumerate(block):
            coldict.setdefault(col, []).append(num)
            if num == max(block):
                rowbig.append((row, col))

    for col in coldict:
        colist = coldict[col]
        for row, num in enumerate(colist):
            if num == min(colist):
                collil.append((row, col))

    return set(
        [
            bigcoo for bigcoo in rowbig
            for lilcoo in collil
            if bigcoo == lilcoo
        ]
    )

