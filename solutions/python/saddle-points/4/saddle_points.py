def saddle_points(matrix):
    if not matrix:
        return set()

    columns = list(zip(*matrix))

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError('inconsistent row lengths')

    return {
        (r+1, c+1)
        for r, row in enumerate(matrix)
        for c, num in enumerate(row)
        if num == max(row) == min(columns[c])
        }
