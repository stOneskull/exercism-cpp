def value(colors):
    return int(
        ''.join(color_code(colors))
        )

def colors():
    return [
        'black', 'brown', 'red', 'orange', 'yellow',
        'green', 'blue', 'violet', 'grey', 'white',
        ]

def color_code(colorlist):
    return [
        str(colors().index(color)) for color in colorlist
        ]
