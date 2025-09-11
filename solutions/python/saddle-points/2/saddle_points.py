def saddle_points(matrix):

    columns = zip(*matrix)

    if len(columns) != len(matrix):
        raise ValueError('some')

    return { (y, x)
        for y,row in enumerate(matrix)
        for x,v in enumerate(row)
        if max(row) == v == min(columns[x])
    }
