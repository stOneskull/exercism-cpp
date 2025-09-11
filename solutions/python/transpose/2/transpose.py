from itertools import zip_longest

def transpose(rows):
    columns = zip_longest(
        *rows.split('\n'), fillvalue='*')

    return '\n'.join(
        ''.join(column).rstrip('*').replace('*', ' ')
            for column in columns)
