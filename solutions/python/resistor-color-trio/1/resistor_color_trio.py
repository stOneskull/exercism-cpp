def label(colors):
    band_dict = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'grey': 8,
        'white': 9
    }
    first = band_dict[colors[0]]
    second = band_dict[colors[1]]
    zeros = band_dict[colors[2]]

    if first:
        duo = str(first) + str(second)
    else:
        duo = str(second)
  
    if not second:
        duo = duo[0]
        if first:
            zeros += 1

    prefix, zeros = divmod(zeros, 3)
    prefix = ['', 'kilo', 'mega', 'giga'][prefix]
    zeros = '' + zeros * '0'
    return f'{duo}{zeros} {prefix}ohms'
