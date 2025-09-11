def colors():
    return [
        'black', 'brown', 'red', 'orange', 'yellow',
        'green', 'blue', 'violet', 'grey', 'white',
        ]

def color_code(color):
    return colors().index(color)

def code_color(code):
    return colors()[code]
