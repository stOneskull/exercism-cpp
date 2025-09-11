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

    lead = int(str(first) + str(second))
    if lead and not lead % 10:
        lead //= 10
        zeros += 1

    prefix, zeros = divmod(zeros, 3)
    prefix = ['', 'kilo', 'mega', 'giga'][prefix]
    zeros = '' + zeros * '0'
    
    return f'{lead}{zeros} {prefix}ohms'
