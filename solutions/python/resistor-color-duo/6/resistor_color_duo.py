def value(bands):
    return int(
    ''.join(str(colors().index(color)) for color in bands)
    )
    
def colors():
    return [
    'black', 'brown', 'red', 'orange', 'yellow',
    'green', 'blue', 'violet', 'grey', 'white',
    ]
