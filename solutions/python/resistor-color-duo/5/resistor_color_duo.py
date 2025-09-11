def value(colors):
    code = [
    'black', 'brown', 'red', 'orange', 'yellow',
    'green', 'blue', 'violet', 'grey', 'white',
    ]
    
    return int(
    ''.join(str(code.index(color)) for color in colors)
    )

