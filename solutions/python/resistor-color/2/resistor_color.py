def value(colors):
    return int(
        ''.join(str(color_code(*colors)))
        )

def colors():
    return [
        'black', 'brown', 'red', 'orange', 'yellow',
        'green', 'blue', 'violet', 'grey', 'white',
        ]

def color_code(color):
    return colors().index(color)
