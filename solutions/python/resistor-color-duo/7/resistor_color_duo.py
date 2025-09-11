def value(bands):
    return int(
    ''.join(str(color_code(color)) for color in bands)
    )
    
def color_code(color):
    return colors().index(color)
    
def colors():
    return [
    'black', 'brown', 'red', 'orange', 'yellow',
    'green', 'blue', 'violet', 'grey', 'white',
    ]
