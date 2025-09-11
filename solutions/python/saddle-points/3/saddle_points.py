def saddle_points(matrix):

    columns = list(zip(*matrix))

    if len(columns) != len(matrix):
        raise ValueError('inconsistent row lengths')

    return {
        (r, c)
        for r, row in enumerate(matrix)
        for c, num in enumerate(row)
        if num == max(row) == min(columns[c])
        }
