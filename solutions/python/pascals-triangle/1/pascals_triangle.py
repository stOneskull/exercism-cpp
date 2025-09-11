def rows(row_count):
    if row_count < 0:
        raise ValueError(f'value must be a whole number, not: {row_count}')

    if row_count == 0:
        return []
        
    if row_count == 1:
        return [[1]]

    triangle = rows(row_count-1)

    row = triangle[-1]

    next_row = [1] + [row[k] + row[k+1] for k in range(len(row)-1)] + [1]

    return triangle + [next_row]


if __name__ == '__main__':
    for row in rows(int(input('rows? '))):
        print(row) 
