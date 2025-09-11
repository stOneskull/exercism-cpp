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
    'white': 9,
}
tol_dict = {
    'grey': 0.05,
    'violet': 0.1,
    'blue': 0.25,
    'green': 0.5,
    'brown': 1,
    'red': 2,
    'gold': 5,
    'silver': 10,
}
prefix_dict = {
    1_000_000_000: "giga",
    1_000_000: "mega",
    1_000: "kilo",
    1: '',
}


def resistor_label(colors):
    if len(colors) == 1:
        return '0 ohms'

    value = f'{band_dict[colors[0]]}{band_dict[colors[1]]}'
    if len(colors) == 5:
        value += str(band_dict[colors[2]])

    multiplier = band_dict[colors[-2]]
    tolerance = tol_dict[colors[-1]]

    value = int(value) * 10 ** multiplier

    for magnitude, prefix in prefix_dict.items():
        if value >= magnitude:
            value /= magnitude
            if value == int(value):
                value = int(value)
            return f'{value} {prefix}ohms ±{tolerance}%'
